# Handoff — circulation-held capacity `K(C)`, anchored on KaiABC

*Working doc. Pick up here. The test is kill-gated: run the make-or-break before the build.*
*Status (2026-06-25): **two curve points + the QEC keep-as-capacity anchor landed, all folded into canon.**
(1) KaiABC — `K = b₁(1)+phase(1) = 2`, forced-not-fitted (`experiments/kaiabc_capacity.py`; both kill-gates
cleared). (2) Peroxidase-oxidase (BFSO model) — `K = b₁(3)+phase(1) = 4`, the first **distinct** point, via two
coupled enzyme redox loops (`experiments/bfso_capacity.py`). (3) **QEC keep-as-capacity anchor**
(`experiments/qec_keep_capacity.py`, 2026-06-25): the core §The wall anchored on the surface/toric code — keep
= b₁ = #logical-qubits **literal** (k=2−χ), distance-vs-keep split exact, the wall = the code's **channel
capacity** (rigorous), replacing the derivation's `O(N log N)` heuristic (does item 5b; 5a still owed). Receipts
+ frontier updated. **The `2nd-point` gate is met; → core is NOT — blocked on the deeper items (see "Where it
lands").** Source PDFs in `docs/rust/`, `docs/second_capacity_substrate/` (gitignored, copyrighted).*

## The object

A decomposition surfaced over a long session (Rube-Goldberg → NESS → tape → here):

> **Organization = circulation-held part `K(C)` + archive-held part.**

`K(C)` = *circulation-retainable complexity* — the organization a running NESS recovers after **complete turnover of its constituent parts**, without consulting a static record beyond replacement of generic components. The archive-held part = the distinctions whose fidelity requirements **exceed** the circulation's self-specifying capacity (this is what DNA *is*, on this reading — not "a bootstrap file," but the standing high-dimensional part-spec the running fluxes can't regenerate).

The frontier object is a **capacity curve**: archive bits required as a function of maintained organizational complexity. Whirlpool / Bénard ≈ 0 archive → KaiABC low → regulatory net moderate → minimal cell high → modern cell very high. The science is: *where does circulation-held capacity fail, and is that ceiling universal or substrate-specific?*

## Settled this session — do not re-walk

1. **The "9 definers / thickened seam" is not a hole.** Geometry is already housed (realization/value sector); structure-on-the-seam is the boundary-malformation error (cf. tombstones `flip-cost-across-zero`, `sign-kill-bisection`).
2. **Drive-locked vs topology-locked was a mis-framing** (mine). Drive-arrow oddness is universal (Gallavotti–Cohen) — the triad reverses under its own drive reversal too. The real axis is **carrier depth** (N=2 continuous Gaussian vs N≥3 discrete frustration), *not* lock strength. The gyrator is a bona fide protected current, shallowly carried.
3. **The ~1-bit templating cap is capacity/rank (`b₁`), not copy-fidelity.** A single loop carries ~1 protected bit (rank-1 field); even a perfect copier transmits 1 bit. The three outside "proofs" (Eigen / siphoning / TUR) all argue *fidelity* — a different ceiling. "Can't copy a running loop" is **false** (cells copy their tape while fully running). Retire that phrasing.
4. **The mint→tape write factors as `consolidate ∘ copy`; the direct topological→metric write is TDT-barred** (a derived Weismann / Central-Dogma). Bootstrap circularity = the von Neumann threshold restated. This is a `composition`, un-instanced — it lives in receipts/frontier, **not** core. The candidate core line **dissolved**: it is either redundant with TDT + "structurally stored," or it imports von Neumann. No core edit.
5. **Replication/heredity is a different framework** (von Neumann / Eigen / pop-gen). Character's north star already separates **alive (recursive circulation) ≠ reproduction**. Character owns the *record-free regime* and the *boundary*; it does not own the theory of the archive.
6. **The reproduction/record split** (the new clean cut): eliminating *reproduction* is free for an immortal (no death → no daughters); eliminating the *record* is possible only **below the `K` bound**. New York proves the split — no daughter-New-York, yet record-saturated (blueprints, codes, archives). So the engineering examples (internet/grid/city) are record-*dependent* maintenance with the record outsourced — they cut *against* "no record," and they're human-domain (banned framing) anyway.

## The test (kill-first)

Substrate: **KaiABC** — the cleanest existing record-free maintained circulation. In-vitro (Nakajima et al. 2005, *Science*): KaiA + KaiB + KaiC + ATP oscillate ~24 h with **no DNA / no transcription in the loop**. Parts (phosphate groups, individual hexamers) turn over continuously; the collective phase/direction persists on ATP alone. The archive specifies the *proteins* (→ period); the *running state* (phase, direction, sync) is circulation-borne.

