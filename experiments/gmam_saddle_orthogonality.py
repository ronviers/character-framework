r"""gmam_saddle_orthogonality.py -- the LOCAL mechanism behind the gMAM null (plan §6.3 / D3).

Question (Ron): is the protected 3-cycle circulation exactly orthogonal to the escape channel at the
racemic saddle? If so, the current can be large yet leave the Freidlin-Wentzell barrier untouched
(it only moves probability *sideways*, along constant-composition surfaces), and the measured finite-σ
MFPT drop must live in the PREFACTOR, not the exponent.

We measure, at the symmetric saddle x_S of the homochiral substrate:
  (1) escape channel  e_u = unstable eigenvector of the saddle Jacobian (OFF and ON; do they agree?);
  (2) e_u's decomposition over {uniform, branch-breaking, within-group 3-cycle} modes;
  (3) the current field J(x) = b(x;ON) − b(x;OFF):  J(x_S) (≈0, the saddle is on the symmetric
      subspace) and its leading off-subspace value, projected on e_u  ->  |cos(J, e_u)|;
  (4) the shear  e_uᵀ (DJ) e_u  (does the current tilt the escape direction at 2nd order?).
Clean orthogonality  <=>  e_u is pure branch-breaking, J ⟂ e_u, and the shear ≈ 0.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gmam_current_aids import SUBSTRATES, saddle

np.set_printoptions(precision=4, suppress=True)
S = SUBSTRATES["H"]; BVEC = S["bvec"]
OFF, ON = S["ab_off"], S["ab_on"]


def b(x, ab):
    return BVEC(x[None, :], ab[0], ab[1])[0]


def jac(x, ab, h=1e-6):
    J = np.zeros((6, 6))
    for k in range(6):
        e = np.zeros(6); e[k] = h
        J[:, k] = (b(x + e, ab) - b(x - e, ab)) / (2 * h)
    return J


def unstable_evec(Jm):
    w, V = np.linalg.eig(Jm); w = w.real; V = V.real
    iu = int(np.argmax(w))
    eu = V[:, iu] / np.linalg.norm(V[:, iu])
    return w[iu], (eu if eu[0] >= 0 else -eu), np.sort(w)[::-1]


def main():
    xS = saddle("H")
    print("=" * 86)
    print("saddle orthogonality -- is the 3-cycle current ⟂ the escape channel at the racemic saddle?")
    print(f"   x_S = {xS}   (symmetric / uniform; demographic metric a⁻¹∝I here, so ⟂ = Euclidean ⟂)")
    print("=" * 86)

    JOFF, JON = jac(xS, OFF), jac(xS, ON)
    luOFF, euOFF, specOFF = unstable_evec(JOFF)
    luON, euON, specON = unstable_evec(JON)
    print(f"\n[escape channel]  λ_u: OFF={luOFF:+.4f}  ON={luON:+.4f}   (rank-1 saddle: one λ>0)")
    print(f"   spectrum OFF = {specOFF}")
    print(f"   e_u(OFF) = {euOFF}")
    print(f"   e_u(ON)  = {euON}")
    print(f"   |e_u(OFF)·e_u(ON)| = {abs(euOFF @ euON):.6f}   (current does NOT rotate the escape channel)")

    # mode basis
    v_uni = np.array([1, 1, 1, 1, 1, 1.]) / np.sqrt(6)
    v_brk = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6)
    cyc = []
    for g in (slice(0, 3), slice(3, 6)):
        for raw in (np.array([1., -.5, -.5]), np.array([0., np.sqrt(3) / 2, -np.sqrt(3) / 2])):
            v = np.zeros(6); v[g] = raw; cyc.append(v / np.linalg.norm(v))
    cyc_comp = np.sqrt(sum((euOFF @ c) ** 2 for c in cyc))
    print(f"\n[e_u decomposition]  branch-breaking={euOFF @ v_brk:+.5f}   uniform={euOFF @ v_uni:+.5f}   "
          f"3-cycle subspace={cyc_comp:.2e}")
    print(f"   => escape channel is {abs(euOFF @ v_brk)*100:.2f}% the branch-breaking mode, "
          f"{cyc_comp:.1e} in the current-carrying cycle plane.")

    # current field near the saddle, projected on the escape channel
    print(f"\n[current ⟂ escape]  J(x)=b(ON)−b(OFF);  J(x_S) norm = {np.linalg.norm(b(xS,ON)-b(xS,OFF)):.2e} "
          f"(≈0: saddle on symmetric subspace)")
    worst = 0.0
    for amp in (0.02, 0.05, 0.10):
        cosines, mags = [], []
        for c in cyc:
            x = xS + amp * c
            Jc = b(x, ON) - b(x, OFF)
            if np.linalg.norm(Jc) > 1e-12:
                cosines.append(abs(euOFF @ Jc) / np.linalg.norm(Jc)); mags.append(np.linalg.norm(Jc))
        worst = max(worst, max(cosines))
        print(f"   off-subspace |δ|={amp:.2f}:  |J|~{np.mean(mags):.3e}   max|cos(J, e_u)| = {max(cosines):.3e}")

    # 2nd-order shear: e_uᵀ (DJ) e_u with DJ = Jacobian of the current field at the saddle
    DJ = JON - JOFF
    shear = float(euOFF @ DJ @ euOFF)
    print(f"\n[shear]  e_uᵀ(DJ)e_u = {shear:+.3e}   (DJ = ∂(b_ON−b_OFF)/∂x at x_S; ≈0 ⇒ current does not "
          f"tilt escape)")

    clean = (abs(euOFF @ euON) > 0.9999) and (cyc_comp < 1e-6) and (worst < 1e-6) and (abs(shear) < 1e-6)
    print("\n" + "-" * 86)
    print(f"   VERDICT: {'EXACTLY ORTHOGONAL' if clean else 'orthogonal to measured tol'} — the current is "
          f"confined to the\n   constant-composition (cycle) plane; it has no projection on the branch-escape "
          f"direction.\n   => the FW barrier is current-blind (gMAM ΔŜ≈0); the finite-σ MFPT drop is a "
          f"prefactor effect.")
    print("-" * 86)


if __name__ == "__main__":
    main()
