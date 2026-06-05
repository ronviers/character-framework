"""
TDT on the glass / aging sector — putting the cross-rule to rest by a current SWEEP.

The cross-rule (character.md §The cross-rule) asserts: "aging never couples to circulation"
(orthogonality), and "proximity couples them" (selection rule). Asserted, not computed-by-cranking.
This is the same situation the surface-code reading was in before QEC move 2 — so the transverse-
decomposition test (TDT) travels here.

Ron's design: don't test one current value — SWEEP the current, with the established current values
a SUBSET of the sweep, and show the aging observable is flat across the whole range. Put it to rest.

Substrate: a biased ring (N-state cyclic Markov NESS) — the established-current family (cycle
affinity 𝒜 = N·ln(p₊/p₋) is literally the triad/gMAM current). Hold the relaxation scale s=p₊+p₋
fixed and sweep the bias = sweep 𝒜 at fixed "temperature". By the ring's Z_N translation symmetry the
generator is circulant:
    Re(λ_k) = s·(cos θ_k − 1)   — the relaxation / AGING spectrum: depends only on s, NOT on the bias.
    Im(λ_k) = (p₋−p₊)·sin θ_k    — the OSCILLATION: carries the current.
So the metric (aging) sector lives in Re(λ), the protected current in Im(λ): orthogonal, exactly.

  (A) the spectrum: cranking 𝒜 slides eigenvalues along Im (the current) while Re (aging) is pinned.
  (B) the aging rate |Re λ_slow| is FLAT across 𝒜∈[0,30] (machine precision) — established currents
      (gMAM 0→21.8, twin-cycle 21.8) sit inside the sweep. Meanwhile max|Im λ| (the current) is cranked
      hard. Aging ⊥ circulation — put to rest, not at a point but over the whole range.
  (C) break the ring's translation symmetry (δ): the aging rate starts moving with 𝒜 (∝δ² onset here)
      — the cross-rule's "proximity couples them". The robust invariant is the threshold (exactly zero
      iff the symmetry holds), not the onset power. Exact, analytic (eigenvalues of an N×N generator).
"""
import sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

N = 24
S = 1.0                                   # p+ + p-  (relaxation scale, held FIXED across the sweep)
OUT = r"H:\character-framework\experiments\glass_aging_transverse.png"
XI = np.cos(2 * np.pi * np.arange(N) / N)  # fixed translation-breaking pattern

def rates(A):                              # A = cycle affinity = N ln(p+/p-)
    r = np.exp(A / N)
    return S * r / (1 + r), S / (1 + r)    # p+, p-
def generator(A, delta=0.0):
    pp, pm = rates(A); L = np.zeros((N, N))
    for i in range(N):
        f = 1.0 + delta * XI[i]            # site-dependent rate scaling: breaks translation, keeps the
        wp, wm = pp * f, pm * f            # per-bond ratio (so the loop affinity 𝒜 is unchanged)
        L[(i + 1) % N, i] += wp            # i -> i+1
        L[(i - 1) % N, i] += wm            # i -> i-1
        L[i, i] -= wp + wm
    return L
def spectrum(A, delta=0.0): return np.linalg.eigvals(generator(A, delta))
def aging_rate(A, delta=0.0):              # |Re λ_slow| = slowest nonzero relaxation = aging timescale^-1
    re = np.real(spectrum(A, delta))
    nz = re[re < -1e-9]
    return -np.max(nz)
def current_mag(A, delta=0.0):             # max |Im λ| — the circulation's spectral signature
    return np.max(np.abs(np.imag(spectrum(A, delta))))

# ---- (A)/(B) the sweep at delta=0 (symmetry protected) ----
As = np.linspace(0, 30, 200)
gap = np.array([aging_rate(A) for A in As])
cur = np.array([current_mag(A) for A in As])
print("=" * 72)
print(f"biased ring, N={N}, relaxation scale s=p₊+p₋={S} held fixed; sweep 𝒜 = N·ln(p₊/p₋) ∈ [0,30]")
print(f"\n(B) AGING RATE INVARIANCE (δ=0, symmetry-protected):")
print(f"    |Re λ_slow| over the whole 𝒜-sweep = {gap.mean():.6f}  ± {gap.std():.2e}  (max dev "
      f"{np.ptp(gap):.2e} — machine-precision FLAT)")
