# Character — next-session handoff

State pointer for the next session. Thin by design; delete lines as work lands.

## Banked this session

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
  sign-coupling, not the numbers. **Receipts/frontier edits applied (uncommitted), held for review** — incl.
  the open core proposal: `both`'s core description ("mirror branches") generalized to cover co-handed
  branches. NB: folded in the **already-banked demographic-noise robustness** (it was still marked *owed* in
  receipts §Branch-survival barrier + frontier — stale; now both owed items read paid).
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
2. **Twin-cycle μ-sweep** *(cheap strengthening; touches open review Q1)* — the twin instances `both` at
   `μ=1.6`, but a μ-sweep would test whether the competitive-exclusion threshold `μ_c=(1+a+b)/3` and the
   *linear* `ΔV∝(μ−μ_c)` recur under the **exchange** symmetry (universality of the normal form across
   symmetry type, not just parity). Reuses `mu_sweep.py`'s structure with the twin field. Low appetite,
   but it would turn the open pitchfork-vs-competitive-exclusion question into a cross-symmetry data point.

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
  `reset_redrive_test.py`, `mu_sweep.py`, `hopfield_corner.py`, `neither_corner.py`,
  `beta_collapse.py`, `deformer_loop.py`, `twin_cycle_corner.py` (+ PNGs). `identity_survival_barrier.py`
  gained a `noise_kind` arg (additive default unchanged; `compare` runs additive vs demographic).
  `twin_cycle_corner.py` imports the validated `ep_affinity` (cycle_affinity) and the homochiral field
  (identity_survival_barrier) for the measured parity-vs-exchange sign contrast; `smoke` arg for a fast probe.
- Committed to `main` and pushed at session end (README + grounding method + experiments + the core edits).
- **Uncommitted as of the twin-cycle session:** `twin_cycle_corner.py` (+ PNG), and ledger edits to
  `character_receipts.md` (§Branch-survival barrier, §Two-survivals plane) + `character_frontier.md`
  (Recently-crossed Owed line, the two-survivals battery) — held for review. Open core proposal (not yet
  applied): generalize `both`'s `character.md` description from "mirror branches" to also cover co-handed
  (exchange) branches.
