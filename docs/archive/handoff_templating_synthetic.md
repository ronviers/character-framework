# Templating synthetic — build plan: can a recursive closure copy its own sign(𝒜)? (turnkey, for a fresh session)

> **STATUS: BUILT + RAN 2026-06-19 — outcome (b) DEGENERATE TEMPLATING (the prediction), all six gates pass.**
> Artifact: `experiments/templating_kernel.py` + `experiments/templating_kernel.png` (3 panels). The
> von Neumann discriminator `I(s_parent;s_child)` **saturates** at `C=½log₂(1+κ²/σ_b²)=1.0 bit ≪ k`
> (`I/k→0`), the field-ON kernel is assortative (`P(same)=0.89`, parity-exact, drive-independent, flips
> only on rewiring), the `κ=0` control is exact 50/50, and the lineage decays (no Pólya lock-in). Reading:
> a low-dimensional physical field templates sign(𝒜) **faithfully but degenerately** — open-ended heredity
> is sub-von-Neumann-threshold without a copyable tape; the von Neumann threshold is **located**, not lifted.
> Doc updates landed: `character_frontier.md` · `self-referential-closure` (templating MEASURED degenerate),
> `character_receipts.md` §Composition · *Templating*. **No `character.md` edit** (synthetic = calibration,
> below the line). Open next: self-wiring (the bigger layer) + the real-substrate / copyable-tape question.
> *(Original turnkey plan preserved below for provenance.)*
>
> ---
>
> **(Original status:) NOT BUILT — next-session single move.** Pre-registered falsifier in §1; **run before reading the
> result.** This calibrates the templating channel of a recursive `⊗`; it is the **bootstrap test** for
> `character_frontier.md` · `self-referential-closure` (templating layer), not the advanced cascade work.
> Imports it stands on (now in `character_prior_art.md`): `multitype-branching`, `channel-capacity`,
> `von-neumann-automata`, `cairns-smith`, `kondepudi`/`frank-autocatalysis`, `polya-urn`. A synthetic run
> **calibrates, it cannot vindicate** (`project_killshot_synthetic_is_imported_math`): the headline is *where
> the von Neumann threshold sits for a physical channel*, not "we got reproduction from physics."

**Read this first; it is self-contained.** It tells a fresh session exactly what to build, why it is **not
trivial**, the pre-registered decision rules, the discipline tripwires, and the single artifact to look at
together afterward.

---

## 0. The one-paragraph why

The logged question (`self-referential-closure`): *can a protected circulation bias sign(𝒜) of newly minted
protected circulations produced through its own recursive closure?* The naive run — "does the sign
propagate?" — is **trivial and misleading**: a stirred field biases the handedness of what crystallizes in it
(Viedma/Kondepudi deracemization), so a physics-only medium will pass "sign propagates" and be **mistaken for
the bootstrap**. The real, non-trivial question is the one `von-neumann-automata` forces: is the propagation
**degenerate** (a field copies *one* fixed pattern faithfully — flame/crystal class, evolutionarily dead) or
**open-ended** (the closure copies an *arbitrary* message — which needs a copyable description / tape)? We make
that a measurement: drive the closure with a **k-bit string** of signs and read **I(parent string; child
string) as k grows.** A physical shared medium saturates at its channel capacity `C ~ O(1)` regardless of k
(degenerate); a tape gives `I ~ k` (open-ended). The saturation curve **is** the von Neumann threshold made
visible. Pre-registered prediction: a physically-natural medium saturates `≪ k` — physics gives ~1 bit of
degenerate heredity, and the bootstrap genuinely needs a tape.

## 1. The question + the non-triviality criterion + pre-registered decision rules

**Measure the offspring-sign kernel and its information capacity** for a recursive `⊗` whose only parent→child
channel is the parent's *physical current acting as a field* (no sign-copy — §2, §3):

- **(K) single-step kernel** `M = P(sign(𝒜_child) | sign(𝒜_parent))`, field-ON vs field-OFF, parity-paired.
- **(I) channel scaling** `I(s_parent ; s_child)` as the string length `k = 1, 2, 4, 8, …` grows, with the
  coupling medium held at **fixed physical dimensionality** (a shared stirred bath, *not* k labelled registers).
