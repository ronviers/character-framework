# Character — next-session handoff

State pointer — **forward-facing only**: where things are now and what to do next. The chronology lives in
git + canon (`character.md` / `character_receipts.md` / `character_frontier.md` / `character_substrate_ledger.md`);
**do not accrete dated session-history blocks** — *rewrite* the current-state section each session, don't append.
All canonical work below is committed + pushed. The two believing-mode docs are deliberately local (untracked).

## Where things stand (current — 2026-06-21)

**The make-or-break has resolved toward the C-middle.** Two independent results now bound the framework's
ceiling:
- **Universal-invariant classification — clean negative** (receipts §Universal-invariant classification;
  `docs/universal_invariant returns.md`): there is **no model-independent classifying structure** under which
  `sign(𝒜)` is a universal invariant. The literature's structures are substrate-bound (Polettini
  gauge-cohomology — new key `pa:gauge-thermodynamics`; Harary/Zaslavsky balance; Andrieux–Gaspard cycle
  theory). The deformation framing is obstructed (same-sign substrates aren't deformable into one another).
- **Composition-law build — C-middle** (`experiments/composition_law.py`; receipts §Composition-law build):
  minting *does* compose by one substrate-general law (well-defined, unital `0⊗0→1`, associative,
  forced-not-fitted) — **but it is the cycle-space homology import**, not novel machinery, and it **splits**:
  the *existence/frustration* bit composes as a clean cycle-space algebra; the *value* bit `sign(𝒜)` is
  ℝ-additive / coupling-dependent (no group fusion).

So the grand **"physical category / new state variable" claim is disfavored** (no novel structure: the two
results agree). **Metaphor-collapse is averted** — two *computed* cross-substrate laws stand (the
transverse-decomposition theorem + this composition law). The honest verdict: the framework is a
**substrate-general, problem-formulating reading built on imported structure** — its durable value is as a
**constraint-language** (it carves messy domains into well-posed questions and clean nos), independent of the
grand-claim verdict.

**Also closed/synced this session:**
- `curvature-as-coupling-bias` **✗ → tombstone**: three outbound passes — the surviving `O(𝒜²)` coefficient is
  the leading *analytic* response coefficient (resolvent sum / equilibrium covariance), **not** a geometric
  curvature; reinforces the transverse theorem. `character.md` §Motion and proximity + cross-rule aligned.
- `chiral-rotor-triad` **↑ → `battery:chiral-rotor-triad`** (synced from the Triskele build, calibration; all
  three kill-switches pass): carried the *corrected* mechanism — the deterministic triad locks, the protected
  current is **noise-activated hopping**, non-reciprocity is drive-generated, the current lives in the
  collective configuration. Physical build still owed.
- `character.md` audited and **aligned** (3 flat-out-wrong spots fixed: the curvature straggler, the
  composition over-claim, the pre-existing `𝒜≠0 ⟺ complex pair` iff that contradicted the binding receipt).

**The session's most generative arc (the abiogenesis / origins line):** reproduction is cheap (degenerate
pattern-replication everywhere); the substrate ladder **object → dissipative medium → ecology**;
**environment = information × reader** (relational, not anthropic — "a place to be fit in"); the
`escape-degenerate-replication` reframe (the question is not *how to replicate* but *how to break the
degeneracy*); the **scale-of-character** prediction + **gravity-contingent carbon** (gravity sets the strata
window → casts which assembly scale, hence which chemistry, participates); the `battery:strata-current`
sort-vs-mint discriminator (built, `strata_sort.py`); and the **`reading-transition`** — *reading splits like
reproduction*: cheap (metric, the cross-rule, pre-heredity) vs hard (bit-level, superselection-gated, only
across replacement = **proto-heredity**), so reader and heredity co-emerge at the bit and the tape stays
unforced. The strong-model read named the load-bearing beam: **"define reading before heredity — the framework
lives or dies there."** **`battery:readability` is now built and run (`experiments/readability.py`) and puts a
number on that beam** (receipts §Readability battery): metric readability turns on generically; the
within-lifetime bit-readability null is machine-exact (the gradient is curl-free — superselection holds); and
the order parameter `R_hard = ∂⟨sign 𝒜⟩/∂d` evaluated **over a lineage** is 0 below the symmetry-break and
turns on ∼linearly above it. **Strong-model sharpening (this session, folded into `reading-transition`):** the
two readings sit in different superselection sectors and mirror the two reproductions exactly (metric:state ::
degenerate:pattern; bit:sign :: heritable:bit); **selection is the unique channel from the metric into the
topological sector** (a projection operator: metric ecology → replacement → bit retention, no instantaneous
route); so the framework predicts a kingdom of **metric readers** (responsiveness, `∂M/∂E≠0` with `∂𝒜/∂E=0`
in a lifetime), and the threshold is the **appearance of ecological access to the protected sector** — reader
and heredity, same bridge, opposite projections.

