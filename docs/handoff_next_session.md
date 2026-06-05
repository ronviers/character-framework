# Character — next-session handoff

State pointer. Thin by design: committed detail lives in `character_receipts.md` / `character_frontier.md` /
`character.md` / git — this file holds **current state + open threads** only. All work below is committed + pushed.

## Where things stand

**Latest (2026-06-05, session 3 — shell dead-ended, substrate ledger created, QEC transverse-decomposition computed):**
- **Shell T2 on real Collins data → weak pass → FAIL.** The real-normal endpoint (`shell_t2_collins.py`,
  184 shells) settles (84% converge) but only to a sub-region (within/pooled 0.34) and barely beats a
  stage-shuffle null (0.90). A weak pass is a fail. **Shell is a dead-end SUBSTRATE** — *not* a tombstone
  (tombstone = an overturned core claim; a weak pass is just a dead end). Shell morphometrics are a frozen
  projection carrying no σ / 𝒜 / perturbable response. New memory `feedback_substrate_affordance_filter`
  (salience ≠ affordance; generate, don't hunt; run the affordance gate on the substrate×modality pair
  *before* any data hunt).
- **Substrate ledger created** — `framework/character_substrate_ledger.md`: a scannable roster (status +
  deposit per substrate) so we stop recovering ground. Human-first, the antidote to the dense frontier.
- **Shell wasn't a total bust** — it deposited the candidate sentence *"a logical bit set at unit cost,
  flipped only at the code distance,"* which is substrate-general and **re-homed to QEC**.
