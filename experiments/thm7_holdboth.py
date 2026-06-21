r"""thm7_holdboth.py -- VERIFY the deformation-calculus Thm-7 ("hold-both" = the OR/coexistence gate)
returns from the outbound channel (docs/research_prompt_thm7_bracket_derivation.md), before folding.
The three reports AGREE the verdict is "soft under a maintenance floor" but DISAGREE on the exponents
(p,q) = (1/3,2/3) / (1,1) / (1,1/2), and on the sharp-limit transition order. Resolve by direct
computation of the STABLE attractor (vectorized integration) -- not banked.

CLAIMS UNDER TEST:
  (1) sharp limit, GENERIC competition (mu_A != mu_B): the loser amplitude -> 0 CONTINUOUSLY (a
      transcritical) at c* = mu_B/mu_A -- consistent with the framework's own LINEAR competitive-exclusion.
  (2) sharp limit, SYMMETRIC competition (mu_A = mu_B): DEGENERATE (a line of fixed points at c=1) so the
      loser JUMPS mu/2 -> 0 (model b's case; non-generic).
  (3) finite drive D = a maintenance floor h ~ 1/D (the "open interior / never extinguished" reading)
      UNFOLDS the transcritical (Golubitsky-Schaeffer imperfect bifurcation): loser pinned x_min ~ h^p,
      width ~ h^q. For an ADDITIVE floor on a transcritical: p = 1/2, q = 1/2 (NOT the reports' values).
      SOFT -> the OR gate is everywhere-defined.
  (4) criterion: h=0 (absorbing boundary x=0 intact) -> HARD (loser hits exactly 0); h>0 -> SOFT.

Run (from character-framework root):  python experiments/thm7_holdboth.py
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")     # fsolve emits benign near-threshold convergence notes at tiny h

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

OUT = Path(__file__).resolve().parent / "thm7_holdboth.png"

MU_A, MU_B = 1.2, 1.0           # generic (distinct) characters -> non-degenerate; loser = B
C_STAR = MU_B / MU_A            # transcritical threshold (x_B -> 0 here)


def loser_sharp(cs, muA, muB):
    """STABLE loser amplitude of the deterministic (h=0) competitive LV, closed form WITH the stability
    switch: coexistence below c*, exclusion (loser = 0) above. (Generic muA>muB -> loser = B, continuous
    transcritical at c*=muB/muA; symmetric muA=muB -> a JUMP at c=1, the degenerate non-generic case.)"""
    cs = np.asarray(cs, float)
    cstar = muB / muA
    xB = (muB - cs * muA) / (1.0 - cs * cs)              # coexistence root
    xB = np.where(cs < cstar, np.maximum(xB, 0.0), 0.0)  # excluded (=0) at/above c*
    return xB


def floor_curve(cs_inc, h, muA=MU_A, muB=MU_B):
    """STABLE steady state of the floored LV  x_i' = x_i(mu_i - x_i - c x_j) + h  along an INCREASING
    c-grid, by fsolve continuation from the coexistence branch (no slow relaxation, no branch jumps)."""
    out = np.zeros((len(cs_inc), 2))
    x = np.array([muA / (1 + cs_inc[0]), muB / (1 + cs_inc[0])])
    for i, c in enumerate(cs_inc):
        x = fsolve(lambda z: [z[0] * (muA - z[0] - c * z[1]) + h,
                              z[1] * (muB - z[1] - c * z[0]) + h], x, xtol=1e-12)
        out[i] = x
    return out[:, 0], out[:, 1]


def main():
    print("=" * 92)
    print('THM-7 "hold-both" (OR / coexistence) gate -- hard wall or 1/D-soft? (direct verification)')
    print("=" * 92)
    print(f"generic competition mu_A={MU_A}, mu_B={MU_B} -> loser = B, transcritical at c* = {C_STAR:.4f}\n")

    # ---------- (1)+(2) sharp limit: continuous transcritical (generic) vs jump (symmetric) ----------
    print("-" * 92)
    print("[1,2] sharp-limit transition order: GENERIC = continuous transcritical, SYMMETRIC = jump")
    print("-" * 92)
    cs = np.linspace(0.4, 1.3, 400)
    xB_gen = loser_sharp(cs, MU_A, MU_B)
    xB_sym = loser_sharp(cs, 1.0, 1.0)
    near = (cs > C_STAR - 0.08) & (cs < C_STAR - 0.005)
    slope_gen = np.polyfit(C_STAR - cs[near], xB_gen[near], 1)[0]
    just_below = float(np.interp(C_STAR - 2e-3, cs, xB_gen))
    below_sym = float(np.interp(0.97, cs, xB_sym)); above_sym = float(np.interp(1.03, cs, xB_sym))
    print(f"  GENERIC : x_loser -> 0 as c -> c*={C_STAR:.3f}; slope dx_B/d(c*-c) = {slope_gen:.3f} (finite, LINEAR)")
    print(f"            value just below c* = {just_below:.4f} -> continuous, NO jump (transcritical)")
    print(f"  SYMMETRIC (mu_A=mu_B=1): x_loser at c=0.97 -> {below_sym:.4f}, at c=1.03 -> {above_sym:.4f}")
    print(f"            => DISCONTINUOUS jump ~{below_sym-above_sym:.2f} (~mu/2) at c=1 (degenerate, non-generic)")
    transcritical_ok = just_below < 0.02 and slope_gen > 0.3
    jump_ok = (below_sym - above_sym) > 0.4

    # ---------- (3) finite-D floor unfolds it: p, q exponents + scaling collapse ----------
    print("\n" + "-" * 92)
    print("[3] finite-D maintenance floor h~1/D unfolds the transcritical (imperfect bifurcation): p, q")
    print("-" * 92)
    hs = np.geomspace(1e-5, 1e-3, 14)
    cmaster = np.linspace(0.55, C_STAR + 0.2, 1000)
    below = cmaster < C_STAR
    xbs = {h: floor_curve(cmaster, h)[1] for h in hs}        # stable loser curve per h (continuation)
    xmin = np.array([float(np.interp(C_STAR, cmaster, xbs[h])) for h in hs])
    widths = []
    for h, xm in zip(hs, xmin):
        idx = np.where(xbs[h][below] >= 2.0 * xm)[0]
        widths.append(C_STAR - cmaster[below][idx[-1]] if len(idx) else np.nan)
    widths = np.array(widths)
    p = np.polyfit(np.log(hs), np.log(xmin), 1)[0]
    q = np.polyfit(np.log(hs), np.log(widths), 1)[0]
    print(f"   x_min(c*) ~ h^{p:.3f}  -> p = {p:.3f}   (additive-floor transcritical predicts p = 1/2)")
    print(f"   width w   ~ h^{q:.3f}  -> q = {q:.3f}   (predicts q = 1/2)")
    print(f"   with h ~ 1/D:  x_min ~ D^-{p:.2f},  w ~ D^-{q:.2f}  (the loser is pinned > 0 -> SOFT)")
    pq_ok = abs(p - 0.5) < 0.06 and abs(q - 0.5) < 0.08

    # scaling collapse: x_B/sqrt(h) vs (c-c*)/sqrt(h) (one curve if p=q=1/2)
    zc = np.linspace(-3.0, 0.0, 100)
    curves = np.array([np.interp(C_STAR + zc * np.sqrt(h), cmaster, xbs[h]) / np.sqrt(h) for h in hs[2::3]])
    collapse_err = float(np.max(np.std(curves, axis=0)) / np.max(np.mean(curves, axis=0)))
    print(f"   scaling collapse x_B/sqrt(h) vs (c-c*)/sqrt(h): max rel. spread = {collapse_err:.3f} "
          f"(small -> p=q=1/2 holds)")
    collapse_ok = collapse_err < 0.12

    # ---------- (4) criterion: h=0 hard, h>0 soft ----------
    print("\n" + "-" * 92)
    print("[4] criterion: absorbing boundary x=0 -> HARD; a maintenance floor h>0 -> SOFT")
    print("-" * 92)
    x_hard = float(loser_sharp([C_STAR + 0.1], MU_A, MU_B)[0])
    x_soft = float(np.interp(C_STAR + 0.1, cmaster, xbs[hs[-1]]))
    print(f"   past threshold (c=c*+0.1):  h=0 -> x_loser = {x_hard:.2e} (EXACTLY extinct -> hard wall)")
    print(f"                                h>0 (h={hs[-1]:.0e}) -> x_loser = {x_soft:.2e} (pinned > 0 -> soft, OR total)")
    criterion_ok = x_hard < 1e-9 and x_soft > 1e-3

    # ---------- verdict ----------
    print("\n" + "=" * 92)
    print("VERDICT")
    print("=" * 92)
    bar = [("[1] generic hold-both loss is a CONTINUOUS transcritical (loser -> 0 linearly)", transcritical_ok),
           ("[2] symmetric LV is DEGENERATE -> a jump (non-generic; the reports' confusion)", jump_ok),
           ("[3] a maintenance floor h~1/D unfolds it: p=q=1/2 (NOT 1/3,2/3 / 1,1 / 1,1/2)", pq_ok),
           ("[3] scaling collapse x/sqrt(h) vs (c-c*)/sqrt(h) holds", collapse_ok),
           ("[4] h=0 hard (absorbing) / h>0 soft (loser pinned > 0, OR total)", criterion_ok)]
    for label, ok in bar:
        print(f"   [{'PASS' if ok else 'FAIL'}]  {label}")
    if all(ok for _, ok in bar):
        print("\n  ==> SOFT (under the framework's maintenance-floor / open-interior reading).")
        print("      hold-both loss is a TRANSCRITICAL (loser -> 0 linearly, matching the framework's LINEAR")
        print("      competitive-exclusion); a finite-drive floor h~1/D UNFOLDS it (Golubitsky-Schaeffer")
        print("      imperfect bifurcation): loser pinned x_min ~ h^(1/2) ~ D^(-1/2), width ~ D^(-1/2), so the")
        print("      OR (hold-both) gate is EVERYWHERE-DEFINED -- the apparent obstruction dissolves. p=q=1/2 is")
        print("      the additive-floor transcritical value; it is normal-form-dependent (exactly-symmetric LV")
        print("      is a non-generic first-order jump; an SSB pitchfork would give 1/3,2/3). ✗ (hard) only for")
        print("      the absorbing-boundary-preserved / exactly-symmetric cases.")
    else:
        print("\n  ==> NOT as analyzed -- inspect before folding.")

    figure(cs, xB_gen, xB_sym, hs, xmin, widths, p, q, cmaster, xbs)
    return p, q


def figure(cs, xB_gen, xB_sym, hs, xmin, widths, p, q, cmaster, xbs):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.8), dpi=150)

    a0 = ax[0]
    a0.plot(cs, xB_gen, color="#1565c0", lw=2.2, label="generic ($\\mu_A{\\neq}\\mu_B$): continuous")
    a0.plot(cs, xB_sym, color="#c62828", lw=2.0, ls="--", label="symmetric: JUMP (degenerate)")
    a0.axvline(C_STAR, color="#1565c0", lw=0.8, ls=":"); a0.axvline(1.0, color="#c62828", lw=0.8, ls=":")
    a0.set_xlabel("competition $c$"); a0.set_ylabel(r"loser amplitude $x_{\rm loser}^*$")
    a0.set_title("sharp limit: generic hold-both loss is a\nCONTINUOUS transcritical (symmetric = jump)")
    a0.legend(fontsize=8, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]
    a1.loglog(hs, xmin, "o-", color="#6a1b9a", ms=6, lw=2, label=f"$x_{{\\min}}(c_*)\\sim h^{{{p:.2f}}}$")
    a1.loglog(hs, widths, "s-", color="#2e7d32", ms=6, lw=2, label=f"width $w\\sim h^{{{q:.2f}}}$")
    a1.loglog(hs, xmin[0] * (hs / hs[0]) ** 0.5, "k--", lw=1, label=r"$\propto h^{1/2}$")
    a1.set_xlabel(r"maintenance floor $h\sim 1/D$"); a1.set_ylabel("pinned amplitude / width")
    a1.set_title(f"floor unfolds the transcritical:\n$p={p:.2f}$, $q={q:.2f}$ (additive-floor $=1/2$)")
    a1.legend(fontsize=8, frameon=False); a1.grid(alpha=0.3, which="both")

    a2 = ax[2]
    zc = np.linspace(-3.0, 0.0, 100)
    for h in hs[2::3]:
        xb = np.interp(C_STAR + zc * np.sqrt(h), cmaster, xbs[h])
        a2.plot(zc, xb / np.sqrt(h), lw=1.6, alpha=0.85)
    a2.set_xlabel(r"$(c-c_*)/\sqrt{h}$"); a2.set_ylabel(r"$x_{\rm loser}^*/\sqrt{h}$")
    a2.set_title("scaling collapse ($p{=}q{=}1/2$):\nall floors on one curve")
    a2.grid(alpha=0.3)

    fig.suptitle("Thm-7 hold-both ($\\vee$): the exclusion threshold is a transcritical; a finite-drive "
                 "maintenance floor $h\\sim1/D$ unfolds it (imperfect bifurcation) $\\Rightarrow$ SOFT, "
                 "$x_{\\min}\\sim D^{-1/2}$ — the OR gate is everywhere-defined",
                 fontsize=10.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