**Two believing-mode generators (LOCAL, untracked, fenced):** `docs/character_credo.md` (the framework as
settled science) and `docs/character_abiogenesis.md` (origins as if vindicated). For generating ideas from,
not at; each carries the credo's prohibitions so scenarios stay viable. Not committed (repo is public).

## ► PICK UP HERE (ranked; none blocking)

**★ NEWEST (2026-06-24) — circulation-held capacity `K(C)`: two curve points landed + folded into canon.**
Own handoff: [`handoff_circulation_held_capacity.md`](handoff_circulation_held_capacity.md). Decomposition —
*Organization = circulation-held `K(C)` + archive-held* (DNA = the distinctions whose fidelity exceeds the
circulation's self-specifying capacity), `K(C) = K_topo(b₁) + K_metric`. **(1) KaiABC** `K=2` (Rust 2007
phosphoform model, `kaiabc_capacity.py`; both kill-gates cleared, forced-not-fitted). **(2) Peroxidase-oxidase**
`K=4` — the first **distinct** point, via b₁=3 (two coupled enzyme redox loops; BFSO model, `bfso_capacity.py`).
Receipts + frontier (`circulation-held-capacity`, `battery:circulation-capacity`) updated. The cut is shown
substrate-general across two enzyme modalities. **► NEXT SESSION STARTS WITH the engine→character transition**
(Stage 2→3): character is **not an add-on to engines — it is a *phase* available to sufficiently structured
engines**, so the question parallels "can an engine generate metabolism?" → *can an engine generate character?*
Task = make the crossing a **measured phase boundary**: a metric engine (`𝒜=0`) structured past a threshold
turns on a protected current (`𝒜≠0`); seed apparatus = `battery:strata-current` (sort-vs-mint) + the
symmetry-break onset from `battery:readability`/TDT. See `handoff_circulation_held_capacity.md` ► NEXT SESSION.
**Deeper blockers preserved behind it (route to core):** the **archive term** (deepest, unmeasured —
`docs/research_prompt_archive_term.md`, in-hand candidate = embryonic cell-cycle); the **QEC keep-as-capacity
anchor** for the derived **finite-wall** result (`research_prompt_keep_derivation.md`, 3/3 models agree —
heuristic flagged); plus K_metric≥2, class-generality, K_topo-uniformity. Sits on the
`escape-degenerate-replication` / `self-referential-closure` line; reproduction is a different framework
(von Neumann/Eigen), the write-bar = TDT.

0. **DONE this session — `battery:readability` built + run** (`experiments/readability.py`; receipts
   §Readability battery; `character_frontier.md` `battery:readability` + `reading-transition` updated). All
   kill-switches pass synthetically (metric reading on; within-lifetime bit-readability null machine-exact;
   `R_hard` over a lineage 0→nonzero at the symmetry break, ∼linear onset; co-emergence needs both channels).
   Synthetic = calibration: the **real-substrate reader is the owed instance** (→ item 3, the bootstrap).
1. **The colloid superselection premise on real data — the one remaining real-data make-or-break.** On an
   SLM/EOM ring-trap rig (Bechinger/Seifert lineage) sweep the optical potential through *exact* reflection
   symmetry and measure the relaxation rate's linear-in-current coefficient `c₁` crossing zero **linearly** —
   software-only on existing hardware. Draft the one-page proposal from `experiments/colloid_ring_transverse.py`
   (we can write the proposal; the rig isn't ours). This tests the premise the whole composition/classification
   edifice rests on.
2. **`battery:strata-current` — scan engineering separation data.** Centrifuges, fluidized beds, granular
   segregation, distillation trays, sedimentation: abundant real data, all on the sorting axis (`𝒜=0`) — a free
   **✗-harvest** ruling out a salient class as *stage*. The **↑-scan** is the rare exception: a sort-independent
   inter-strata circulation (oscillatory/cyclic segregation; a granular rock-paper-scissors) at the
   Batchelor–Ozmidov scale.
3. **The `escape-degenerate-replication` bootstrap (hard, open).** Generate from `character_abiogenesis.md`, but
   the owed instance is the genuinely hard one: a protected bit minted on a *real* dissipative medium that
   *reads* its ecology (breaks degeneracy) — i.e. the **real-substrate reader** `battery:readability` calls for
   (`R_hard≠0` over a lineage on real data). The framework's current best is the templating result (degenerate,
   ~1 bit, needs a tape).