Modality: **operator from measured parts** (the winning modality — same as DNA network / gyrator / repressilator). Rate source: the ordered-phosphorylation reduced model, Rust–Markson–Lenz–Glass–O'Shea 2007, *Science* (phosphoform cycle U→T→ST→S→U, measured constants; pull the SI tables). Thermodynamics cross-check: van Zon–Lubensky–Altena–ten Wolde 2007, *PNAS*. **Use the reduced phosphoform master equation, NOT the full stochastic hexamer ensemble** (the latter is the memory-bound super-linear trap — see `feedback_keep_tests_under_one_hour`). Time a small probe, extrapolate, stay under an hour.

Operationalize `K(C)` so it is **not** circular:

- **Archive-held = operator parameters** (the rate constants — set by protein structure).
- **Circulation-held = the attractor's slow-state coordinates** that survive scrambling molecular identity at fixed parameters:
  - `K_topo = b₁` (protected, reset-stable, digital — the gauge-irremovable cycle signs).
  - `K_metric = dim` of the turnover-stable slow manifold beyond the fixed point (analog, reset-fragile — e.g. the limit-cycle phase = 1; a torus = 2; weakly-coupled sub-clocks add more).
- `K(C) = K_topo + K_metric`.

Compute on KaiABC: build the operator → confirm the phospho-cycle is a genuine NESS current (ATP-driven, detailed balance broken), with `sign(𝒜)` **forced-not-fitted** (= sign of the directly-solved NESS current) and structure-locked (ordered phosphorylation enforced by KaiA/KaiB → external-rewiring-mode → reset-recoverable). Then read off `b₁` and the slow-manifold dimension.

## Make-or-break — run THIS first

**Two kills, before any elaboration:**

