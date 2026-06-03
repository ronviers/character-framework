# Character — next-session handoff

State pointer for the next session. Thin by design; delete lines as work lands.

## Banked this session

- **`both` ACROSS A SECOND BIFURCATION MECHANISM — INSTANCED (2026-06-03), within-reach #2 paid.**
  (Calibrated by the channel: "across two distinct constructions," not yet "mechanism-independent" — that
  needs >2 instances + a clean normal-form reduction. Supported claim: **symmetry breaking does not fix the
  barrier scaling; the saturation mechanism does**.) Two steps:
  **Step 1 (branch, current-free, `autocat_pitchfork.py`):** a 2-species Kondepudi–Nelson substrate
  (`dL = k1 + (g−kd)·L·(1−(L+R)/cap) − k3·L·R`, control = racemic input `k1`) gives a clean **supercritical
  pitchfork** — `ee*²=1−k1` LINEAR (R²=1.00000), `A∝(k1c−k1)^1.05`, barrier `ΔU∝(k1c−k1)^2.06` **QUADRATIC**,
  parameter-free collapse `ΔU∝ee*⁴` R²=0.9994, noisy `ln MFPT∝ΔU` corr 0.998 — a different universality class
  from the twin's hard/linear. **Step 2 (add the current, `autocat_both.py`):** each handedness → a 3-ring
  with an internal `a≠b` cycle (strength `ec`). ec-scan finds a **coexistence window `ec∈[0.05,0.20]`** where
  the soft pitchfork SURVIVES (`ee*²`-R²=1.0, `ΔU∝ee*⁴` R²=0.997) with a current `𝒜≈0.6–3.5` nats (complex
  pair, noise-indep) and reset ~50/50; past `ec≈0.25` the cycle's within-group competition (the hard-exclusion
  ingredient) kills the branch — the cycle *participates* in the bifurcation, so it's a finite coexistence
  window, not unconditional survival (the current↔branch coupling = `current-aids-escape`). So `both` is now
  instanced across **two symmetry types AND two bifurcation mechanisms**; the supported, falsification-safe
  claim is **symmetry breaking does NOT fix the barrier scaling — the saturation mechanism does** (exclusion
  →linear, soft pitchfork→quadratic). Promoted (calibrated) to receipts §Branch-survival barrier +
  §Two-survivals plane, frontier. **Decisive credit: the outbound review channel** (`ee*²` not `ee*`; `k1`
  not `g`; the `ee*⁴` collapse; MFPT two-level framing; and the claim-calibration: "two constructions" not
  "mechanism-independent"). **Open core proposal (held):** add to core §The two-survivals plane the
  conservative sentence — *the barrier scaling is set by the saturation mechanism, not by the mere presence of
  a `Z₂` symmetry-breaking transition* — NOT the stronger "distinct universality classes" (owed: a clean
  normal-form reduction).
- **Competitive-exclusion review returned + metabolized (2026-06-03).** 3 independent outside analyses
  (`docs/review_prompt_competitive_exclusion.md`) agree and **resolve the open review Q**: the L↔R transition
  is a **symmetric transcritical** (boundary-supported branches, exchange of stability), NOT a pitchfork; no
  bare-LV regime gives a soft pitchfork (folded into receipts §Branch-survival barrier). Two downstream
  effects: (i) the **second-mechanism `both`** design is now sharp — add autocatalysis (true
  Frank/Kondepudi cubic) for a genuine soft-pitchfork `both`; Z₃ is *not* a different mechanism (still
  competitive exclusion; skip).
  (ii) the `ΔV≪ΔU` gap is a confirmed non-gradient signature (gMAM to pin it); reviewers split on
  current-vs-metric source → new `current-aids-escape` `[steeping]` (frontier) with a decisive `a=b` vs `a≠b`
  test that bears on whether the two survivals are dynamically coupled in the `both` corner.