4. **Standing threads (low priority):** Tier-2 sgMAM (μ≈3 barrier-invariance corner); β-collapse R3 sum-rule;
   the nudge corpus (HELD). See below.

**Discipline (carry):** synthetic = calibration, never vindication (the build + batteries calibrate; the
real-substrate is the frontier — `project_killshot_synthetic_is_imported_math`). The **reader** is the one
novel object; the **tape is unforced** (von Neumann threshold — not bootstrapped by reading); **carbon is
contingent** (gravity-cast, not necessary). Don't over-fire ↑ (the composition build passed its mechanical
checklist yet only earned the C-middle — calibration ≠ category); don't over-bank ✗ (a clean negative is a
result; the metaphor verdict is *not* forced). Read `character_substrate_method.md` (salience ≠ affordance)
before hunting any substrate.

## Portable protocol — the transverse-decomposition test (TDT)

A **reusable test** for the metric ⊥ topological orthogonality (`pa:transverse-decomposition`) in any driven
substrate — run on the homochiral triad (gMAM), the surface code (QEC), the aging/glass sector, and the driven
colloid ring. **Preconditions** (affordance gate first): a driven NESS with (i) a tunable **protected current**
𝒜, (ii) a **metric-sector observable** `B` (barrier ΔV, logical-error exponent, aging rate…), (iii) a
**separating symmetry** under which 𝒜 is odd and `B` even, (iv) a **knob δ** that breaks it. **The three
moves:** (1) orthogonality — current in a different irrep from `B`'s mode (`cos≈0`); (2) invariance —
`∂B/∂𝒜|₀ = 0` symmetry-forbidden (flat to machine precision in the degenerate case; only the analytic `O(𝒜²)`
coefficient surviving generically — *not* a geometric curvature); (3) onset — break δ, `B` reopens `∝ δ`, the
**threshold (zero iff symmetric)** is the robust invariant. Output: converts an *asserted* decoupling into a
measured one; each substrate broadens the class of `B` shown to exclude the current.

## Open threads (ranked; none blocking)

1. **Tier-2 Hamiltonian sgMAM** — confirm barrier-invariance at extreme exclusion (μ≈3), where Tier-1
   ε-gMAM hits its noise floor. Symmetry *predicts* invariance (saddle orthogonality machine-exact); the
   Hamiltonian sgMAM (Grafke–Schäfer–Vanden-Eijnden, no ε) is the right tool. Low urgency.
2. **β-collapse R3 sum-rule** *(low)* — `α_s+β=1` (model c) vs no-exponent (a/b); a side complementarity
   relation, not the collapse. Let it rest unless the sum rule itself interests.
3. **Nudge corpus** — HELD. Next loaded-endpoint / steering-miss → log as a nudge; promote nothing; watch for
   clustering in the apparent-structure≠protected shape.

## Doc + experiment state

- **Frontier (`character_frontier.md`):** tombstone `curvature-as-coupling-bias`; `battery:chiral-rotor-triad`;
  `universal-invariant-classification` [sharpening, resolved → C-middle]; `escape-degenerate-replication`
  [sharpening, + scale prediction + gravity-contingent-carbon corollary]; `reading-transition` [sharpening, +
  the `R_hard`-over-a-lineage / selection-as-projection sharpening folded in]; `battery:strata-current`;
  `battery:readability` [**built + run 2026-06-21**; all kill-switches pass synthetically].
- **Receipts (`character_receipts.md`):** §Universal-invariant classification (clean negative); §Composition-law
  build (C-middle); §Readability battery (the reading transition as an order parameter — metric/bit split,
  machine-exact superselection null, `R_hard` over a lineage); §Chiral-rotor triad (Triskele calibration);
  strengthened §The binding (per-substrate carrier named). **Prior-art:** `gauge-thermodynamics` (Polettini 2012).
- **Core (`character.md`):** §Composition under coupling resolved (the build); §The cross-rule, §Frustration,
  §Motion and proximity aligned (curvature + iff fixes). *(readability is calibration → stays in frontier +
  receipts; not promoted to core — synthetic ≠ vindication.)*
- **`experiments/` (new this session):** `composition_law.py` (the C-middle build), `strata_sort.py`
  (the sort-vs-mint battery), `readability.py` (the reading-transition order parameter). Prior clusters
  (colloid / QEC+glass / gMAM / minting instances) unchanged — see git.
- **`docs/`:** `roadmap_universal_invariant.md` (Phase A resolved), `build_composition_law.md`,
  `universal_invariant returns.md`, `research_prompt_curvature_as_coupling_bias.md` (returns folded);
  **`character_credo.md`** + **`character_abiogenesis.md`** (LOCAL believing-mode generators, untracked).
