# Character — frontier (the maturity ledger)

The fourth axis. The other three say *what is claimed* ([`character.md`](character.md)), *how it
is derived* ([`character_receipts.md`](character_receipts.md)), and *what is borrowed*
([`character_prior_art.md`](character_prior_art.md)). This one says **how settled each thing is,
and exactly what would move it** — the single source of truth for everything not yet
load-bearing. Its job is not to feed the core but to keep provisional work *out* of it until it
earns in: the structure here is quarantine, not on-ramp. The value of `character.md` is that
everything in it is committed; that guarantee survives only if the line below is strict.

---

## Gates — the state machine

Five rungs and a hard line. An item occupies exactly one rung at a time; a rung change is an
explicit event with a recorded trigger (no lore promotions).

```
steeping ──▶ sharpening ──▶ battery ──▶ staked ──╮
   │             │             │           │      │  COMMIT LINE
   ▼             ▼             ▼           ▼      ▼  ───────────────
 discarded (tombstone) at any rung      promoted → character.md / receipts / prior-art
```

**Promotion gates** (the condition to cross each boundary):
- `steeping → sharpening` — the speculation acquires *either* a concrete mechanism *or* a way to
  test it. Pure intuition with neither stays steeping.
- `sharpening → battery` — a runnable falsifier spec exists: finite operating point, a
  forced-not-fitted target, explicit kill **and** vindicate conditions.
- `battery → staked` — the spec is planted in the receipts as a falsifier of record (the `staked`
  tag), un-instanced by design.
- `staked → promoted` *(crosses the line)* — requires all of: (a) a **real cross-substrate
  instance** (a synthetic pass is calibration, never vindication), or for a non-instance claim a
  **forced-not-fitted derivation**; (b) the move **shrinks** the falsifiable surface, never enlarges
  it; (c) for a refinement that *defends* an existing claim, a **second independent instance**.

**Demotion / kill gates:** an item whose promotion gate is disproven goes to `discarded` with a
one-line tombstone (so it is never silently re-explored). A `staked` falsifier that **fires** does
not merely demote — it kills the core claim it defended, and the kill propagates into the core.

**Schema (mandatory).** Every entry carries: `key` **[rung]** — *verdict* (current belief, one
line) · **↑** promote-gate · **✗** kill-condition · **→** core target.

---

## Invariants — auditable

- **I1 — bridge integrity.** Every `staked` receipt ↔ exactly one frontier entry at `[staked]`. The
  staked rung is the only place an item is simultaneously in the core and on the frontier.
- **I2 — no orphans.** Every entry has a `→` target, or is `pure-exploration` (steeping only).
- **I3 — purity of the core.** Nothing above the line lives in a working file; nothing below it
  lives in `character.md`/receipts/prior-art. The core contains only what crossed.
- **I4 — recorded triggers.** No rung change without a logged trigger meeting the named gate.
- **I5 — self-application.** The framework is itself a dissipative register-system, so its own
  claims face the filters it applies to substrates. Every `staked`/`promoted` claim must pass three:
  **collapse** (over-determined — a binding or falsifier, never a single-register identity);
  **iff-chain** (its architecture is a stated entailment, not an asserted axiom); **flow** (every
  dynamical quantity moves with the operating point — no inert constant). A claim failing any sits
  in the framework's own metaphor regime and cannot stake.
- **I6 — no silently-committed conjectures.** A core claim carrying a falsifier must be in one of
  three states: its falsifier has a recorded run, it is a forced-not-fitted derivation, or it is
  explicitly `staked`. A claim with an un-run falsifier and no derivation that is neither `staked`
  nor on the frontier is malformed and demotes. (This is the gate a boundary-import claim slips when
  no interior apparatus exists to run it: the antidote is that boundary behaviour is an entailed
  theorem of the interior, never an un-run import asserted at the limit.)

---

## Register

### Steeping — speculation (no commitment)

* `flow-resident-number` **[steeping]** — *verdict:* a candidate number-type whose identity is a
  non-terminating trajectory under the coarse-graining flow (the affinity-as-orbit, the slow-manifold
  trace, the running $\beta$-functions); value-readings are static projections. · **↑** a closed
  composition algebra under the flow + a natural metric. · **✗** no closed algebra. · **→**
  `pure-exploration`. The algebraic side of the generative-recursion question (paired with
  `frustration-ascent`).
* `fractional-operator-algebra` **[steeping]** — *verdict:* an operator set on memory regimes
  $\beta\in(0,1]$ recovering the integer-$\beta$ operators at $\beta=1$; the algebra of *coupled*
  fractional systems is open. · **↑** a closed algebra at finite $\beta$ + a deformation-calculus
  analog + boundary rules at $\beta\to1^-$. · **✗** no closed algebra. · **→** a memory-regime operator
  layer.
* `two-reframe-parallel` **[steeping]** — *verdict:* the Boolean limit ($D\to\infty$, static) and the
  marginal point ($\varepsilon\to1$, dynamical) share architecture; watch for a third axis. · **↑** a
  third concrete reframe axis, instanced. · **✗** the parallel is cosmetic. · **→** `pure-exploration`.
* `secondary-regime-operators` **[steeping]** — *verdict:* damping, phase-locking, and coarse-graining
  regime trichotomies as further operator-algebra candidates; memory regimes are the cleanest first.
  · **↑** a closed algebra on any one trichotomy. · **✗** no closed composition. · **→** `pure-exploration`.
* `post-threshold-universality` **[steeping]** — *verdict:* a candidate seam mechanism, no mechanism
  yet. · **↑** a concrete link to the seam-width law. · **✗** no link survives. · **→** `pure-exploration`
  (feeds `thm9-crossover`).
