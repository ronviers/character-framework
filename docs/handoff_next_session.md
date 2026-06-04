# Character — next-session handoff

State pointer. Thin by design: committed detail lives in `character_receipts.md` / `character_frontier.md` /
`character.md` / git — this file holds **current state + open threads** only. All work below is committed + pushed.

## Where things stand

**Latest (this session): `current-aids-escape` — homochiral 3σ, autocat null, interpreted; next session = gMAM.**
The arc:
- **Homochiral (committed `12d3b0e`):** the protected current *lowers* the FW branch-escape barrier — `ΔV`
  drops monotonically `0.328→0.272` as `𝒜:0→21.8`, 3σ, metric held to 7e-12 (`current_aids_escape.py`).
- **Autocat (the would-be 2nd instance): clean null** — flip counts identical within Poisson as `𝒜:0→2.3`
  (NaN-robust readout: flip *counts*, not censoring-contaminated MFPT). Not just small-`𝒜` (H's per-nat
  sensitivity predicts a ~10× excess; observed ~0) → the coupling is **not mechanism-general**.
- **Outside reports (3, unanimous):** a **geometric selection rule** — current lowers the barrier *iff* it
  projects onto the escape path (`research_prompt_current_aids_escape_interpretation.md`).
- **My deterministic test of their cheap predictor:** it is **null by symmetry** — `J=f(a≠b)−f(a=b)≡0` on the
  whole escape route (saddle, attractor, heteroclinic all uniform-within-group, even at `a≠b`; `J` lives only
  *off* it). ⟹ the effect is a **higher-order instanton excursion** off the symmetric subspace →
  **gMAM is required, not optional** (`current_aids_escape_alignment.py`).
- **HELD:** the interpretive frontier/receipts rewrite + the `character.md` core caveat — pending gMAM. Only
  empirical facts are recorded. **► Next session = gMAM: turnkey plan `docs/gmam_plan.md` + scaffold
  `experiments/gmam_current_aids.py`.** See Open threads #1–#2.

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

1. **`current-aids-escape` — confirmed on homochiral (3σ), NULL on autocat; outside interpretation in
   flight.** `[sharpening]`. Homochiral (`experiments/current_aids_escape.py`, committed `12d3b0e`): metric
   held (`a+b=1.5` pins `μ_c` + racemic breaking eig to 7e-12), `a−b` dials `𝒜:0→21.8`, Kramers FW `ΔV`
   **drops monotonically** `0.328→0.295→0.284→0.272` (`R²>0.99`, 3.0σ) — current lowers the barrier.
   **Autocat (would-be 2nd instance): clean null** — same protocol (`ec,a+b` fixed, dial `a−b`, `𝒜:0→2.3`),
   flip counts identical within Poisson across the activated window (probes only; no committed experiment
   file). Not just small-`𝒜`: H's per-nat sensitivity predicts a ~10× excess on A, observed ~0. So the
   coupling is **not mechanism-general**; H vs A differ in 3 confounded axes (hard-transcritical / boundary
   `m*=±1` / `𝒜≈21.8` vs soft-pitchfork / interior `m*=±0.71` / `𝒜≈2.3`). **Status: outbound interpretation
   prompt drafted** (`docs/research_prompt_current_aids_escape_interpretation.md`) — asks whether
   current-assisted escape is regime-dependent (instanton–current alignment? a Péclet-like threshold?) and
   how to disentangle the 3 confounds. Reports returned (3 models, unanimous: a **geometric selection rule**
   — current lowers the barrier iff it projects onto the escape path). My deterministic test of their cheap
   predictor (`current_aids_escape_alignment.py`) found it **null by symmetry** — `J≡0` on the whole escape
   route (saddle, attractor, heteroclinic all uniform-within-group, even at `a≠b`) → the effect is a
   **higher-order instanton excursion** off the symmetric subspace → **gMAM is required, not optional**.
   **The frontier/receipts interpretive rewrite + the `character.md` core caveat stay HELD pending gMAM.**
   ► **NEXT SESSION = gMAM. Turnkey plan: [`docs/gmam_plan.md`](gmam_plan.md); scaffold:
   `experiments/gmam_current_aids.py`** (fields/saddle/attractor/initial-path/`S_hat` wired; minimizer
   stubbed). Validation ladder Maier–Stein → autocat (interior, expect `ΔŜ≈0`) → homochiral (boundary,
   expect `Ŝ(a=b)≈0.328`, `Ŝ(a≠b)≈0.272`, instanton bends off-subspace). Decision rules + anchors + risks
   all in the plan.
