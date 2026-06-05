r"""
Minting on a REAL measured substrate — the electrical autonomous Brownian gyrator.

This is NOT synthetic. Every circuit number is the MEASURED value from a published experiment:
  Chiang, Lee, Lai, Jun, "Electrical Autonomous Brownian Gyrator," Phys. Rev. E 96, 032123 (2017);
  arXiv:1703.10762. Two capacitively-coupled RC circuits, resistor R1 cooled in liquid-nitrogen
  vapor (real Johnson-noise bath T1) while R2 sits at room temperature T2 -> a genuine NESS.

We BUILD THE OPERATOR from those measured parts (generate-don't-hunt, calibrated to the real
system) and read it through the minting protocol, then VALIDATE against the paper's own measured
rotation curve (their Fig. 4: <phi_dot> proportional to dT, vanishing at T1=T2; a non-monotonic
peak vs coupling at Cc ~ 700 pF, ~5 rev/s at T1=120 K).

Measured Langevin model (their Eq. 1):   R_hat C_hat Vdot = -V + xi
  R_hat = diag(R1, R2),   C_hat = [[C1+Cc, -Cc], [-Cc, C2+Cc]]
  Johnson noise:  <xi_i(t) xi_j(t')> = 2 kB T_i R_i delta_ij delta(t-t')
=> OU:  Vdot = -M V + M xi,   M = (R_hat C_hat)^-1,   diffusion D = (1/2) M Xi M^T,
        Xi = 2 kB diag(T1 R1, T2 R2).   Stationary cov Sigma:  M Sigma + Sigma M^T = 2 D.

THE MINTING READING (the framework's only contribution -- a dissipative reading of this imported
structure; pa:cycle-affinity, pa:ness-currents):
  * a DETAILED-BALANCED baseline: with the drive off (T1 = T2) the steady current is EXACTLY zero
    (Sigma_eq = kB T C_hat^-1 solves the Lyapunov eq and gives M Sigma_eq - Sigma_eq M^T = 0);
  * COUPLING mints it: with Cc = 0 the two modes decouple -> no cycle -> zero current even at
    dT != 0.  The protected circulation appears ONLY when BOTH the coupling AND the drive are on;
  * the sign is DRIVE-LOCKED by sign(dT) * sign(coupling): deforming the (reciprocal) R, C values
    cannot flip it, only reversing dT can;
  * SUSTAINED, not stored: as T1 -> T2 the circulation collapses to zero (the measured equilibrium).

Run (from character-framework root):  python experiments/gyrator_minting.py
"""
import sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from numpy.polynomial.hermite_e import hermegauss
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# ---- MEASURED circuit parameters (Chiang et al. 2017, Sec. II + Fig. 4) ----
kB = 1.380649e-23
C1, R1 = 488e-12, 9.01e6     # node 1: 488 pF, 9.01 MOhm
C2, R2 = 420e-12, 9.51e6     # node 2: 420 pF, 9.51 MOhm
T2_ROOM = 296.0              # second reservoir held at room temperature (K)
CC_FIG2 = 1.0e-9            # coupling used in their Figs 2 & 4(a,b)
OUT = r"H:\character-framework\experiments\gyrator_minting.png"


def build(Cc, T1, T2=T2_ROOM):
    """Operator (M, D) from the measured Langevin model. Pure measured inputs."""
    Rhat = np.diag([R1, R2])
    Chat = np.array([[C1 + Cc, -Cc], [-Cc, C2 + Cc]])
    M = np.linalg.inv(Rhat @ Chat)                 # Vdot = -M V + M xi
    Xi = 2.0 * kB * np.diag([T1 * R1, T2 * R2])    # <xi xi> strength
    D = 0.5 * (M @ Xi @ M.T)                        # FP diffusion
    return M, D


def sigma_of(M, D):
    """Stationary covariance: solve M S + S M^T = 2D (Kronecker, column-major vec)."""
    n = M.shape[0]
    K = np.kron(np.eye(n), M) + np.kron(M, np.eye(n))
    S = np.linalg.solve(K, (2.0 * D).flatten(order="F")).reshape(n, n, order="F")
    return 0.5 * (S + S.T)