* `palm-self-probe` **[steeping]** — *verdict:* the two-frame iff-chain re-projected into queueing —
  the time-stationary average (external) and the Palm / event-conditioned average (self-probe) are an
  inequivalent pair; Poisson arrivals are the degenerate $X\equiv1$ case. On a non-reversible cyclic
  queueing network it reinstantiates: self-probe defined $\Leftrightarrow$ net circulation $\ne0
  \Leftrightarrow$ routing affinity $\ne0\Leftrightarrow$ a directed routing cycle. · **↑** resolve the
  self-probe-current crux (the protected current is the routing-cycle affinity, not the arrival rate) +
  a spec on a 3-station cyclic network. · **✗** a non-reversible cyclic queueing NESS where the two
  frames agree despite affinity $\ne0$, or disagree with no routing cycle. · **→** the two-frame
  construction (new projection) + the queueing adoption row.
* `epsilon-hub-transport` **[steeping]** — *verdict:* a transport law on the distance-to-marginal-point
  $\varepsilon$ — one $\varepsilon$ in four registers (aging $\beta\approx1-\varepsilon$, heat-tax
  $\alpha(\varepsilon)$, branching $\to1$, critical length); degenerate at both endpoints, content in the
  interior. · **↑** a runnable collapse spec measuring $\ge2$ registers and inverting to a common
  $\varepsilon$. · **✗** the maps are mutually inconsistent, or two registers are tied definitionally.
  · **→** the memory-exponent and SOC falsifiers; coarse-graining.
* `affinity-hub-transport` **[steeping]** — *verdict:* a transport law on the affinity $a$ — one $a$ in
  three registers (queue load $-\ln\rho$, relaxation-oscillation $Q(a)$, phase-lock suppression);
  degenerate at both ends, signal in the mid-band. · **↑** a runnable collapse spec inverting $Q$ and
  phase-lock suppression to a common $a$. · **✗** the two inferred $a$'s cannot agree by construction.
  · **→** the queueing adoption row + the relaxation-oscillation and phase-locking claims.
* `predictor-soft-sector-blindness` **[steeping]** — *verdict:* an output-trained (feedforward) predictor
  occupies the **neither corner** by architecture — large soft-sector capability, hard sector structurally
  absent (acyclic adjacency ⇒ $\mathcal{A}\equiv0$). On a hard-sector question it is biased
  **confident-and-false**: a narrow-but-wrong confidence interval is the metric-sector signature of
  *averaging across* a topological branch boundary the predictor cannot represent — distinct from contingent
  under-sampling, which more data fixes. (Surfaced from the AlphaFold / prediction-powered-inference case —
  Angelopoulos–Bates–Jordan: 200M predicted protein structures give tight-but-wrong CIs on a
  phosphorylation×fluctuation test; phosphorylation is a driven NESS cycle — `pa:kinetic-proofreading`.)
  · **↑** a substrate where soft/hard cases are labelable: the bias **concentrates on hard-sector cases**,
  does **not** shrink with soft-sector data, and boundary-straddling ground truth (anchors at the separatrix)
  restores coverage with fewer labels than uniform anchoring. · **✗** the bias is uniform or shrinks with any
  added data — then it is plain under-sampling and character adds nothing. · **→** `character.md` §The
  two-survivals plane (the neither corner; soft-sector capability silent on the hard sector). Same shape as
  `nudge:loaded-endpoint-descent` — apparent capability ≠ the protected observable.
