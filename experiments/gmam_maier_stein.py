r"""gmam_maier_stein.py -- §6.1 of docs/gmam_plan.md: the code-correctness gate for the gMAM minimizer.

Reproduce a PUBLISHED instanton/action before any homochiral number is trusted (the gMAM core lives in
gmam_current_aids.py: geom_action / geom_grad / arc_reparam / gmam_minimize).

Maier-Stein system (Maier & Stein 1993/1997; Heymann & Vanden-Eijnden 2008):
    b(x,y) = ( x - x^3 - beta*x*y^2 ,  -(1 + x^2)*y ) ,   additive noise (a = I).
Fixed points: stable (+-1, 0), saddle (0,0).  Escape studied: (-1,0) -> (0,0).

Two checks:
  (GATE, beta=1, GRADIENT)  d_x b1 = -2*beta*x*y = d_y b2  =>  b = -grad U with
        U = -x^2/2 + x^4/4 + (1+x^2)*y^2/2.   On-axis is the minimizer; EXACT action
        Shat = 2[U(0,0) - U(-1,0)] = 2*(1/4) = 0.5 ,  instanton on the x-axis (y == 0).
  (CAPABILITY, beta=10, NON-gradient, beta > beta_c ~ 4)  the optimal path BOWS OFF the x-axis
        (Maier-Stein symmetry-breaking of the MPEP) with action < 0.5 -- the same off-invariant-
        subspace bend the homochiral instanton must perform to harvest the protected current.

PASS  <=>  beta=1 action within ~2% of 0.5 AND on-axis (max|y| ~ 0) ; beta=10 action < 0.5 with max|y|>0.
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
from gmam_current_aids import geom_action, gmam_minimize, arc_reparam  # the core under test

OUT = Path(__file__).resolve().parent
X_A = np.array([-1.0, 0.0])           # source basin
X_S = np.array([0.0, 0.0])            # saddle
ADD_INV = lambda X: np.ones_like(X)   # additive metric a = I, batched  (noqa: E731)


def ms_drift(beta):
    def b(X):                          # batched: X (S,2) -> (S,2)
        x, y = X[:, 0], X[:, 1]
        return np.stack([x - x ** 3 - beta * x * y ** 2, -(1.0 + x ** 2) * y], axis=1)
    return b


def U(x, beta=1.0):                                   # potential (valid only at beta=1; for the contour)
    return -x[0] ** 2 / 2 + x[0] ** 4 / 4 + (1 + x[0] ** 2) * x[1] ** 2 / 2


def initial_path(N=80, ybump=0.15):
    """straight line (-1,0)->(0,0) with a sin y-bump: breaks the y->-y symmetry so a beta>beta_c path
    can bow out, and tests that beta=1 descent drives the bump back to the axis."""
    s = np.linspace(0, 1, N + 1)
    path = np.stack([(1 - s) * X_A[0] + s * X_S[0], ybump * np.sin(np.pi * s)], axis=1)
    return path


def run(beta, **kw):
    drift = ms_drift(beta)
    p0 = initial_path()
    path, S, hist = gmam_minimize(p0, drift, ADD_INV, clip_pos=False, **kw)
    return dict(beta=beta, path=path, S=S, hist=hist, maxy=float(np.abs(path[:, 1]).max()),
                S0=float(geom_action(p0, drift, ADD_INV)))


def main():
    print("=" * 88)
    print("gMAM VALIDATION GATE -- Maier-Stein (plan §6.1). Exact target: beta=1 action = 0.500, on-axis.")
    print("=" * 88)
    g1 = run(1.0, n_iter=15000, dtau=8e-3, reparam_every=25)
    g10 = run(10.0, n_iter=12000, dtau=1e-3, reparam_every=25)

    err = abs(g1["S"] - 0.5) / 0.5
    gate_b1 = (err < 0.01) and (g1["maxy"] < 5e-3)
    cap_b10 = (g10["S"] < 0.5 - 1e-3) and (g10["maxy"] > 1e-2)

    for g, tag, target in ((g1, "beta=1 (gradient)", "0.5000 exact"),
                           (g10, "beta=10 (non-grad)", "< 0.5, off-axis")):
        print(f"\n[{tag}]  target {target}")
        print(f"   S_hat: initial(seed)={g['S0']:.4f}  ->  minimized={g['S']:.4f}   "
              f"(iters tracked: {len(g['hist'])})")
        print(f"   instanton max|y| = {g['maxy']:.4f}   "
              f"({'ON-axis' if g['maxy'] < 1e-2 else 'OFF-axis (bowed out)'})")
    print(f"\n   beta=1  relative error vs 0.5 : {err*100:.2f}%")
    print("-" * 88)
    verdict = "PASS" if (gate_b1 and cap_b10) else "FAIL"
    print(f"   GATE (beta=1 -> 0.5 on-axis): {'PASS' if gate_b1 else 'FAIL'}    "
          f"CAPABILITY (beta=10 bow-out): {'PASS' if cap_b10 else 'FAIL'}")
    print(f"   §6.1 VERDICT: {verdict}  "
          f"-- {'minimizer trustworthy; proceed to A then H' if verdict=='PASS' else 'fix before substrates'}")
    print("-" * 88)

    # ---- figure: instantons over the U-contour + action convergence ----
    fig, (axp, axc) = plt.subplots(1, 2, figsize=(13, 5.2))
    xs = np.linspace(-1.4, 0.4, 220); ys = np.linspace(-0.85, 0.85, 220)
    XX, YY = np.meshgrid(xs, ys)
    UU = -XX ** 2 / 2 + XX ** 4 / 4 + (1 + XX ** 2) * YY ** 2 / 2
    axp.contour(XX, YY, UU, levels=24, colors="0.82", linewidths=0.7, zorder=0)
    axp.plot(g1["path"][:, 0], g1["path"][:, 1], "-", lw=2.4, color="#1f77b4",
             label=f"β=1  Ŝ={g1['S']:.3f} (exact 0.5)")
    axp.plot(g10["path"][:, 0], g10["path"][:, 1], "-", lw=2.4, color="#d62728",
             label=f"β=10 Ŝ={g10['S']:.3f} (bows out)")
    axp.plot([-1, 0], [0, 0], "k:", lw=1, label="x-axis (on-axis MAP)")
    axp.scatter([-1, 0], [0, 0], c="k", s=45, zorder=5)
    axp.annotate("attractor\n(-1,0)", (-1, 0), textcoords="offset points", xytext=(6, -28), fontsize=9)
    axp.annotate("saddle\n(0,0)", (0, 0), textcoords="offset points", xytext=(6, 8), fontsize=9)
    axp.set_xlabel("x"); axp.set_ylabel("y"); axp.set_title("Maier-Stein gMAM instantons")
    axp.legend(loc="lower left", fontsize=9); axp.set_aspect("equal", "box")
    axc.plot(np.arange(len(g1["hist"])), g1["hist"], "-o", ms=2.5, color="#1f77b4", label="β=1")
    axc.plot(np.arange(len(g10["hist"])), g10["hist"], "-o", ms=2.5, color="#d62728", label="β=10")
    axc.axhline(0.5, color="0.4", ls="--", lw=1, label="0.5 (exact β=1)")
    axc.set_xlabel("reparam step"); axc.set_ylabel("Ŝ (geometric action)")
    axc.set_title("action convergence"); axc.legend(fontsize=9)
    fig.suptitle(f"gMAM §6.1 validation gate -- VERDICT: {verdict}", fontweight="bold")
    fig.tight_layout()
    png = OUT / "gmam_maier_stein.png"
    fig.savefig(png, dpi=140); plt.close(fig)
    print(f"\n   figure -> {png.name}")
    return verdict


if __name__ == "__main__":
    sys.exit(0 if main() == "PASS" else 1)