- **(R) across-generation** sign-correlation `⟨s₀ · s_n⟩` vs generation `n` (Pólya lock-in vs random-walk decay).

**The non-triviality criterion (the whole point — do not ship a run that skips this).** A run that only reports
"sign propagates" (single-bit K assortative) is **insufficient** — it cannot tell degenerate from open-ended.
The run must report **I vs k** and show whether it **saturates** (degenerate) or **scales** (open-ended), with
the medium's independent-channel count audited (§8). Three outcomes, pre-registered:

- **(a) No templating — apparatus null.** Field-ON kernel symmetric too (`P(same)=0.5`). ⟹ the parent current
  is not coupling to child minting; the physical channel is mis-wired. **Fix the apparatus, not a result.**
- **(b) Degenerate templating — THE PREDICTION.** Field-ON kernel assortative (`P(same)>0.5`, parity-equivariant
  to machine precision), field-OFF symmetric, **and `I(s_parent;s_child)` saturates at `≤ C ≈ O(1)` bits as k
  grows (`≪ k`)**, with `⟨s₀·s_n⟩` either locking to the *field's* sign (not the parent's string) or decaying.
  ⟹ physics templates **faithfully but degenerately**; the von Neumann threshold is real and we have *measured
  where it sits*; the framework's honest "not off the ground without a tape" is **calibrated and vindicated**.
  Clean expected result — a weak "sign propagates" pass would have hidden exactly this.
- **(c) Open-ended without a tape — the surprise / kill.** `I ~ k` while the coupling medium provably carries
  `< k` independent channels. ⟹ **audit hard for a smuggled copy step (§8) — by far the likeliest cause** — or
  a bug. If it survives the audit as genuine, it is **beyond calibration**: a recursive closure acting as a
  universal constructor would be a real discovery / a forbidden-novelty flag — **escalate, do not quietly bank
  it.** (`feedback_prepared_for_invalidation`: a clean (b) is the strong result; an unaudited (c) is a trap.)

## 2. What makes it non-trivial — and the anti-trivial checklist

The von Neumann discriminator is the multi-bit channel scaling (I vs k). It works because a low-dimensional
**field** can impose only its own fixed pattern on all k child-bits at once — it cannot transmit an *arbitrary*
k-bit parent string — whereas faithfully copying an arbitrary string requires k independent registers, i.e. a
tape. So `I(s_parent;s_child) ≈ min(k, C)`, `C` = the medium's channel capacity (`channel-capacity`), and
`C` **is** the von Neumann tape capacity. Measuring whether `C` scales with k is the test.

**Anti-trivial checklist — a run that does any of these proves nothing; reject it:**
1. **Smuggled tape.** Child edge-signs set `=` parent edge-signs (or k labelled parent→child registers). This
   *is* a von Neumann tape by hand; it trivially gives open-ended (c) and tests nothing. The medium must be a
   **fixed-dimension shared coupling** justified as a physical bath/flow.
2. **Single-bit only.** `k=1` cannot distinguish degenerate (b) from open-ended (c) — a field passes and is
   mistaken for the bootstrap. **k must sweep.**
3. **No field-OFF control.** Without κ=0 you cannot attribute the bias to the physical channel vs the
   minting's own intrinsic sign preference.
4. **Boundary read.** Reading sign(𝒜) at or near the achiral `𝒜≈0` point is malformed
   (`feedback_attach_math_in_the_interior`). Read at finite affinity, sign bounded away from 0.
5. **Chasing a frequency.** A noisy 37/63 over 100 ICs is finite-sample; use parity-paired seeds and verify
   equivariance to machine precision (`feedback_demonstrate_symmetry_not_sample`).
6. **Child never decoupled.** If the "child" is just a permanent sub-block of one big system, that is not
   minting (§The minting claim) — the child must be a *minted* circulation absent before coupling and present
   after, sustained only while coupled.

