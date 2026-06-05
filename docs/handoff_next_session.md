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
- **The QEC arc generalized into a portable protocol** — the **transverse-decomposition test (TDT)**,
  written up in §TDT below — and immediately **run on a third substrate, glass**
  (`glass_aging_transverse.py`): on a biased ring the aging/relaxation spectrum is invariant to the
  protected current to machine precision across a wide affinity sweep (the established currents inside
  it), the current confined to the imaginary part; breaking the ring's $Z_N$ symmetry couples them (∝δ²
  onset). This **computes the cross-rule** ("aging never couples to circulation") — asserted in
  `character.md` §The cross-rule, now measured — and broadens it: the protected current is barred from
  *all* metric-sector observables (barrier / logical-error exponent / aging exponent). Glass's ledger 💎
  filled.

**► PICK UP HERE (updated 2026-06-05 session 3).** The QEC transverse-decomposition arc is complete and
banked (moves 1–3; Open Thread #2 resolved). The **shell program is closed** — dead-end substrate; see the
substrate ledger (`framework/character_substrate_ledger.md`), which now holds the verdict + the re-homed
deposit. Open, ranked, none blocking:
1. **Frontier de-mess — DONE this session.** A scannable **Dashboard** index (all rungs, one row per
   entry: `key | one-line verdict`, substrate foregrounded) sits at the top of `character_frontier.md` —
   additive and lossless, the dense prose preserved verbatim below. The four dead shell Steeping entries
   were deleted (recorded in the substrate ledger). Any further compression is optional; the de-mess
   principle is established (additive dashboard + delete only genuinely-dead/redundant, never the
   categorically-necessary cross-doc repetition).
2. **Optional QEC move 4** — a *real* substrate showing barrier-invariance to a symmetry-separated current
   (plus the leak under mixing) would push `qec-transverse-decomposition` from calibration toward vindication.
3. The standing open threads below (Tier-2 sgMAM #1; β-collapse R3 #3).
**Consult the substrate ledger before proposing or hunting any new substrate** (affordance gate first).

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

## Portable protocol — the transverse-decomposition test (TDT)

The QEC arc was not about QEC; it is a **reusable test** for the metric ⊥ topological orthogonality
(`pa:transverse-decomposition`) in any driven substrate. Run on the homochiral triad (gMAM),
the surface code (QEC), and the aging/glass sector (receipts §Glass aging transverse — a third clean
run). May now graduate to `character_grounding_method.md`.

**Preconditions — run the affordance gate first** (`feedback_substrate_affordance_filter`): a driven
NESS with (i) a **protected current** 𝒜 you can tune, (ii) a **metric-sector observable** `B` (an
escape barrier ΔV, a logical-error exponent, an aging exponent…), (iii) a **symmetry** separating the
current's sector from `B`'s mode, and (iv) a **knob δ** that breaks it. No tunable current ⇒ vacuous
(an equilibrium / aging-only substrate fails here, the dead-shell trap).

**The three moves:**
1. **Orthogonality** — show the current lives in a different sector/irrep from `B`'s escape/relaxation
   mode (`cos≈0`, or zero syndrome, or a Re/Im split).
2. **Invariance** — sweep 𝒜 **with the established current values as a subset of the sweep**; `B` is
   invariant across the *whole* range (not one cherry-picked point). This is `ΔV⊥𝒜` / "aging never
   couples to circulation." The current rides the prefactor / the imaginary part / the conjugate sector.
3. **Selection rule** — turn on δ (break the protecting symmetry / add proximity); `B` becomes
   𝒜-sensitive **∝ δ**. The orthogonality is *symmetry-protected, not generic*.

**Output:** converts an *asserted* decoupling into a *measured* one; deposits a candidate sentence; and
each new substrate broadens the class of metric observable `B` shown to exclude the current.

**Realizations (all run):** triad (`B` = escape barrier ΔV; gMAM) · surface code (`B` = logical-error
exponent; CSS X/Z = the symmetry) · glass (`B` = aging exponent / relaxation rate; the ring's `Z_N`
translation = the symmetry — machine-precision invariance across the affinity sweep,
`glass_aging_transverse.py`).

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

- **Core (committed):** `character.md` (§Two-tangent-sectors, §two-survivals `ΔV⊥𝒜`, §The cross-rule
  *computed*), `character_receipts.md` (§Branch-survival; **§QEC transverse decomposition**; **§Glass aging
  transverse**), `character_frontier.md` (opens with a **Dashboard** index; + `qec-transverse-decomposition`
  [sharpening]; dead shell entries removed; `current-aids-escape` tombstoned), `character_prior_art.md`
  (`pa:transverse-decomposition` + QEC/glass instances), **`character_substrate_ledger.md`** (the substrate
  roster), `character_grounding_method.md`.
- **`experiments/` — QEC + glass (session 3, the transverse-decomposition test):**
  `qec_transverse_decomposition`, `qec_syndrome_current`, `qec_within_sector_current`, `glass_aging_transverse`;
  the dead-end shell tests `shell_t2_anchor`/`_volume`/`_collins` (substrate closed — see ledger).
- **`experiments/` (gMAM cluster, session 1):** `gmam_current_aids` (the runner — validated minimizer +
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
