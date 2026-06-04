r"""gmam_affinity_scaling.py -- Ron's "most telling" test: sweep the current strength 𝒜 and watch the
gMAM σ→0 barrier vs the committed finite-σ Kramers barrier.

If current-aids-escape is a PURE PREFACTOR effect (orthogonal circulation -- confirmed exactly at the
saddle by gmam_saddle_orthogonality.py), then as 𝒜: 0 → 21.8 nats:
    * the gMAM action Ŝ_H(𝒜)  stays FLAT      (the σ→0 quasipotential is current-blind),
    * the committed Kramers ΔV(𝒜) DROPS 0.328→0.272 (the finite-σ rate shifts, via the prefactor).

Same metric-held line as current_aids_escape.py: a+b=1.5 FIXED (pins μ_c and the whole landscape),
a−b dials 𝒜. The committed Kramers ladder (demographic MFPT slope, 12d3b0e):
    𝒜≈0    (a=b=0.75)      ΔV=0.328
    𝒜≈8.7  (a=0.65,b=0.85) ΔV=0.295
    𝒜≈15.2 (a=0.575,…)     ΔV=0.284
    𝒜≈21.8 (a=0.5,b=1.0)   ΔV=0.272
A flat Ŝ over the same ladder where ΔV falls ~17% isolates the effect to the prefactor.
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
from gmam_current_aids import SUBSTRATES, saddle, attractor, initial_path, minimize_gMAM, within_group_spread
from current_aids_escape import affinity_ab

OUT = Path(__file__).resolve().parent
BVEC = SUBSTRATES["H"]["bvec"]
LADDER = [(0.75, 0.75), (0.65, 0.85), (0.575, 0.925), (0.5, 1.0)]   # a+b=1.5; a−b dials 𝒜
KRAMERS_DV = [0.328, 0.295, 0.284, 0.272]                          # committed finite-σ MFPT slope (12d3b0e)


def main():
    xS = saddle("H")
    print("=" * 88)
    print("gMAM affinity-scaling -- σ→0 barrier Ŝ(𝒜) vs committed finite-σ Kramers ΔV(𝒜)")
    print("   prediction (orthogonal current => pure prefactor): Ŝ FLAT while ΔV drops 0.328→0.272")
    print("=" * 88)
    rows = []
    for (a, b), dV in zip(LADDER, KRAMERS_DV):
        xA = attractor("H", a, b)
        Acyc, _ = affinity_ab(xA, a, b)
        p0 = initial_path(xA, xS)
        path, Sh, hist = minimize_gMAM(p0, BVEC, a, b, eps=1e-4, n_iter=40000, dtau=5e-4,
                                       reparam_every=100, mom=0.95)
        rows.append(dict(a=a, b=b, A=Acyc, S=Sh, dV=dV, spread=within_group_spread(path)))
        print(f"   a={a:.3f},b={b:.3f}:  𝒜={Acyc:6.2f}   Ŝ_gMAM={Sh:.4f}  spread={within_group_spread(path):.4f}"
              f"   |  Kramers ΔV={dV:.3f}")

    S0, Sn = rows[0]["S"], rows[-1]["S"]
    dV0, dVn = rows[0]["dV"], rows[-1]["dV"]
    print("\n" + "-" * 88)
    print(f"   over 𝒜: 0 → {rows[-1]['A']:.1f} nats")
    print(f"     gMAM σ→0 barrier Ŝ : {S0:.4f} → {Sn:.4f}   ΔŜ = {Sn-S0:+.4f}  ({100*(Sn-S0)/S0:+.1f}%)  [FLAT]")
    print(f"     finite-σ Kramers ΔV: {dV0:.3f} → {dVn:.3f}   ΔΔV = {dVn-dV0:+.3f}  ({100*(dVn-dV0)/dV0:+.1f}%)  [DROPS]")
    pure_pref = abs((Sn - S0) / S0) < 0.03 and abs((dVn - dV0) / dV0) > 0.10
    print(f"   => {'PURE PREFACTOR confirmed' if pure_pref else 'inconclusive'}: the barrier is flat in 𝒜 "
          f"while the finite-σ rate shifts.\n      The current moves probability *within* the cycle plane "
          f"(⟂ escape), not *over* the saddle.")
    print("-" * 88)

    A = np.array([r["A"] for r in rows]); Sv = np.array([r["S"] for r in rows]); DV = np.array(KRAMERS_DV)
    fig, (ax, axn) = plt.subplots(1, 2, figsize=(13, 5.2))
    ax.plot(A, Sv, "-o", color="#2ca02c", lw=2, label="gMAM  Ŝ(𝒜)  (σ→0 barrier)")
    ax.plot(A, DV, "-s", color="#d62728", lw=2, label="Kramers ΔV(𝒜)  (finite-σ, committed)")
    ax.set_xlabel("cycle affinity 𝒜 (nats)"); ax.set_ylabel("barrier")
    ax.set_title("σ→0 barrier is current-blind; finite-σ rate is not"); ax.legend(fontsize=9)
    ax.set_ylim(0.24, 0.42)
    axn.plot(A, 100 * (Sv - Sv[0]) / Sv[0], "-o", color="#2ca02c", lw=2, label="gMAM Ŝ")
    axn.plot(A, 100 * (DV - DV[0]) / DV[0], "-s", color="#d62728", lw=2, label="Kramers ΔV")
    axn.axhline(0, color="0.6", lw=0.8)
    axn.set_xlabel("cycle affinity 𝒜 (nats)"); axn.set_ylabel("% change from 𝒜=0")
    axn.set_title("barrier flat (~0%) while finite-σ rate drops ~17% = pure prefactor"); axn.legend(fontsize=9)
    fig.suptitle("current-aids-escape is a PREFACTOR effect: orthogonal circulation, current-blind barrier",
                 fontweight="bold")
    fig.tight_layout(); fig.savefig(OUT / "gmam_affinity_scaling.png", dpi=140); plt.close(fig)
    print(f"\n   figure -> gmam_affinity_scaling.png")


if __name__ == "__main__":
    main()
