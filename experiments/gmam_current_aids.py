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
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from identity_survival_barrier import field_many, ee            # H field; F=1, mu=1.6
from autocat_both import field as field_autocat                 # A field; field(X,k1,ec,a,b)

OUT = Path(__file__).resolve().parent
K1A, ECA = 0.05, 0.15

# ---- substrate fields b(X; a, b). BATCHED: (S,6) in -> (S,6) out (used by the vectorized gMAM core).
#      H_b/A_b keep the single-state convention for the saddle/attractor settlers below. ----
def H_bvec(X, a, b):
    return field_many(X, a=a, b=b)                                  # F=1, mu=1.6 (defaults)

def A_bvec(X, a, b):
    return field_autocat(X, K1A, ECA, a=a, b=b)

def H_b(x, a, b):
    return field_many(x[None, :], a=a, b=b)[0]

def A_b(x, a, b):
    return field_autocat(x[None, :], K1A, ECA, a=a, b=b)[0]

SUBSTRATES = {
    "H": dict(b=H_b, bvec=H_bvec, ab_off=(0.75, 0.75), ab_on=(0.5, 1.0), mu_note="F=1,mu=1.6",
              dV_ref=(0.328, 0.272)),
    "A": dict(b=A_b, bvec=A_bvec, ab_off=(0.75, 0.75), ab_on=(0.5, 1.0), mu_note="k1=0.05,ec=0.15",
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


# ---- within-group 3-cycle modes (winning group), transverse to the uniform subspace where J≡0 ----
_CYC1 = np.array([1.0, -0.5, -0.5])
_CYC2 = np.array([0.0, np.sqrt(3) / 2, -np.sqrt(3) / 2])


# ---- initial path: straight line x_A -> x_S, SEEDED OFF the symmetric subspace (plan §5.2) ----
def initial_path(x_A, x_S, N=120, seed_amp=0.15, turns=1.0):
    """N+1 points. The straight line lives in the uniform-within-group subspace (a symmetric critical
    point where J≡0). The current is ROTATIONAL in the 3-cycle plane, so we seed a rotational excursion
    sweeping BOTH transverse modes (cos·CYC1 + sin·CYC2, angle = turns·π·s) — giving descent full access
    to any current-harvesting bent instanton, not just a single c₁ bump. A fair test of plan §5.2: if the
    bend pays, descent rolls into it; if not, it relaxes back toward the symmetric subspace."""
    s = np.linspace(0, 1, N + 1)
    path = (1 - s)[:, None] * x_A[None, :] + s[:, None] * x_S[None, :]
    win = slice(0, 3) if x_A[:3].sum() >= x_A[3:].sum() else slice(3, 6)
    th = turns * np.pi * s
    env = np.sin(np.pi * s)                                           # 0 at endpoints, max mid-path
    pert = seed_amp * env[:, None] * (np.cos(th)[:, None] * _CYC1[None, :]
                                      + np.sin(th)[:, None] * _CYC2[None, :])
    path[:, win] += pert
    return np.clip(path, 1e-9, None)


# ---- Tier-1 geometric-action evaluator (UN-VALIDATED; validate vs Maier-Stein first, plan §6.1) ----
def a_inv(x, metric, eps=1e-4):
    if metric == "additive":
        return np.ones_like(x)
    return 1.0 / np.maximum(x, eps)                                  # demographic: diag(1/x), eps-regularized


# ---- generic geometric-action core. drift/ainv are BATCHED closures: (S,d)->(S,d). ----
# (the substrate fields field_many/field are already vectorized, so the per-segment work is one
#  batched field eval over all S=M-1 midpoints; the FD gradient costs 2*d batched evals per iter.)
def _seg_vec(xa, xb, drift, ainv):
    """per-segment Heymann-VE geometric action for stacks of segments. xa,xb: (S,d) -> (S,)."""
    dx = xb - xa
    xm = 0.5 * (xa + xb)
    bm = drift(xm)
    ai = ainv(xm)
    dxn = np.sqrt(np.maximum((ai * dx * dx).sum(1), 0.0))
    bn = np.sqrt(np.maximum((ai * bm * bm).sum(1), 0.0))
    return dxn * bn - (dx * (ai * bm)).sum(1)


def geom_action(path, drift, ainv):
    """discretized Heymann-VE geometric action of a curve (path (M,d); drift/ainv batched)."""
    return float(_seg_vec(path[:-1], path[1:], drift, ainv).sum())


def geom_grad(path, drift, ainv, fd=1e-6):
    """numerical dS/dx, interior points only. S = Σ_i L_i(x_i,x_{i+1}); perturb every segment's left
    endpoint (then right) once per coordinate -> 2*d batched evals, vs M*d scalar evals."""
    M, d = path.shape
    xa, xb = path[:-1], path[1:]                                     # (M-1,d) each
    L0 = _seg_vec(xa, xb, drift, ainv)                              # base segment actions (M-1,)
    g = np.zeros((M, d))
    e = np.zeros(d)
    for k in range(d):
        e[k] = fd
        dLa = (_seg_vec(xa + e, xb, drift, ainv) - L0) / fd         # ∂L_i/∂x_{i,k}
        dLb = (_seg_vec(xa, xb + e, drift, ainv) - L0) / fd         # ∂L_i/∂x_{i+1,k}
        e[k] = 0.0
        g[:-1, k] += dLa                                            # L_i feeds point i  (left endpoint)
        g[1:, k] += dLb                                             # L_i feeds point i+1 (right endpoint)
    g[0] = 0.0; g[-1] = 0.0                                         # endpoints pinned
    return g


def arc_reparam(path):
    """resample the curve to equal Euclidean arc length (interior moves, endpoints pinned)."""
    seg = np.sqrt(((path[1:] - path[:-1]) ** 2).sum(1))
    s = np.concatenate([[0.0], np.cumsum(seg)])
    if s[-1] <= 0:
        return path
    snew = np.linspace(0.0, s[-1], len(path))
    return np.stack([np.interp(snew, s, path[:, k]) for k in range(path.shape[1])], axis=1)


def gmam_minimize(path, drift, ainv, n_iter=6000, dtau=2e-3, reparam_every=20,
                  clip_pos=False, tol=1e-9, mom=0.0, verbose=False):
    """Tier-1 gMAM (plan §3): (heavy-ball) descent on the geometric action + periodic arc-length reparam.
    Endpoints fixed. clip_pos keeps the path in the positive orthant (demographic substrates).
    `mom`∈[0,1): heavy-ball momentum — accelerates the slow transverse mode ~1/(1-mom)× while the
    boundary-stiff modes stay damped at the same dtau (needed for the ill-conditioned H boundary)."""
    path = path.copy()
    vel = np.zeros_like(path)
    hist = [geom_action(path, drift, ainv)]
    for it in range(n_iter):
        g = geom_grad(path, drift, ainv)
        vel[1:-1] = mom * vel[1:-1] - dtau * g[1:-1]
        path[1:-1] += vel[1:-1]
        if clip_pos:
            path = np.clip(path, 1e-9, None)
        if (it + 1) % reparam_every == 0:
            path = arc_reparam(path)
            hist.append(geom_action(path, drift, ainv))
            if verbose and (it + 1) % (reparam_every * 25) == 0:
                print(f"      iter {it+1:5d}  S_hat={hist[-1]:.5f}")
            if abs(hist[-1] - hist[-2]) < tol:
                break
    return path, geom_action(path, drift, ainv), np.array(hist)


def S_hat(path, bvec, a, b, metric="demographic", eps=1e-4):
    """geometric action for a batched substrate field bvec(X,a,b). Thin wrapper over geom_action."""
    return geom_action(path, lambda X: bvec(X, a, b), lambda X: a_inv(X, metric, eps))


def within_group_spread(path):
    L, R = path[:, :3], path[:, 3:]
    return float(max((L.max(1) - L.min(1)).max(), (R.max(1) - R.min(1)).max()))


# ---- substrate-facing wrapper over the generic minimizer (demographic metric, positive orthant) ----
def minimize_gMAM(path, bvec, a, b, metric="demographic", eps=1e-4, **kw):
    """gMAM instanton + quasipotential for a batched substrate field bvec(X,a,b). Validated on
    Maier-Stein (gmam_maier_stein.py, plan §6.1) before any substrate number is trusted. `eps`
    regularizes the demographic boundary a⁻¹=1/max(x,eps) (report Ŝ vs eps on H per plan §5.3)."""
    drift = lambda X: bvec(X, a, b)                                  # noqa: E731
    ainv = lambda X: a_inv(X, metric, eps)                          # noqa: E731
    return gmam_minimize(path, drift, ainv, clip_pos=(metric == "demographic"), **kw)


# ---- diagnostics: project the instanton to reveal the off-subspace excursion (plan §7) ----
def cycle_proj(path, win=slice(0, 3)):
    """project the winning group onto the two non-uniform 3-cycle modes (origin = on the symmetric
    subspace where J≡0). Nonzero magnitude along the path = the instanton harvesting the current."""
    G = path[:, win]
    return G @ _CYC1, G @ _CYC2


def order_param(path):
    L = path[:, :3].sum(1); R = path[:, 3:].sum(1)
    return (L - R) / (L + R + 1e-12)                    # ee along the path (1 at attractor -> 0 at saddle)


# ---- per-substrate run config. mom = heavy-ball (boundary-stiff H needs it; calibrated 2026-06-04).
#      Result is robust across mom∈[0.8,0.95], seed_amp∈[0.05,0.3], turns∈[0.5,1.0]. ----
RUN = {
    "A": dict(dtau=2e-3, n_iter=14000, reparam_every=60, eps=1e-4, mom=0.9),
    "H": dict(dtau=5e-4, n_iter=40000, reparam_every=80, eps=1e-4, mom=0.95),
}


def run_substrate(name, eps=None, n_iter=None, dtau=None):
    cfg = RUN[name]; S = SUBSTRATES[name]; xS = saddle(name)
    eps = cfg["eps"] if eps is None else eps
    n_iter = cfg["n_iter"] if n_iter is None else n_iter
    dtau = cfg["dtau"] if dtau is None else dtau
    res = {"xS": xS}
    for tag, (a, b) in (("OFF", S["ab_off"]), ("ON", S["ab_on"])):
        xA = attractor(name, a, b)
        p0 = initial_path(xA, xS)
        path, Sh, hist = minimize_gMAM(p0, S["bvec"], a, b, eps=eps, n_iter=n_iter, dtau=dtau,
                                       reparam_every=cfg["reparam_every"], mom=cfg["mom"])
        res[tag] = dict(a=a, b=b, xA=xA, path=path, S=Sh, hist=hist,
                        spread=within_group_spread(path), spread0=within_group_spread(p0))
    res["dS"] = res["OFF"]["S"] - res["ON"]["S"]
    return res


def _panel(ax_sp, ax_cy, ax_bar, name, res, dVref):
    for tag, col in (("OFF", "#1f77b4"), ("ON", "#d62728")):
        p = res[tag]["path"]; s = np.linspace(0, 1, len(p))
        L = p[:, :3]; spr = L.max(1) - L.min(1)
        ax_sp.plot(s, spr, "-", color=col, lw=2, label=f"{tag}  Ŝ={res[tag]['S']:.3f}")
        c1, c2 = cycle_proj(p)
        ax_cy.plot(c1, c2, "-", color=col, lw=2, label=tag)
    ax_sp.set_xlabel("path progress (attractor→saddle)"); ax_sp.set_ylabel("within-group spread")
    ax_sp.set_title(f"[{name}] instanton bend"); ax_sp.legend(fontsize=8)
    ax_cy.scatter([0], [0], c="k", s=30, zorder=5); ax_cy.set_xlabel("3-cycle mode c₁")
    ax_cy.set_ylabel("c₂"); ax_cy.set_title(f"[{name}] off-subspace excursion"); ax_cy.legend(fontsize=8)
    ax_cy.set_aspect("equal", "box")
    bars = ax_bar.bar(["OFF a=b", "ON a≠b"], [res["OFF"]["S"], res["ON"]["S"]],
                      color=["#1f77b4", "#d62728"], alpha=0.85)
    for x, (lab, ref) in enumerate(zip(("OFF", "ON"), dVref)):
        if ref is not None:
            ax_bar.plot([x - 0.4, x + 0.4], [ref, ref], "k--", lw=1.3)
            ax_bar.annotate(f"ΔV={ref}", (x, ref), textcoords="offset points", xytext=(0, 4), fontsize=8)
    ax_bar.set_ylabel("Ŝ (quasipotential)")
    ax_bar.set_title(f"[{name}] ΔŜ={res['dS']:+.4f}")
    for bar, tag in zip(bars, ("OFF", "ON")):
        ax_bar.annotate(f"{res[tag]['S']:.3f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        textcoords="offset points", xytext=(0, 2), ha="center", fontsize=8)


def main():
    print("=" * 90)
    print("gMAM substrate run -- the instanton + quasipotential for current-aids-escape (plan §6.2/§6.3).")
    print("   minimizer validated on Maier-Stein (gmam_maier_stein.py: β=1→0.500 exact, PASS).")
    print("=" * 90)
    results = {}
    for name in ("A", "H"):                                          # A first (interior; plan §6 ladder)
        cfg = RUN[name]
        print(f"\n[{name}] dtau={cfg['dtau']:.0e} n_iter={cfg['n_iter']} eps={cfg['eps']:.0e}  "
              f"({SUBSTRATES[name]['mu_note']})")
        res = run_substrate(name)
        results[name] = res
        for tag in ("OFF", "ON"):
            r = res[tag]
            print(f"   {tag:3s} a={r['a']:.2f},b={r['b']:.2f}:  Ŝ {r['hist'][0]:.4f}→{r['S']:.4f}  "
                  f"spread {r['spread0']:.3f}→{r['spread']:.3f}  (reparams={len(r['hist'])})")
        ref = SUBSTRATES[name]["dV_ref"]
        refstr = f"   ref ΔV: OFF={ref[0]} ON={ref[1]}  ΔV_ref={None if ref[0] is None else round(ref[0]-ref[1],3)}"
        print(f"   ΔŜ_{name} = {res['dS']:+.4f}{refstr if ref[0] else '   (A: expect ΔŜ≈0, the null)'}")

    # ---- H eps-convergence (Tier-1 boundary check, plan §5.3) ----
    print("\n" + "-" * 90)
    print("[H] eps-convergence (boundary a⁻¹=1/max(x,eps); Ŝ should stabilize as eps→0):")
    eps_tab = []
    for epsv in (1e-3, 3e-4, 1e-4, 3e-5):
        rH = run_substrate("H", eps=epsv)
        eps_tab.append((epsv, rH["OFF"]["S"], rH["ON"]["S"], rH["dS"]))
        print(f"   eps={epsv:.0e}:  Ŝ(a=b)={rH['OFF']['S']:.4f}  Ŝ(a≠b)={rH['ON']['S']:.4f}  ΔŜ={rH['dS']:+.4f}")

    # ---- decision readout (plan §1) ----
    dSH, dSA = results["H"]["dS"], results["A"]["dS"]
    bendH = results["H"]["ON"]["spread"] - results["H"]["OFF"]["spread"]
    print("\n" + "=" * 90)
    print("DECISION READOUT (plan §1):")
    print(f"   D1 action drop : ΔŜ_H={dSH:+.4f} (target +0.056)   ΔŜ_A={dSA:+.4f} (target ≈0, null)")
    print(f"   D2 H bend      : spread ON={results['H']['ON']['spread']:.3f} vs OFF="
          f"{results['H']['OFF']['spread']:.3f}  (ON−OFF={bendH:+.3f}; want ON≫OFF, OFF≈0)")
    print(f"   D3 A null-geom : spread ON={results['A']['ON']['spread']:.3f} vs OFF="
          f"{results['A']['OFF']['spread']:.3f}")
    vind = (dSH > 0.02) and (abs(dSA) < 0.02) and (bendH > 0.02)
    verdict = ("VINDICATE+PROMOTE (scoped)" if vind else
               "KILL (ΔŜ_H≈0)" if abs(dSH) < 0.02 else "SCOPE/HOLD (re-examine)")
    print(f"   → tentative verdict: {verdict}   [weighty core edit — surface to Ron before committing]")
    print("=" * 90)

    # ---- figures ----
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    for row, name in enumerate(("A", "H")):
        _panel(axes[row, 0], axes[row, 1], axes[row, 2], name, results[name],
               SUBSTRATES[name]["dV_ref"])
    fig.suptitle(f"gMAM instanton — current-aids-escape   (verdict: {verdict})", fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "gmam_substrates.png", dpi=140); plt.close(fig)

    fig2, ax = plt.subplots(figsize=(7, 5))
    ev = np.array([e[0] for e in eps_tab])
    ax.plot(ev, [e[1] for e in eps_tab], "-o", label="Ŝ(a=b)", color="#1f77b4")
    ax.plot(ev, [e[2] for e in eps_tab], "-o", label="Ŝ(a≠b)", color="#d62728")
    ax.plot(ev, [e[3] for e in eps_tab], "-s", label="ΔŜ", color="#2ca02c")
    ax.axhline(0.328, color="#1f77b4", ls=":", lw=1); ax.axhline(0.272, color="#d62728", ls=":", lw=1)
    ax.axhline(0.056, color="#2ca02c", ls=":", lw=1)
    ax.set_xscale("log"); ax.invert_xaxis(); ax.set_xlabel("eps (→0)"); ax.set_ylabel("Ŝ")
    ax.set_title("[H] gMAM action — eps-convergence (dotted = committed Kramers ΔV)")
    ax.legend(); fig2.tight_layout(); fig2.savefig(OUT / "gmam_H_eps.png", dpi=140); plt.close(fig2)
    print(f"\n   figures -> gmam_substrates.png , gmam_H_eps.png")


if __name__ == "__main__":
    main()
