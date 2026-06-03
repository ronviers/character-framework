r"""reset_redrive_test.py -- the DIRECT discriminator for structurally-stored vs spontaneously-frozen,
run from the other side (measured, not inferred).

The classification claim is itself a test: reset fully from RANDOM initial conditions, re-drive,
and read the protected sign over many resets.
  structurally-stored  -> the sign RETURNS the same every reset (wiring-set)         -> ~100% one sign
  spontaneously-frozen -> the sign is RE-CHOSEN at random (broken-symmetry accident)  -> ~50/50

Homochiral is the known-spontaneous control (its H1 showed exact 50/50). RPS is the substrate whose
classification this session reclassified (spontaneous -> structural) by reading the code; here we
MEASURE it. If RPS is ~100% one sign it is structural (reclassification earns its place); if ~50/50
it is spontaneous (the original character.md was right -> revert).
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
from identity_survival_barrier import field_many as homo_field, ee, settle   # noqa: E402  (homochiral)

E1 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
E2 = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)


# ---- homochiral: protected sign = which hand wins (ee sign) ----
def homochiral_sign(seed, spread=0.06):
    rng = np.random.default_rng(seed)
    X = np.clip(0.2 + spread * rng.standard_normal((1, 6)), 1e-9, None)
    Xs = settle(X)
    return int(np.sign(ee(Xs)[0]))


# ---- RPS (May-Leonard): protected sign = spiral chirality = sign(circulation J) ----
def ml_field(x, a, b):
    xp = np.roll(x, -1); xm = np.roll(x, +1)
    return x * (1.0 - x - a * xp - b * xm)


def rps_sign(seed, a=0.5, b=1.0, sigma=0.01, T=1500.0, dt=0.01, spread=0.3):
    rng = np.random.default_rng(seed)
    xstar = np.full(3, 1.0 / (1.0 + a + b))
    x = np.clip(xstar + spread * rng.standard_normal(3), 1e-6, None)   # RANDOM initial condition
    n = int(T / dt); sq = np.sqrt(dt); burn = n // 5
    area = 0.0; cnt = 0
    for k in range(n):
        f = ml_field(x, a, b)
        xn = np.clip(x + f * dt + sigma * rng.standard_normal(3) * sq, 1e-6, None)
        if k > burn:
            d = x - xstar; dn = xn - xstar
            u = d @ E1; v = d @ E2
            udot = (dn @ E1 - u) / dt; vdot = (dn @ E2 - v) / dt
            area += (u * vdot - v * udot); cnt += 1
        x = xn
    return int(np.sign(area / max(cnt, 1)))


def report(name, signs, expect):
    s = np.array(signs)
    npos = int((s > 0).sum()); nneg = int((s < 0).sum())
    frac = max(npos, nneg) / len(s)
    verdict = "SPONTANEOUS (~50/50)" if frac < 0.7 else "STRUCTURAL (~one sign)"
    print(f"  {name:12s}: +{npos:2d} / -{nneg:2d}  over {len(s)} resets  ->  {100*frac:.0f}% majority  =>  {verdict}")
    print(f"               (expected: {expect})")
    return frac


def main():
    print("=" * 84)
    print("RESET-AND-RE-DRIVE DISCRIMINATOR -- structural (sign returns) vs spontaneous (re-rolls)")
    print("=" * 84)
    N = 40
    print(f"\n{N} random-IC resets per substrate; protected sign read each time:\n")

    homo = [homochiral_sign(s) for s in range(N)]
    fh = report("homochiral", homo, "~50/50 (spontaneous control: which hand wins, parity SSB)")

    rps = [rps_sign(1000 + s) for s in range(N)]
    fr = report("RPS", rps, "~100% if structural (sign=sign(alpha-beta)); ~50/50 if spontaneous")

    print("\n" + "-" * 84)
    if fh < 0.7 and fr > 0.85:
        print("  => apparatus distinguishes the two: homochiral re-rolls (SPONTANEOUS), RPS returns the")
        print("     SAME sign every reset (STRUCTURAL). The reclassification is MEASURED, not inferred:")
        print("     RPS is structurally-stored. [reclassification stands]")
    elif fr < 0.7:
        print("  => RPS ALSO re-rolls ~50/50: it is SPONTANEOUS after all. The reclassification was WRONG;")
        print("     the original character.md was right. [REVERT the character.md edit]")
    else:
        print("  => ambiguous; inspect the per-reset signs before ruling.")
    print("-" * 84)


if __name__ == "__main__":
    main()
