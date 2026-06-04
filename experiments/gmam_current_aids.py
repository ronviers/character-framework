r"""gmam_current_aids.py -- SCAFFOLD for the gMAM instanton of `current-aids-escape`.
See docs/gmam_plan.md for the full plan, decision rules, validation ladder, and anchors.

WHAT IS WIRED (reusable, runnable now): both substrate fields; symmetry-preserving saddle finder;
attractor finder; off-subspace-seeded initial path; a Tier-1 geometric-action evaluator S_hat(path).
WHAT IS STUBBED (next session): the minimizer (gradient descent on S_hat + arc-length reparam), and
the Maier-Stein validation (§6.1 of the plan -- DO THIS FIRST to validate S_hat before trusting numbers).

The geometric action (Heymann-Vanden-Eijnden 2008), minimized over curves x_A -> x_S:
   S_hat(γ) = Σ_i [ |Δx_i|_{a⁻¹} · |b̄_i|_{a⁻¹} − ⟨Δx_i, a⁻¹ b̄_i⟩ ] ,  metric a = diag(x) (demographic).
At the minimum S_hat = quasipotential ΔV; target (committed, demographic Kramers): H a=b 0.328, a≠b 0.272.
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
from identity_survival_barrier import field_many, ee            # H field; F=1, mu=1.6
from autocat_both import field as field_autocat                 # A field; field(X,k1,ec,a,b)

OUT = Path(__file__).resolve().parent
K1A, ECA = 0.05, 0.15

# ---- substrate fields b(x; a, b), single-state (6,) in -> (6,) out ----
def H_b(x, a, b):
    return field_many(x[None, :], a=a, b=b)[0]

def A_b(x, a, b):
    return field_autocat(x[None, :], K1A, ECA, a=a, b=b)[0]

SUBSTRATES = {
    "H": dict(b=H_b, ab_off=(0.75, 0.75), ab_on=(0.5, 1.0), mu_note="F=1,mu=1.6",
              dV_ref=(0.328, 0.272)),
    "A": dict(b=A_b, ab_off=(0.75, 0.75), ab_on=(0.5, 1.0), mu_note="k1=0.05,ec=0.15",
              dV_ref=(None, None)),
}


# ---- saddle (symmetric racemic point, symmetry-preserving 1D settle) ----
def saddle(name):
    if name == "H":
        F, mu, ab = 1.0, 1.6, 1.5
        m = 1.0 / 3.0
        for _ in range(int(2000.0 / 0.005)):
            m = max(m + m * (F - m * (1.0 + ab + 3.0 * mu)) * 0.005, 1e-12)
    else:
        g, kd, k3, cap, ab = 0.70, 0.50, 1.0, 2.0, 1.5
        m = 1.0 / 3.0
        for _ in range(int(4000.0 / 0.005)):
            dm = K1A + (g - kd) * m * (1 - 6 * m / cap) - k3 * m * (3 * m) - ECA * m * (ab * m)
            m = max(m + dm * 0.005, 1e-12)
    return np.full(6, m)


# ---- attractor (biased settle; same for a=b and a≠b) ----
def attractor(name, a, b, bias=0.05, T=1500.0, dt=0.01):
    bfun = SUBSTRATES[name]["b"]
    X = np.clip(np.array([1 + bias, 1 + bias, 1 + bias, 1 - bias, 1 - bias, 1 - bias]) / 3.0, 1e-12, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + bfun(X, a, b) * dt, 1e-12, None)
    return X


# ---- initial path: straight line x_A -> x_S, SEEDED OFF the symmetric subspace (plan §5.2) ----
def initial_path(x_A, x_S, N=120, seed_amp=0.05):
    """N+1 points. The straight line lives in the uniform-within-group subspace (a symmetric critical
    point where J≡0); we add a 3-cycle bump on the winning group so descent can find the bent instanton."""
    s = np.linspace(0, 1, N + 1)[:, None]
    path = (1 - s) * x_A[None, :] + s * x_S[None, :]
    win = slice(0, 3) if x_A[:3].sum() >= x_A[3:].sum() else slice(3, 6)
    bump = np.zeros(6); bump[win] = np.array([1.0, -0.5, -0.5])       # within-group 3-cycle mode
    env = np.sin(np.pi * s)[:, 0]                                     # 0 at endpoints, max mid-path
    path[:, win] += seed_amp * env[:, None] * bump[win][None, :]
    return np.clip(path, 1e-9, None)


# ---- Tier-1 geometric-action evaluator (UN-VALIDATED; validate vs Maier-Stein first, plan §6.1) ----
def a_inv(x, metric, eps=1e-4):
    if metric == "additive":
        return np.ones_like(x)
    return 1.0 / np.maximum(x, eps)                                  # demographic: diag(1/x), eps-regularized


def S_hat(path, bfun, a, b, metric="demographic", eps=1e-4):
    """discretized Heymann-VE geometric action. metric: 'demographic' (a=diag x) or 'additive' (a=I)."""
    tot = 0.0
    for i in range(len(path) - 1):
        dx = path[i + 1] - path[i]
        xm = 0.5 * (path[i] + path[i + 1])
        bm = bfun(xm, a, b)
        ai = a_inv(xm, metric, eps)                                  # diagonal metric inverse
        dx_n = np.sqrt(max(np.sum(ai * dx * dx), 0.0))
        b_n = np.sqrt(max(np.sum(ai * bm * bm), 0.0))
        tot += dx_n * b_n - np.sum(dx * (ai * bm))
    return float(tot)


def within_group_spread(path):
    L, R = path[:, :3], path[:, 3:]
    return float(max((L.max(1) - L.min(1)).max(), (R.max(1) - R.min(1)).max()))


# ============================ STUB: the gMAM minimizer (next session) ============================
def minimize_gMAM(path, bfun, a, b, metric="demographic", n_iter=4000, dtau=1e-3, reparam_every=10):
    """STUB. Implement Tier-1 (plan §3): gradient descent on S_hat + arc-length reparameterization.

    Loop:
      1. g = numerical ∂S_hat/∂x_i for each interior point i (perturb each of the 6 coords by ~1e-7,
         recompute S_hat; O(N·6) field evals per step -- fine for N~120).  Endpoints x_0,x_N fixed.
      2. path[1:-1] -= dtau * g[1:-1]              (steepest descent; or precondition by the metric)
      3. clip to >0; every `reparam_every` steps, reparameterize to EQUAL ARC LENGTH:
            cumulative chord length -> linear-interpolate the 6D path onto a uniform grid.
      4. track S_hat; stop when |ΔS_hat| < tol.
    Return (path, S_hat). Upgrade to Tier-2 sgMAM (Hamiltonian, plan §3) if the eps-regularized boundary
    on H is unstable. VALIDATE on Maier-Stein (plan §6.1) BEFORE trusting any homochiral number.
    """
    raise NotImplementedError("implement per docs/gmam_plan.md §3 + §6; see comments above")
# =================================================================================================


def main():
    print("=" * 88)
    print("gMAM scaffold -- wiring check (saddle / attractor / initial path / S_hat). Minimizer is STUBBED.")
    print("   see docs/gmam_plan.md ; validate S_hat on Maier-Stein (§6.1) before trusting numbers.")
    print("=" * 88)
    for name in ("H", "A"):
        S = SUBSTRATES[name]; xS = saddle(name)
        for tag, (a, b) in (("OFF a=b", S["ab_off"]), ("ON  a≠b", S["ab_on"])):
            xA = attractor(name, a, b)
            p0 = initial_path(xA, xS)
            Shat = S_hat(p0, S["b"], a, b, metric="demographic")
            print(f"\n[{name} {tag}]  ({S['mu_note']})")
            print(f"   x_A={np.round(xA,4)}  ee={ee(xA[None,:])[0]:+.3f}   x_S={np.round(xS,4)}")
            print(f"   initial path: {len(p0)} pts, within-group spread (seeded)={within_group_spread(p0):.3f}")
            print(f"   S_hat(initial straight+seed, demographic, eps=1e-4) = {Shat:.4f}   "
                  f"[un-validated; ΔV_ref={S['dV_ref'][0 if 'OFF' in tag else 1]}]")
    print("\n" + "-" * 88)
    print("  NEXT: (1) implement Maier-Stein gMAM, reproduce its known instanton/action (validates S_hat +")
    print("        minimizer). (2) implement minimize_gMAM. (3) run A (interior, expect ΔŜ≈0). (4) run H")
    print("        (boundary; expect Ŝ(a=b)≈0.328, Ŝ(a≠b)≈0.272, instanton bends off-subspace). See plan.")
    print("-" * 88)


if __name__ == "__main__":
    main()
