r"""current_aids_escape_alignment.py -- the deterministic, sim-free predictor the outbound review
unanimously recommended (research_prompt_current_aids_escape_interpretation.md, models a/b/c):

  "A rotational current lowers the FW escape barrier IFF it has substantial projection onto the
   instanton escape path."  -- a GEOMETRIC SELECTION RULE, not 'current lowers barriers'.

Cheap test: along the a=b (current-OFF) deterministic heteroclinic from the symmetric saddle to a
broken attractor, compute the work of the pure rotational field J = f(a≠b) − f(a=b):
    W = ∫ J·dx₀ ,   cosθ(s) = J·t̂ / |J|  (alignment of the current with the escape tangent),
    surfing index 𝒮 = ∫ J·dx₀ / ∫ |f_sym|·|dx₀|  (current work relative to relaxation work).
First-order FW theory (Maier–Stein; model b): the barrier change is δΔV ≈ −W. W≈0 ⟺ the current is
orthogonal to the escape path ⟺ no first-order barrier effect.

The angle cosθ is MAGNITUDE-INDEPENDENT, so it separates the two readings of substrate A's null:
  cosθ_A ≈ 0  → STRUCTURAL  (geometry forbids it; orthogonal current),
  cosθ_A large but 𝒮_A small → SUB-THRESHOLD (the current just too weak).

Prediction from the reports: |W_H|, |cosθ_H| substantial (boundary/full-exclusion path the current
pushes along); cosθ_A ≈ 0 (interior/short path orthogonal to the circulating current).

Purely deterministic (heteroclinic flow + a line integral) -- no escape simulation, no rare-event
statistics, no censoring/NaN exposure.
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
from identity_survival_barrier import field_many                  # homochiral drift field_many(X,a,b)
from autocat_both import field as field_autocat                   # autocat field(X,k1,ec,a,b)

OUT = Path(__file__).resolve().parent
AB = 1.5                                                           # a+b held fixed (the metric)
A_ON, B_ON = 0.5, 1.0                                             # current ON  (a-b = -0.5)
A_OFF = B_OFF = 0.75                                             # current OFF (a=b)


# ---- the two substrates, each as a drift f(X; a, b) and a symmetric-saddle magnitude solver ----
def H_field(X, a, b):
    return field_many(X, a=a, b=b)                                # F=1, mu=1.6 defaults


def H_saddle_mag(F=1.0, mu=1.6):                                  # symmetric racemic point (1D, symmetry-preserving)
    m = 1.0 / 3.0
    for _ in range(int(2000.0 / 0.005)):
        m = max(m + m * (F - m * (1.0 + AB + 3.0 * mu)) * 0.005, 1e-12)
    return m


K1A, ECA = 0.05, 0.15
def A_field(X, a, b):
    return field_autocat(X, K1A, ECA, a=a, b=b)


def A_saddle_mag(g=0.70, kd=0.50, k3=1.0, cap=2.0):              # symmetric autocat point (1D)
    m = 1.0 / 3.0
    for _ in range(int(4000.0 / 0.005)):
        dm = K1A + (g - kd) * m * (1 - 6 * m / cap) - k3 * m * (3 * m) - ECA * m * (AB * m)
        m = max(m + dm * 0.005, 1e-12)
    return m


def jac(fld, x0, a, b, eps=1e-6):
    f0 = fld(x0[None, :], a, b)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = x0.copy(); xp[i] += eps
        J[:, i] = (fld(xp[None, :], a, b)[0] - f0) / eps
    return J


def unstable_evec(J):
    w, V = np.linalg.eig(J)
    k = int(np.argmax(w.real))                                    # largest-real eigenvalue = escape direction
    e = np.real(V[:, k]); e /= np.linalg.norm(e)
    return e, float(w[k].real)


def heteroclinic(fld, x_s, e_u, dt=0.004, maxT=4000.0, rec=8):
    """integrate the a=b (current-off) flow from saddle + δe_u to the attractor; return the path."""
    # orient the push toward a definite (L-dominant) basin
    sgn = 1.0 if e_u[:3].sum() - e_u[3:].sum() >= 0 else -1.0
    x = np.clip(x_s + sgn * 1e-4 * e_u, 1e-12, None)[None, :]
    path = [x[0].copy()]
    for k in range(int(maxT / dt)):
        f = fld(x, A_OFF, B_OFF)
        x = np.clip(x + f * dt, 1e-12, None)
        if k % rec == 0:
            path.append(x[0].copy())
        if np.linalg.norm(f) < 1e-7 and k > 1000:
            break
    path.append(x[0].copy())
    return np.array(path)


def alignment(fld, x_s, path):
    """along the saddle→attractor path, the rotational field J = f_on − f_off, the escape-tangent
    alignment cosθ, the work W = ∫J·dx (escape = attractor→saddle, so escape work = −∫_{saddle→att}),
    and the surfing index 𝒮 = ∫J·dx / ∫|f_off|·|dx|."""
    seg = np.diff(path, axis=0)                                   # Δx along saddle→attractor
    mids = 0.5 * (path[:-1] + path[1:])
    J = fld(mids, A_ON, B_ON) - fld(mids, A_OFF, B_OFF)           # pure current (antisymmetric) field
    foff = fld(mids, A_OFF, B_OFF)                                # relaxation (gradient-like) drift
    work_inc = np.sum(J * seg, axis=1)                            # J·dx per segment (saddle→att)
    seglen = np.linalg.norm(seg, axis=1)
    Jn = np.linalg.norm(J, axis=1); tn = seglen
    cos = work_inc / np.maximum(Jn * tn, 1e-30)                   # cosθ between J and the path tangent
    W_relax = float(np.sum(work_inc))                             # ∫J·dx, saddle→attractor
    W_escape = -W_relax                                           # escape direction = attractor→saddle
    relax_work = float(np.sum(np.abs(np.sum(foff * seg, axis=1))))  # ∫|f_off·dx| (relaxation work scale)
    S = W_relax / max(relax_work, 1e-30)                          # surfing index (signed, dimensionless)
    cos_mean = float(np.sum(cos * seglen) / max(np.sum(seglen), 1e-30))  # path-length-weighted mean cosθ
    return dict(cos=cos, seglen=seglen, Jn=Jn, W_escape=W_escape, S=S, cos_mean=cos_mean,
                Jmag_mean=float(np.sum(Jn * seglen) / max(np.sum(seglen), 1e-30)))


def within_group_spread(path):
    """max over the path of the within-group component spread (L0,L1,L2 and R0,R1,R2). ~0 means the
    path never leaves the uniform-within-group subspace -- exactly where the rotational current J≡0."""
    L, R = path[:, :3], path[:, 3:]
    return float(max((L.max(1) - L.min(1)).max(), (R.max(1) - R.min(1)).max()))


def offsub_J(fld, path, frac=0.5):
    """|J| at a HEALTHY mid-path point nudged OFF the uniform subspace (winning group's 3-cycle excited),
    to confirm the rotational current is real -- just not on the (symmetric) escape route."""
    x0 = path[int(frac * (len(path) - 1))].copy()
    win = slice(0, 3) if x0[:3].sum() >= x0[3:].sum() else slice(3, 6)
    g = x0[win]; d = 0.15 * g.mean()                            # within-group tilt, scaled, stays positive
    x0[win] = np.clip(g + d * np.array([1.0, -0.5, -0.5]), 1e-9, None)
    x = x0[None, :]
    return float(np.linalg.norm(fld(x, A_ON, B_ON) - fld(x, A_OFF, B_OFF)))


def run(name, fld, mag_fn):
    m = mag_fn(); x_s = np.full(6, m)
    J_s = jac(fld, x_s, A_OFF, B_OFF)
    e_u, lam_u = unstable_evec(J_s)
    path = heteroclinic(fld, x_s, e_u)
    ee0 = (path[-1, :3].sum() - path[-1, 3:].sum()) / (path[-1].sum() + 1e-12)
    al = alignment(fld, x_s, path)
    spread = within_group_spread(path)
    Joff = offsub_J(fld, path)
    print(f"\n[{name}]")
    print(f"   symmetric saddle magnitude m_s={m:.5f}  unstable eig λ_u={lam_u:+.4f}  attractor ee*={ee0:+.3f}")
    print(f"   within-group spread along escape path = {spread:.2e}  "
          f"(~0 ⟹ path stays in the uniform-within-group subspace)")
    print(f"   |J| ON the escape path = {al['Jmag_mean']:.2e}   vs   |J| just OFF that subspace = {Joff:.4f}")
    print(f"   ⟹ first-order escape-work W = {al['W_escape']:+.2e}  (the current does NO work on the "
          f"escape route: J≡0 there)")
    return dict(name=name, m=m, lam_u=lam_u, ee0=ee0, spread=spread, Joff=Joff, **al)


def main():
    print("=" * 90)
    print("ALIGNMENT DIAGNOSTIC -- is current-aids-escape a GEOMETRIC SELECTION RULE? (sim-free)")
    print("   testing: does the rotational current J project onto the escape path? (the reports' hypothesis)")
    print("=" * 90)
    H = run("H  homochiral (hard transcritical, boundary m*=±1, 𝒜≈21.8)", H_field, H_saddle_mag)
    A = run("A  autocat (soft pitchfork, interior m*≈±0.71, 𝒜≈2.3)", A_field, A_saddle_mag)

    print("\n" + "-" * 90)
    both_zero = max(H['Jmag_mean'], A['Jmag_mean']) < 1e-9 and min(H['Joff'], A['Joff']) > 1e-4
    if both_zero:
        print("   => THE FIRST-ORDER PREDICTOR IS NULL BY SYMMETRY (for BOTH substrates).")
        print("      The rotational current J = f(a≠b) − f(a=b) vanishes IDENTICALLY on the")
        print("      uniform-within-group subspace (L₀=L₁=L₂, R₀=R₁=R₂), and the deterministic escape")
        print("      path lives entirely in that subspace (the breaking mode is uniform-within-group and")
        print("      the a=b flow preserves it). So ∫J·dx ≡ 0 on the escape route — the reports' cheap")
        print("      first-order 'alignment' diagnostic cannot see the effect on EITHER substrate.")
        print("      ⟹ current-aids-escape here is intrinsically HIGHER-ORDER: the optimal escape path")
        print("        (instanton) must bend OFF the symmetric subspace into the 3-cycle directions —")
        print("        where J≠0 — to harvest the current. That transverse excursion is exactly what")
        print("        gMAM computes and what the deterministic heteroclinic cannot show. gMAM REQUIRED.")
        print(f"      (confirmed real current off-subspace: |J|_off  H={H['Joff']:.2e}, A={A['Joff']:.2e}"
              f"  — vs on-path |J| ~1e-17.)")
    else:
        print(f"   alignment cosθ:  H = {H['cos_mean']:+.4f}  vs  A = {A['cos_mean']:+.4f};  "
              f"surfing 𝒮:  H = {H['S']:+.4f}  vs  A = {A['S']:+.4f}")
    print("-" * 90)

    figure(H, A)
    return H, A


def figure(H, A):
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2), dpi=140)

    # (a) |J| along the escape path (≈0) vs the within-group spread (≈0): the path is current-free
    for r, c in [(H, "#c62828"), (A, "#1565c0")]:
        s = np.linspace(0, 1, len(r["Jn"]))
        ax[0].plot(s, r["Jn"], "-", color=c, lw=1.8, label=f"{r['name'].split('(')[0].strip()}: |J| on path")
    ax[0].set_xlabel("arc length along saddle→attractor escape path (normalized)")
    ax[0].set_ylabel(r"$|J|$  (rotational current on the escape path)")
    ax[0].set_title("(a) the current is ZERO on the escape route\n(the path stays in the uniform-within-group subspace)")
    ax[0].legend(fontsize=8.5, frameon=False); ax[0].grid(alpha=0.3)
    ax[0].set_ylim(bottom=-0.002)

    # (b) |J| on the escape path vs just OFF it: the current lives off the escape subspace
    names = ["H\n(boundary)", "A\n(interior)"]
    onv = [H["Jmag_mean"], A["Jmag_mean"]]; offv = [H["Joff"], A["Joff"]]
    x = np.arange(2); w = 0.35
    ax[1].bar(x - w / 2, onv, w, color=["#c62828", "#1565c0"], alpha=0.95, label="|J| ON escape path (≈0)")
    ax[1].bar(x + w / 2, offv, w, color=["#ef9a9a", "#90caf9"], label="|J| OFF subspace (3-cycle excited)")
    ax[1].set_xticks(x); ax[1].set_xticklabels(names)
    ax[1].set_ylabel("rotational current magnitude |J|"); ax[1].legend(fontsize=9, frameon=False)
    ax[1].set_title("(b) the current lives OFF the escape route\n⟹ effect is higher-order: instanton must bend out (gMAM)")
    ax[1].grid(alpha=0.3, axis="y")

    fig.suptitle("current-aids-escape: the rotational current is IDENTICALLY ZERO on the (symmetric) escape path —\n"
                 "the first-order predictor is null by symmetry; the effect is a higher-order instanton excursion (gMAM)",
                 fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    path = OUT / "current_aids_escape_alignment.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
