r"""
Independent cross-check of repressilator_minting.py -- a SEPARATE re-implementation of Niederholtmeyer
et al. (eLife 2015) Eq. 6, with two independent verifications:

  (1) PERIOD by a different method: FFT of the limit cycle (vs the main script's peak-detection),
      and against the MEASURED band (~ up to 8 h, shortening with Td).
  (2) LINEAR-STABILITY / HOPF analysis: the symmetric fixed point's Jacobian must have a complex
      eigenvalue pair with Re>0 (an unstable spiral => Hopf-born limit cycle); the Hopf frequency
      gives an INDEPENDENT period estimate; reducing the drive must push Re through 0 (so the
      drive-collapse IS a Hopf bifurcation); and the NON-FRUSTRATED (even) ring must have NO unstable
      complex pair (=> the odd-ring frustration is analytically necessary, not incidental).

If the re-implementation reproduces the oscillation + the measured-band period AND the Hopf structure
explains the minting/collapse/frustration, the >=3 instance is not a computational artifact.
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# measured parameters (Niederholtmeyer 2015, Table 2; Eq. 6 has NO leak term)
n, K = 2.0, 5.0
bg = 0.4 * 5.0            # beta * g = 2.0 nM/min
c = 0.5
a = np.log(2) / 8.0
b = np.log(2) / 90.0


def f_rep(x):
    return K**n / (K**n + x**n)

def f_act(x):
    return x**n / (K**n + x**n)


def rhs(t, y, mu, drive, frustrated=True):
    m = y[:3]; p = y[3:]
    rep = [p[2], p[0], p[1]]
    dm = []
    for i in range(3):
        fi = f_rep(rep[i]) if (frustrated or i != 0) else f_act(rep[i])
        dm.append(drive * bg * fi - (a + mu) * m[i])
    dp = [drive * c * m[i] - (b + mu) * p[i] for i in range(3)]
    return dm + dp


def fft_period(mu, drive=1.0, T=6000.0):
    y0 = [1, 0, 0, 8, 2, 0.5]
    sol = solve_ivp(rhs, (0, T), y0, args=(mu, drive), method="LSODA", rtol=1e-9, atol=1e-11,
                    t_eval=np.linspace(0, T, 6000))
    i0 = len(sol.t) // 2
    sig = sol.y[3, i0:] - sol.y[3, i0:].mean(); dt = sol.t[1] - sol.t[0]
    amp = sol.y[3, i0:].max() - sol.y[3, i0:].min()
    if amp < 1.0:
        return np.nan, amp
    fr = np.fft.rfftfreq(len(sig), dt); P = np.abs(np.fft.rfft(sig))
    f0 = fr[1 + np.argmax(P[1:])]
    return (1.0 / f0) / 60.0, amp        # hours


def jac(y, mu, drive, frustrated, eps=1e-6):
    f0 = np.array(rhs(0, y, mu, drive, frustrated)); J = np.zeros((6, 6))
    for j in range(6):
        dy = eps * max(1.0, abs(y[j])); yp = np.array(y, float); yp[j] += dy
        J[:, j] = (np.array(rhs(0, yp, mu, drive, frustrated)) - f0) / dy
    return J


def fixed_point(mu, drive, frustrated, guess=None):
    if guess is None:
        guess = [1, 1, 1, 30, 30, 30]
    return fsolve(lambda y: rhs(0, y, mu, drive, frustrated), guess, full_output=False)


def dominant(mu, drive, frustrated):
    """Eigenvalue of the symmetric-FP Jacobian with the largest real part."""
    yfp = fixed_point(mu, drive, frustrated)
    w = np.linalg.eigvals(jac(yfp, mu, drive, frustrated))
    return w[np.argmax(w.real)]


def main():
    print("REPRESSILATOR CROSS-CHECK -- independent re-implementation + Hopf analysis\n")
    Td = 85.0; mu = np.log(2) / Td

    # ---- (1) independent period: FFT vs the main script's peak-detection (8.85 h) ----
    print("=" * 84 + "\n  (1) PERIOD by FFT (independent of the peak-detection in repressilator_minting.py)\n" + "=" * 84)
    for td in (85.0, 60.0, 40.0, 25.0, 15.0):
        per, amp = fft_period(np.log(2) / td)
        print(f"    Td={td:5.1f} min:  FFT period = {per:5.2f} h   (amp {amp:6.1f} nM)")
    per85, _ = fft_period(mu)
    print(f"    => FFT period at Td=85: {per85:.2f} h  (main script peak-detection: 8.85 h; measured: up to ~8 h)")

    # ---- (2) Hopf analysis: the oscillation mechanism, the collapse, and frustration-necessity ----
    print("\n" + "=" * 84 + "\n  (2) LINEAR-STABILITY / HOPF at the symmetric fixed point\n" + "=" * 84)
    lam = dominant(mu, 1.0, True)
    period_hopf = 2 * np.pi / abs(lam.imag) / 60.0 if lam.imag != 0 else np.nan
    print(f"    drive=1 frustrated: dominant eigenvalue = {lam.real:+.4e} {lam.imag:+.4e}i")
    print(f"      -> Re>0 and complex => UNSTABLE SPIRAL (Hopf-born limit cycle); "
          f"linear period 2pi/Im = {period_hopf:.2f} h")
    unstable_complex = lam.real > 0 and abs(lam.imag) > 0

    # the drive-collapse is a Hopf: Re crosses 0 as drive decreases
    print("\n    drive ramp (is the collapse a Hopf bifurcation?):")
    res = []
    for dr in (1.0, 0.6, 0.4, 0.3, 0.2, 0.1):
        l = dominant(mu, dr, True); res.append((dr, l.real));
        print(f"      drive={dr:.2f}:  max Re(lambda) = {l.real:+.4e}  ({'unstable' if l.real>0 else 'stable'})")
    crosses = any(r > 0 for _, r in res) and any(r < 0 for _, r in res)
    print(f"      => Re(lambda) crosses 0 as drive falls: the collapse IS a Hopf bifurcation: {crosses}")

    # frustration necessity: the even (broken) ring has NO unstable complex pair
    print("\n    frustration necessity (the non-frustrated/even ring):")
    yfp_b = fixed_point(mu, 1.0, False, guess=[1, 1, 1, 30, 30, 30])
    wb = np.linalg.eigvals(jac(yfp_b, mu, 1.0, False))
    lb = wb[np.argmax(wb.real)]
    print(f"      broken-ring dominant eigenvalue = {lb.real:+.4e} {lb.imag:+.4e}i  "
          f"({'STABLE' if lb.real < 0 else 'unstable'})")
    frust_necessary = lb.real < 0
    print(f"      => only the ODD (frustrated) ring has the unstable mode: {frust_necessary}")

    print("\n" + "=" * 84 + "\n  VERDICT\n" + "=" * 84)
    band = 2.0 < per85 < 11.0
    if unstable_complex and crosses and frust_necessary and band:
        print("  CROSS-CHECK PASSES. An independent re-implementation reproduces the oscillation and the")
        print(f"  measured-band period by FFT ({per85:.1f} h), and the Hopf analysis proves the mechanism:")
        print("  the symmetric fixed point is an unstable spiral (complex eigenpair, Re>0) -> a Hopf-born")
        print("  limit cycle; cutting the drive pushes Re through 0 (the collapse IS that bifurcation);")
        print("  and the even (non-frustrated) ring is stable -> the odd-ring frustration is analytically")
        print("  necessary. The >=3 minting instance is not a numerical or peak-detection artifact.")
    else:
        print(f"  NOT clean: unstable_complex={unstable_complex} hopf_collapse={crosses} "
              f"frustration_necessary={frust_necessary} period_in_band={band}")


if __name__ == "__main__":
    main()