* `chirality-cascade-pinning` **[steeping]** — *verdict:* along a single shell's growth trajectory the
  topological bit (handedness) must be **pinned across every scale** and change *only by discrete rewiring* —
  never a continuous morph from one hand toward the other (the hard bit changes only by rewiring, never by
  deformation). The rare teratological reversals / scalariform aberrations are the test cases: are they all
  **abrupt jumps** (rewiring events), never gradual? · **↑** within-shell reversal specimens showing the flip
  is discrete, not a continuous handedness drift → `sharpening`. · **✗** a shell that continuously rotates its
  winding from one hand toward the other with no discrete rewiring. · **→** `character.md` §Frustration and the
  protected current (the hard bit changes only by rewiring); rides on rare specimens (data hunt
  `docs/research_prompt_shell_data_sources.md` #4). *Moved from the `cross-stratum-transduction` runnable test
  (2026-06-04): a clean kill but on rare specimens, vs T2's abundant heteromorph trajectories.*
* `determinate-growth-terminus` **[steeping]** — *verdict:* shells stop growing — character reads the stop as
  the **threshold crossing** (`a→0`, the *drive* axis, distinct from `cross-stratum-transduction`'s scale-axis
  marginal point): growth is the gain process and halts where gain can no longer beat the load of the next
  increment. The clock-hand analogy is exact — the hand stalls at a predictable phase where rising load
  (gravity) overtakes the fixed drive (torque). **Self-similar growth is self-terminating:** the same fixed-point
  geometry that converges the cascade (each whorl a scaled-up copy) *forces* the descent in `a` past threshold —
  increment cost grows geometrically while metabolic gain saturates (allometry) — so a self-similar accretor
  *must* stop; the terminal lip/flare is below-threshold relaxation. **The stop is an absorbing basin, not a pause:**
  the next phase cannot climb out — the same geometry that forced the descent forbids the return, since every
  possible next whorl is *larger* and costs more than the last the system already couldn't afford, so there is no
  uphill move and the drive that would power a re-ascent is exactly what ran out (a one-way ratchet built into the
  fixed point; the topological sector pays no such toll — it rides through for free, `cross-stratum-transduction`).
  · **↑** a mechanism or test that **beats the
  standing life-history alternative** (growth stops at maturity to reallocate energy to reproduction): the
  cessation point tracks a measurable gain/loss balance, or growth never halts while `a≫0` absent an external
  cause. · **✗** shells stopping while clearly above threshold (drive ≫ load) with no external cause; or
  cessation size unrelated to any gain/loss balance. · **→** `character.md` §Threshold regimes (monotone descent
  in `a`; below-threshold relaxation). *Raised 2026-06-04 (the clock-hand probe); abundant + visible (every
  mature terminal lip) but confounded by life-history theory — must out-predict it to climb.*
* `shell-space-layer-manifest` **[steeping]** — *verdict:* the accretionary shell **manifests the
  space-layer architecture without apparatus** — the first *real macroscopic* instance (vs the synthetic
  RPS / homochiral triad / surface code), where the two sectors sit in facts no one disputes. Three
  truisms *are* the architecture: handedness conserved exactly apex→aperture across every scale while
  size flows (scale-invariant protected bit; the metric flows and never couples to it); no continuous
  deformation carries one hand to the other, **only reflection** (gauge-irremovable, parity-only); form
  varies at fixed hand and hand flips at fixed form — mirror twins (the two sectors independent). The bit
  is set once at the developmental bifurcation (maternal formin `Lsdia1`, Davison–Kuroda) at **one bit**,
  then expressed redundantly along every whorl and **reversed only at the code distance** of that encoding
  — the error-correcting signature, same content as the surface-code/DFS reading (`chirality-protection`;
  Open Thread #2). **Scope: space layer only** — a dead shell is uncoupled and undriven, the frozen record
  of a driven accretionary cascade, not a sustained current; it reaches the architecture, never the
  coupling/minting or sustained-circulation claims. · **↑** the code-distance reversal-cost reading earns a
  receipt — the surface-code/DFS computation, *or* the **`Lsdia1`-vs-Wnt double dissociation** (an early
  1-gene switch flips the discrete bit while Wnt signalling deforms the continuous metric E/T and leaves
  handedness intact; Noshita growing-tube extraction) → `sharpening`, and the bare status fact ("a real
  macroscopic space-layer instance exists") promotes to `character.md`. · **✗** a protected bit whose
  reversal cost does **not** scale with its encoding redundancy (kills the code-distance reading); or the
  shell's coherence shown to be observer-selection not dynamics (the `coherence-as-attractor-diagnostic`
  control fails) — then "manifest" is curation, not character. · **→** `character.md` status / §The two
  tangent sectors (a real space-layer instance) + §Branch membership (reversal at code distance); receipts
  §Chirality protection. Cross: `chirality-protection`, `chirality-cascade-pinning`,
  `cross-stratum-transduction`. *Raised 2026-06-04.* **Substrate dead-ended 2026-06-05** (shell
  morphometrics carry no $\sigma$ / $\mathcal{A}$ / perturbable response — substrate ledger); its
  deposited sentence (unit-cost write / code-distance flip) **re-homed and instanced in
  `qec-transverse-decomposition`**.

  *Draft for `character.md` (held below the line; promotes only with the receipt above):*
  > **The accretionary shell — a space-layer instance.** The two-sector architecture is realized, without
  > apparatus, in the most familiar accretionary substrate: the coiled mollusc shell. Its continuous form —
  > size, spire, aperture outline — is the metric sector, flowing under growth as the order-parameter
  > magnitude flows under load; its coiling handedness (dextral / sinistral) is the topological sector. The
  > handedness is conserved exactly from the embryonic protoconch to the adult lip — across the entire
  > ontogenetic cascade, every order of magnitude — while the metric flows the whole way; the protected bit
  > carries the scale-invariance and the metric never couples to it. No continuous deformation carries one
  > handedness to the other, only reflection: the bit is gauge-irremovable in the strict sense, changeable by
  > a parity operation, not by any relabeling or smooth deformation. It is set once at the developmental
  > bifurcation (a single maternal factor — *Lsdia1* in *Lymnaea*) and thereafter expressed redundantly along
  > every whorl — cheap to write as one bit, costly to reverse as the whole built structure: the
  > error-correcting signature of the protected sector, a logical bit set at unit cost and flipped only at the
  > code distance. The two sectors are manifestly independent — conspecific shells vary continuously in form
  > at fixed handedness, and mirror-image individuals share a form at opposite handedness. This is the space
  > layer (the morphospace and its two tangent sectors), not the coupling layer: a single shell is uncoupled
  > and, once dead, undriven — the frozen record of a driven accretionary cascade, not a sustained current.
  > Strip the drive and the trajectory and the same coordinates describe inert geometry — an arbitrary
  > self-similar form carrying a handedness, a mathematical fractal and not a character.

* `coherence-as-attractor-diagnostic` **[steeping]** — *verdict:* the shell/fractal asymmetry is a
  diagnostic — **almost no** triplex-power fractals survive the "pretty" (coherent-structure) test
  (coherence is a measure-zero, *observer-curated* subset of an arbitrary generator space — 3D has no
  division algebra, Hurwitz/Frobenius; the multiplication is hand-picked, its handedness
  gauge-at-the-convention), while **almost all** shells do (coherence is the *generic* output). So
  coherence-prevalence separates **form-as-dynamical-attractor** (selected by the dynamics) from
  **form-as-uniform-sample** (selected by an observer) — and *immunizes the shell-morphospace against the
  "we only see the pretty ones" worry*: there are no ugly shells to ignore, so the prettiness is the
  dynamics', not ours. The mandelbulb is the **negative control** — self-similar form + a handedness, but
  no drive and no trajectory: character's no-drive degenerate face (`a=0`), geometry not character —
  isolating **drive + trajectory** as the load-bearing difference. Caveat: *not* "driven ⇒ coherent"
  (equilibrium crystals are coherent-and-generic); the clean axis is **attractor vs uniform-sample**, the
  drive only telling a NESS attractor from a crystal's. · **↑** a measure (coherence-fraction over a
  generator family) separating attractor-output from uniform-sample, instanced on ≥1 driven substrate vs
  its uniform-sample control, the equilibrium-attractor case handled → `sharpening`. · **✗** a
  uniform-sampled generator generically coherent with no attractor, or a dynamical attractor generically
  incoherent — then coherence-prevalence carries no attractor information. · **→** `character.md` §The
  morphospace (occupancy reflects dynamics, not the observer) + §Isolation (the no-drive face); guards the
  occupancy reading against selection artifact. Cross: `shell-space-layer-manifest`,
  `predictor-soft-sector-blindness`. *Raised 2026-06-04 (cross-post probe).*
### Nudges — steering candidates (a parallel doc-gate track; HELD)

A **nudge** corrects how character *steers a reader* — a sentence the core is missing or mis-places,
diagnosed from a misread — not a claim about a substrate. It does **not** climb the world-rungs above (no
substrate, no falsifier-instance); its path is two-rung: `candidate → (recurrence: a 2nd independent
misread trips the same wire) → core`. The `↑` is recurrence; the `✗` is "the existing core text already
steers correctly — the miss was reader sloppiness." Each entry additionally logs its *trigger(s)* (the
misreads = its support) and the *shape* it instances (the steering-failure class).

