r"""rps_affinity.py -- RPS as the STRUCTURALLY-STORED exemplar (the contrast to homochiral's
spontaneously-frozen kind), instancing character.md's "two basin geometries" dichotomy.

The closure attempt revealed RPS is NOT a second spontaneously-frozen instance: the May-Leonard
triad has ONE coexistence fixed point and handedness = sign(α−β), set by the wiring and flipped
only by rewiring (α↔β) -- structurally stored, single basin, NO racemic saddle, so NO noise-driven
ΔV. What RPS gives instead is the structural half of the dichotomy:

  homochiral (spontaneously-frozen): two mirror basins, ΔV≈0.018 (noise escape) + 𝒜≈21.8 (affinity)
  RPS        (structurally-stored) : one basin, 𝒜 (affinity), NO ΔV; identity flips by REWIRING

Both carry a noise-independent affinity 𝒜 (computed here, reusing the validated rotational-OU frame
in cycle_affinity.py); only the spontaneously-frozen one hosts a noise-activated identity barrier.
This is exactly character.md's: "a structurally-stored bit occupies a single basin whose mirror is
not thermally reachable, so escape demands rewiring; a spontaneously-frozen bit occupies one of two
mirror basins split by a saddle ... escapes by a noise-driven crossing."
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
from cycle_affinity import ep_affinity, P   # noqa: E402  (validated rotational-OU affinity frame)

ALPHA, BETA = 0.5, 1.0                       # exact RPS operating point from rps_triad.py


def rps_jac(alpha, beta):
    """May-Leonard Jacobian at coexistence: M = -x*(I + αS + βS²), x*=1/(1+α+β)."""
    xs = 1.0 / (1.0 + alpha + beta)
    S = np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])
    return -xs * (np.eye(3) + alpha * S + beta * S @ S)


def main():
    print("=" * 80)
    print("RPS AFFINITY -- structurally-stored exemplar; the two-basin-geometries dichotomy")
    print("=" * 80)
    M = rps_jac(ALPHA, BETA)
    ev = np.linalg.eigvals(M)
    B2 = P @ M @ P.T
    hand = int(np.sign(ALPHA - BETA))
    print(f"RPS (α={ALPHA}, β={BETA}): coexistence Jacobian eigenvalues = {np.array2string(ev, precision=3)}")
    print(f"   handedness = sign(α−β) = {hand:+d}  (WIRING-set; flips only by α↔β rewiring)")
    print(f"   one fixed point, one basin -> NO racemic saddle -> NO noise-driven ΔV\n")

    print("cycle affinity 𝒜 at several noise levels (must be D-independent, like homochiral):")
    Ds = (0.01, 0.02, 0.04)
    As = []
    for d in Ds:
        r = ep_affinity(B2, d)
        As.append(r["Acyc"])
        print(f"   d=σ²={d:.3f}: κ={r['kappa']:.4f}, ω₀={r['om0']:.4f}, ⟨σ⟩={r['sigma']:.4f}, "
              f"𝒜={r['Acyc']:.4f} nats/cycle")
    A_rps = float(np.mean(As))
    spread = float(np.std(As))
    print(f"\n   𝒜(RPS) = {A_rps:.4f} nats/cycle  (spread over D = {spread:.2e} -> noise-INDEPENDENT)\n")

    print("-" * 80)
    print("  THE DICHOTOMY, two substrates, two basin geometries (character.md §Identity):")
    print(f"   homochiral (spontaneously-frozen): two mirror basins | ΔV≈0.018 (NOISE escape) | 𝒜≈21.8")
    print(f"   RPS        (structurally-stored)  : one basin         | NO ΔV (REWIRING flip)   | 𝒜≈{A_rps:.1f}")
    print("   => both carry a noise-independent affinity 𝒜; only the spontaneously-frozen substrate")
    print("      hosts a noise-activated identity barrier ΔV. The identity-survival barrier is the")
    print("      SPONTANEOUSLY-FROZEN-SPECIFIC quantity -- structurally-stored identity flips by rewiring.")
    print("      [closes the two-basin-geometries dichotomy; corrects RPS's misclassification as")
    print("       spontaneously-frozen]")
    print("-" * 80)
    return A_rps


if __name__ == "__main__":
    main()
