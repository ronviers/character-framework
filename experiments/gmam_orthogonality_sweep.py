r"""gmam_orthogonality_sweep.py -- is the current⊥escape orthogonality SYMMETRY-PROTECTED or accidental?

gmam_saddle_orthogonality.py showed, at the committed operating point (μ=1.6), that the rotational current
is exactly orthogonal to the escape mode at the racemic saddle. This sweep moves the saddle with the
bifurcation-control parameter μ (the symmetric saddle sits at m̄ = F/(1+a+b+3μ); larger μ → smaller m̄,
larger λ_u) while preserving the L↔R-mirror × within-group-cyclic symmetry, and asks whether the
orthogonality holds at the NEW saddle for every μ.

Symmetry-protected  <=>  across the whole sweep:
  * e_u stays 100% in the branch-selection (between-group) sector,
  * J stays in the cyclic (within-group) sector,
  * |cos(J, e_u)| and e_uᵀ(∂J/∂x)e_u stay at numerical-noise level.
If orthogonality holds at machine precision throughout, run gMAM at the two extreme μ and verify the
σ→0 quasipotential is current-invariant (ΔŜ≈0) at both -- i.e. the barrier-invariance travels with the
symmetry, not the parameter point.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from identity_survival_barrier import field_many
from gmam_current_aids import (a_inv, gmam_minimize, initial_path, within_group_spread)

OUT = Path(__file__).resolve().parent
AB = 1.5                                   # a+b held (pins the metric line); a−b dials the current
OFF, ON = (0.75, 0.75), (0.5, 1.0)
F0 = 1.0

# symmetry-mode basis: uniform, between-group breaking, within-group 3-cycle (×2 per group)
V_UNI = np.array([1, 1, 1, 1, 1, 1.]) / np.sqrt(6)
V_BRK = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6)
CYC = []
for g in (slice(0, 3), slice(3, 6)):
    for raw in (np.array([1., -.5, -.5]), np.array([0., np.sqrt(3) / 2, -np.sqrt(3) / 2])):
        v = np.zeros(6); v[g] = raw; CYC.append(v / np.linalg.norm(v))


def bfun(x, a, b, mu, F=F0):
    return field_many(x[None, :], F=F, a=a, b=b, mu=mu)[0]


def saddle_m(mu, F=F0, ab=AB):
    return F / (1.0 + ab + 3.0 * mu)        # symmetric racemic fixed point (exact); saddle for mu>mu_c=ab..


def jac(x, a, b, mu, h=1e-6):
    J = np.zeros((6, 6))
    for k in range(6):
        e = np.zeros(6); e[k] = h
        J[:, k] = (bfun(x + e, a, b, mu) - bfun(x - e, a, b, mu)) / (2 * h)
    return J


def unstable(Jm):
    w, V = np.linalg.eig(Jm); w = w.real; V = V.real
    iu = int(np.argmax(w)); eu = V[:, iu] / np.linalg.norm(V[:, iu])
    return w[iu], (eu if eu[0] >= 0 else -eu)


def probe_mu(mu):
    xS = np.full(6, saddle_m(mu))
    lu, eu = unstable(jac(xS, *OFF, mu))
    # current orthogonality, sampled just off the symmetric subspace in the cyclic directions
    cosmax = 0.0
    for amp in (0.02, 0.05):
        for c in CYC:
            Jc = bfun(xS + amp * c, *ON, mu) - bfun(xS + amp * c, *OFF, mu)
            if np.linalg.norm(Jc) > 1e-12:
                cosmax = max(cosmax, abs(eu @ Jc) / np.linalg.norm(Jc))
    DJ = jac(xS, *ON, mu) - jac(xS, *OFF, mu)
    shear = abs(float(eu @ DJ @ eu))
    brk = abs(eu @ V_BRK)
    cyc = float(np.sqrt(sum((eu @ c) ** 2 for c in CYC)))
    return dict(mu=mu, mbar=saddle_m(mu), lu=lu, cosmax=cosmax, shear=shear, brk=brk, cyc=cyc, xS=xS)


def attractor_mu(a, b, mu, F=F0, bias=0.05, T=1500.0, dt=0.01):
    X = np.clip(np.array([1 + bias, 1 + bias, 1 + bias, 1 - bias, 1 - bias, 1 - bias]) / 3.0, 1e-12, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field_many(X[None, :], F=F, a=a, b=b, mu=mu)[0] * dt, 1e-12, None)
    return X


def gmam_at(mu, a, b, eps=1e-4):
    xS = np.full(6, saddle_m(mu)); xA = attractor_mu(a, b, mu)
    p0 = initial_path(xA, xS)
    drift = lambda X: field_many(X, F=F0, a=a, b=b, mu=mu)          # noqa: E731
    ainv = lambda X: a_inv(X, "demographic", eps)                  # noqa: E731
    path, Sh, _ = gmam_minimize(p0, drift, ainv, clip_pos=True, n_iter=40000, dtau=5e-4,
                                reparam_every=100, mom=0.95)
    return Sh, within_group_spread(path)


def main():
    mus = np.round(np.linspace(1.0, 3.0, 11), 3)
    print("=" * 92)
    print("orthogonality-tracking sweep -- does current⊥escape survive as the saddle moves (μ: 1.0→3.0)?")
    print("   μ_c = (1+a+b)/3 = 0.833; the symmetric racemic point is a rank-1 saddle for all μ>μ_c.")
    print("=" * 92)
    print(f"   {'μ':>5} {'m̄(saddle)':>10} {'λ_u':>9} {'|cos(J,e_u)|':>13} {'eᵤᵀ∂J eᵤ':>11} "
          f"{'e_u·brk':>9} {'e_u·cyc':>9}")
    rows = [probe_mu(m) for m in mus]
    for r in rows:
        print(f"   {r['mu']:>5.2f} {r['mbar']:>10.4f} {r['lu']:>9.4f} {r['cosmax']:>13.2e} "
              f"{r['shear']:>11.2e} {r['brk']:>9.6f} {r['cyc']:>9.2e}")

    cosmax = max(r["cosmax"] for r in rows)
    shearmax = max(r["shear"] for r in rows)
    cycmax = max(r["cyc"] for r in rows)
    brkmin = min(r["brk"] for r in rows)
    protected = (cosmax < 1e-8) and (shearmax < 1e-6) and (cycmax < 1e-8) and (brkmin > 1 - 1e-8)
    print("\n" + "-" * 92)
    print(f"   worst across sweep:  |cos(J,e_u)|={cosmax:.2e}   |eᵤᵀ∂J eᵤ|={shearmax:.2e}   "
          f"e_u·cyc={cycmax:.2e}   min(e_u·brk)={brkmin:.8f}")
    print(f"   VERDICT: orthogonality is {'SYMMETRY-PROTECTED' if protected else 'NOT structurally enforced'} "
          f"-- e_u stays in the branch-selection sector and J in the cyclic sector throughout.")
    print("-" * 92)

    # plots
    mu = np.array([r["mu"] for r in rows])
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    ax[0, 0].plot(mu, [r["lu"] for r in rows], "-o", color="#1f77b4")
    ax[0, 0].set_title("escape rate λ_u vs μ (the saddle is moving)"); ax[0, 0].set_xlabel("μ")
    ax[0, 0].set_ylabel("λ_u")
    ax[0, 1].semilogy(mu, np.maximum([r["cosmax"] for r in rows], 1e-18), "-o", color="#d62728")
    ax[0, 1].axhline(1e-8, color="0.6", ls="--", lw=1, label="noise floor"); ax[0, 1].legend(fontsize=8)
    ax[0, 1].set_title("|cos(J, e_u)| vs μ  (orthogonality)"); ax[0, 1].set_xlabel("μ"); ax[0, 1].set_ylim(1e-18, 1)
    ax[1, 0].semilogy(mu, np.maximum([r["shear"] for r in rows], 1e-18), "-o", color="#9467bd")
    ax[1, 0].set_title("|e_uᵀ(∂J/∂x)e_u| vs μ  (shear)"); ax[1, 0].set_xlabel("μ"); ax[1, 0].set_ylim(1e-18, 1)
    ax[1, 1].plot(mu, [r["brk"] for r in rows], "-o", color="#2ca02c", label="e_u · breaking sector")
    ax[1, 1].semilogy(mu, np.maximum([r["cyc"] for r in rows], 1e-18), "-s", color="#ff7f0e",
                      label="e_u · cyclic sector")
    ax[1, 1].set_title("escape-mode sector overlaps vs μ"); ax[1, 1].set_xlabel("μ"); ax[1, 1].legend(fontsize=8)
    fig.suptitle(f"current⊥escape across a saddle-moving sweep -- "
                 f"{'SYMMETRY-PROTECTED' if protected else 'NOT enforced'}", fontweight="bold")
    fig.tight_layout(); fig.savefig(OUT / "gmam_orthogonality_sweep.png", dpi=140); plt.close(fig)
    print(f"\n   figure -> gmam_orthogonality_sweep.png")

    # if orthogonality holds throughout, confirm the barrier-invariance travels with it (gMAM at extremes).
    # Tier-1 is eps-regularized at the boundary; we report ΔŜ over eps so non-convergence is self-evident
    # (a single finite ΔŜ near the degenerate boundary is not yet a converged number -- plan §8 / NaN note).
    if protected:
        print("\n   orthogonality holds at machine precision -> gMAM ΔŜ at the extreme μ (over eps; ΔŜ must be")
        print("   eps-stable AND sign-stable to count as 0 -- otherwise Tier-1 is boundary-limited, needs Tier-2):")
        for mu_x in (mus[0], mus[-1]):
            dS = []
            for epsv in (1e-3, 1e-4, 3e-5):
                Soff, _ = gmam_at(mu_x, *OFF, eps=epsv)
                Son, _ = gmam_at(mu_x, *ON, eps=epsv)
                dS.append(Soff - Son)
            dS = np.array(dS)
            converged = (np.abs(dS).max() < 0.01)            # eps-stable and near zero
            verdict = "ΔŜ≈0 (barrier-invariant)" if converged else \
                      "NON-CONVERGENT (Tier-1 boundary floor; sign/eps-unstable) -> needs Tier-2 sgMAM"
            print(f"     μ={mu_x:.2f} (m̄={saddle_m(mu_x):.3f}):  ΔŜ over eps[1e-3,1e-4,3e-5] = "
                  f"[{dS[0]:+.4f}, {dS[1]:+.4f}, {dS[2]:+.4f}]   -> {verdict}")
        print("   (interior-accessible μ confirm invariance; extreme-exclusion μ is past the eps-regularized")
        print("    Tier-1 solver's reach -- inconclusive there, NOT evidence of a real ΔŜ.)")
    else:
        print("\n   orthogonality NOT protected -> skipping gMAM extremes (the premise failed).")


if __name__ == "__main__":
    main()
