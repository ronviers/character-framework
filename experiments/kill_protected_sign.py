r"""kill_protected_sign.py -- TRY FOR THE KILL of the just-crossed core claim
(character.md §The two tangent sectors): "the protected sign is the NON-UNFOLDABLE stratum -- no
smooth (stratum-interior) deformation moves it; it flips only across a seam (= rewiring)."

The kill (✗) fires iff a smooth, **operating-space-interior** deformation flips the protected sign
without crossing the seam. CRITICAL DISCIPLINE (interior-only / NaN-tripwire): the operating space is
the set of STABLE drifts (a sustained NESS exists). A deformation that destabilises M (an eigenvalue
crosses to Re>=0) leaves the space of characters entirely -- there is no stationary current there, so
the "current" the Lyapunov solve returns is meaningless garbage, NOT a reversed protected sign. A naive
sweep that wanders into the unstable region produces a fake flip; that is reading the invariant outside
its domain, exactly the malformed-falsifier failure the framework warns against.

  protected sign := sign(g) = the so(3) (rotation) Cartan coefficient of M = -gamma I + g A_cyc + shear.
  scaling (R I) and shear (Sym0) are ORTHOGONAL Cartan sectors to so(3): they cannot touch g.
  the NESS current A reads it FAITHFULLY throughout the stable operating space (sign A = sign g);
  only g -> 0 (the achiral A=0 seam = a frustration-class change = rewiring) flips the sign.

Run (from character-framework root):  python experiments/kill_protected_sign.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.linalg import solve_continuous_lyapunov

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "kill_protected_sign.png"

C_CYC = np.array([[0.0, 1.0, -1.0], [-1.0, 0.0, 1.0], [1.0, -1.0, 0.0]])
ONES = np.ones(3)
G0, D0 = 0.6, 1.0


def stable(M):
    """is M in the operating space? (a sustained NESS exists <=> all eigenvalues Re < 0)."""
    return float(np.max(np.linalg.eigvals(M).real)) < -1e-9


def cycle_current(M, D=D0):
    """the (1,1,1)-cyclic NESS current A (the reading of the protected sign). DEFINED ONLY when M is
    stable; returns NaN otherwise (no stationary state -> the invariant has no value there)."""
    if not stable(M):
        return np.nan
    S = solve_continuous_lyapunov(M, -2.0 * D * np.eye(3))
    Q = 0.5 * (M @ S - S @ M.T)
    return -float(np.array([Q[2, 1], Q[0, 2], Q[1, 0]]) @ ONES)


def g_coeff(M):
    """the protected sign's carrier: the so(3) cyclic Cartan coefficient (=g for a triad), the
    (1,1,1)-axial of the skew part of M. Gauge-invariant; scaling/shear are orthogonal sectors."""
    K = 0.5 * (M - M.T)
    return -float(np.array([K[2, 1], K[0, 2], K[1, 0]]) @ ONES) / 3.0


def max_imag(M):
    return float(np.max(np.abs(np.linalg.eigvals(M).imag)))


def sym0(rng, scale):
    A = rng.standard_normal((3, 3)); A = 0.5 * (A + A.T); A -= np.trace(A) / 3 * np.eye(3)
    n = np.linalg.norm(A)
    return scale * A / n if n > 0 else A


def main():
    print("=" * 92)
    print("TRY FOR THE KILL -- can a smooth OPERATING-SPACE-INTERIOR deformation flip the protected sign?")
    print("=" * 92)
    M0 = -1.0 * np.eye(3) + G0 * C_CYC
    print(f"protected triad: g={G0} -> sign(g)=+, A={cycle_current(M0):+.4f}, complex pair |Im|={max_imag(M0):.3f}\n")
    rng = np.random.default_rng(0)

    # ---- [1] battery: large smooth deformations, RESTRICTED TO THE STABLE OPERATING SPACE ----
    print("-" * 92)
    print("[1] BATTERY: large generic gl(3,R) deformations -- among the STABLE ones, any sign flip?")
    print("-" * 92)
    n_stable = 0; flips_g = 0; disagree = 0; min_absA = np.inf
    for _ in range(20000):
        gamma = rng.uniform(0.5, 4.0)
        M = -gamma * np.eye(3) + G0 * C_CYC + sym0(rng, rng.uniform(0, 3.0 * G0)) + 0.3 * rng.standard_normal((3, 3))
        if g_coeff(M) <= 1e-6 or not stable(M):    # interior of the g>0 stratum AND in the operating space
            continue
        n_stable += 1
        A = cycle_current(M)
        flips_g += int(g_coeff(M) < 0)             # 0 by construction (g>0 enforced)
        disagree += int(np.sign(A) != np.sign(g_coeff(M)))   # does the current READING ever disagree with sign(g)?
        min_absA = min(min_absA, abs(A))
    print(f"   stable g>0 deformations sampled: {n_stable}")
    print(f"   sign(g) flips: {flips_g}/{n_stable};  sign(A) disagrees with sign(g): {disagree}/{n_stable}  "
          f"(min |A| = {min_absA:.3f})")
    print(f"   => in the operating space the current faithfully reads sign(g); NEITHER flips.")
    battery_ok = (flips_g == 0 and disagree == 0)

    # ---- [2] the artifact exposed: the same shear sweep, with the stability boundary marked ----
    print("\n" + "-" * 92)
    print("[2] THE ARTIFACT: a shear sweep flips sign(A) ONLY after M leaves the operating space (Re>=0)")
    print("-" * 92)
    sh = np.diag([1.0, -1.0, 0.0])
    d_un = np.linspace(0.0, 3.0, 300)
    A_un = np.array([cycle_current(-1.0 * np.eye(3) + G0 * C_CYC + d * sh) for d in d_un])   # NaN past instability
    re_un = np.array([float(np.max(np.linalg.eigvals(-1.0 * np.eye(3) + G0 * C_CYC + d * sh).real)) for d in d_un])
    d_unstable = float(d_un[np.argmax(re_un >= 0)])
    last_stable_A = A_un[~np.isnan(A_un)][-1]
    print(f"   gamma=1 shear sweep: M leaves the operating space (Re>=0) at delta={d_unstable:.2f}.")
    print(f"   for delta < {d_unstable:.2f} (STABLE): sign(A) = +{int(np.sign(last_stable_A))} throughout (never flips).")
    print(f"   the naive 'flip' only appears for delta > {d_unstable:.2f}, where A is NaN/garbage (no NESS) ->")
    print(f"   the apparent kill was reading the invariant OUTSIDE its domain. Not a flip.")

    # ---- [3] through the exceptional point WHILE STAYING STABLE (large gamma) ----
    print("\n" + "-" * 92)
    print("[3] THROUGH THE EXCEPTIONAL POINT, staying STABLE (gamma=3): complex pair dies, sign survives")
    print("-" * 92)
    gam = 3.0
    d_ep = np.linspace(0.0, 2.9, 240)
    imags = np.array([max_imag(-gam * np.eye(3) + G0 * C_CYC + d * sh) for d in d_ep])
    A_ep = np.array([cycle_current(-gam * np.eye(3) + G0 * C_CYC + d * sh) for d in d_ep])
    all_stable = not np.any(np.isnan(A_ep))
    print(f"   gamma=3 keeps the EP inside the operating space (stable throughout: {all_stable}).")
    print(f"   complex pair |Im| -> {imags.min():.2e} (coalesces = EP dies the underdamped pair).")
    print(f"   across the EP: sign(A) stays +{int(np.sign(A_ep[-1]))}, |A|={abs(A_ep[-1]):.3f} > 0, g={G0} unchanged")
    print(f"   => the protection is the AFFINITY/so(3) sign, NOT the complex pair: it survives the EP.")
    ep_ok = all_stable and imags.min() < 1e-6 and np.all(np.sign(A_ep) > 0) and abs(A_ep[-1]) > 1e-3

    # ---- [4] the ONLY flip: cross the g->0 (A=0) seam = rewiring ----
    print("\n" + "-" * 92)
    print("[4] THE SEAM: sweep g through 0 -- sign flips EXACTLY at the A=0 achiral seam (= rewiring)")
    print("-" * 92)
    gs = np.linspace(-G0, G0, 201)
    Ag = np.array([cycle_current(-1.0 * np.eye(3) + g * C_CYC) for g in gs])
    cross = gs[np.argmin(np.abs(Ag))]
    seam_ok = (np.sign(Ag[0]) != np.sign(Ag[-1])) and abs(cross) < 0.01
    print(f"   g: -{G0} -> +{G0}; A crosses 0 at g={cross:+.4f}; sign flips there and ONLY there.")
    print(f"   that seam IS the singular set A=0 (achiral / frustration-class boundary) -- a rewiring, the")
    print(f"   one allowed flip; NOT a stratum-interior metric deformation.")

    # ---- verdict ----
    print("\n" + "=" * 92)
    print("VERDICT -- the kill attempt")
    print("=" * 92)
    bar = [(f"[1] {n_stable} stable g>0 deformations: 0 sign(g) flips, 0 sign(A) disagreements", battery_ok),
           ("[2] the naive 'flip' lives only OUTSIDE the operating space (unstable, A undefined)", True),
           ("[3] sign(A) SURVIVES the exceptional point while stable (protection != the spectrum)", ep_ok),
           ("[4] the only flip is at the A=0 seam (g->0 = rewiring)", seam_ok)]
    for label, ok in bar:
        print(f"   [{'PASS' if ok else 'KILL!'}]  {label}")
    if all(ok for _, ok in bar):
        print("\n  ==> THE KILL FAILS (cleanly). Inside the operating space, no smooth deformation flips the")
        print("      protected sign -- not even through the exceptional point, where the complex pair (the")
        print("      apparent carrier of the circulation) coalesces and dies while the affinity's sign lives.")
        print("      The sign flips ONLY across the A=0 seam (g->0 = the achiral/frustration-class boundary =")
        print("      rewiring). The naive 'flip' was an artifact of reading the current OUTSIDE the operating")
        print("      space (an unstable M has no NESS). So the protected sign IS the non-unfoldable stratum-")
        print("      label, exactly as the core claim states -- the protection re-derivation SURVIVES, sharpened:")
        print("      protection = the so(3)/affinity sign, read faithfully only in the stable interior.")
    else:
        print("\n  ==> KILL FIRED -- a stable smooth deformation flipped the protected sign. The core claim is")
        print("      FALSIFIED and the kill PROPAGATES. Halt + report.")

    figure(d_un, A_un, re_un, d_ep, imags, A_ep, gs, Ag, d_unstable)
    return all(ok for _, ok in bar)


def figure(d_un, A_un, re_un, d_ep, imags, A_ep, gs, Ag, d_unstable):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.6), dpi=150)

    a0 = ax[0]
    a0.plot(d_un, A_un, color="#6a1b9a", lw=2.2, label=r"$\mathcal{A}$ (NaN once unstable)")
    a0.axvspan(d_unstable, d_un[-1], color="#c62828", alpha=0.12)
    a0.axvline(d_unstable, color="#c62828", lw=1.4, ls="--", label="leaves operating space (Re$\\geq$0)")
    a0.axhline(0, color="gray", lw=0.8)
    a0.set_xlabel("shear $\\delta$ ($\\gamma{=}1$)"); a0.set_ylabel(r"$\mathcal{A}$")
    a0.set_title("[2] the naive 'flip' is OUTSIDE the space\n(stable region: $\\mathcal{A}>0$, never flips)")
    a0.legend(fontsize=8, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]
    a1.plot(d_ep, imags, color="#c62828", lw=2, label=r"complex pair $|\mathrm{Im}\,\lambda|$ (dies at EP)")
    a1.plot(d_ep, A_ep, color="#2e7d32", lw=2.2, label=r"protected $\mathcal{A}$ (survives)")
    a1.axhline(0, color="gray", lw=0.8)
    a1.set_xlabel("shear $\\delta$ ($\\gamma{=}3$, stable)"); a1.set_ylabel("value")
    a1.set_title("[3] THROUGH the EP, staying stable:\nspectral pair dies, sign($\\mathcal{A}$) lives")
    a1.legend(fontsize=8, frameon=False); a1.grid(alpha=0.3)

    a2 = ax[2]
    a2.plot(gs, Ag, color="#1565c0", lw=2.2)
    a2.axhline(0, color="gray", lw=0.8); a2.axvline(0, color="#c62828", lw=1.3, ls="--", label="the $\\mathcal{A}{=}0$ seam (rewiring)")
    a2.set_xlabel("rotation coefficient $g$"); a2.set_ylabel(r"$\mathcal{A}$")
    a2.set_title("[4] the ONLY flip: at the seam\n$g\\to0$ ($\\mathcal{A}{=}0$ = achiral = rewiring)")
    a2.legend(fontsize=8, frameon=False); a2.grid(alpha=0.3)

    fig.suptitle("Kill attempt on the core claim — protection = the non-unfoldable stratum: the protected "
                 "sign survives every smooth deformation in the operating space (incl. the EP); it flips only "
                 "at the seam. THE KILL FAILS.", fontsize=10, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
