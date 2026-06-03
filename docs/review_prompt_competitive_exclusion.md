# Outside-review prompt — competitive exclusion vs supercritical pitchfork

Self-contained dynamical-systems / large-deviations question for the outbound research channel. No
framework jargon by design — any strong applied-math model should be able to engage. The returned
report gets filed alongside and folded into `character_receipts.md` §Branch-survival barrier (the open
review question) + the `ΔV/ΔU` prefactor item in the handoff.

Background it bears on: the homochiral / twin-cycle branch-survival result — `μ_c=(1+a+b)/3=0.833`, the
order parameter jumps (competitive exclusion), `ΔV∝(μ−μ_c)` linear (not the pitchfork `(μ−μ_c)²`), and
the handedness-blindness of `a(μ)` across parity/exchange (`twin_mu_sweep.py`).

---

## Competitive exclusion vs. supercritical pitchfork in a symmetric, parity-related Lotka–Volterra competition — and the Freidlin–Wentzell barrier scaling

I have a deterministic-plus-noise dynamical model with a spontaneously broken ℤ₂ symmetry and I want a
rigorous check on (i) the bifurcation type, (ii) the noise-activated barrier scaling, and (iii) the right
way to pin the large-deviation prefactor.

**Model.** Six variables in two symmetry-related groups of three, `L = (L₀,L₁,L₂)` and `R = (R₀,R₁,R₂)`,
indices mod 3, with `S_L = ΣLᵢ`, `S_R = ΣRᵢ`:

```
dLᵢ/dt = Lᵢ ( F − [ Lᵢ + a·Lᵢ₊₁ + b·Lᵢ₋₁ ] − μ·S_R )
dRᵢ/dt = Rᵢ ( F − [ Rᵢ + b·Rᵢ₊₁ + a·Rᵢ₋₁ ] − μ·S_L )
```

Parameters `F = 1`, `a = 0.5`, `b = 1`, `μ ≥ 0`; let `c ≡ 1+a+b = 2.5`. Each group is an internal
asymmetric 3-cycle (a≠b); the two groups inhibit each other through their totals. The `R` group swaps
`a↔b` — i.e. it is the mirror of `L` (parity). A co-handed variant (both groups use `a·next + b·prev`, an
exchange/permutation symmetry instead of mirror) gives identical results for everything below.

**What I observe (deterministic + noisy, `dx = drift·dt + σ·dW`).**
- The symmetric ("racemic") fixed point has all six components equal to `x* = F/(c+3μ)`.
- Its symmetry-breaking mode (uniform `L−R`) has eigenvalue `a(μ) = F(3μ−c)/(c+3μ)`, crossing zero at
  `μ_c = c/3 ≈ 0.833`.
- Below `μ_c`: one symmetric basin, no broken state.
- Above `μ_c`: the order parameter `m = (S_L−S_R)/(S_L+S_R)` jumps essentially to ±1 (winner-take-all /
  competitive exclusion) — it does **not** grow as `√(μ−μ_c)`.
- The noise-activated barrier `ΔV` for an `L↔R` basin crossing scales **linearly**, `ΔV ∝ (μ−μ_c)`,
  tracking the deterministic `ΔU = a(μ)·m²/4` with `m` pinned at full exclusion — **not** the
  supercritical-pitchfork `ΔV ∝ (μ−μ_c)²`.
- `a(μ)` and `μ_c` are identical to machine precision whether the two groups are mirror images (parity)
  or identical copies (exchange), because the breaking mode is uniform within each group and blind to the
  internal cyclic structure.

**Questions.**
1. Is winner-take-all competitive exclusion the correct generic reduction for this symmetric two-group LV
   competition above the coexistence-instability threshold, or is there a parameter regime where a genuine
   **supercritical pitchfork** (soft, continuous `|m| ∝ √(μ−μ_c)`) appears? I know bare symmetric 2-species
   LV competition (`ẋ=x(1−x−αy)`, `ẏ=y(1−y−αx)`) is bistable/winner-take-all for `α>1` with a degenerate
   (transcritical-like) transition at `α=1` — does the internal 3-cycle structure, or near-threshold
   coupling to the internal modes, change that picture?
2. Is the **linear** `ΔV ∝ (μ−μ_c)` the right Freidlin–Wentzell quasipotential scaling here (a degenerate /
   hard-saturating normal form), or is the quadratic pitchfork scaling recoverable in some limit?
3. **FW barrier vs. deterministic potential.** My noisy escape-MFPT gives `ln(MFPT) ∝ ΔU` but with a slope
   (≈7.5) far below `1/σ²` (≈156) in the shallow-barrier regime — i.e. the true FW barrier ≠ the
   deterministic `ΔU`. For a non-gradient (genuinely non-equilibrium, NESS) system like this, what is the
   correct way to compute / pin the FW-barrier prefactor?
4. **Literature anchors** you would point me to: symmetric LV competition normal forms and the
   competitive-exclusion-vs-coexistence bifurcation type; May–Leonard; replicator / payoff-symmetric
   dynamics; Kondepudi–Frank chiral symmetry breaking; and large-deviation barriers for noise-induced
   transitions between symmetry-related attractors.
