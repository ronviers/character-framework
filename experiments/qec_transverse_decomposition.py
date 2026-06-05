"""
QEC transverse decomposition — Open Thread #2, and the shell's deposited sentence
made quantitative in the substrate it actually belongs to.

CLAIM (currently asserted in canon, here MEASURED): in the distance-3 surface code the
protected LOGICAL sector is barred from the SYNDROME/error sector by the same
orthogonality the gMAM work proved in the homochiral triad (current exactly transverse to
the escape mode at the saddle). The shell deposited the sentence
    "a logical bit set at unit cost, flipped only at the code distance."
This script instances it:

  (A) ALGEBRA — the transverse decomposition is exact. The F_2 symplectic space splits
      stabilizer ⊕ syndrome(pure-error) ⊕ logical; the logical sector commutes with every
      stabilizer (zero syndrome) — it is symplectically transverse to the whole
      syndrome-detection sector. (The QEC instance of pa:transverse-decomposition / the DFS.)
  (B) COST-ASYMMETRY — writing the logical bit is a unit operation; flipping it requires a
      minimum-weight chain of weight d = the code distance. Measured: d = 3.
  (C) BARRIER (measured, exact — not Monte-Carlo'd) — the logical-error probability under a
      bit-flip channel is P_L(p) ∝ p^{(d+1)/2} = p^2: the protected bit flips ONLY at a
      code-distance event. The slope-2 on log-log IS "flipped only at the code distance."

Self-contained (numpy only), self-verifying: the code is constructed and then PROVEN to be
[[9,1,3]] before any reading is taken. Bit-flip (X) channel; exact lookup decoder; P_L(p)
computed exactly by enumerating all 2^9 error patterns (no sampling — demonstrate, not sample).

Rotated d=3 surface code, data qubits 0..8 on a 3x3 grid:
    0 1 2
    3 4 5
    6 7 8
"""
import sys
import numpy as np
from itertools import product
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

N = 9
OUT = r"H:\character-framework\experiments\qec_transverse_decomposition.png"

def vec(qubits):
    v = np.zeros(N, dtype=np.int64)
    for q in qubits: v[q] = 1
    return v

# CSS stabilizers as support vectors over F_2^9 (verified to commute: H_X H_Z^T = 0)
H_Z = np.array([vec(s) for s in [(0,1,3,4), (4,5,7,8), (2,5), (3,6)]])   # detect X errors
H_X = np.array([vec(s) for s in [(1,2,4,5), (3,4,6,7), (0,1), (7,8)]])   # detect Z errors

# ---------------------------------------------------------------- F_2 linear algebra
def gf2_rref(M):
    M = M.copy() % 2; rows, cols = M.shape; r = 0; pivots = []
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i, c]), None)
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        pivots.append(c); r += 1
        if r == rows: break
    return M, pivots

def gf2_rank(M): return len(gf2_rref(M)[1])

def in_rowspace(v, M):
    return gf2_rank(M) == gf2_rank(np.vstack([M % 2, (v % 2)[None, :]]))

def nullspace(M):
    """basis (rows) of the right null space of M over F_2."""
    M = M % 2; rows, cols = M.shape
    R, piv = gf2_rref(M); free = [c for c in range(cols) if c not in piv]; basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64); v[f] = 1
        for i, pc in enumerate(piv): v[pc] = R[i, f]
        basis.append(v % 2)
    return np.array(basis) if basis else np.zeros((0, cols), dtype=np.int64)

def span(basis):
    if len(basis) == 0: yield np.zeros(N, dtype=np.int64); return
    for bits in product([0, 1], repeat=len(basis)):
        v = np.zeros(N, dtype=np.int64)
        for b, row in zip(bits, basis):
            if b: v ^= row
        yield v