## 3. Substrate + apparatus (turnkey)

**A character = a driven 3-node frustrated cycle**, linear-OU form (the framework's standard synthetic, the
deformation-chart so(3) direction): `dx = M x dt + √(2) dW`, `M = −γ I + g A_cyc`, `A_cyc` the antisymmetric
cyclic generator. **`sign(𝒜) = sign(g)`** (rotation sense = sign of `Im λ` of the complex pair = cycle
orientation). Read the sign in the **interior**: `|g|` fixed at a value giving a clean complex pair, `γ` fixed,
drive ≫ 0 — never sweep `g` through 0 to read the kernel.

**Minting a child (real, per §The minting claim — not a copy).** Append 3 fresh nodes; form the 6-node union.
Choose the parent↔child coupling `Γ_AB` so the **child cycle in the union graph is frustrated** ⟹ the child
mints its own circulation with `sign(𝒜_child) = sign` of the child-cycle skew part. Verify minting honestly:
`𝒜_child = 0` before coupling (fresh nodes detailed-balanced), `𝒜_child ≠ 0` after, and `→ 0` when the drive
is cut (sustained-not-stored).

**The physical channel (the bias — Viedma/Kondepudi stirred-field analog).** Make the *skew part* of `Γ_AB`
carry a term `κ · g_parent` — the parent's circulation "stirs" the medium the child forms in, so
`sign(g_child)` is pulled toward `sign(g_parent)` **without ever reading or copying the parent's edge signs.**
`κ` is the stirring strength. **Control: κ = 0** (field off) ⟹ `Γ_AB` skew drawn symmetric ⟹ `sign(g_child)`
unbiased (50/50). This is the field-ON / field-OFF contrast of (K).

**Multi-bit (the von Neumann discriminator).** A character is now **k independent triads** (3k nodes), string
`s = (sign(g₁),…,sign(g_k))`. The coupling medium is a **single shared stirred field** = a fixed
low-dimensional projection of the parent's k currents (e.g. the net/low-rank circulation), the **same** field
biasing all k child cycles. This medium has a **fixed channel count `C` independent of k** — that is the
physical constraint (and trap #1's tripwire: if you find yourself giving each child-bit its own parent-bit
coupling, you have built a k-register tape). Recurse: child→parent→grandchild for (R).

**Scaffold to create:** `experiments/templating_kernel.py` — fields (`make_triad(g,γ)`, `union_mint(parent,
child_seed, Γ, κ)`), a `sign_affinity(M)` reader (sign of Im of the dominant complex pair / Schnakenberg
`𝒜`), the parity-paired sampler, the k-sweep, and the I/kernel/correlation estimators. Validate the minting
(`𝒜` before/after/drive-cut) **before** trusting any kernel.

## 4. Observables + the artifact (one picture, looked at together)

One figure, three panels (`feedback_single_move_design` — ship one inspectable artifact, decide next move from it):
- **Panel A — kernel heatmap.** `M` (2×2) field-ON vs field-OFF, parity-paired (500/500), with the
  equivariance residual (must be `~ machine-eps`).
- **Panel B — the von Neumann curve.** `I(s_parent;s_child)` vs `k` (1,2,4,8,…), field-ON, with the diagonal
  `I=k` (open-ended) and the saturating `I→C` (degenerate) references drawn. **This panel is the result.**
- **Panel C — across-generation.** `⟨s₀·s_n⟩` vs `n`, and (multi-bit) whether the lineage locks to the
  *parent's string* or to the *field's pattern* (Pólya lock-in vs field-fixation vs decay).

## 5. Discipline tripwires (carry these)

- **Parity-paired, not sampled** (`feedback_demonstrate_symmetry_not_sample`): matched ± seeds; verify the
  kernel is parity-equivariant to machine precision; the 50/50 null is exact by symmetry, not a frequency.
- **Interior only** (`feedback_attach_math_in_the_interior`): the kernel is read at finite affinity; the
  achiral `𝒜=0` point is never visited as a measurement.
