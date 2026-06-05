# Character — next-session handoff

State pointer — **forward-facing only**: where things are now and what to do next. The chronology lives in
git + canon (`character.md` / `character_receipts.md` / `character_frontier.md` / `character_substrate_ledger.md`);
**do not accrete dated session-history blocks** — *rewrite* the current-state section each session, don't append.
All work below is committed + pushed.

## Where things stand (current)

**State (2026-06-05, end of the real-data arc).** The live frontier is the **transverse decomposition**,
generalized into the portable **transverse-decomposition test (TDT)** (§below), run synthetically on the triad
(gMAM), surface code (QEC), and glass (aging) — and now carried to a **real substrate** for the first time.

- **The cross-rule is upgraded** (`character.md` §The cross-rule; receipts §Colloid ring transverse). No longer
  "aging never couples to circulation" (exact invariance) but a **symmetry-protected linear selection rule** —
  the *linear-response face of the transverse decomposition*: `∂(aging rate)/∂𝒜|₀ = 0` is symmetry-forbidden,
  reopening `∝ δ` once the symmetry breaks. Exact flatness (the glass) is the **degenerate** special case; the
  generic colloid gives `c₁ = kδ + O(δ³)`. **The invariant is the forbidden linear channel, not flatness.**
- **First real-substrate-calibrated instance — the driven colloid on a ring** (Bechinger/Seifert toroidal trap =
  the physical glass-ring). Path A done (`experiments/colloid_ring_transverse.py`): operator validated vs the
  analytic free ring; Move 1 = the Re/Im split Blickle 2009 (arXiv:0902.2650) measured; threshold machine-zero
  iff reflection-symmetric (symmetric finite-difference **and** degenerate 2×2 PT); onset `c₁=kδ` slope 1 over
  seven decades. 🔵 live in the ledger. Real-*data* vindication is the owed experiment (PICK UP HERE #1).
- **The real-data hunt converged on a structural law** (ledger §Structural finding): the TDT needs a *transverse*
  current with an affinity *decoupled* from the barrier — a driven-NESS-with-fuel property real **devices** lack
  (no current / collinear current / co-tuned current). `r(δ) ≠ the test`. That is why the device hunt stalled.
- **The door-widening method is canon:** **[`framework/character_substrate_method.md`](../framework/character_substrate_method.md)**
  — the reproducible process that broke the stymie (affordance gate → the three failure modes → the two wideners
  [discrete symmetries qualify; target the linear selection rule, not exact invariance] → read-primaries
  discipline → generate-don't-hunt → the numerical protocol). **Read it before proposing or hunting any substrate.**

**► PICK UP HERE.** The cross-rule arc is complete and banked (canon + `character_substrate_method.md`). Open,
ranked, none blocking:
1. **The owed colloid experiment — the real-data vindication now in reach.** On an SLM/EOM ring-trap rig
   (Bechinger/Seifert lineage) sweep the optical potential through *exact* reflection symmetry (symmetric
   `V₀cos x + V₂cos 2x` ↔ ratchet `+ δ·sin 2x`) and measure the relaxation rate's linear-in-current coefficient
   `c₁` crossing zero **linearly** at the symmetric point — the predicted signature, **software-only** on existing
   hardware. Draft the one-page proposal (prediction + sweep + falsifier) from
   `experiments/colloid_ring_transverse.py`; pin parameters to Blickle 2009 if the PDF lands in `docs/temp`. Open
   archive class still to scout (each owes a transversality check): **stochastic pumps, non-Hermitian relaxation
   spectra, transverse reaction networks** (`character_substrate_method.md` §7).
2. The standing open threads below (Tier-2 sgMAM #1; β-collapse R3 #3).

**Before proposing or hunting any new substrate: read [`character_substrate_method.md`](../framework/character_substrate_method.md)
and consult the substrate ledger** (affordance gate first).

## Portable protocol — the transverse-decomposition test (TDT)

The QEC arc was not about QEC; it is a **reusable test** for the metric ⊥ topological orthogonality
(`pa:transverse-decomposition`) in any driven substrate. Run on the homochiral triad (gMAM), the surface code
(QEC), the aging/glass sector (receipts §Glass aging transverse), and the driven colloid ring (receipts §Colloid
ring transverse). May graduate to `character_grounding_method.md`.

**Preconditions — run the affordance gate first** (`character_substrate_method.md`; `feedback_substrate_affordance_filter`):
a driven NESS with (i) a **protected current** 𝒜 you can tune, (ii) a **metric-sector observable** `B` (an escape
barrier ΔV, a logical-error exponent, an aging/relaxation exponent…), (iii) a **separating symmetry** under which
𝒜 is odd and `B` even, and (iv) a **knob δ** that breaks it. No tunable current ⇒ vacuous (the dead-shell trap);
current collinear with `B`'s coordinate ⇒ fails (iii) (the bistable-memory trap).

**The three moves:**
1. **Orthogonality** — the current lives in a different sector/irrep from `B`'s escape/relaxation mode
   (`cos≈0`, or zero syndrome, or a Re/Im split).
2. **Invariance (the selection rule)** — the *linear* coupling of `B` to the current is symmetry-forbidden:
   `∂B/∂𝒜|₀ = 0`. In the degenerate/special case (QEC, glass) `B` is flat to machine precision across the whole
   𝒜-sweep; generically (the colloid) only the linear coupling vanishes, leaving `O(𝒜²)` curvature. The current
   rides the prefactor / the imaginary part / the conjugate sector.
3. **Selection rule onset** — turn on δ (break the symmetry / add proximity); `B` becomes 𝒜-sensitive, reopening
   `∝ δ` (the onset power is parity-dependent; the **threshold** — zero iff symmetric — is the robust invariant).

**Output:** converts an *asserted* decoupling into a *measured/computed* one; each new substrate broadens the
class of metric observable `B` shown to exclude the current.

**Realizations (all run):** triad (`B` = escape barrier ΔV; gMAM) · surface code (`B` = logical-error exponent;
CSS X/Z = the symmetry) · glass (`B` = aging exponent; `Z_N` translation — exact, the degenerate limit) · **driven
colloid on a ring** (`B` = relaxation rate; reflection symmetry — the generic linear selection rule `c₁=kδ`;
`colloid_ring_transverse.py`).

## Open threads (ranked; none blocking)

1. **Tier-2 Hamiltonian sgMAM — confirm barrier-invariance at extreme exclusion (μ≈3).** The Tier-1
   ε-regularized gMAM converges cleanly at the operating point (μ=1.6) and the interior end (μ=1.0: `ΔŜ=0`
   eps-stable), but at strong exclusion (μ=3.0, attractor jammed on the orthant boundary) it hits its noise
   floor — `ΔŜ` scatters `±0.09` and flips sign in both nit and eps (`gmam_orthogonality_sweep.py` extremes).
   The saddle orthogonality there is still machine-exact (symmetry-protected), so the symmetry argument
   *predicts* invariance; the Hamiltonian sgMAM (Grafke–Schäfer–Vanden-Eijnden, first-derivative-only, no ε
   — momentum stays finite as `xᵢ→0`) is the right tool to verify it without the boundary blowup. Plan §3
   Tier-2 + §8. Low urgency (the verdict doesn't hinge on it; this closes the one boundary-limited corner).
2. **β-collapse R3 sum-rule check** *(low priority)* — model c's `α_s+β=1` vs a/b's no-exponent; the vary-`k`
   probe repurposed (confined fLE + CK estimator). A *side* finding (complementarity relation), **not** the
   collapse. Or close R3 clean. My lean: let it rest unless the sum rule itself interests.
3. **Nudge corpus** — HELD. Next loaded-endpoint / steering-miss → log as a nudge (or add a trigger to an
   existing one); promote nothing. Watch whether they cluster in the apparent-structure≠protected shape.

## Doc + experiment state

- **Core (committed):** `character.md` (§Two-tangent-sectors, §two-survivals `ΔV⊥𝒜`, **§The cross-rule — now the
  symmetry-protected linear selection rule**), `character_receipts.md` (§QEC transverse decomposition; §Glass
  aging transverse; **§Colloid ring transverse**), `character_frontier.md` (Dashboard index; `qec-transverse-
  decomposition` [sharpening]; `current-aids-escape` tombstoned), `character_prior_art.md`
  (`pa:transverse-decomposition`), **`character_substrate_ledger.md`** (substrate roster + §Structural finding),
  **`character_substrate_method.md`** (the door-widening method), `character_grounding_method.md`.
- **`experiments/` — colloid (this session, the cross-rule upgrade):** `colloid_ring_transverse.py` — the
  driven-colloid Fokker–Planck operator: free-ring validation, the Re/Im split (Move 1), the machine-zero
  threshold (Move 2, two methods), the `c₁=kδ` selection rule (Move 3, degenerate 2×2 PT), and the
  degenerate-step diagnostic (single-harmonic → +V₂ cos 2x); PNG.
- **`experiments/` — QEC + glass:** `qec_transverse_decomposition`, `qec_syndrome_current`,
  `qec_within_sector_current`, `glass_aging_transverse`; the dead-end shell tests
  `shell_t2_anchor`/`_volume`/`_collins` (substrate closed — see ledger).
- **`experiments/` (gMAM cluster):** `gmam_current_aids` (the runner — validated minimizer + A/H run + eps-sweep),
  `gmam_maier_stein` (the §6.1 validation gate, exact 0.5), `gmam_saddle_orthogonality` (current⊥escape at the
  saddle, machine-exact), `gmam_affinity_scaling` (Ŝ(𝒜) flat vs Kramers ΔV(𝒜) drop), `gmam_orthogonality_sweep`
  (symmetry-protection across μ + the μ=3 Tier-1 boundary floor), `gmam_symmetry_break_probe` (cos(J,e_u)∝δ —
  orthogonality *is* the symmetry), `gmam_mixing_test` (selection rule — barrier turns on as irreps mix). Prior:
  identity_survival_barrier, current_aids_escape (+ _alignment), cycle_affinity, rps_affinity, reset_redrive_test,
  mu_sweep, hopfield_corner, neither_corner, beta_collapse, deformer_loop, twin_cycle_corner, twin_mu_sweep,
  autocat_pitchfork, autocat_both (+ PNGs).
- **Research records (`docs/`):** the driven-NESS substrate-scout prompts (`research_prompt_driven_ness_transverse.md`,
  `research_prompt_ring_laser_move3_data.md`, `research_prompt_tdt_move4_real_substrate.md`); **gmam_plan** (the
  as-built record + verdict + the owed Tier-2); research_prompt_current_aids_escape_prefactor_theorem;
  research_prompt_current_aids_escape_interpretation; review_prompt_competitive_exclusion;
  review_request_identity_survival; beta_collapse_3rd_register_design; research_prompt_beta_3rd_register_substrate;
  research_prompt_beta_r3_derivation.
