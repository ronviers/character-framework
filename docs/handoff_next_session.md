# Character — next-session handoff

State pointer. Thin by design: committed detail lives in `character_receipts.md` / `character_frontier.md` /
`character.md` / git — this file holds **current state + open threads** only. All work below is committed + pushed.

## Where things stand

The two-survivals plane is fully instanced (all four corners), and **`both` (`ΔV>0 ∧ 𝒜≠0`) is now reached two
ways on each of two independence axes** — *symmetry* and *bifurcation mechanism*:

- **`both` via exchange-SSB** — the co-handed twin-cycle (`twin_cycle_corner.py`): `𝒜≈21.8`, `ΔV≈0.018`;
  sign(`𝒜`) *preserved* across the branch flip where parity *reverses* it (the orthogonality made visible a
  way parity can't). The competitive-exclusion mechanism is **handedness-blind** (`twin_mu_sweep.py`,
  `max|Δa|≈2.4e-11`; same `μ_c=0.833`, same linear `ΔV`).
- **`both` via soft pitchfork** — the autocatalytic (Kondepudi–Nelson) substrate (`autocat_pitchfork.py`
  current-free; `autocat_both.py` with current): `ee*²` linear, `ΔU∝ee*⁴` **quadratic** (vs the twin's
  hard/linear), coexistence window `ec∈[0.05,0.20]`. **Calibrated claim (channel, honest):** symmetry breaking
  does NOT fix the barrier scaling — the *saturation mechanism* does. NOT "mechanism-independent" (owed: a
  clean normal-form reduction + >2 instances). Core sentence committed (`character.md` §The two-survivals plane).
- **Competitive-exclusion review metabolized** (`docs/review_prompt_competitive_exclusion.md`): the L↔R
  transition is a **symmetric transcritical** (boundary branches, exchange of stability), not a pitchfork; no
  bare-LV regime gives a soft pitchfork. Folded into receipts §Branch-survival barrier.
- **Nudge track** (`character_frontier.md` §Nudges) — a parallel *doc-gate* track for steering candidates;
  first entry `nudge:loaded-endpoint-descent` (from the sleep lay-question). **Policy: HELD** — accumulate the
  corpus, read the shapes, promote nothing to core yet (even the mature-looking
  *apparent-structure ≠ protected-observable* shape).
- **β-collapse 3rd register — CLOSED (theory-first).** Three channel derivations
  (`docs/research_prompt_beta_r3_derivation.md`) unanimously reject `α_s=β` on the linear-Gaussian confined
  fractional process — structurally: the FDR is an *amplitude ratio*, so `β` cancels; only the nonlinear
  response sector could supply it. Parked as a clean negative result. The **2-register collapse** (R1
  covariance + R2 Norros queue, `beta_collapse.py`) is the banked-strong over-determination. Record:
  `docs/beta_collapse_3rd_register_design.md`.

## Open threads (ranked; none blocking)

1. **`current-aids-escape`** `[steeping]` (frontier) — *the deepest live question.* Does the protected current
   lower the FW branch-escape barrier (`ΔV<ΔU` because the instanton surfs the flow)? Decisive test: `a=b`
   (no current) vs `a≠b`, comparing `ΔV`. If the gap appears only for `a≠b`, the two survivals are
   **dynamically coupled** in the `both` corner (orthogonal in existence, coupled in escape). The autocat
   substrate (`ec`-knob tunes the current cleanly) is the natural place to run it — and the autocat-`both`
   result already showed the cycle *participating* in the bifurcation, which is the same coupling.
2. **`ΔV ≠ ΔU` quasipotential mismatch** — the slope gap (≈7.5 vs `1/σ²`) is a genuine non-gradient signature
   (`ΔV≪ΔU`), *not* a Kramers prefactor (which moves the intercept). The true barrier is computable by **gMAM**
   (E–Ren–Vanden-Eijnden; Maier–Stein 2D non-gradient escape). Value owed; ties into #1.
3. **β-collapse R3 sum-rule check** *(low priority)* — model c's `α_s+β=1` vs a/b's no-exponent; the vary-`k`
   probe repurposed (confined fLE + CK estimator). A *side* finding (complementarity relation), **not** the
   collapse. Or close R3 clean. My lean: let it rest unless the sum rule itself interests.
4. **autocat-`both` noisy barrier** *(low priority)* — a gMAM/noisy-FW barrier on the soft-pitchfork `both`
   (Step-2 used the deterministic `ΔU∝ee*⁴`).
5. **Nudge corpus** — HELD. Next loaded-endpoint / steering-miss → log as a nudge (or add a trigger to an
   existing one); promote nothing. Watch whether they cluster in the apparent-structure≠protected shape.

## Doc + experiment state

- **Core (committed):** `character.md`, `character_receipts.md`, `character_frontier.md`
  (`battery:two-survivals-plane` crossed; `current-aids-escape` `[steeping]`; §Nudges HELD),
  `character_grounding_method.md`.
- **`experiments/`:** identity_survival_barrier (+ `noise_kind` arg; demographic-noise robustness),
  cycle_affinity, rps_affinity, reset_redrive_test, mu_sweep, hopfield_corner, neither_corner, beta_collapse,
  deformer_loop, twin_cycle_corner, twin_mu_sweep, autocat_pitchfork, autocat_both (+ PNGs).
- **Research records (`docs/`):** review_prompt_competitive_exclusion, review_request_identity_survival,
  beta_collapse_3rd_register_design, research_prompt_beta_3rd_register_substrate, research_prompt_beta_r3_derivation.