- **(K is philosophy) — RUN structurally 2026-06-24, SURVIVES.** The original risk: if circulation-held vs
  archive-held cannot be separated choice-independently — because KaiC cooperativity makes the rates
  state-dependent, blurring "parameter" vs "state" — then `K(C)` is not a well-posed observable. **Resolution
  (against the model FORM, no constants):** the *reduced phosphoform* model carries the cut as its own
  published factorization, `w_ij(state) = k_ij⁰ · g(A_free)` with `A_free` a **mean-field functional of the
  collective S/ST fractions**. So `k_ij⁰` (intrinsic constants + sequestration stoichiometry, set by protein
  structure) is **archive**; the collective phospho-fractions + the limit-cycle phase are **circulation**. The
  operational choice-independence test passes: scrambling molecular identity at fixed `k⁰` and fixed collective
  fractions leaves the generator invariant (the coupling is population-level, not per-molecule). Decisive point:
  we did **not** impose this cut to rescue `K` — Rust–Markson 2007 already writes the rates as
  (intrinsic constant) × (KaiA-availability as a function of collective state). The blur returns **only** in the
  full per-hexamer allosteric ensemble (intra-hexamer cooperativity → a single molecule's rate depends on its
  own micro-state) — which is *also* the memory-bound super-linear trap (`feedback_keep_tests_under_one_hour`),
  so the reduced model is right on both counts. (Fuel filing: ATP is a held boundary condition in vitro →
  archive-side; were it depleting it would add a slow coordinate → *raises* `K`, doesn't blur the cut.)
- **(K is redundant) — RUN 2026-06-24, VINDICATED.** `K(KaiABC) = b₁ + phase = 1 + 1 = 2 > 1`, computed
  forced-not-fitted from the measured Rust 2007 constants (`experiments/kaiabc_capacity.py`). Evidence, all
  passing: (i) the measured constants give a sustained limit cycle (period ≈ 20.7 h, amplitude 1.36 µM); (ii) a
  genuine **forward** cyclic current `J_cyc = +0.025 µM/h`, equal across all four ring edges (Kirchhoff, single
  loop) — and it **collapses to zero** when the drive is cut (`[KaiA]=0` → all KaiC → U); (iii) the winding sign
  is **structure-locked** (0 flips in 26 oscillating rate-deformations); (iv) `b₁ = 1` (the U-T-D-S ring,
  E−V+1); (v) the monodromy/Floquet multipliers are `[1.000, 0.046, 6.6e-5]` — **exactly one marginal direction
  (the phase)** beyond the fixed point → `K_metric = 1`. **The "what's new":** the protected current is *not* a
  frozen-rate bias — the frozen-operator affinity is *negative* at high KaiA and flips sign with S, yet the
  limit cycle carries a robust forward current. The circulation is dynamically generated by the collective
  KaiA-sequestration feedback (it lives in the collective configuration — cf. `battery:chiral-rotor-triad`). So
  `K` is a real new observable on this substrate, **not** `b₁` relabeled.

**Vindicate:** `K(C)` computes cleanly, forced-not-fitted, **and `K > b₁`** (the phase / slow metric coordinates are circulation-held organization beyond the protected count). Expected on KaiABC: `b₁ ≈ 1`, `K_metric ≈ 1` (the phase) → `K ≈ 2 > 1`. If that holds *and the separation is choice-independent under cooperativity*, `K` is a real new observable and KaiABC is the curve's anchor point.

Then — and only then — the program has legs: port the method to a **second** substrate for point 2 of the curve. The affordance scan this session nominated same-modality candidates: **cardiac SA node**, the **CDK/APC cell-cycle oscillator**, **yeast glycolytic oscillation** (all genuine protected currents with published operator-buildable kinetics).

## ► NEXT SESSION — start here: the archive-held term (the deepest blocker)

**The engine→character transition was gated this session (2026-06-25) and resolved to: DON'T BUILD IT.**
Ron's reframe (character is a *phase* available to sufficiently structured engines — folded into
`character_credo.md` §The object, `character_abiogenesis.md` §Before the reader, the engine) is right, but a
*synthetic* engine→character phase-boundary sweep is a **demonstration, not a test**: `𝒜` is algebraically
pinned to the wiring by cycle-space homology (`strata_sort.py` run: `𝒜 = Ω` exactly, drive-independent;
`𝒜 ≡ 0` to machine zero at `Ω=0`), so it can only re-trace §Frustration + imported Schnakenberg — it **cannot
come out otherwise** (the `feedback_no_synthetic_sidequests` gate: works→nothing new, fails→nothing dies,
could-it-be-otherwise→no). And **the crossing is already instanced on real substrates**: KaiABC (ATP-engine,
the current is feedback-generated and collapses at drive-off) and PO (redox-engine, b₁=3) are engine→character
unities *past* the crossing. The only un-instanced piece is a **real pure-metric engine at `𝒜=0`** — an
affordance-poor substrate hunt (a Bénard cell *displays* a metric engine but can't afford the topological
sector; salience ≠ affordance), **not a build**. If the crossing is ever pursued it is a *real-substrate*
instance/proposal (Lane–Martin alkaline-vent bioenergetics, affordance-gated), parked. **Do NOT re-attempt the
synthetic engine→character sweep.**

