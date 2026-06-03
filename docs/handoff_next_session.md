# Character — next-session handoff

State pointer for the next session. Thin by design; delete lines as work lands.

## Banked this session

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

1. **Embodiment-minting instance** — compute the Schnakenberg affinity of a concrete closed
   perception-action loop (a frustrated controller vs a relaxational servo); instances the
   "frustrated ⇒ mints `𝒜≠0`" leaf. Cheap; the natural sequel to the embodiment grounding.
2. **Multiplicative-noise robustness of `ΔV`** — re-run `identity_survival_barrier.py` with demographic
   `√x` noise (the Freidlin–Wentzell quasipotential is noise-metric-dependent). Owed since the barrier landed.
3. **Second independent "both"-corner substrate** — a spontaneously-frozen system *outside* the
   homochiral family (`mpa-conform/scripts/{chiral_bonding,chiral_selffield,homochiral_cascade}.py`) to
   robustify branch survival. RPS does **not** qualify (structural).
4. **β-collapse** — the framework's *sharpest* falsifier (one `β` governing `α_s`, queue-tail, kernel),
   never run. Infrastructure exists (`mpa-central/library/primitives/{kww_oracle,east,voter}`); ~30 min
   post-processing.

## Open from outside review

- Is competitive-exclusion (degenerate / hard-saturating normal form, `ΔV` linear) the right reduction
  for the symmetric Lotka–Volterra L↔R competition, or does it coexist with a supercritical-pitchfork
  regime? (review-doc Q)
- The frame-sensitive `ΔV / ΔU` prefactor (FW barrier vs deterministic potential) — noted, not pinned.

## Doc + experiment state

- Core: `character.md` (branch membership; §The two-survivals plane), `character_receipts.md`,
  `character_frontier.md` (`battery:two-survivals-plane` crossed; `branch-survival` crossed),
  `character_grounding_method.md` (embodiment tree, Group II).
- `experiments/`: `identity_survival_barrier.py`, `cycle_affinity.py`, `rps_affinity.py`,
  `reset_redrive_test.py`, `mu_sweep.py`, `hopfield_corner.py`, `neither_corner.py` (+ PNGs).
- Committed to `main` and pushed at session end (README + grounding method + experiments + the core edits).