def area_rate(M, S):
    """Exact probability-current circulation Phi = (1/2)<V1 V2dot - V2 V1dot> = (1/2)(M S - S M^T)_12.
    Zero iff detailed balance. This is the minting scalar A (sign = gyration sense)."""
    return 0.5 * (M @ S - S @ M.T)[0, 1]


def ang_velocity(M, D, S, NH=80):
    """Mean angular velocity <phi_dot> (rad/s), their measured observable, by deterministic
    Gauss-Hermite quadrature over the stationary Gaussian (NOT a stochastic simulation).
    <phi_dot> = E[(V x v_flow)/|V|^2],  v_flow = Omega V,  Omega = D Sigma^-1 - M."""
    Omega = D @ np.linalg.inv(S) - M
    w, U = np.linalg.eigh(S)
    Lh = np.sqrt(np.clip(w, 1e-300, None))
    z, wt = hermegauss(NH)                          # weight exp(-z^2/2)
    acc = 0.0
    for i in range(NH):
        for j in range(NH):
            V = U @ (Lh * np.array([z[i], z[j]]))   # whitened -> physical
            vf = Omega @ V
            acc += wt[i] * wt[j] * (V[0] * vf[1] - V[1] * vf[0]) / (V @ V)
    return acc / (2.0 * np.pi)                       # normalize the 2D Gaussian weight


def phi(Cc, T1, T2=T2_ROOM):
    M, D = build(Cc, T1, T2); return area_rate(M, sigma_of(M, D))


def revps(Cc, T1, T2=T2_ROOM):
    M, D = build(Cc, T1, T2); return ang_velocity(M, D, sigma_of(M, D)) / (2.0 * np.pi)