2. **gMAM — the exact instanton (now the active next-session build; see [`docs/gmam_plan.md`](gmam_plan.md)).**
   Subsumes the old `ΔV≠ΔU` item: the slope gap (≈7.5 vs `1/σ²`) is a genuine non-gradient signature
   (`ΔV≪ΔU`), and gMAM gives the *exact* (σ→0) barrier + the instanton path. It is now the **required** tool
   for #1 (the cheap predictor is null-by-symmetry), and it doubles as the route to *promote* #1: if the
   homochiral instanton bends off-subspace and `ΔŜ` reproduces the `0.328→0.272` drop, the coupling crosses
   into the core (scoped). Falsification risk: gMAM may show `ΔŜ≈0` (the Kramers drop was finite-σ/prefactor)
   — a clean kill. Plan has the full method, anchors, validation ladder, decision rules.
3. **β-collapse R3 sum-rule check** *(low priority)* — model c's `α_s+β=1` vs a/b's no-exponent; the vary-`k`
   probe repurposed (confined fLE + CK estimator). A *side* finding (complementarity relation), **not** the
   collapse. Or close R3 clean. My lean: let it rest unless the sum rule itself interests.
4. **autocat-`both` noisy barrier** — *attempted (probes), returned a null* (folded into #1). The
   `a=b` vs `a≠b` `ΔV(𝒜)` comparison on the soft-pitchfork `both` showed **no current effect** on escape
   (flip counts identical within Poisson, `𝒜:0→2.3`). Diagnostics: the activated σ-window is brutally
   narrow (0 flips → saturated over a thin band), current intrinsically weak (the weak cycle that makes it
   a soft pitchfork makes its current weak), branches interior (`m*=0.71`). Not worth a committed
   experiment file as-is; revisit only if the outbound report (#1) suggests a deeper-branch / different
   operating point worth measuring.
5. **Nudge corpus** — HELD. Next loaded-endpoint / steering-miss → log as a nudge (or add a trigger to an
   existing one); promote nothing. Watch whether they cluster in the apparent-structure≠protected shape.

## Doc + experiment state

- **Core (committed):** `character.md`, `character_receipts.md`, `character_frontier.md`
  (`battery:two-survivals-plane` crossed; `current-aids-escape` now `[sharpening]` — vindicated once,
  2nd instance owed; §Nudges HELD), `character_grounding_method.md`.
- **`experiments/`:** identity_survival_barrier (+ `noise_kind` arg; demographic-noise robustness),
  current_aids_escape (the `current-aids-escape` decisive test — `ΔV(𝒜)` at fixed metric),
  current_aids_escape_alignment (deterministic predictor — finds `J≡0` on the symmetric escape path → gMAM required),
  gmam_current_aids (**SCAFFOLD** — fields/saddle/attractor/initial-path/`S_hat` wired, minimizer stubbed; see plan),
  cycle_affinity, rps_affinity, reset_redrive_test, mu_sweep, hopfield_corner, neither_corner, beta_collapse,
  deformer_loop, twin_cycle_corner, twin_mu_sweep, autocat_pitchfork, autocat_both (+ PNGs).
- **Research records (`docs/`):** **gmam_plan** (the turnkey next-session build plan),
  research_prompt_current_aids_escape_interpretation (3 reports: geometric selection rule),
  review_prompt_competitive_exclusion, review_request_identity_survival,
  beta_collapse_3rd_register_design, research_prompt_beta_3rd_register_substrate, research_prompt_beta_r3_derivation.
