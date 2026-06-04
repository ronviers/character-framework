# β-collapse 3rd register — design pass

Design-only (no run yet). Pins the substrate, the identity under test, the falsifier, the risks, and the
de-risking probe for a *genuinely independent* third register of the memory-exponent transport law.

> **RECALIBRATED after the 3-channel research** (`research_prompt_beta_3rd_register_substrate.md`). Headline
> changes: (1) the substrate is confirmed = the **confined fractional Langevin equation (fLE)**, not fOU and
> not East/CTRW; (2) **`α_s = 2−2H` is an OPEN CONJECTURE, not a citable theorem** — the third register is an
> *original derivation* (Cugliandolo–Kurchan relation + the known confined-fLE two-time covariance), not a
> "confirm a known exponent" run; (3) the honest independence caveat: on a linear-Gaussian substrate `C` and
> `R` are both functionals of one propagator, so R3 is *more* independent than free fBm (confinement breaks
> the degeneracy) but *weaker* than R2's genuinely-distinct-functional independence. This makes the 3rd
> register a real theory undertaking — strengthening, not blocking; the 2-register collapse (R1+R2) is the
> banked-strong result, which all three channels called "unusually solid."

## Channel synthesis (what to do, and what to drop)

- **Substrate = confined fLE** (3/3). fOU and "external-fGn-OU" are weaker (response decoupled from noise
  history → messy FDR); the FLE puts the memory into the friction kernel, where the aging is analytically
  tractable (Kursawe–Schulz–Metzler give the confined two-time covariance).
- **CTRW / Bouchaud trap — REJECTED.** Models a, b liked it (renewal statistics → genuinely non-trivial
  aging), but model c's argument is decisive for an *over-determination* claim: the correlation, the
  extreme-value functional, and the FDR are all Laplace transforms of the *same* waiting-time `ψ(t)` — three
  formulas, not three independent theorems — and it loses the fGn-based Norros R2.
- **East / FA KCM — REJECTED (3/3).** No single master exponent: `β_K → 0` in the glass limit; persistence,
  aging, relaxation exponents are model/dimension-specific, related by inequalities not clean identities.
- **Field-free estimator = Cugliandolo–Kurchan** adapted to the confined fLE: linear drift `F=−kx` makes the
  force–observable cross-correlations `⟨F(x_t)x_s⟩` computable from the *known* two-time covariance — giving
  both the analytical handle for the derivation and a low-variance numerical estimator. (LCZ is superior for
  discrete-time numerics; Malliavin is the rigorous-derivation backstop.)
- **The identity must be DERIVED.** Expected scaling: `X(t,t_w) ~ (t/t_w)^{α_s}` in the window
  `t_w ≪ τ_conf ≪ t` (i.e. `k t_w^2 ≪ 1 ≪ k t^2`), with `α_s` controlled by the crossover scaling
  `k·t^{2−2H}` (Kursawe et al. show the TAMSD depends on this combination). Whether `α_s = 2−2H` exactly, or
  some other clean function of `H`, is the open question — and a contentful (falsifiable) one, unlike free
  fBm where it is forced.

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
fractional process can. **NB (channel synthesis): `α_s = 2−2H` is an open conjecture, not a citable
theorem** — `α_s` could come out a *different* clean function of `H`; either way it is contentful (unlike
free fBm, where it is forced). So R3 is an *original derivation*, not a confirm-a-known-exponent run.

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

1. **Process.** Harmonically-confined fractional Langevin equation (memory in the friction kernel), per the
   channel synthesis — *not* the external-fGn fOU (whose response decouples from the noise history → messy
   FDR). Quench start (out of equilibrium) → an **aging transient** before the confined stationary state.
2. **Two-time correlation** `C(t,t_w) = ⟨x(t) x(t_w)⟩` in the aging window.
3. **Two-time response** `R(t,t_w) = δ⟨x(t)⟩/δh(t_w)`. Prefer a **field-free estimator** (Gaussian /
   Malliavin-weight, à la Cugliandolo–Kurchan) over direct perturbation (noisy). For a *linear* confined
   process the response is analytic — a clean check that the estimator is right.