- **NaN is a tripwire** (`feedback_nan_is_falsification_tripwire`): never clip a state var at 0; any NaN/Inf in
  `𝒜`, the eigensolve, or `I` **halts and is diagnosed**, never filled. A symmetric kernel that is actually a
  silent degeneracy (eigensolve returning a real pair) is a fake null — confirm a genuine complex pair first.
- **Under one hour** (`feedback_keep_tests_under_one_hour`): time a `k=1, n=50` probe, extrapolate with ×3
  margin before the full `k`-sweep × `n`-realization grid. Read the **current sign directly** (cheap), not an
  expensive ensemble response. If the I-estimator at large k needs many samples, cap k and **log the cap** —
  do not silently truncate.
- **Calibration, not vindication** (`project_killshot_synthetic_is_imported_math`): outcome (b) measures where
  the threshold sits; it does **not** solve abiogenesis. Say so in the artifact caption.

## 6. Imports it calibrates against (and what it cannot conclude)

- `multitype-branching` — `M` is the mean/transition kernel; its Perron structure gives the lineage's
  asymptotic sign distribution (panel C). The run *measures* `M`; the asymptotics are imported.
- `channel-capacity` — `I(s_parent;s_child) ≤ C`; panel B reads `C` and whether it scales with k.
- `von-neumann-automata` — `C` **is** the tape capacity; `C` not scaling with k = the threshold, physics on the
  degenerate side of it.
- `kondepudi`/`frank-autocatalysis` (+ Viedma deracemization) — the stirred-field bias mechanism; the physical,
  *degenerate* templating precedent the κ-term instances.
- `polya-urn` — panel C's lock-in-vs-decay is the reinforced-process reading (heredity-without-genealogy, 1 bit).
- `cairns-smith` — the (unproven) candidate that geometry could be the tape; this run is whether a *physical*
  (non-register) medium has tape-like capacity. A saturating C is evidence the naive geometric tape is degenerate.

**Cannot conclude:** that a physical loop *can* reproduce with heredity (synthetic = calibration). Outcome (b)
**confirms the bootstrap is gated by the tape** — it does not lift the gate. Outcome (c) must clear the §8 audit
before it means anything at all.

## 7. Deliverables

- `experiments/templating_kernel.py` (+ the validation that minting is real: `𝒜` before/after/drive-cut) and the
  three-panel PNG.
- The numbers: `M` field-ON/OFF + equivariance residual; the `I(k)` curve + fitted `C`; `⟨s₀·s_n⟩(n)`.
- Then the **held** doc update lands per §1: `character_frontier.md` · `self-referential-closure` records the
  measured `C` and which outcome fired (b expected → templating-reading calibrated, bootstrap-needs-tape
  recorded; c → escalation note). Update this plan's status. **No `character.md` edit** — this is below the line
  (synthetic = calibration); the core is untouched unless a forced derivation later crosses the staked gate.

## 8. Risks / the smuggled-tape audit (the load-bearing check)

- **Outcome (c) is almost always a smuggled tape.** Before treating `I ~ k` as real, audit: (i) does any code
  path set child signs from parent signs directly? (ii) does the medium carry `≥ k` independent channels (count
  the rank of the parent→child coupling that touches the skew sector)? (iii) does field-OFF still give `I ~ k`
  (then the "templating" is leakage, not the channel)? Only `I ~ k` with a provably rank-`< k` medium and a
  clean field-OFF null survives — and that survivor is the escalation case, not a quiet win.
- **Fake null (a)/(b) confusion.** A symmetric field-ON kernel could be a mis-wired κ (no bias) *or* a real
  null; distinguish by checking the κ-term actually enters the child's skew sector (perturb κ, see `M` move).
- **Scope creep.** The goal is the kernel + the I(k) curve on these triads. Resist building a general minting
  engine or chasing a real substrate — that is the parked north star, behind this gate.
- **The honest framing in the writeup:** physics buys self-maintenance + (b) one bit of degenerate, faithful
  templating; open-ended heredity is sub-von-Neumann-threshold without a tape. That is the result this run is
  built to *measure*, not to overturn.