- **QEC re-aim, moves 1–3 computed** (`qec_transverse_decomposition.py`, `qec_syndrome_current.py`,
  `qec_within_sector_current.py`; receipts §QEC transverse decomposition; frontier
  `qec-transverse-decomposition`): (1) logical ⊥ syndrome exact + cost-asymmetry (write 1 / flip d) + barrier
  $P_L\propto p^{(d+1)/2}$; (2) bit-flip barrier **exact-invariant** to a syndrome-active phase current, leak
  ∝ δ under Y-mixing; (3) d=5: **no** within-sector exact-transverse current → exact invariance is
  **symmetry-protected, not generic** (the triad's $Z_3$ boundary, mirrored one-to-one). **Open Thread #2
  resolved.** Synthetic = calibration, not vindication — but the content (protected information shielded from
  the syndrome churn) is the operationally load-bearing fact.

**Latest (2026-06-04, session 2 — shell data acquired, T2 apparatus calibrated, the synthesis landed in frontier):**
- **Data in hand** (`data/shell/`, see `ACQUISITION_CHECKLIST.md`): Collins 2021 normal-gastropod aperture
  trajectories (Dryad `p5hqbzknw` — Ron browser-downloaded past the Dryad/Anubis bot-wall; the report's
  Zenodo `12159344` was a wrong DOI, caught by gate-check), Misaki 2023 heteromorph-ammonite growing-tube
  E/C/T (Dryad `q573n5tnz`, T crosses zero), Liew heteromorph-gastropod meshes (Figshare, non-watertight),
  Noshita growing-tube extractor (GitHub), Filin centerline morphospace (Zenodo).
- **Apparatus calibrated** (`experiments/shell_t2_*.py`, `shell_gauge_vs_chirality.py` — uncommitted):
  growing-tube null recovers constant (E,C,T) to 1e-10; the refined test (Ron's volume idea) = the
  **allometric slope** logA-vs-logV → 2/3 (clean null), with the **robustness split** established — volume
  robust (4.7% over noise), area fragile (67%); the C,T continuous fit is noise-brittle (NaN ≥0.5% — a
  'bad-test' NaN, not the boundary tripwire). Gauge demo: surface normal is gauge (flips under path/profile
  reversal), chirality protected (reflection-only).
- **The session's real product → `character_frontier.md` §Steeping:** `shell-space-layer-manifest` (the
  shell manifests the two-sector architecture *without testing* — three truisms = the architecture; the
  error-correction reading: handedness set at one bit, reversed at code distance; **scope: space layer
  only**; full draft passage held as a quarantined blockquote) and `coherence-as-attractor-diagnostic` (the
  shell/mandelbulb asymmetry — coherence-generic ⇒ dynamical attractor, not observer-selection; mandelbulb
  = negative control; crystal caveat).
- **Decision:** the seashell stays OUT of `character.md` — a vivid example anchors readers/AI and crowds
  out the dynamical core (new memory `feedback_vivid_examples_anchor_in_canon`). Promotes only with a
  receipt + salience-care.

**Latest (2026-06-04, cont.): story landed; seashell work reframed into character's native register; two
outbound prompts are out — resume when their data returns.** (commits `32b22e8`, `9f84a7a`, `1cbc5e9`,
`a521729`, `2e0d0c3`, `020dbc9` — all pushed.)
- **`character.md` §The conjugate cascade upgraded** — Harada–Sasa's level-to-level lift is now the
  coarse-graining EP split (`σ_tot = σ_res + σ_hid`, Esposito / Bo–Celani) bound to `ε<1`, anchored to the Schur
  transverse-decomposition; receipts §Conjugate-cascade ledger, prior-art `pa:timescale-ep`, frontier
  `cascade-ledger-split` [sharpening].
- **`README.md` now leads with the story** — a prose walk through the engine (point → space → closure → cascade →
  the self-referential horizon → the β bet), named imports kept out of the body.
- **AlphaFold/morphospace → frontier:** `predictor-soft-sector-blindness` [steeping] — a feedforward predictor is
  confident-and-false on hard-sector questions (the neither corner made real by AlphaFold/PPI).
- **Seashell, reframed.** `cross-stratum-transduction` [sharpening] = a single shell is a recorded cascade ascent
  (apex→aperture, a *trajectory* — character's native register, not a between-specimen ensemble where the human
  fingerprints live).
  - **Lead = T2 (heteromorphy = the marginal point `ε→1`)**: a normal trajectory converges to a self-similar
    growth fixed point; a heteromorph loses it.
  - Steeping: `chirality-cascade-pinning` (T1 — handedness pinned across scales, reversals only by discrete
    rewiring) · `determinate-growth-terminus` (the clock — growth stops at the threshold `a→0`; **self-similar
    growth is self-terminating**, and the stop is an **absorbing basin** the next phase can't climb out of, the
    same geometry forbidding the return).
  - **The two sectors' opposite fates:** the metric *pays and gets trapped* (descends in `a`, ends in the basin);
    the topology *rides free* (handedness propagated laterally + vertically at zero marginal cost — *why* it
    survives the tower). A dead shell = a stopped metric carrying a free, permanent topology = "the topological
    sector is the irreducible residue," in hand.
  - **Noted, un-stubbed:** `cost-asymmetry-of-the-two-sectors` — the metric's construction cost (→0 at the stop)
    vs the topology's zero maintenance cost is a *third* readout (energy axis); rides on the same prompt-2 data,
    held until the channel reports.
  - Prediction A (between-specimen chirality ⊥ shape) = **logged near-miss**: came back messy / weak-against-
    strict (*Amphidromus* not exact mirrors, *Partula* weak pleiotropy — human-sized data). Don't re-run; the
    within-shell register replaced it. Self-similarity itself is gnomonic growth (D'Arcy Thompson), not ours.

**► PICK UP HERE (updated 2026-06-05 session 3).** The QEC transverse-decomposition arc is complete and
banked (moves 1–3; Open Thread #2 resolved). The **shell program is closed** — dead-end substrate; see the
substrate ledger (`framework/character_substrate_ledger.md`), which now holds the verdict + the re-homed
deposit. Open, ranked, none blocking:
1. **Frontier de-mess** *(Ron's standing ask)* — `character_frontier.md` is too dense for a human to get
   caught up. Agreed approach: **additive only** — git holds everything; add a scannable dashboard/index at
   the *top* (one row per entry: `key | rung | one-line verdict`, like the ledger), **never restructure the
   dense prose**. Offer a one-section slice first (Steeping) so Ron can confirm nothing below moves. He is
   wary of touching it — lead with the git-safety + additive framing.
2. **Optional QEC move 4** — a *real* substrate showing barrier-invariance to a symmetry-separated current
   (plus the leak under mixing) would push `qec-transverse-decomposition` from calibration toward vindication.
3. The standing open threads below (Tier-2 sgMAM #1; β-collapse R3 #3).
**Consult the substrate ledger before proposing or hunting any new substrate** (affordance gate first).

*Original data-hunt prompts (resolved — kept for reference).* Two outbound prompts were out:
1. `docs/research_prompt_chirality_sector_independence.md` — *already returned, messy* (reports appended;
   prediction A demoted). No further action unless a clean chirality + morphometrics dataset surfaces.
2. `docs/research_prompt_shell_data_sources.md` — **the live one.** When its reports land: append them under the
   prompt, then triage what data actually exists against the readouts — **T2** (heteromorph vs normal growth
   trajectories — does the heteromorph lose the self-similar fixed point?), **T1** (teratological reversal
   specimens — are flips discrete?), **the clock** (determinate-growth-to-cessation + energetic budget — does the
   stop track a gain/loss balance, beating the life-history alternative?), **cost-asymmetry** (energetic budget
   alongside the trajectory). First move: decide which readout is *runnable on the data that exists* → promote
   that one toward `battery`, park the rest. **The data is the gate — nothing in the seashell program is runnable
   without it.**

**Prior session — gMAM built + adjudicated — `current-aids-escape` KILLED as a barrier effect,
metabolized as the transverse-decomposition theorem.** The arc:
- **gMAM minimizer implemented + validated** (Maier–Stein gate: gradient action `0.5000` to 0.01%, and the
  `β>β_c` instanton correctly bows off-axis — `gmam_maier_stein.py`).
- **Homochiral: the σ→0 quasipotential is FLAT in the current** — `ΔŜ_H≈0` over `𝒜:0→21.8`
  (`Ŝ=0.382→0.380`, vs the finite-σ slope's `−17%`), robust across seed/momentum/eps/both-groups; the
  instanton never bends off the symmetric subspace (`gmam_current_aids.py`, `gmam_affinity_scaling.py`).
  Autocat A: the consistent null. So the committed finite-σ `ΔV` drop (`0.328→0.272`) is the **irreversible
  Eyring–Kramers PREFACTOR**, not the FW barrier (`ΔV_eff = ΔV_true + σ²·logK(𝒜)`).
- **Why (symmetry):** the current is *exactly transverse* to the escape mode at the saddle
  (`|cos(J,e_u)|~1e-15`; escape = 100% the between-group breaking mode, current = within-group 3-cycle),
  **symmetry-protected** — exact across a saddle-moving μ-sweep (`gmam_orthogonality_sweep.py`), broken `∝δ`
  by a within-group Z₃ break (`gmam_symmetry_break_probe.py`). Barred from `ΔV` by the
  **transverse-decomposition theorem** (Graham–Haken; FW §4.3; Bouchet–Reygner). 3 outside reports unanimous
  (`docs/research_prompt_current_aids_escape_prefactor_theorem.md`).
- **Selection rule confirmed in-substrate:** mixing the irreps with that same δ turns the barrier effect ON
  (`ΔŜ_H: 0→0.33` as `e_u·cyclic→0.64` — the Maier–Stein bow-out, `gmam_mixing_test.py`).
- **LANDED in canon:** `pa:transverse-decomposition` (new prior-art); receipts §Branch-survival barrier
  (reversed reading); frontier §Tombstones `current-aids-escape`; `character.md` §Two tangent sectors (the
  large-deviation face of the DFS) + §The two-survivals plane (`ΔV⊥𝒜` by symmetry). Broader implication —
  the metric⊥topological orthogonality, asserted in five dialects across `character.md`, is **one mechanism**
  (Schur → transverse decomposition; protected current barred from the metric sector's barriers, confined to
  their prefactors). **► Next: Tier-2 Hamiltonian sgMAM** (no ε) to confirm invariance at extreme exclusion
  (μ≈3, past the Tier-1 ε-floor where ΔŜ scatters); the surface-code reading (same orthogonality) is asserted
  not computed. See Open threads #1–#2.

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

1. **Tier-2 Hamiltonian sgMAM — confirm barrier-invariance at extreme exclusion (μ≈3).** The Tier-1
   ε-regularized gMAM converges cleanly at the operating point (μ=1.6) and the interior end (μ=1.0: `ΔŜ=0`
   eps-stable), but at strong exclusion (μ=3.0, attractor jammed on the orthant boundary) it hits its noise
   floor — `ΔŜ` scatters `±0.09` and flips sign in both nit and eps (`gmam_orthogonality_sweep.py` extremes).
   The saddle orthogonality there is still machine-exact (symmetry-protected), so the symmetry argument
   *predicts* invariance; the Hamiltonian sgMAM (Grafke–Schäfer–Vanden-Eijnden, first-derivative-only, no ε
   — momentum stays finite as `xᵢ→0`) is the right tool to verify it without the boundary blowup. Plan §3
   Tier-2 + §8. Low urgency (the verdict doesn't hinge on it; this closes the one boundary-limited corner).
2. **The surface-code reading — ✓ RESOLVED 2026-06-05** (computed; frontier `qec-transverse-decomposition`,
   receipts §QEC transverse decomposition). The asserted barrier-invariance reading is now measured: logical
   ⊥ syndrome exact; bit-flip barrier exact-invariant to a syndrome-active phase current; leak ∝ δ under
   Y-mixing; and the boundary mapped — exact invariance is symmetry-protected, not generic (no within-sector
   exact-transverse current at d=5). Unifies the three checked substrates under one mechanism (Schur).
   Remaining (optional): a real-substrate instance → vindication (PICK-UP #2).
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

- **Core (committed):** `character.md` (+ §Two-tangent-sectors large-deviation note, §two-survivals `ΔV⊥𝒜`),
  `character_receipts.md` (§Branch-survival barrier reversed to the prefactor reading), `character_frontier.md`
  (`battery:two-survivals-plane` crossed; `current-aids-escape` **tombstoned**; §Nudges HELD),
  `character_prior_art.md` (+ `pa:transverse-decomposition`), `character_grounding_method.md`.
- **`experiments/` (gMAM cluster, this session):** `gmam_current_aids` (the runner — validated minimizer +
  A/H run + eps-sweep), `gmam_maier_stein` (the §6.1 validation gate, exact 0.5), `gmam_saddle_orthogonality`
  (current⊥escape at the saddle, machine-exact), `gmam_affinity_scaling` (Ŝ(𝒜) flat vs Kramers ΔV(𝒜) drop),
  `gmam_orthogonality_sweep` (symmetry-protection across μ + the μ=3 Tier-1 boundary floor),
  `gmam_symmetry_break_probe` (cos(J,e_u)∝δ — orthogonality *is* the symmetry), `gmam_mixing_test` (selection
  rule — barrier turns on as irreps mix). Prior: identity_survival_barrier, current_aids_escape (+ _alignment),
  cycle_affinity, rps_affinity, reset_redrive_test, mu_sweep, hopfield_corner, neither_corner, beta_collapse,
  deformer_loop, twin_cycle_corner, twin_mu_sweep, autocat_pitchfork, autocat_both (+ PNGs).
- **Research records (`docs/`):** **gmam_plan** (the as-built record + verdict + the owed Tier-2),
  research_prompt_current_aids_escape_prefactor_theorem (3 reports, unanimous: the transverse-decomposition
  theorem + irreversible EK prefactor), research_prompt_current_aids_escape_interpretation (the earlier
  geometric-selection-rule round), review_prompt_competitive_exclusion, review_request_identity_survival,
  beta_collapse_3rd_register_design, research_prompt_beta_3rd_register_substrate, research_prompt_beta_r3_derivation.
