r"""
Independent cross-check of gyrator_minting.py -- a DIFFERENT computational path on the SAME
measured circuit (Chiang et al., PRE 96, 032123, 2017).

gyrator_minting.py computes the rotation via the closed-form stationary covariance (Lyapunov) +
Gauss-Hermite quadrature of <phi_dot>. This script instead DIRECTLY INTEGRATES the measured
Langevin SDE (Euler-Maruyama) and reads <phi_dot> off the SLOPE of the unwrapped angle phi(t) --
exactly the paper's primary method (their Fig. 4a). If the two independent paths agree, the
operator + the closed-form result are not an artifact.

  R_hat C_hat Vdot = -V + xi,   <xi_i xi_j> = 2 kB T_i R_i delta_ij delta(t-t')
  => Vdot = -M V + M xi,   M = (R_hat C_hat)^-1
"""
import sys
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

kB = 1.380649e-23
C1, R1 = 488e-12, 9.01e6
C2, R2 = 420e-12, 9.51e6
T2 = 296.0


def operator(Cc, T1):
    Rhat = np.diag([R1, R2])
    Chat = np.array([[C1 + Cc, -Cc], [-Cc, C2 + Cc]])
    M = np.linalg.inv(Rhat @ Chat)
    s = np.sqrt(2.0 * kB * np.array([T1 * R1, T2 * R2]))   # per-bath noise amplitude
    return M, s


def closed_form_revps(Cc, T1, NH=80):
    """The gyrator_minting.py path: Lyapunov Sigma + Gauss-Hermite <phi_dot> (rev/s)."""
    from numpy.polynomial.hermite_e import hermegauss
    M, s = operator(Cc, T1)
    Xi = np.diag(s**2)
    D = 0.5 * (M @ Xi @ M.T)
    n = 2
    K = np.kron(np.eye(n), M) + np.kron(M, np.eye(n))
    S = np.linalg.solve(K, (2 * D).flatten(order="F")).reshape(n, n, order="F")
    S = 0.5 * (S + S.T)
    Om = D @ np.linalg.inv(S) - M
    w, U = np.linalg.eigh(S); Lh = np.sqrt(np.clip(w, 1e-300, None))
    z, wt = hermegauss(NH); acc = 0.0
    for i in range(NH):
        for j in range(NH):
            V = U @ (Lh * np.array([z[i], z[j]])); vf = Om @ V
            acc += wt[i] * wt[j] * (V[0] * vf[1] - V[1] * vf[0]) / (V @ V)
    return acc / (2 * np.pi) / (2 * np.pi)


def sim_revps(Cc, T1, dt=2e-6, T_tot=12.0, seeds=12, seed0=0):
    """Direct Euler-Maruyama; <phi_dot> from the total winding of phi(t) (the paper's Fig 4a method)."""
    M, s = operator(Cc, T1)
    nstep = int(T_tot / dt)
    rng = np.random.default_rng(seed0)
    V = np.zeros((2, seeds))                                  # parallel trajectories
    sdt = np.sqrt(dt)
    phi_prev = np.zeros(seeds); wind = np.zeros(seeds); burn = nstep // 10
    for k in range(nstep):
        eta = (s[:, None] * rng.standard_normal((2, seeds))) * sdt
        V = V + (-(M @ V)) * dt + M @ eta
        if k == burn:
            phi_prev = np.arctan2(V[1], V[0])
        elif k > burn:
            ph = np.arctan2(V[1], V[0])
            d = ph - phi_prev
            d = (d + np.pi) % (2 * np.pi) - np.pi                # unwrap step
            wind += d; phi_prev = ph
    rate = wind / ((nstep - burn) * dt) / (2 * np.pi)           # rev/s per trajectory
    return float(np.mean(rate)), float(np.std(rate) / np.sqrt(seeds))


def main():
    print("GYRATOR CROSS-CHECK -- direct SDE simulation vs closed-form (same measured circuit)\n")
    print(f"{'Cc(pF)':>8} {'T1(K)':>6} | {'closed-form':>12} | {'direct SDE':>16} | {'agree'}")
    print("-" * 68)
    ok_all = True
    for Cc, T1 in [(1.0e-9, 120.0), (0.661e-9, 120.0), (1.0e-9, 200.0), (1.0e-9, 296.0)]:
        cf = closed_form_revps(Cc, T1)
        sm, se = sim_revps(Cc, T1)
        agree = abs(cf - sm) < max(3 * se, 0.15 * abs(cf) + 0.05)
        ok_all &= agree
        print(f"{Cc*1e12:8.0f} {T1:6.0f} | {cf:+12.3f} | {sm:+8.3f} ± {se:5.3f} | {agree}")
    print("\n" + "=" * 68)
    if ok_all:
        print("  CROSS-CHECK PASSES: the independent SDE path reproduces the closed-form rotation")
        print("  (including ~0 at T1=T2, the DB baseline). The minting result is not a computational")
        print("  artifact -- two independent methods on the measured circuit agree, as in the paper.")
    else:
        print("  MISMATCH -- investigate before trusting gyrator_minting.py.")


if __name__ == "__main__":
    main()