def main():
    print("MINTING ON A REAL MEASURED SUBSTRATE -- electrical Brownian gyrator (Chiang et al. 2017)\n")
    print(f"  measured parts: C1={C1*1e12:.0f}pF R1={R1/1e6:.2f}MOhm  C2={C2*1e12:.0f}pF "
          f"R2={R2/1e6:.2f}MOhm  T2={T2_ROOM:.0f}K  (T1 swept 120-296K, Cc 100pF-10nF)\n")

    TOL = 1e-18  # current scale is ~1e-15..1e-13 (charge^2/s units); equilibrium must be <<

    # ---------- [MINTING] coupling x drive ----------
    print("=" * 88 + "\n  [MINTING]  the protected circulation needs BOTH the coupling AND the drive\n" + "=" * 88)
    A_eq   = phi(CC_FIG2, T2_ROOM)          # drive off: T1 = T2 (detailed balance)
    A_noc  = phi(0.0,     120.0)            # coupling off: Cc = 0 (no cycle)
    A_both = phi(CC_FIG2, 120.0)            # both on
    print(f"    drive off   (T1=T2=296K, Cc=1nF): A = {A_eq:+.3e}   <- detailed balance, no current")
    print(f"    coupling off (Cc=0, T1=120K):      A = {A_noc:+.3e}   <- no cycle to circulate")
    print(f"    BOTH on     (Cc=1nF, T1=120K):     A = {A_both:+.3e}   <- MINTED circulation")
    minted = abs(A_eq) < TOL and abs(A_noc) < TOL and abs(A_both) > 1e3 * TOL
    print(f"    => coupling mints the protected current under drive: {minted}")

    # ---------- [PROTECTION] drive-locked sign, deformation-robust ----------
    print("\n" + "=" * 88 + "\n  [PROTECTION]  sign(A) = sign(dT)*sign(coupling); reciprocal deformations cannot flip it\n" + "=" * 88)
    s_cold = np.sign(phi(CC_FIG2, 120.0))   # T1<T2 -> dT>0
    s_hot  = np.sign(phi(CC_FIG2, 350.0))   # T1>T2 -> dT<0 (extrapolated past the measured range)
    print(f"    sign at dT>0 (T1=120K): {s_cold:+.0f}   sign at dT<0 (T1=350K, extrapolated): {s_hot:+.0f}"
          f"   -> drive reversal flips it: {s_cold != s_hot}")
    rng = np.random.default_rng(0); flips = 0
    for _ in range(400):
        f = np.exp(0.3 * rng.standard_normal(5))             # scale R1,R2,C1,C2,Cc (reciprocal params)
        g = dict();
        Rh = np.diag([R1*f[0], R2*f[1]])
        Cc = CC_FIG2*f[4]
        Ch = np.array([[C1*f[2]+Cc, -Cc], [-Cc, C2*f[3]+Cc]])
        M = np.linalg.inv(Rh @ Ch)
        Xi = 2.0*kB*np.diag([120.0*R1*f[0], T2_ROOM*R2*f[1]])
        D = 0.5*(M @ Xi @ M.T)
        flips += int(np.sign(area_rate(M, sigma_of(M, D))) != s_cold)
    print(f"    reciprocal R,C deformations (n=400, dT fixed): sign-flips = {flips}/400")
    protected = (s_cold != s_hot) and flips == 0
    print(f"    => sign is drive-locked, deformation-robust: {protected}")

    # ---------- [SUSTAINED] collapse as the drive is removed ----------
    print("\n" + "=" * 88 + "\n  [SUSTAINED]  remove the drive (T1 -> T2) -> circulation collapses\n" + "=" * 88)
    for T1 in (120.0, 200.0, 260.0, 290.0, 296.0):
        print(f"    T1={T1:6.1f}K (dT={T2_ROOM-T1:+6.1f}K):  A = {phi(CC_FIG2, T1):+.3e}")
    collapses = abs(phi(CC_FIG2, 295.99)) < abs(A_both) * 1e-3
    print(f"    => collapses to the equilibrium (DB) value as dT->0: {collapses}")

    # ---------- [VALIDATION] reproduce the paper's MEASURED rotation curve ----------
    print("\n" + "=" * 88 + "\n  [VALIDATION vs MEASUREMENT]  reproduce Chiang et al. Fig. 4 from the measured parts\n" + "=" * 88)
    dT_grid = np.linspace(0, 176, 12)                     # T1 from 296 down to 120 K
    rps_dT  = np.array([revps(CC_FIG2, T2_ROOM - d) for d in dT_grid])
    # linearity through the origin:
    sl = np.polyfit(dT_grid, rps_dT, 1)
    print(f"    <phi_dot> vs dT (Cc=1nF): {rps_dT[0]:+.3f} rev/s at dT=0  ->  {rps_dT[-1]:+.3f} rev/s at dT=176K")
    print(f"      linear fit: {sl[0]:+.4f} rev/s per K, intercept {sl[1]:+.4f} rev/s (paper: linear through 0)")
    Cc_grid = np.geomspace(100e-12, 10e-9, 40)
    rps_Cc  = np.array([revps(c, 120.0) for c in Cc_grid])
    ipk = int(np.argmax(np.abs(rps_Cc)))
    print(f"    <phi_dot> vs Cc (T1=120K): PEAK at Cc = {Cc_grid[ipk]*1e12:.0f} pF, "
          f"|<phi_dot>| = {abs(rps_Cc[ipk]):.2f} rev/s")
    print(f"      MEASURED (paper Fig 4c): peak near Cc ~ 700 pF, ~5 rev/s")
    peak_ok = 300e-12 < Cc_grid[ipk] < 1500e-12 and 2.0 < abs(rps_Cc[ipk]) < 9.0

    print("\n" + "=" * 88 + "\n  VERDICT\n" + "=" * 88)
    if minted and protected and collapses and peak_ok:
        print("  PASS. A real, measured, decades-old analog-electronics NESS instances the MINTING claim:")
        print("  a capacitive COUPLING mints a protected gyrating current under the thermal DRIVE (dT),")
        print("  from a detailed-balanced baseline (T1=T2), sign drive-locked and deformation-robust,")
        print("  collapsing as the drive is removed. The operator built from the MEASURED parts")
        print(f"  reproduces the paper's measured rotation curve (peak {Cc_grid[ipk]*1e12:.0f}pF / "
              f"{abs(rps_Cc[ipk]):.1f}rev/s vs measured ~700pF/~5rev/s). NOT synthetic.")
        print("  Honest scope: a 2-mode Gaussian *current-only* NESS (continuous gyrator), not a >=3")
        print("  frustrated cycle -- the generic minting selection rule, not the DNA's exact-cancellation")
        print("  special case. Second real substrate, distinct from the DNA chemical network.")
    else:
        print(f"  NOT clean: minted={minted} protected={protected} collapses={collapses} peak_ok={peak_ok}")
        print("  Read honestly and debug before claiming anything.")

    figure(dT_grid, rps_dT, Cc_grid, rps_Cc, ipk)