4. **FDR** `X(t,t_w) = T·R / (∂_{t_w} C)`; the **aging segment** (long lag, `X<1`) has slope `α_s`. (At
   equilibrium `X→1` — the two-step structure of `staked:gfdr-two-step`: short-lag `X=1` is *not*
   below-threshold; the long-lag aging slope is the discriminator.)
5. Compare `α_s` to `2−2H`; overlay R1/R2 on the collapse plot.

## Design risk to resolve at de-risk (the crux)

**Confinement ⟂ aging trade-off (the crux all three channels flagged).** Response non-trivial only with
`k>0`, but strong `k` equilibrates fast → no aging window (model b: "no clean `(k,t_w)` regime"); weak `k`
→ trivial (free-fBm-like). The sweet spot (models a, c): `t_w ~ τ_conf`, i.e. the window `t_w ≪ τ_conf ≪ t`
(`k t_w^2 ≪ 1 ≪ k t^2`), the transient-aging regime of Kursawe–Schulz–Metzler. **The vary-`k` smoking-gun
probe (model c's recommendation — the decisive, cheap first step):**
- confined fLE at one `H` (e.g. `H=0.7`, `β=0.6`); measure `R(t,t_w)` via the CK field-free estimator;
- **sweep `k`:** at `k→0`, `α_s` → the free-fBm value (= R1, confirming the triviality is recovered); at
  intermediate `k`, `α_s` is independent of R1 and (conjecture) collapses onto `β`. The `α_s(k)` curve
  separating from the trivial value *is* the independence demonstration.
**Outcome gates.** Clean independent `α_s` tracking `2−2H` over a `k`-window → promote, then the 3-`H`
collapse + the original CK derivation. No clean window (model b's pessimism confirmed) → **park**: the
2-register collapse stands as the strong result, and "the FDR-aging exponent of a confined fractional
process is/ isn't `2−2H`" is logged as an open theory conjecture (not a framework falsification — the
identity was never a theorem). Either outcome is a clean, honest result.

## Numerical-hygiene gates (carry over)

- **Refinement-invariance** on `α_s` and the `C/R` slopes (halve `dt` and the fGn grid) — the aging window
  sits near the long-time tail where discretization can masquerade as physics (the fake-NaN / quiet-form
  discipline; `feedback_nan_is_falsification_tripwire`).
- No clip-at-zero; the confined process stays interior by construction.
- fGn via the validated Davies–Harte circulant embedding already in `beta_collapse.py` (reuse, don't
  re-derive).

## Literature anchors (from the channel reports)

- R1 fOU covariance `k^{2H−2}`: Cheridito et al. (2003). R2 fGn-queue Weibull tail: Norros (1994).
- R3 confined fLE aging (the two-time covariance to feed CK): **Kursawe–Schulz–Metzler, PRE 88, 062124
  (2013)** ("Transient ageing in fractional Brownian and Langevin-equation motion"); Jeon–Metzler PRE 81,
  021103 (2010); Pottier (2003); Lutz (2001).
- Field-free response: Cugliandolo–Kurchan, PRL 71, 173 (1993); Lippiello–Corberi–Zannetti PRE 71, 036104
  (2005) & PRE 81, 011124 (2010); Baiesi–Maes–Wynants (2009).
- Why East/CTRW were rejected: Teomy–Shokef PRE 92, 032133 (2015) (KCM `β_K→0`); the CTRW "all three are
  transforms of one `ψ(t)`" point (model c).

## Status

Design recalibrated by the 3-channel research. Not started; not blocking (strengthening only). **Next action
= the vary-`k` smoking-gun probe** (confined fLE, CK estimator, one `H`) — decisive and cheap; it answers
"does a clean independent `α_s` window exist, and does it track `2−2H`?" before any investment in the
original CK derivation or the 3-`H` collapse. Open question for the program owner: whether this strengthening
is worth the original-derivation cost, or whether the banked 2-register collapse is enough and R3 should be
logged as an open conjecture.