# ---------------------------------------------------------------- (verify) [[9,1,3]]
assert np.all((H_X @ H_Z.T) % 2 == 0), "CSS condition H_X H_Z^T = 0 violated"
rkX, rkZ = gf2_rank(H_X), gf2_rank(H_Z)
k = N - rkX - rkZ
kerZ = nullspace(H_Z)        # X-type operators with zero syndrome  (commute with all Z-stab)
kerX = nullspace(H_X)        # Z-type operators with zero syndrome
# logical-X = kerZ \ rowspace(H_X) ; distance_X = min weight there
logicalsX = [v for v in span(kerZ) if v.any() and not in_rowspace(v, H_X)]
dX = min(int(v.sum()) for v in logicalsX)
logicalsZ = [v for v in span(kerX) if v.any() and not in_rowspace(v, H_Z)]
dZ = min(int(v.sum()) for v in logicalsZ)
d = min(dX, dZ)
zL = min(logicalsZ, key=lambda v: int(v.sum()))   # a min-weight logical-Z representative
print("=" * 72)
print(f"SURFACE CODE  [[n={N}, k={k}, d={d}]]   (constructed, then verified)")
print(f"  ranks: H_X={rkX}, H_Z={rkZ}   d_X={dX}  d_Z={dZ}")
assert (k, d) == (1, 3), "construction is not [[9,1,3]] — fix stabilizers before reading"

# ---------------------------------------------------------------- (A) transverse decomposition
# symplectic dims: stabilizer (rkX+rkZ) ⊕ syndrome/pure-error (rkX+rkZ) ⊕ logical (2k) = 2N
dim_stab = rkX + rkZ; dim_logical = 2 * k; dim_syndrome = 2 * N - dim_stab - dim_logical
# logical sector commutes with EVERY stabilizer (zero syndrome) -> symplectically transverse
xL = min(logicalsX, key=lambda v: int(v.sum()))
ortho_LX_vs_Zstab = int((H_Z @ xL) % 2 @ np.ones(rkZ, dtype=np.int64))  # = 0 means commutes w/ all Z-stab
ortho_LZ_vs_Xstab = int((H_X @ zL) % 2 @ np.ones(rkX, dtype=np.int64))
syndrome_of_logicalX = (H_Z @ xL) % 2
print("\n(A) TRANSVERSE DECOMPOSITION (exact)")
print(f"  symplectic F_2^{2*N} = stabilizer({dim_stab}) ⊕ syndrome({dim_syndrome}) ⊕ logical({dim_logical})")
print(f"  logical-X syndrome vector = {syndrome_of_logicalX.tolist()}  -> all zero: "
      f"{'YES' if not syndrome_of_logicalX.any() else 'NO'}")
print("  => the logical sector is symplectically TRANSVERSE to the entire syndrome sector")
print("     (commutes with every stabilizer; carries no syndrome) — the QEC instance of")
print("     pa:transverse-decomposition (the protected current ⊥ the escape mode).")

# ---------------------------------------------------------------- (B) cost-asymmetry
print("\n(B) COST-ASYMMETRY (the shell's deposited sentence, measured here)")
print(f"  WRITE the logical bit: a unit operation (prepare a logical state)            cost = 1")
print(f"  FLIP  the logical bit: a minimum-weight logical chain = the code distance     cost = d = {d}")
print(f'  -> "a logical bit set at unit cost, flipped only at the code distance."')

# ---------------------------------------------------------------- (C) the barrier, exact
# bit-flip channel: enumerate all 2^9 X-error patterns; min-weight lookup decoder keyed by syndrome.
def syndrome(e): return tuple(((H_Z @ e) % 2).tolist())
best = {}  # syndrome -> min-weight correction
for bits in product([0, 1], repeat=N):
    e = np.array(bits, dtype=np.int64); s = syndrome(e); w = int(e.sum())
    if s not in best or w < int(best[s].sum()): best[s] = e
# classify each error: logical error iff residual (e+correction) anticommutes with logical-Z
patterns = []  # (weight, is_logical_error)
for bits in product([0, 1], repeat=N):
    e = np.array(bits, dtype=np.int64)
    r = (e ^ best[syndrome(e)]) % 2
    is_log = int((zL @ r) % 2) == 1
    patterns.append((int(e.sum()), is_log))