- **Second independent `both`-corner — INSTANCED (2026-06-03), within-reach #1 paid.** The two-survivals
  plane had only ONE `both` (`ΔV>0 ∧ 𝒜≠0`): the homochiral triad (parity SSB). The **co-handed twin-cycle**
  is a second, outside the chiral family: the homochiral skeleton with the *one* change mirror→copy (two
  **identical** same-handed cyclic 3-clusters under the same competitive cross-inhibition), moving the broken
  symmetry from **parity (reflection)** to **exchange (`S₂` permutation)**. Both axes read with the same
  apparatus: `𝒜≈21.8` nats (complex Jacobian pair, noise-independent, Lyapunov frame), `ΔV≈0.018`
  (σ-collapse rms `0.0046`, Kramers), reset re-rolls 20/20 (spontaneous/thermalized). **Decisive
  independence (measured, not asserted):** holding `(a,b,μ,F)` identical, sign(`𝒜`) is *preserved* across the
  branch flip (twin `−/−`) where the homochiral parity flip *reverses* it (`−/+`) — branch membership and
  current handedness decoupled at the level of sign, a separation parity structurally cannot show.
  `experiments/twin_cycle_corner.py` (+ `twin_cycle_corner.png`). Magnitudes coincide with homochiral *by
  design* (shared skeleton, a controlled comparison isolating the symmetry); the claim is the symmetry type +
  sign-coupling, not the numbers. **Committed + pushed** (`a963bf9`): receipts/frontier + the core edit
  (`both` generalized from "mirror branches" to co-handed too) + the folded-in **demographic-noise robustness**
  stale-fix (both owed items now read paid).
- **Twin μ-sweep — competitive exclusion is HANDEDNESS-BLIND (2026-06-03).** The twin shares the homochiral's
  mechanism *provably*, not just numerically: the symmetry-breaking mode `[1,1,1,−1,−1,−1]` is uniform-within-
  cluster, so it cannot see the intra-cluster handedness → the breaking eigenvalue `a(μ)` is identical across
  exchange and parity to machine precision (`max|Δa|=2.4e-11`), giving the same `μ_c=0.833` and the same LINEAR
  `ΔV∝(μ−μ_c)` (order parameter jumps = competitive exclusion; pitchfork falsified). Resolves the open
  pitchfork-vs-competitive-exclusion question the same way under BOTH SSB types. `experiments/twin_mu_sweep.py`
  (+ PNG). NB the noisy-FW slope (7.5) ≠ 1/σ²=156 is the known `ΔV≠ΔU` quasipotential mismatch (a *slope*
  effect — the barrier itself differs — NOT a Kramers prefactor, which only moves the intercept), same as
  homochiral — not a twin issue; the deterministic sweep is the airtight leg.