**Policy — HELD.** No nudge promotes to core yet, even one that already looks recurrence-mature.
Accumulate the corpus and read where the shapes cluster *first*; the holding pen exists to see the shape
before committing a sentence. Promotion is a deliberate later event, never automatic on the gate.

* `nudge:loaded-endpoint-descent` **[nudge]** — *verdict:* a loaded macro-phenomenon (sleep, a market, a
  mood) is read by **descent** to its substrate-general skeleton, never directly — `ℭ` is degenerate at
  loaded endpoints exactly as at the boundary faces $\{0,1,\infty\}$. Two steering misses. **(A) Periodicity
  is not the hard bit** — an observable oscillation establishes neither a protected current nor a minted
  bit; only the *protection test* does (noise-independent $\mathcal{A}$; a sign that reset-and-re-drive
  shows is wiring-set or re-rolled). The §Composition gate ("the spectral count is circular; the
  non-circular observable is the protection test") sits *downstream* of the minting language instead of
  guarding it, so a reader walks past it. **(B) Decompose before composing** — a switch is **branch-only**,
  an oscillator at most **current-only**; their co-occurrence is two corners, not a `both`, until the union
  graph's frustration is exhibited and the composite's current *measured*. · **↑** recurrence — a 2nd
  loaded-endpoint misread tripping the same wire (then a HELD-policy review, not auto-promotion). · **✗**
  the existing §Composition gate already steers correctly and the miss was reader sloppiness (then drop).
  · **→** `character.md` §Composition (the protection test), §The two-survivals plane (locate the corner
  before any composite claim), the open-interval/degeneracy discipline.
  · *trigger:* the outside-model sleep essay (2026-06-03) — read sleep as a minted `both`.
  · *shape:* **apparent-structure ≠ the protected observable** (only the protection test certifies the
  hard bit). Already recurring in-core (logged, NOT promoted): the neither-corner corollary ("soft-sector
  capability is silent on the hard sector"), the §Composition circularity gate, and this nudge; cf. the
  deformer $\lambda{=}0$ reciprocal case ($\mathcal{A}{=}0$) and the detailed-balanced DNA cycle
  ($\mathcal{A}{\approx}0$ pre-fuel). Watch: whether the next nudges land in this shape or open a new one.

### Sharpening — active work on a named owed item

* `thm9-crossover` **[sharpening]** — *verdict:* the Boolean-deviation theorem is a singular crossover
  scaling function (width exponent $\alpha$ + profile class), not a $1/D$ series; fitted-not-forced as it
  stands ($\alpha$ swings with the input-noise closure). · **↑** the noise law derived from a substrate
  FDR forces $\alpha$, validated by scaling collapse on a real substrate. · **✗** no stable $\alpha$, no
  collapse, or incompatible collapse families. · **→** receipts §Deformation calculus; operationalized by
  `battery:seam-collapse`.
* `thm6-bulk-series` **[sharpening]** — *verdict:* a genuine $D^{-1}$ bulk series, conditional on
  smooth-merge closures. · **↑** the closures derived, not assumed. · **✗** the series fails off the
  fitted closures. · **→** receipts §Deformation calculus.
* `thm7-bracket` **[sharpening]** — *verdict:* hinges on whether the hold-both threshold is hard or
  $1/D$-soft (the open-interval discipline suggests soft → dissolves the apparent obstruction). · **↑**
  the softening law pinned. · **✗** a hard threshold confirmed. · **→** receipts §Deformation calculus.
* `two-faces-boundary` **[sharpening]** — *verdict:* the amplitude and topological faces (independent in
  the bulk) are conjectured corresponded at their boundaries — a candidate wall-crossing law (complex
  pair $\Leftrightarrow\mathcal{A}\ne0$; boundary = eigenvalue coalescence). · **↑** index-grade criteria
  (exact pairing, transversality). · **✗** the faces independent at the boundary too. · **→** a refinement
  of the independence commitment, not a break.
* `dimensionless-substrate` **[sharpening]** — *verdict:* the dimensionless self-probe instanced on
  rock-paper-scissors; the residual is a *second* real substrate to promote the self-probe ruler. · **↑**
  a second real substrate hosting the dimensionless self-probe at the standard operating points →
  `battery`. · **✗** the dimensionless self-probe fails to close on a real frustrated substrate. · **→**
  the self-probe ruler; ties `battery:dimensionless-self-probe`.
* `consolidation-ascent` **[sharpening]** — *verdict:* one heat-tax mechanism, three faces — it forces an
  *endogenous* offline drive-withdrawal duty cycle, the compression operator contends with active
  maintenance for a shared server, and the tower ascent that *is* consolidation; the topological bit
  threads branch membership through the duty cycle (persist the protected-current generator, not the amplitude
  state). · **↑** a runnable spec on a named $\beta<1$ substrate: fan-in saturation + nesting, the
  coarse-grained kernel form measured forced-not-fitted → `battery`. · **✗** a substrate whose
  coarse-grained level fails the two-mode-kernel form (kills RG-closure for $\beta<1$); or an endogenous
  duty-cycler lacking the mechanism. · **→** receipts §RG closure (the $\beta<1$ open item); gated on a
  real $\beta<1$ substrate (the synthetic kernel is dynamically flat — cannot host this test).
* `frustration-ascent` **[sharpening]** — *verdict:* the generative-recursion bet, resolved **conditional**
  — *generative* of organization/chirality/topology (these flow with the NESS affinity, so they are
  mintable — legal) and *parasitic* on the drive (continuous-amplitude autonomy is supplied, not minted —
  receipts §Amplitude autonomy, a closed negative). The single-substrate triple obstruction (self-light +
  gapped + complex-pair-seedable mutually frustrate) is a **same-level** closure obstruction, **evaded by a
  two-level stratified cascade**: a base self-lights and selects a handedness, a gapped upper carries an
  autonomous protected cycle that survives drive removal. The legal three components (minting / protection /
  sustained-as-run-loop) were shown end-to-end (calibration) and confirmed on the DNA reaction network
  (composite branch, crossed). · **↑** a *real* substrate where a coarse register's chirality mints **and**
  the cascade closes robustly (the only legal mintable). · **✗** amplitude-autonomy minting — **closed
  negative** by necessity. · **→** the closure / composition; stays sharpening for the remaining
  real-substrate chirality-minting joint instance + full end-to-end robustness.
* `wall-as-type-boundary` **[sharpening]** — *verdict:* the marginal point is a type-boundary **ladder** of
  plateaus (normally hyperbolic invariant manifolds carrying the universal normal form) connected by three
  boundary kinds — ignition (the constructive landing), topological flip (the free sign-face transition),
  and closure-loss ($\varepsilon\to1$, loss of normal hyperbolicity); only the last is wall-like. The
  plateau side is instanced on the coupled Stuart–Landau cascade (CLV minimum angle bounded), and the
  closure-loss side via a Benjamin–Feir route ($\theta_{\min}\to0$, $\lambda_{\max}>0$); the $N{=}3$ cascade
  reaches the boundary *without* chaosing — instancing *loss-of-hyperbolicity ≠ forced chaos*. · **↑** on a
  real cascade: levels read as plateaus, transitions as the named boundaries, a level at $\varepsilon\to1$
  shows $\theta_{\min}\to0$ → promotes the ladder. · **✗** the CLV discriminator fails to separate plateau
  from boundary, or a real cascade level is not such a plateau. · **→** coarse-graining (the marginal point
  as loss of normal hyperbolicity); receipts §Marginal point. The canonical delay-driven mechanism and both
  sides on a faithful real cascade are still owed.
* `chirality-protection` **[sharpening]** — *verdict:* the protected object in a minted circulation is the
  gauge-irremovable affinity / discrete graph-flux sign — **not** the exceptional pair (suppressible) and
  **not** an integer charge (holonomy sub-integer); run synthetically (sign 0/200 graph-fixed deformations,
  exceptional pair killed 53/200, holonomy $\le0.16$); the binding discharged by import. Below the line
  because synthetic = calibration. · **↑** a *second, real-substrate* instance of the affinity/exceptional-pair
  separation. · **✗** a graph-fixed smooth deformation reversing the sign without rewiring; or a substrate
  where overdamping the exceptional pair also erases the affinity. · **→** receipts §Chirality protection,
  §Topological-drain; `battery:sign-interior`.
* `cascade-ledger-split` **[sharpening]** — *verdict:* the conjugate cascade's two ledgers are one
  coarse-graining EP decomposition — $\langle\sigma\rangle_{\text{tot}}=\langle\sigma\rangle_{\text{res}}+\langle\sigma\rangle_{\text{hid}}$,
  the hidden part the integrated-out fast circulation's dissipation, aligned with the metric/protected split
  exactly by Schur (`pa:transverse-decomposition`); closes by composing standing imports (heat-tax tower +
  transverse decomposition + `pa:esposito-coarse-graining`/`pa:timescale-ep`), analytical-only. · **↑** a real
  two-level substrate measuring $\langle\sigma\rangle_{\text{res}}$, $\langle\sigma\rangle_{\text{hid}}$,
  $\langle\sigma\rangle_{\text{tot}}$ — they sum, and the hidden part sits in the protected sector →
  `battery`. · **✗** a two-level substrate where the three fail to sum, or the hidden EP sits in the metric
  sector. · **→** core §The conjugate cascade; receipts §Conjugate-cascade ledger.
* `qec-transverse-decomposition` **[sharpening]** — *verdict:* the surface-code reading of the
  transverse decomposition, **computed** (was asserted; Open Thread #2 resolved). In the verified
  $[[9,1,3]]$ / $[[25,1,5]]$ rotated surface code the logical sector carries zero syndrome
  (symplectically transverse to the syndrome sector), the protected bit is **written at unit cost and
  flipped only at the code distance** ($P_L\propto p^{(d+1)/2}$, enumerated), and the bit-flip barrier
  exponent is **exactly invariant** to a syndrome-active phase (Z) current — CSS X/Z independence *is*
  the transverse separation — leaking $\propto\delta$ only under Y-mixing. **Boundary mapped:** a
  *same-sector* current is never exactly transverse (every detectable error lies on a min-weight
  logical string), so exact $\Delta V\perp\mathcal{A}$ is **symmetry-protected, not generic** — the
  same boundary as the triad's $Z_3$ (`gmam_symmetry_break_probe`). Below the line because synthetic =
  calibration; but it unifies the three checked substrates (triad, surface code, cascade) under one
  mechanism (Schur), and carries the seashell's re-homed deposit. · **↑** a *real* substrate showing
  barrier-invariance to a symmetry-separated current plus the leak under mixing → `battery`. · **✗** a
  CSS code whose logical-barrier exponent shifts under a pure conjugate-sector current; or a
  within-sector current shown exactly transverse with no protecting symmetry. · **→** `character.md`
  §The two tangent sectors + §The two-survivals plane; receipts §QEC transverse decomposition;
  `pa:transverse-decomposition`. *Raised + computed 2026-06-05.*
* `cross-stratum-transduction` **[sharpening]** — *verdict:* a coupling *tower* transduces the **topological**
  sector faithfully across the embedding while the **metric** carrier is fungible. Read this **within a single
  shell**: apex→aperture is a recorded ascent of the growth cascade — a *trajectory*, character's native
  register, not a between-specimen ensemble (which is where the human-fingerprinted statistics live). Three
  things are visible along it: the metric sector at its **RG fixed point** (self-similar coiling — but that is
  gnomonic growth, D'Arcy Thompson, **not** character's to claim); the topological bit (handedness, set by the
  maternal formin `Lsdia1` at the one-cell stage — Davison–Kuroda) **pinned across every scale** and
  **propagated laterally for free** — every cell and whorl inherits the hand at zero marginal cost (a sign is free
  to maintain), which is *why* the topology survives the tower while the costly, locally-built metric is the
  fungible carrier; and, when present, the **marginal point**. **Lead runnable test (T2 — heteromorphy = the
  marginal point):** a normal trajectory converges to a stable self-similar growth fixed point; a
  **heteromorph** (Okamoto's uncoiling ammonites; scalariform aberrants) trajectory **loses** it — character
  reads heteromorphy as the cascade at `ε→1` ("the levels stop telescoping into a single character"). Secondary
  (T3 — the cleaned prediction A): watch *one* shell flow through a metric regime change (the maturity flare,
  ontogenetic allometry) and check the topological bit is untouched — within-specimen, replacing the messy
  between-specimen test. · **↑** within-shell trajectory data: heteromorph trajectories show loss-of-fixed-point
  where normal ones don't, **and** the topological invariant stays pinned through metric regime shifts →
  `battery`; data hunt `docs/research_prompt_shell_data_sources.md`. · **✗** heteromorph trajectories show the
  *same* stable self-similar fixed point as normal shells (heteromorphy isn't marginal); or the topological
  invariant tracks the metric flow within a shell. · **→** `character.md` §Coarse-graining and the marginal
  point + §The two-survivals plane + §The space of characters. *Trigger (T2 lead, 2026-06-04):* prompt-1
  (between-specimen sector independence) returned **messy / weak-against-strict** — *Amphidromus inversus*
  dextral/sinistral not exact mirrors, *Partula* weak chirality pleiotropy (~0.2–1% variance, human-sized data);
  prediction A demoted to a logged near-miss, the test moved into the native within-shell trajectory register.

### Battery — executable falsifier specs

* `battery:seam-collapse` **[battery]** — *verdict:* the amplitude/drive-seam scaling-collapse battery;
  runnable on synthetic now, the forcing needs a real substrate with a measurable FDR. Target invariant
  $(\alpha, F)$, not a coefficient series. · **↑** stable $\alpha$ + universal collapse + substrate-family
  profile classes on a real substrate → promotes `thm9-crossover`. · **✗** width saturates as $D\to\infty$;
  or no single $\alpha$; or equal $(\alpha,w)$ with incompatible profiles. · **→** receipts §Deformation
  calculus.
* `battery:sign-interior` **[battery]** — *verdict:* the protected-sign interior-circulation kill — interior
  measurement only (never the never-attained boundary), reading the binary sign of the affinity, not a graded
  triality. Vindicated on rock-paper-scissors (a real substrate carries a protected sign on a directed
  3-cycle, drive-independent, flipping only by rewiring; the symmetric null carries none). · **↑** a protected
  sign on a real substrate always sits on a frustrated triad → promotes the central commitment *(fired —
  crossed)*. · **✗** a real substrate with a protected sign and no triad; or the synthetic sign flips under
  finite drive variation without rewiring. · **→** the protected current; receipts §Central commitment, §Two
  bits.
* `battery:wall-ladder` **[battery]** — *verdict:* the plateau-ladder falsifier — a cascade's levels are
  normally hyperbolic plateaus separated by the three boundary kinds; the discriminator is the CLV minimum
  angle $\theta_{\min}$ + the smallest transverse exponent. Both faces demonstrated: the plateau side on the
  coupled Stuart–Landau cascade ($\theta_{\min}$ bounded, false-positive controlled), the closure-loss side via
  a Benjamin–Feir route ($\theta_{\min}\to0$, $\lambda_{\max}>0$). · **↑** on a real cascade: levels read as
  plateaus, a level at $\varepsilon\to1$ shows $\theta_{\min}\to0$ → promotes `wall-as-type-boundary`. · **✗**
  the discriminator fails, or a real cascade level is not such a plateau. · **→** `wall-as-type-boundary`;
  coarse-graining. The canonical delay-driven mechanism stays the deferred test.
* `battery:dimensionless-self-probe` **[battery]** — *verdict:* the dimensionless self-probe ($\mathcal{T}\ge1$)
  + the canonical affinity, instanced on rock-paper-scissors (the empirical winding affinity closes onto the
  forced form to 1.7%, and the affinity and $\omega/\gamma$ are noise-independent). Scope: the
  noise-independence is the symmetric-multiplicative-drive case (a thermodynamic-force drive would make the
  affinity drive-dependent). · **↑** a second real substrate with the same noise-independent affinity →
  promotes the self-probe ruler. · **✗** the affinity or $\omega/\gamma$ noise-dependent on a real substrate,
  or the self-probe fails to close. · **→** the self-probe ruler; promotes `dimensionless-substrate`.
* `battery:scale-covariant-circulation` **[battery]** — *verdict:* the topological bit on the scale axis — the
  same circulation read at two scales splits into a scale-**invariant** affinity (the bit) and a
  scale-**covariant** magnitude. Instanced: a legitimate adiabatic projection leaves the affinity invariant in
  sign and value while the current renormalizes exactly by the eliminated-mode timescale; the illegitimate maps
  (driven fast subspace; loop contraction) are the pre-excluded failures. · **↑** the split shown on a
  continuous affinity-bearing substrate → promotes the scale-relativity claim. · **✗** under a legitimate map
  the affinity flips or erases. · **→** scale-relativity; coarse-graining.
* `battery:two-survivals-plane` **[battery]** — *verdict:* branch survival ($\Delta V$, the basin-escape
  quasipotential) and current survival ($I(0)$, set by the cycle affinity $\mathcal{A}$) are **independent
  axes**; substrates fill all four cells, so "no protected current" is not "no dynamical landscape." Already
  core: **current-only** (structurally stored — bare RPS, fuel-driven DNA: $\mathcal{A}\ne0$, mirror reachable
  only by rewiring) and **both** (spontaneously selected — homochiral: $\mathcal{A}\approx21.8$,
  $\Delta V\approx0.018$; **second instance** the co-handed twin-cycle via exchange/$S_2$ SSB, not parity). New corners: **branch-only** (metastable — a symmetric Hopfield attractor net gives
  $\Delta V\approx0.97$ with $\langle\sigma\rangle=\mathcal{A}=0$ to machine precision, real Jacobian;
  `experiments/hopfield_corner.py`), the mirror of bare RPS; **neither** (soft-metric — a 2-layer feedforward
  net on a Gaussian mixture: measured capability $I(\hat Y;Y)\approx2.9$ bits → the Bayes ceiling, the hard
  sector **structurally** absent — node-adjacency nilpotent ($\mathcal{A}\equiv0$ by acyclicity), $\Delta V$
  undefined for want of recurrence; `experiments/neither_corner.py`), the first *non-trivial* substrate with no
  hard bit. Column boundary = **frustration** ($\mathcal{A}:0\to\ne0$); row boundary = a **coexisting mirror**
  (rewiring → thermal crossing). Corollary: soft-sector capability is silent on the hard sector — the most
  *informative* corner carries no protected current at all. · **↑** *(crossed)* — all four corners instanced →
  core §The two-survivals plane + receipts §Two-survivals plane. · **✗** a
  symmetric/gradient attractor net with
  $\mathcal{A}\ne0$; or a feedforward/acyclic substrate carrying a sustained protected current; or branch
  survival and current survival shown *not* independent on a real substrate. · **→** core §Branch membership +
  the fidelity–protection split ("three layers, not one"). `pa:cycle-affinity`.

### Staked — planted in the core, un-instanced (mirrors the receipts `staked` tag — I1)

* `staked:gfdr-two-step` **[staked]** — *verdict:* near-threshold FDR is two-step; a short-lag $X{=}1$ is not
  below-threshold. · **↑** a second instance — recurrence of the confusion, or a real glass/quantum/brain
  substrate exercising the two-step. · **✗** a substrate where short-lag $X{=}1$ genuinely *is* below
  threshold. · **→** receipts §Two FD frames — two-step.
* `staked:auto-tuning` **[staked]** — *verdict:* a substrate's slow rates auto-tune to the
  diagonally-stabilising weight $W=\mathrm{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$. · **↑** a substrate
  requiring diagonal stability shown to auto-tune to the inverse form. · **✗** a stable maintained state on a
  non-PSD frustration-free topology whose measured rates give an indefinite $W\gamma+\gamma^TW$. · **→**
  receipts §Auto-tuning.
* `staked:memory-collapse` **[staked]** — *verdict:* $\beta\approx1-\varepsilon$ near the marginal point. ·
  **↑** $\beta(\varepsilon)$ measured near the marginal point on a real hierarchical substrate, linear with
  both endpoints respected. · **✗** $\beta$ departs from $1-\varepsilon$. · **→** receipts §Memory collapse;
  `character.md` Coarse-graining.

### Recently crossed the line

Promoted this campaign, now in the core (recorded in receipts §Corrections and promoted refinements):
the **central commitment** and **two-frame construction** (on rock-paper-scissors); the **deformation
chart** and **homochirality** (on rock-paper-scissors and the homochiral triad); the **exact
two-frame magnitude identity** (a forced-not-fitted derivation on the rotational-OU testbed);
**composite branch** (on the fuel-driven DNA reaction network — the manifold and closure lifts both
crossed, now `character.md` §The space of characters and §Composition under coupling); and **branch
survival** (the racemic-saddle quasipotential $\Delta V\approx0.018$ on the homochiral triad, separated
from $I(0)$ by noise-scaling and by controlled embedding — receipts §Branch-survival barrier). The
$\mu$-sweep is run: branch survival is born at $\mu_c=(1+a+b)/3=0.833$ by **competitive exclusion**,
with $\Delta V\propto(\mu-\mu_c)$ linear (the pitchfork $(\mu-\mu_c)^2$ superseded) and zero below
threshold. **Both owed items now paid (receipts §Branch-survival barrier):** the multiplicative-noise
robustness (demographic $\sqrt{x}$ noise — $\Delta V$ rescales to $\approx0.273$ but existence and protection
survive, so not an additive artifact), and a second independent thermalized-crossing substrate — the
**co-handed twin-cycle** ($\mathcal{A}\approx21.8$, $\Delta V\approx0.018$), which instances `both` through a
spontaneously broken **exchange** ($S_2$) symmetry, *not* parity. Decisive independence: sign($\mathcal{A}$)
is preserved across the branch flip (both clusters co-handed) where the homochiral parity flip reverses it —
the two survivals shown orthogonal a way the parity instance structurally cannot. The competitive-exclusion
mechanism is **handedness-blind** (μ-sweep): $\mu_c$ and the linear $\Delta V(\mu)$ are machine-precision
identical across exchange and parity, since the breaking mode is uniform-within-cluster — so the open
pitchfork-vs-competitive-exclusion question resolves the same under both SSB types.
`experiments/twin_cycle_corner.py`, `twin_mu_sweep.py`. And **`both` across a second bifurcation mechanism**:
an autocatalytic (Kondepudi–Nelson) substrate gives a genuine **soft pitchfork** — $ee_*^2\propto(k_{1c}-k_1)$
linear ($R^2{=}1$), barrier $\Delta U\propto ee_*^4\propto(k_{1c}-k_1)^2$ **quadratic** (vs the twin's
hard/linear); adding an $a\neq b$ 3-cycle opens a **coexistence window** $ec\in[0.05,0.20]$ that mints
$\mathcal{A}\approx0.6$–$3.5$ nats while the soft pitchfork holds ($ee_*^2$-$R^2{=}1$, $\Delta U\propto
ee_*^4$ $R^2{=}0.997$, reset ~50/50); past $ec\gtrsim0.25$ the cycle destabilises the branch (it
*participates* in the bifurcation, not merely decorates it). Supported claim: **symmetry breaking does not
fix the barrier scaling — the saturation mechanism does** (two distinct constructions, not yet
"mechanism-independent"; receipts §Branch-survival barrier, §Two-survivals plane).
`experiments/autocat_pitchfork.py`, `autocat_both.py`.

---

## Tombstones — discarded false starts (kept so they are not re-explored)

* `flip-cost-across-zero` — protection-as-a-flip-cost across the sign-erased zero. **Died:** formulating
  protection as a measurement that visits the affinity-zero is malformed by the open-interval discipline (the
  zero is never attained). **Replaced by:** the interior sign-stability test (`battery:sign-interior`). The
  $\ge1$-bit flip floor fired entirely — a sign flip is a reversible bijection (no erasure, no Landauer floor).
* `sign-kill-bisection` — the can-kill-can't-vindicate standdown that split the test into kill-only. **Died:** a
  boundary-gated formulation; the framework is degenerate at the boundary, rich in the interior. **Replaced
  by:** the interior, can-kill-and-vindicate `battery:sign-interior`.
* `thm9-coefficient-series` — the Boolean-deviation bound→equality as an analytic $1/D$ coefficient series.
  **Died:** two passes converged that the seam is a crossover scaling function, not a series; the series stayed
  fitted-not-forced. **Replaced by:** the scaling-collapse target $(\alpha, F)$.
* `alignment-dependent-active-stress` — the alignment-dependent form for the active-stress fingerprint.
  **Died:** it captures only the flocked-state correction, not the leading scaling. **Replaced by:** the
  alignment-independent fingerprint $\beta/\alpha\sim v_0^2\tau_R/D_{\text{trans}}$.
* `quadratic-lyapunov-candidate` — a quadratic Lyapunov form. **Died:** fails the critical-point test
  ($\partial V/\partial x_i|_{x^*}\ne0$). **Replaced by:** the relative-entropy form (receipts §Frustration-free
  Lyapunov).
* `current-aids-escape` — the protected current read as a *resource that lowers the branch-escape barrier*
  ($\Delta V$ falling with the affinity $\mathcal{A}$). **Died:** the exact instanton (gMAM, validated on
  Maier–Stein to $0.01\%$) gives a $\sigma\to0$ quasipotential **flat** in $\mathcal{A}$ ($\Delta\hat S_H
  =-0.4\%$ over $\mathcal{A}:0\to21.8$ vs the finite-$\sigma$ slope's $-17\%$), the instanton never bending
  off the symmetric subspace — because the current is **exactly transverse** to the escape mode at the
  saddle ($|\cos(J,e_u)|\sim10^{-15}$, symmetry-protected: escape and current in different irreps, broken
  $\propto\delta$ by a $Z_3$ break). The current's own ✗ ("gMAM shows the finite-window slope mis-ordered
  the true actions") fired. **Replaced by:** an imported reading — the **transverse-decomposition theorem**
  leaves $\Delta V$ invariant; the measured drop is the **irreversible Eyring–Kramers prefactor**
  (receipts §Branch-survival barrier; `pa:transverse-decomposition`). The two-survivals separation is
  *reinforced* ($\Delta V\perp\mathcal{A}$ by a symmetry theorem); a current reaches a barrier only where
  coupling mixes the irreps (the in-substrate Maier–Stein turn-on, `gmam_mixing_test.py`).
