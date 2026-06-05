"""
QEC move 2 — barrier-invariance + the selection rule (the gMAM arc, mirrored exactly).

Move 1: the logical sector is symplectically transverse to the syndrome sector; P_L(p) ∝ p^2.
That is the static orthogonality. The result with teeth — what gMAM delivered for the homochiral
triad — is that the escape BARRIER is INVARIANT to the protected current (ΔV ⊥ 𝒜), and only moves
when the two sectors MIX.

The faithful, syndrome-ACTIVE, exactly-transverse current in a CSS code:
    measure the BIT-FLIP (X) logical barrier P_L^X(p), and crank a PHASE-flip (Z) current 𝒜.
The Z-current fires the X-stabilizers (the decoder is genuinely busy — syndrome-active), but Z
errors live in the Z-sector: they cannot produce an X-logical error. CSS X/Z independence IS the
transverse decomposition. So:

  (A) δ=0 (pure-Z current): P_L^X is EXACTLY invariant to 𝒜 — to all orders, not just the
      exponent — even as the syndrome activity (X-stabilizer firings) climbs.  [ ΔV ⊥ 𝒜 ]
  (B) δ>0 (mixing = Y-correlation): the current acquires an X-shadow on the logical string,
      opening a p^1 leak — the barrier exponent collapses 2 → 1.  [ the selection rule ]
  (C) the leak amplitude (p^1 coefficient) is LINEAR in the mixing δ.  [ cos(current,logical) ∝ δ ]

Two tiers, same as gMAM: the EXPONENT is a binary selection rule (2 iff transverse); the leak
COEFFICIENT scales smoothly with the mixing. Self-contained, exact (enumerate 2^9), no sampling.
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
OUT = r"H:\character-framework\experiments\qec_syndrome_current.png"
def vec(qs):
    v = np.zeros(N, dtype=np.int64)
    for q in qs: v[q] = 1
    return v
def onehot(j):
    v = np.zeros(N, dtype=np.int64); v[j] = 1; return v

H_Z = np.array([vec(s) for s in [(0,1,3,4), (4,5,7,8), (2,5), (3,6)]])   # detect X errors
H_X = np.array([vec(s) for s in [(1,2,4,5), (3,4,6,7), (0,1), (7,8)]])   # detect Z errors (fired by the Z-current)

# ---- minimal F_2 toolkit ----
def gf2_rref(M):
    M = M.copy() % 2; rows, cols = M.shape; r = 0; piv = []
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i, c]), None)
        if p is None: continue
        M[[r, p]] = M[[p, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        piv.append(c); r += 1
        if r == rows: break
    return M, piv
def gf2_rank(M): return len(gf2_rref(M)[1])
def in_rowspace(v, M): return gf2_rank(M) == gf2_rank(np.vstack([M % 2, (v % 2)[None, :]]))
def nullspace(M):
    M = M % 2; cols = M.shape[1]; R, piv = gf2_rref(M)
    free = [c for c in range(cols) if c not in piv]; basis = []
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

assert np.all((H_X @ H_Z.T) % 2 == 0)
k = N - gf2_rank(H_X) - gf2_rank(H_Z)
logicalsZ = [v for v in span(nullspace(H_X)) if v.any() and not in_rowspace(v, H_Z)]
d = min(int(v.sum()) for v in logicalsZ); zL = min(logicalsZ, key=lambda v: int(v.sum()))
assert (k, d) == (1, 3)

ZSYND = tuple([0] * H_Z.shape[0])
def synd(e): return tuple(((H_Z @ e) % 2).tolist())
best = {}
for bits in product([0, 1], repeat=N):
    e = np.array(bits, dtype=np.int64); s = synd(e)
    if s not in best or int(e.sum()) < int(best[s].sum()): best[s] = e
def L_ind(x):                                  # X-logical error indicator
    r = (x ^ best[synd(x)]) % 2
    return int((zL @ r) % 2) == 1

ALL_E = [np.array(b, dtype=np.int64) for b in product([0, 1], repeat=N)]
W = np.array([int(e.sum()) for e in ALL_E])
def dist_to_logical(c): return min(int(b.sum()) for b in ALL_E if L_ind((c ^ b) % 2))

# aligned X-shadow = a single X on a qubit one baseline-error from completing the X-logical
jL = next(j for j in range(N) if dist_to_logical(onehot(j)) == 1)
X_inject = onehot(jL)
print("=" * 72)
print(f"[[9,1,3]] verified.  X-logical-Z support = {np.flatnonzero(zL).tolist()}")
print(f"barrier driver: bit-flip (X) rate p.   transverse current: phase-flip (Z) rate 𝒜.")
print(f"mixing X-shadow qubit jL = {jL}  (distance-to-X-logical = {dist_to_logical(X_inject)})")

# Z-current syndrome activity: expected # X-stabilizers fired per shot by i.i.d. Z at rate 𝒜
def z_activity(A): return float(sum(0.5 * (1 - (1 - 2*A) ** int(s.sum())) for s in H_X))

# ---- exact P_L^X(p; 𝒜, δ): transverse-Z contributes baseline; only the Y-shadow (rate 𝒜δ) leaks
_base = np.array([L_ind(e) for e in ALL_E], dtype=float)
_eL = np.array([L_ind((e ^ X_inject) % 2) for e in ALL_E], dtype=float)
def P_L(p, A, delta):
    probs = p ** W * (1 - p) ** (N - W)
    term = (1 - A * delta) * _base + A * delta * _eL
    return float((probs * term).sum())
def exponent(A, delta, ppts=(1e-5, 1e-4, 1e-3)):
    pl = np.clip([P_L(p, A, delta) for p in ppts], 1e-300, None)
    return np.polyfit(np.log(ppts), np.log(pl), 1)[0]
def leak_coeff(A, delta, p=1e-6): return P_L(p, A, delta) / p

print("\n(A) BARRIER INVARIANCE — pure-Z (transverse) current, δ=0: exponent vs current 𝒜")
for A in [0.0, 0.1, 0.2, 0.3, 0.4]:
    print(f"    𝒜={A:.1f}   X-barrier exponent = {exponent(A, 0.0):.3f}  (target 2.0)   "
          f"Z-current fires {z_activity(A):.2f} X-stabilizers/shot (decoder busy)")
print("\n(B) SELECTION RULE — Y-mixed current, δ=1: exponent vs current 𝒜")
for A in [0.0, 0.1, 0.2, 0.3, 0.4]:
    print(f"    𝒜={A:.1f}   X-barrier exponent = {exponent(A, 1.0):.3f}  (collapses to 1 once 𝒜>0)")
print("\n(C) leak amplitude ∝ mixing δ (at 𝒜=0.3):  c1 ∝ cos(current, logical) = δ")
for dl in [0.0, 0.25, 0.5, 0.75, 1.0]:
    print(f"    δ={dl:.2f}   exponent={exponent(0.3, dl):.3f}   leak c1={leak_coeff(0.3, dl):.4f}")

# ================================================================ figure
fig, ax = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("QEC d=3: the bit-flip barrier is INVARIANT to a (syndrome-active) phase current, "
             "and only moves when X and Z mix", fontweight="bold", fontsize=12)

ps = np.logspace(-5, np.log10(0.3), 50)
ax[0].loglog(ps, [P_L(p, 0.0, 0) for p in ps], "o-", color="0.4", ms=4, label="no current")
ax[0].loglog(ps, [P_L(p, 0.3, 0.0) for p in ps], "s", color="tab:blue", ms=7, mfc="none",
             label="transverse Z-current (𝒜=0.3, δ=0)")
ax[0].loglog(ps, [P_L(p, 0.3, 1.0) for p in ps], "^-", color="tab:red", ms=4,
             label="Y-mixed current (𝒜=0.3, δ=1)")
ax[0].set_xlabel("physical bit-flip rate $p$"); ax[0].set_ylabel("X-logical error rate $P_L^X$")
ax[0].set_title("(A) transverse Z-current: curve EXACTLY on 'no current'\n(invisible to the X-barrier); "
                "Y-mixing opens a p¹ leak", fontsize=9.5)
ax[0].legend(fontsize=7.5); ax[0].grid(True, which="both", alpha=0.2)

As = np.linspace(0, 0.4, 17)
ax[1].plot(As, [exponent(A, 0.0) for A in As], "o-", color="tab:blue", label="δ=0  transverse (Z)")
ax[1].plot(As, [exponent(A, 1.0) for A in As], "^-", color="tab:red", label="δ=1  mixed (Y)")
ax[1].axhline(2, color="0.6", ls="--", lw=1); ax[1].axhline(1, color="0.6", ls=":", lw=1)
ax[1].set_xlabel("current $𝒜$"); ax[1].set_ylabel("X-barrier exponent"); ax[1].set_ylim(0.7, 2.3)
axb = ax[1].twinx()
axb.plot(As, [z_activity(A) for A in As], "--", color="tab:green", lw=1.5)
axb.set_ylabel("Z-current syndrome activity\n(X-stabilizer firings/shot)", color="tab:green", fontsize=9)
axb.tick_params(axis="y", labelcolor="tab:green")
ax[1].set_title("(B) activity climbs (green), barrier exponent\nflat at 2 (blue): ΔV ⊥ 𝒜, exactly", fontsize=9.5)
ax[1].legend(fontsize=8, loc="center right")

dls = np.linspace(0, 1, 21); c1 = np.array([leak_coeff(0.3, dl) for dl in dls])
ax[2].plot(dls, c1, "o-", color="tab:purple", label="leak amplitude $c_1$ (𝒜=0.3)")
ax[2].plot(dls, c1[-1] * dls, "k--", lw=1, alpha=0.6, label="linear in δ (∝ cos)")
ax[2].set_xlabel("mixing  δ  =  cos(current, logical)"); ax[2].set_ylabel("p¹ leak amplitude $c_1$")
ax[2].set_title("(C) the leak turns on ∝ the logical overlap\nof the current (the cos ∝ δ mirror)", fontsize=9.5)
ax[2].legend(fontsize=8)

fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(OUT, dpi=140)
print(f"\nsaved {OUT}")
print("=" * 72)