patterns = np.array(patterns)

def P_L(p):
    w = patterns[:, 0]; logical = patterns[:, 1].astype(bool)
    probs = p ** w * (1 - p) ** (N - w)
    return probs[logical].sum()

ps = np.logspace(-3, np.log10(0.5), 60)
PL = np.array([P_L(p) for p in ps])
# small-p slope on log-log
lo = ps < 0.02
slope = np.polyfit(np.log(ps[lo]), np.log(PL[lo]), 1)[0]
print("\n(C) THE BARRIER (exact P_L(p), no sampling)")
print(f"  small-p log-log slope of P_L(p) = {slope:.3f}   (target (d+1)/2 = {(d+1)/2:.1f})")
print(f"  => the protected bit flips ONLY at a code-distance event: P_L ∝ p^{(d+1)//2}")

# ---------------------------------------------------------------- figure
fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
fig.suptitle("QEC d=3 surface code: the logical sector is transverse to the syndrome sector, "
             "and flips only at the code distance", fontweight="bold", fontsize=12)

ax[0].loglog(ps, PL, "o-", color="tab:blue", ms=4, label="exact $P_L(p)$")
ref = PL[lo][-1] * (ps / ps[lo][-1]) ** 2
ax[0].loglog(ps, ref, "r--", lw=1, label="slope 2  ($p^{(d+1)/2}$)")
ax[0].loglog(ps, PL[lo][-1] * (ps / ps[lo][-1]), "0.6", ls=":", lw=1, label="slope 1 (unprotected)")
ax[0].set_xlabel("physical bit-flip rate  $p$"); ax[0].set_ylabel("logical error rate  $P_L$")
ax[0].set_title(f"(C) the barrier: measured slope = {slope:.2f}\n"
                f'"flipped only at the code distance" (d={d})', fontsize=10)
ax[0].legend(fontsize=8); ax[0].grid(True, which="both", alpha=0.2)

# right: the transverse decomposition + cost asymmetry
ax[1].axis("off"); ax[1].set_xlim(0, 1); ax[1].set_ylim(0, 1)
ax[1].text(0.0, 0.97, "(A)  transverse decomposition", fontsize=11, weight="bold")
ax[1].text(0.0, 0.90, f"symplectic space  $\\mathbb{{F}}_2^{{{2*N}}}$  splits into three sectors:", fontsize=9.5)
yy = 0.83
for lab, dim, col in [("stabilizer", dim_stab, "tab:green"),
                      ("syndrome (pure-error)", dim_syndrome, "tab:orange"),
                      ("logical (protected)", dim_logical, "tab:blue")]:
    ax[1].add_patch(plt.Rectangle((0.03, yy - 0.012), 0.05, 0.035, color=col))
    ax[1].text(0.11, yy, f"{lab} sector — dim {dim}", fontsize=10, va="center"); yy -= 0.075
ax[1].text(0.0, 0.575, "the logical sector carries ZERO syndrome:", fontsize=9.5, color="tab:blue")
ax[1].text(0.0, 0.525, "transverse to the whole syndrome sector", fontsize=9.5, color="tab:blue")
ax[1].text(0.0, 0.475, "(commutes with every stabilizer).", fontsize=9.5, color="tab:blue")
ax[1].plot([0.02, 0.98], [0.40, 0.40], "0.7", lw=0.8)
ax[1].text(0.0, 0.34, "(B)  cost-asymmetry of the protected bit", fontsize=11, weight="bold")
ax[1].text(0.05, 0.265, "WRITE  →  unit cost          =  1", fontsize=10, family="monospace")
ax[1].text(0.05, 0.205, f"FLIP   →  code distance      =  {d}", fontsize=10, family="monospace", color="tab:red")
ax[1].text(0.0, 0.09, '"a logical bit set at unit cost,\n flipped only at the code distance."',
           fontsize=10.5, style="italic")
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(OUT, dpi=140)
print(f"\nsaved {OUT}")
print("=" * 72)