def figure(dT_grid, rps_dT, Cc_grid, rps_Cc, ipk):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.8), dpi=150)

    # panel 1: <phi_dot> vs dT -- minting + collapse (their Fig 4b)
    ax[0].plot(dT_grid, rps_dT, "o-", color="#1565c0", lw=1.8)
    ax[0].axhline(0, color="gray", lw=0.8); ax[0].axvline(0, color="gray", lw=0.8)
    ax[0].set_xlabel(r"$\Delta T = T_2 - T_1$  (K)"); ax[0].set_ylabel(r"$\langle\dot\phi\rangle$  (rev/s)")
    ax[0].set_title("MINTING + collapse: rotation $\\propto \\Delta T$,\nzero at $T_1{=}T_2$ (detailed balance)")
    ax[0].grid(alpha=0.3)

    # panel 2: <phi_dot> vs Cc -- the measured optimal-coupling peak (their Fig 4c)
    ax[1].semilogx(Cc_grid * 1e12, np.abs(rps_Cc), "o-", color="#2e7d32", lw=1.8)
    ax[1].axvline(700, color="#c62828", ls="--", lw=1.2, label="measured peak ~700 pF")
    ax[1].plot(Cc_grid[ipk] * 1e12, abs(rps_Cc[ipk]), "*", ms=16, color="#c62828",
               label=f"computed peak {Cc_grid[ipk]*1e12:.0f} pF")
    ax[1].set_xlabel(r"coupling $C_c$  (pF)"); ax[1].set_ylabel(r"$|\langle\dot\phi\rangle|$  (rev/s)")
    ax[1].set_title("VALIDATION: optimal-coupling peak\nfrom measured parts (T$_1$=120 K)")
    ax[1].legend(fontsize=8, frameon=False); ax[1].grid(alpha=0.3, which="both")

    # panel 3: the minted probability current (gyration) at the measured operating point
    M, D = build(CC_FIG2, 120.0); S = sigma_of(M, D); Om = D @ np.linalg.inv(S) - M
    sd = np.sqrt(np.diag(S))
    g = np.linspace(-3, 3, 22)
    X, Y = np.meshgrid(g * sd[0], g * sd[1])
    U = Om[0, 0] * X + Om[0, 1] * Y; W = Om[1, 0] * X + Om[1, 1] * Y
    ax[2].streamplot(X / sd[0], Y / sd[1], U, W, color="#6a1b9a", density=1.1, linewidth=0.8)
    th = np.linspace(0, 2 * np.pi, 100)
    ax[2].plot(np.cos(th), np.sin(th), color="k", lw=0.8, alpha=0.5)        # 1-sigma contour
    ax[2].plot(2 * np.cos(th), 2 * np.sin(th), color="k", lw=0.6, alpha=0.3)
    ax[2].set_xlabel(r"$V_1/\sigma_1$"); ax[2].set_ylabel(r"$V_2/\sigma_2$")
    ax[2].set_title("the minted circulation\n(probability current, $C_c$=1nF, $T_1$=120 K)")
    ax[2].set_aspect("equal"); ax[2].grid(alpha=0.3)

    fig.suptitle("Minting on a real measured substrate: the electrical Brownian gyrator "
                 "(Chiang et al., Phys. Rev. E 96, 032123, 2017)", fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