- **Sleep lay-question → first `nudge`, + a new HELD nudge track (2026-06-03).** An outside model's sleep
  essay overreached *because character mis-steered it* (Ron's framing — character owns the endpoint). Standard
  procedure (strip→skeleton→locate→steelman→park) lands a **nudge, not a battery** (the skeleton is already
  instanced across the corners — switch=branch-only, oscillator=current-only, `both`=homochiral+twin; no owed
  measurement). Built **thin nudge infrastructure** per Ron: a parallel *doc-gate* track in
  `character_frontier.md` §Nudges (a nudge corrects how character steers a reader, not a substrate claim;
  2-rung path `candidate → recurrence → core`; logs *trigger* = support and *shape* = failure-class).
  **Policy: nudges are HELD** — no core promotion until the corpus is big enough to see where the shapes
  cluster. First entry `nudge:loaded-endpoint-descent` with two misses: **(A)** periodicity ≠ the hard bit
  (only the protection test is; the §Composition gate sits *downstream* of the minting language); **(B)** `ℭ`
  is degenerate at *loaded endpoints* (descend to the skeleton). Its **shape** —
  *apparent-structure ≠ the protected observable* — already recurs in-core (neither-corner corollary,
  §Composition circularity gate, + deformer λ=0, DNA pre-fuel), i.e. looks recurrence-mature, but is HELD
  un-promoted by policy. Watch whether the next nudges land in this shape.
- **β-collapse falsifier run — SURVIVED (2026-06-03).** The memory-exponent transport law's *named*
  invalidator (FDR-aging vs queue-tail onto a common `β`) instanced on the Norros fBm-queue: `β=2−2H`
  recovered two independent ways — low-frequency spectral slope (aging/kernel register; `α_s=β_mem` by
  the framework's identity) vs the queue-backlog Weibull stretch (Norros) — collapsing across
  `β∈{0.8,0.6,0.4}` (mean inter-register gap 0.066). `β=0.2` is finite-block resolution-limited but
  demonstrably converging toward the memory register (`β_queue`: 0.455→0.344 as blocks 16k→131k), not a
  register inconsistency. Falsifier did **not** fire. Caveat: aging leg read via the correlator exponent,
  not an independent response (free-fBm response is a trivial integrator → no independent `α_s` on this
  substrate); a genuine 3rd register is parked (within-reach #4). `experiments/beta_collapse.py`
  (+ `beta_collapse.png`). Frontier/receipts promotion (the `≥2-register collapse spec` is now
  instanced) held for review.
- **ΔV branch-survival barrier — robust to the noise metric (2026-06-03).** Re-ran racemic-saddle escape
  under demographic `√x` (multiplicative) noise vs the original additive (`identity_survival_barrier.py
  compare`). Additive leg reproduced the banked `ΔV_KR=0.018` / collapse-rms `0.0046` (refactor
  validated). Demographic gives a finite, well-defined, σ-collapsing barrier: `ΔV_KR≈0.273` (clean
  Kramers line), collapse-rms `0.025` (9% of barrier vs additive's 26%). The FW quasipotential rescales
  with the metric (it must) but existence + protection survive → branch survival is **not** an
  additive-noise artifact. `noise_kind` param added (additive default byte-identical);
  `identity_survival_barrier_demographic.png`.
- **Deformer-loop / embodiment-minting instanced (2026-06-03) — VINDICATE.** The "frustrated ⇒ mints
  `𝒜≠0`" leaf, in the session-opening deformer language: a 3-node loop with a reciprocity knob `λ`.
  `λ=0` (reciprocal cyclic Laplacian = `polyAverageVertex` smoothing) → `⟨σ⟩=0`, `𝒜=0`, real
  eigenvalues — *relaxes, no character*. `λ>0` (antisymmetric cyclic = order-dependent deformer stack)
  → complex eigen-pair, `⟨σ⟩` and `𝒜` rise (`𝒜=10.88` nats at `λ=1`), numeric `𝒜`=analytic
  `4πω₀/κ_eff`, noise-independent (zero spread over `d`). The `λ`-sweep instances *proximity as a
  creation operator for protected current*. `experiments/deformer_loop.py` (+ `deformer_loop.png`).
- **Terminology: identity → branch membership** across the core. The anthropomorphic "identity" is
  retired as a formal term (one bridge note remains, by design); the formal observable is **branch
  membership** (`character.md` §Branch membership). The grounding method keeps "identity" as the
  informal/extrapolation layer.
- **The two-survivals plane crossed to core** (`character.md` §The two-survivals plane; receipts
  §Two-survivals plane). Branch survival (`ΔV`) ⟂ current survival (`𝒜`); four corners instanced:
  - **neither** (feedforward MLP): capability `I(Ŷ;Y)≈2.9` bits *measured*, hard sector
    *structurally* absent (nilpotent DAG ⇒ `𝒜≡0`; `ΔV` undefined). `neither_corner.py`
  - **branch-only** (symmetric Hopfield): `ΔV≈0.97` with `⟨σ⟩=𝒜=0` machine-precision. `hopfield_corner.py`
  - **current-only** (RPS, DNA) and **both** (homochiral): the core instances.
  - Corollary now core: *soft-sector capability ⟂ the hard sector*; corners move under coupling.
- **Branch-survival barrier** `ΔV≈0.018` on the homochiral racemic saddle (σ-collapse rms `4.6e-3`;
  separated from `I(0)` two ways — noise-scaling and controlled embedding). `identity_survival_barrier.py`,
  `cycle_affinity.py` (`𝒜=21.77`), `rps_affinity.py`.
- **RPS reclassified structurally-stored** — the defining reset-and-re-drive discriminator: RPS returns
  the same sign 40/40, homochiral re-rolls 20/20. Corrected a §Identity misclassification. `reset_redrive_test.py`
- **μ-sweep** (`mu_sweep.py`): branch survival is born at `μ_c=(1+a+b)/3=0.833` by **competitive
  exclusion** — `ΔV ∝ (μ−μ_c)` **linear**, *not* the pitchfork `(μ−μ_c)²` (model b's prediction
  corrected; the racemic L↔R transition is winner-take-all). `ΔV=0` below threshold.
- **Embodiment / perception-action loop** grounded (grounding method Group II): closing the loop mints
  `𝒜≠0` *iff* the union graph is frustrated; the bit is the joint loop's, not the substrate's; not
  autonomy, not consciousness.
- **Review doc** `docs/review_request_identity_survival.md` ready for outside opinion (includes the
  μ-sweep result and the open normal-form question).

## Within-reach tests (ranked)

1. **β-collapse 3rd register** *(strengthening; the 2-register form is banked above)* — a genuinely
   independent FDR-aging register. On fBm aging ≡ kernel (one exponent, `α_s = β_mem`), so a true third
   register needs an aging-rich substrate: the **East KCM** (two-time `t_w`-aging + stretched `C(τ)` +
   heavy-tailed persistence tail = three distinct ops) or a confined **fractional-OU** (independent
   aging-response). Parked pending appetite; not blocking.
2. **~~Mechanism-independent `both`~~ — DONE (banked above, `autocat_both.py`).** The soft-pitchfork `both`
   is instanced (window `ec∈[0.05,0.20]`). *Possible follow-ons (low priority):* a noisy FW/gMAM barrier on
   the autocat `both` (Step-1 had the noisy leg; Step-2 used the deterministic `ΔU∝ee*⁴`); and the
   `current-aids-escape` `a=b` vs `a≠b` test (frontier) — the autocat substrate is a natural place to run it
   (the `ec`-knob tunes the current cleanly).

## Open from outside review

- ~~Is competitive-exclusion the right reduction…or a supercritical-pitchfork regime?~~ **RESOLVED by the
  outside review (3 independent analyses, `docs/review_prompt_competitive_exclusion.md`):** the normal form
  is a **symmetric transcritical** (degenerate exchange-of-stability), not a pitchfork — the broken branches
  are *boundary* fixed points `(3F/c,0)` existing for all μ>0 that exchange stability with the symmetric
  state at μc (forced: an interior asymmetric fixed point needs `(S_L−S_R)(c−3μ)=0`). The exact 2D totals
  reduction holds because `a+b=1.5<2` keeps the May–Leonard modes stable. **No regime of the bare LV gives a
  soft pitchfork** — folded into receipts §Branch-survival barrier.
- `ΔV ≠ ΔU` **quasipotential mismatch** (was loosely called the "prefactor" — corrected: a Kramers prefactor
  moves the *intercept*; a *slope* gap means the barrier differs and/or the effective noise ≠ nominal σ) —
  **mechanism identified, value still owed.** The slope gap (≈7.5 vs `1/σ²`=156) is a genuine non-gradient
  signature (`ΔV≪ΔU`), the true barrier computable by **gMAM** (E–Ren–Vanden-Eijnden; Maier–Stein). The reviewers split on the *source* (internal current vs LV metric) → the `current-aids-escape`
  `[steeping]` test (frontier).

## Doc + experiment state

- Core: `character.md` (branch membership; §The two-survivals plane), `character_receipts.md`,
  `character_frontier.md` (`battery:two-survivals-plane` crossed; `branch-survival` crossed),
  `character_grounding_method.md` (embodiment tree, Group II).
- `experiments/`: `identity_survival_barrier.py`, `cycle_affinity.py`, `rps_affinity.py`,
  `reset_redrive_test.py`, `mu_sweep.py`, `hopfield_corner.py`, `neither_corner.py`,
  `beta_collapse.py`, `deformer_loop.py`, `twin_cycle_corner.py`, `twin_mu_sweep.py`,
  `autocat_pitchfork.py` (current-free soft pitchfork), `autocat_both.py` (ec-scan, soft-pitchfork `both`) (+ PNGs).
  `identity_survival_barrier.py` gained a `noise_kind` arg (additive default unchanged; `compare` runs
  additive vs demographic). `twin_cycle_corner.py` imports the validated `ep_affinity` (cycle_affinity) and
  the homochiral field for the measured parity-vs-exchange sign contrast (`smoke` arg for a fast probe);
  `twin_mu_sweep.py` overlays the twin and homochiral μ-sweeps to show handedness-blindness.
- **Nudge track (`character_frontier.md` §Nudges) — HELD, nothing promoted to core.** Candidate steering
  sentences accumulate here (currently one: `nudge:loaded-endpoint-descent`). Policy is to read the *shapes*
  across the corpus before promoting any — do **not** auto-promote on the recurrence gate, even the
  apparent-structure≠protected-observable shape that already looks mature. Next loaded-endpoint or
  steering-miss → log it as a nudge (or add its trigger to an existing one), don't promote.