**Landed instead: the QEC keep-as-capacity anchor** (`experiments/qec_keep_capacity.py`; receipts §QEC
keep-as-capacity; frontier `circulation-held-capacity` + dashboard). The core §The wall anchored on the
surface/toric code already in canon, replacing the derivation's one heuristic with exact code properties +
established QEC theorems: **(1)** keep = b₁ = #logical-qubits **literal** (`k = 2−χ`, two ways — GF(2) rank vs
Euler count; toric `k=2=b₁`, planar `[[9,1,3]]` `k=1=b₁`); **(2)** distance-vs-keep split **exact** (toric: keep
`b₁=2` fixed, distance `d=L` grows — a regular code scales protection-depth, never keep; keep grows only with
heterogeneous topology = the archived part — the §wall's crystal-escape made precise); **(3)** the wall = the
code's **channel capacity** (hashing `k/n ≤ 1−H₂(p)` + threshold `p_th≈0.109`, DKLP 2002), rigorous. *Scope:*
this does item **5(b)** (anchor on QEC), NOT **5(a)** — the general biological `O(N log N)` heterogeneous-wiring
cost is still the owed tightening, so the finite-wall `staked` entry is **not yet earned** (needs both).

**► NEXT SESSION STARTS WITH the archive-held term** — the **deepest** blocker (item 1 below), the second half
of *Organization = circulation-held K(C) + archive-held*, never measured (both anchors sit at archive≈0). The
research prompt is written (`research_prompt_archive_term.md`, open-access-only); the prime lead is **JCVI-Syn3A**
(Breuer 2019 *eLife* e36842 + the Luthey-Schulten Minimal_Cell repo) — a measurable archive (genome bits) + a
buildable metabolic NESS (circulation), where the cut may *blur* (itself the test). Dispatch it / work the
substrate where circulation-held capacity *fails* and a record is required. Behind it: **5(a)** the `O(N log N)`
tightening (completes the finite-wall `staked`); K_metric≥2 (an `[O2]eq` sweep on PO); class-generality (the
inorganic Oregonator, in hand); K_topo uniformity.

## Where it lands

- **VINDICATED + a distinct 2nd point landed (2026-06-24), both folded into canon.** KaiABC `K=2`
  (`kaiabc_capacity.py`) and the peroxidase-oxidase reaction `K=4` (`bfso_capacity.py`, the BFSO detailed model)
  are now empirical receipts + reflected in the `circulation-held-capacity` / `battery:circulation-capacity`
  frontier entries. Two points, two enzyme modalities, distinct K — substrate-generality of the *cut* shown,
  weakly.
- **→ core is blocked on four deeper items (the real frontier now):**
  1. **The archive-held term has never been measured.** Both anchors sit at archive≈0, so the second half of
     `Organization = circulation-held K(C) + archive-held` is untested. *This is the deepest blocker.* Needs a
     substrate where circulation-held capacity *fails* and a record is required. In-hand candidate: the
     **embryonic cell-cycle** (`docs/second_capacity_substrate/DesignSpace...`, archive-coupled — the cut may
     blur, which is itself the test). Research prompt for the cleanest archive-bearing substrate:
     [`research_prompt_archive_term.md`](research_prompt_archive_term.md).
  2. **K_metric is always 1** (two limit cycles). No forced-not-fitted `K_metric≥2` — the metric axis is
     unexercised. (The PO 2-torus was tuning-dependent; not claimed. An [O2]eq-only sweep at literature rates
     is a defensible cheap check, low priority.)
  3. **Generality within one class** (both biochemical enzyme oscillators). A structurally different class is
     owed — the **Oregonator** (inorganic, K=2, FKN constants in hand) is the cheap close (also forces the #4
     resolution); a physical/mechanical oscillator would be stronger.
  4. **K_topo is not uniformly defined** — KaiABC's reversible-cycle affinity sign-bit vs PO's irreversible
     cycle-*count*. One definition spanning both is owed.
  5. **The finite-wall — 5(b) DONE (QEC anchor, 2026-06-25), 5(a) still owed.** An outside-model derivation
     (3/3 models agree, main steps verified; the `O(N log N)` wiring-cost step is the load-bearing heuristic)
     found the keep ceiling is **FINITE** — the keep is a self-correcting code, the deepest keep is topological
     (max b₁), the archive is forced past the code's capacity (`research_prompt_keep_derivation.md`). **5(b) done
     — anchored on the QEC instance in canon** (`experiments/qec_keep_capacity.py`; receipts §QEC
     keep-as-capacity): keep = b₁ = #logical-qubits **literal** (`k=2−χ`), the wall = the code's **channel
     capacity** (rigorous), the crystal-escape exact (a regular code scales protection-depth, not keep). **5(a)
     still owed** for a frontier `staked` entry: tighten the `O(N log N)` wiring-cost step for a *heterogeneous*
     biological network — QEC is the *regular* (crystal) case where the bound is clean; the heterogeneous cost is
     the heuristic. Believing docs carry the resolved framing.
- The big version — progressively substituting archive-supported functions with circulation-supported ones and measuring where they fail (the "best self-specifying circulation," the Ship-of-Theseus Syn3A) — is **north-star-adjacent, parked-deep**. The near-term deliverable is only: *is `K` a real number on KaiABC, and is it `> b₁`?* Work the substrate, not the manifesto.

## Pointers

- Frontier siblings: `escape-degenerate-replication` (replication is cheap/degenerate — the same insight as "reproduction is a hack"), `self-referential-closure` (the alive-loop; self-wiring is the real character frontier this thread kept converging on), `drive-not-primitive` ("the realization is the payload, the bit only its protected projection"; matter is fungible — Ship of Theseus is "sustained, not stored" applied to the atoms), `battery:readability` / `reading-transition` (the metric/bit superselection split; the write-bar).
- Receipts: §Two bits (`b₁` = topological capacity), §QEC/Glass transverse decomposition (TDT = the write-bar), §Composition-law build (the rank-1 / value-bit-rate-dependent result).
- Memory: `feedback_substrate_affordance_filter` (KaiABC passes — real mechanism, generate-don't-hunt), `feedback_keep_tests_under_one_hour`, `feedback_no_synthetic_sidequests` (the gate above is that gate), `project_killshot_synthetic_is_imported_math` (KaiABC is real, so this is *not* the killshot trap — but `K` must be forced-not-fitted or it slides into one).
