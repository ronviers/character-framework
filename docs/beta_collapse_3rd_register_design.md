# β-collapse 3rd register — design pass

Design-only (no run yet). Pins the substrate, the identity under test, the falsifier, the risks, and the
de-risking probe for a *genuinely independent* third register of the memory-exponent transport law.

## The gap (what the banked 2-register form lacks)

`beta_collapse.py` (SURVIVED) recovers one memory exponent `β = 2−2H` two independent ways on the Norros
fBm queue:
- **R1 — memory kernel** `β_mem`: log-log slope of the fGn autocovariance `γ(k) ~ k^(2H−2) = k^(−β)` (a
  two-point correlation).
- **R2 — queue tail** `β_queue`: Norros `P(Q>x) ~ exp(−η x^(2−2H))`, the Weibull stretch `2−2H` (a
  *supremum* functional — the exponent equality is a theorem, not a definition; the registers are not tied
  definitionally).

The transport law names a **third** register — the **FDR-aging exponent `α_s`**, with the framework
identity `α_s = β_mem = β`. But on *free* fBm the linear response is a trivial integrator, so `α_s` read
off the dynamics collapses onto the correlator exponent: **R3 ≡ R1 on free fBm (tautology)**. The owed
test is `α_s` measured from a **response that is independent of the correlator**.

## Identity under test (the actual new content)

> **`α_s = β_mem = 2−2H`**, with `α_s` obtained from a two-time *response* `R(t,t_w)`, on a substrate
> where `R` is **non-trivial** (so `α_s` is not definitionally the correlator slope).

This tests the framework's **FDR-aging ↔ memory-kernel** identity (the `staked:gfdr-two-step` /
two-FD-frames machinery) on a case where it can actually fail. Free fBm cannot falsify it; a confined
fractional process can.

## Substrate decision — confined fractional process (FLE / harmonically-confined fBm)

**Chosen: a harmonically-confined fractional process** (fractional Langevin / confined-fBm family), same
driving fGn Hurst `H` as R1/R2 → same `β = 2−2H`. Confinement adds a relaxation timescale that competes
with the memory, making the linear response `R(t,t_w)` **non-trivial** (no longer the bare integrated
kernel) → an `α_s` independent of `β_mem`.

Why this over the **East KCM** (the other candidate): East genuinely ages and has three distinct ops
(two-time aging, stretched `C(τ)`, heavy-tailed persistence), but it is *not* fGn-driven — its memory is
the hierarchical kinetic constraint, so there is no clean `β = 2−2H` to collapse onto. East would test a
*different, un-pinned* identity. The confined fractional process keeps `β = 2−2H` exact by construction,
so the collapse is a sharp test of the **identity**, not a hunt for an unknown exponent. (East stays a
later, harder "real glassy substrate" option, gated on first writing its β-identity down — do not start
there.)

**Three registers, one `H` (β = 2−2H), three independent operations:**
| reg | operation | exponent | status |
|---|---|---|---|
| R1 kernel | fGn autocovariance slope (2-point correlation) | `β_mem` | banked |
| R2 queue | Norros backlog Weibull stretch (supremum functional) | `β_queue` | banked |
| **R3 FDR-aging** | confined-process two-time **response** `R(t,t_w)`, aging slope | **`α_s`** | **this** |

Collapse across `β ∈ {0.8, 0.6, 0.4}` (`H ∈ {0.6, 0.7, 0.8}`): all three must equal `2−2H`. **Falsifier:**
`α_s ≠ 2−2H` (independently measured) → the FDR-aging↔kernel identity is falsified. A weak/ambiguous
`α_s` is not a pass (see `feedback_prepared_for_invalidation`).

## Measurement plan (R3)

1. **Process.** Harmonically-confined fGn-driven process `dx = −k x dt + dB_H` (or the FDT-consistent
   FLE — decide at de-risk; the confined-fGn-OU is simpler and already breaks the free-fBm tautology).
   Quench start (`x=0`, out of equilibrium) → an **aging transient** before the confined stationary state.
2. **Two-time correlation** `C(t,t_w) = ⟨x(t) x(t_w)⟩` in the aging window.
3. **Two-time response** `R(t,t_w) = δ⟨x(t)⟩/δh(t_w)`. Prefer a **field-free estimator** (Gaussian /
   Malliavin-weight, à la Cugliandolo–Kurchan) over direct perturbation (noisy). For a *linear* confined
   process the response is analytic — a clean check that the estimator is right.
4. **FDR** `X(t,t_w) = T·R / (∂_{t_w} C)`; the **aging segment** (long lag, `X<1`) has slope `α_s`. (At
   equilibrium `X→1` — the two-step structure of `staked:gfdr-two-step`: short-lag `X=1` is *not*
   below-threshold; the long-lag aging slope is the discriminator.)
5. Compare `α_s` to `2−2H`; overlay R1/R2 on the collapse plot.

## Design risk to resolve at de-risk (the crux)

**Confinement ⟂ aging trade-off.** The response is non-trivial only with confinement `k>0`, but a strong
`k` equilibrates fast → no aging window; a weak `k` → response → trivial (free-fBm-like). There is a
window in `(k, t_w)` where `R` is *both* non-trivial *and* the aging regime is resolvable. **De-risking
probe (first implementation step):**
- generate confined fractional process at one `H` (e.g. `H=0.7`, `β=0.6`);
- confirm operationally that `R` is **independent of the correlator** — i.e. the response exponent ≠ the
  raw `C(τ)` slope at `k=0`, and *becomes* a clean aging `α_s` at the chosen `k`;
- confirm `α_s ≈ 2−2H` at that one `H`.
If the probe shows a clean, non-trivial, `2−2H`-tracking `α_s`, scale to the 3-`H` collapse. If no `(k,t_w)`
window gives a clean independent `α_s`, that is itself the finding (the FDR-aging register may not be
cleanly separable on this substrate family → reconsider East with its β-identity written down first).

## Numerical-hygiene gates (carry over)

- **Refinement-invariance** on `α_s` and the `C/R` slopes (halve `dt` and the fGn grid) — the aging window
  sits near the long-time tail where discretization can masquerade as physics (the fake-NaN / quiet-form
  discipline; `feedback_nan_is_falsification_tripwire`).
- No clip-at-zero; the confined process stays interior by construction.
- fGn via the validated Davies–Harte circulant embedding already in `beta_collapse.py` (reuse, don't
  re-derive).

## Status

Design only. Not started; not blocking. Next action = the single-`H` de-risking probe above.