print(f"    meanwhile the current max|Im λ| is cranked 0 → {cur.max():.3f}  (the current IS swept hard)")
print(f"    established currents inside the sweep: gMAM 0→21.8, twin-cycle 21.8 — aging rate identical")
print(f"    => aging ⊥ circulation, over the whole range. Put to rest.")

# ---- (C) selection rule: break translation symmetry, sweep again ----
deltas = [0.0, 0.1, 0.2, 0.4]
print(f"\n(C) SELECTION RULE — break the ring's translation symmetry (δ): does the aging rate move with 𝒜?")
slopes = []
for dl in deltas:
    g = np.array([aging_rate(A, dl) for A in As])
    slope = np.polyfit(As, g, 1)[0]        # d|Re λ_slow|/d𝒜
    slopes.append(slope)
    print(f"    δ={dl:.2f}   d(aging rate)/d𝒜 = {slope:+.2e}   ({'flat — protected (δ=0)' if abs(slope)<1e-9 else 'couples — turns on with δ'})")
print(f"    onset is QUADRATIC: slope(δ=0.2)/slope(δ=0.1) = {slopes[2]/slopes[1]:.1f}, "
      f"slope(δ=0.4)/slope(δ=0.2) = {slopes[3]/slopes[2]:.1f}  (≈4 each ⇒ ∝ δ²) — the robust invariant is")
print(f"    the threshold (exactly zero iff the symmetry holds), not the onset power.")

# ================================================================ figure
fig, ax = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Glass/aging TDT: the aging spectrum is flat across the whole current sweep "
             "(aging ⊥ circulation); only breaking the symmetry couples them", fontweight="bold", fontsize=11)

# A: spectrum in the complex plane at several 𝒜 — Re pinned, Im spreads with the current
for A, col in [(0, "0.6"), (10, "tab:green"), (21.8, "tab:orange"), (30, "tab:red")]:
    ev = spectrum(A)
    ax[0].scatter(np.real(ev), np.imag(ev), s=22, color=col, label=f"𝒜={A}")
ax[0].axvline(0, color="k", lw=0.5)
ax[0].set_xlabel("Re λ  (relaxation / aging)"); ax[0].set_ylabel("Im λ  (oscillation / current)")
ax[0].set_title("(A) cranking 𝒜 slides eigenvalues along Im\n(current); Re (aging) is pinned", fontsize=10)
ax[0].legend(fontsize=8)

# B: aging rate flat across the sweep; current cranked (twin axis)
ax[1].plot(As, gap, "-", color="tab:blue", lw=2, label="aging rate |Re λ_slow|")
ax[1].scatter([0, 21.8], [aging_rate(0), aging_rate(21.8)], color="tab:blue", zorder=5, s=45)
ax[1].axvspan(0, 21.8, color="tab:blue", alpha=0.07)
ax[1].text(10.9, gap.mean() * 1.18, "established currents\n(gMAM 0→21.8, twin 21.8)", fontsize=7.5,
           ha="center", color="tab:blue")
ax[1].set_xlabel("cycle affinity  𝒜  (swept)"); ax[1].set_ylabel("aging rate |Re λ_slow|", color="tab:blue")
ax[1].set_ylim(0, gap.mean() * 2); ax[1].tick_params(axis="y", labelcolor="tab:blue")
axc = ax[1].twinx(); axc.plot(As, cur, "--", color="tab:red", lw=1.3)
axc.set_ylabel("current  max|Im λ|  (cranked)", color="tab:red"); axc.tick_params(axis="y", labelcolor="tab:red")
ax[1].set_title("(B) aging rate FLAT across the whole sweep\n(machine precision); current cranked hard", fontsize=10)

# C: selection rule — aging rate vs 𝒜 for increasing symmetry-breaking δ
for dl, col in zip(deltas, ["tab:blue", "tab:green", "tab:orange", "tab:red"]):
    g = np.array([aging_rate(A, dl) for A in As])
    ax[2].plot(As, g, "-", color=col, lw=1.6, label=f"δ={dl}")
ax[2].set_xlabel("cycle affinity  𝒜"); ax[2].set_ylabel("aging rate |Re λ_slow|")
ax[2].set_title("(C) break the ring's symmetry → the aging rate\nbends with 𝒜 (proximity couples them; ∝δ² onset)", fontsize=10)
ax[2].legend(fontsize=8)

fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(OUT, dpi=140)
print(f"\nsaved {OUT}")
print("=" * 72)
