# Character — grounding method

How a lay-question is run to ground against [`character.md`](character.md): decomposed into a
domino-chained tree of measurement batteries, every branch pushed to a terminal leaf that is
either a **result** (a measurement already instanced, with a receipt) or a **pending-defined
test** (a measurement fully specified but not yet run). No branch is left as prose, and no leaf
is a verdict the framework has not earned.

Status: v0.1. One worked tree (teleportation) plus one worked catch. The appendix is to be
stocked (free will, the hard problem, uploading, longevity). This is a method, not new physics —
it produces no claim that is not either an instanced result or a named pending measurement; the
only thing it ever promotes into the canonical docs is a newly-defined pending test, which lands
in the falsifier ledger / frontier where tests already live.

## Why a tree, and why every branch

A lay-question of the kind people most want the framework to be sure about — *is the teleported
person me, do we have free will, is there a hard problem* — is not answered by a verdict and is
not honestly refused. It is **run to ground**: the question is a first domino whose fall
determines which domino it strikes next, and the discipline is to push *every* branch to a leaf.
A branch stopped early — "here the framework takes no stand," "this is philosophy" — is not a
terminal; it is an un-pushed domino, the same failure as a contingency never gamed out. The
stand the framework takes is the *whole tree*: which leaves are settled, which are pending, and
exactly what measurement decides each.

Two terminal leaves, and only two:

- **result** — the measurement is instanced on a named substrate; cite the receipt and the
  outcome.
- **pending-defined** — the measurement is specified (substrate, observable, both branch
  outcomes) but unrun; state why it is unrun (inaccessible / not-yet-done / self-referential with
  the act). A pending leaf is grounded iff a competent experimenter could run it from the
  description.

"The framework is silent here" is neither, and is therefore never a leaf.

## Calibration — identity is rebranded, not removed

The folk concept of identity points at something real. What the method corrects is the *theory*
of what that something is — a stored substance, a pattern kept somewhere safe — not its
*existence*. Identity is not eliminated; it is re-identified. The move is **storm → tornado**: a
tornado is real, named, tracked, and mortal, yet it is no substance the air contains — it is a
protected circulation the air *runs*, gone when the drive that sustains it goes. You are not a
thing that has a pattern; you are the pattern, and the pattern is real.

This fixes a rule on every tree: **no leaf is unreality.** Each terminal is a *kind of real
pattern* with a stated persistence profile —

- a configuration (population bit): real, and copyable — a recording is a real thing;
- a structurally-stored circulation: real, and regenerable — the tornado that reforms the same;
- a spontaneously-frozen circulation: real, and once-only — the particular tornado that, once
  gone, is replaced by a different real one, never the same.

The tree never asks *are you real*; it asks *which real pattern are you, and what are its survival
rules*. This is one of two by-construction guarantees — paired with the no-verdict guarantee below
— foreclosing the two fears a sincere asker brings: that the method will tell them a false thing
about their identity, or that it will tell them they have none. A reading that hears "your self is
not a stored substance" as "your self is not real" has inverted a reduction into an elimination —
the one outcome this calibration exists to forbid.

**The reassurance is structural, not substantive.** What is guaranteed is that *every leaf is a
kind of real thing*; what is **not** asserted is *which* real thing a given asker is. For a human
that remains the pending leaf — "you do not evaporate into the unreal" is guaranteed, "you are
specifically a protected circulation" is not. Reassure on the structure; stay honest on the
substance.

## The SOP

1. **Translate.** Restate the lay-question as a question about a substrate property. Translation
   may commit the framework's *defined* terms — e.g. identity ≔ the circulation bit (the
   irreducible residue the reservoir permits but does not force). Such a commitment is
   **definitional, not a measurement**: it fixes what the framework's word denotes; it does not
   adjudicate whether the asker's folk concept maps to that term. Flag the map explicitly as the
   asker's commitment, never a framework result.
2. **Root the tree.** Name the first measurable property the answer hinges on, and its branches.
   A fork is a **battery**: a named measurement plus its branch outcomes.
3. **Push every branch.** Each branch resolves to a leaf or strikes the next domino (recurse).
   Completeness is mandatory; an un-pushed branch is a method failure.
4. **Bind every fork to a measurement.** Substrate, observable, outcomes. A fork with no named
   measurement is prose in disguise — reject it.
5. **Classify each leaf** as result or pending-defined. No third terminal.
6. **Read the tree back.** The stand = the tree: settled leaves, pending tests, the measurement
   behind each.
7. **Self-test.** Re-probe with the original lay-question. Pass iff a reader handed the tree lands
   on a leaf for every path and manufactures no verdict the tree does not license. Drift means a
   branch is under-pushed or a fork under-measured.

**The one non-battery node.** The root is sometimes a **definitional gate** rather than a
battery: it routes by what the asker *means*, not by a measurement. A gate may only route to a
meaning — it may never assert which meaning is correct, and it is never itself a leaf. Every
route out of a gate enters a battery or reaches a trivial result.

## Scaffold

```
LAY-QUESTION:          <as asked>
FRAMEWORK TRANSLATION:  <substrate-property restatement; defined-term commitments flagged>

TREE
  Node k — <fork>?   measurement: <observable / how read>
    ├─ <branch> → result | Node j | pending

LEAVES
  [result]  <path> → <outcome>   substrate:<…>  receipt:<…>
  [pending] <path> → <X if test runs way-1; Y if way-2>
            test:<substrate, observable, two readings>   unrun:<why>

READ-BACK:  <your question = this tree; settled leaves; pending tests + meaning>
PROMOTED:   <new pending tests → frontier/falsifiers, else none>
```

## Worked tree — teleportation

**LAY-QUESTION:** Is the person who steps out of the teleporter me?

**FRAMEWORK TRANSLATION:** The framework defines identity as the circulation bit — the
irreducible residue the reservoir configuration permits but does not force. It does **not** decide
whether the folk "you" (the thing you would mourn) is that circulation or your configuration; that
map is the asker's definitional commitment. Given identity ≔ circulation bit, the measurable
question is: *is that circulation preserved under scan → destroy → reconstruct?*

**Definitional gate (root):**
- "me" = configuration → the **population bit**: erasable at the Landauer bound, regenerable from
  the reservoirs, copyable. A teleporter reproduces it → **preserved**, trivially. (The framework
  does not call the configuration "identity," nor deny it is what you value — a different question,
  answered.)
- "me" = the irreducible residue → the **circulation bit** → enter the battery.

```
TREE
  Node 0 — stored or frozen?
    measurement: reset fully, re-drive — does the protected sign return or re-roll?
    ├─ structurally-stored (sign returns) → result: preserved
    └─ spontaneously-frozen (sign re-rolls) → result: twin

LEAVES
  [result]  structurally-stored → PRESERVED. The asymmetric wiring fixes the sign; reproduce the
            wiring and re-supply the drive and the same circulation returns.
            substrate: fuel-driven DNA reaction network (re-fuel restores the sign).
            receipt: Fuel-driven DNA reaction network / Identity.
  [result]  spontaneously-frozen → TWIN. The symmetric wiring stores no direction; the reset
            inherent in scan→reconstruct re-rolls it. Same type, independently chosen sign.
            substrate: rock-paper-scissors replicator; homochiral triad (reset re-chooses 50/50).
            receipt: Rock-paper-scissors; Homochiral triad.
  [pending] which kind the HUMAN identity-circulation is → preserved if structurally-stored,
            twin if spontaneously-frozen.
            test: reset-and-re-drive the human identity-circulation; read sign-return vs re-roll.
            unrun: SELF-REFERENTIAL WITH THE ACT — the deciding measurement (full reset and
            re-drive) is the teleport itself; it cannot be run as a prior test.
```

**READ-BACK:** You are real, and you are the tornado kind of real — a sustained pattern, not a
stored substance. The only thing teleportation puts in question is which sustaining-rule your
pattern follows: a copyable configuration is reproduced outright (you survive), a
structurally-stored circulation reforms identically (you survive), a spontaneously-frozen one is
once-only (the arrival is a real twin, not you). At no branch do you evaporate — every outcome is
a kind of real thing with a known persistence. Which one you are reduces to a single substrate
property (structurally-stored vs spontaneously-frozen), once you have committed that the "you" at
stake is the irreducible residue rather than the copyable configuration. The fork is settled and
measured on synthetic substrates; for the human it is undecided, and the deciding experiment is
the teleport itself — which is why the question has never had a clean answer: not mystical, one
self-referential measurement.

**PROMOTED:** *self-referential-with-the-act* as a defined-but-unrunnable test class →
[`character_frontier.md`](character_frontier.md) (if new to the ledger).

## Worked catch — a definitional commitment misread as a substrate verdict

A capable reading of `character.md`, citing it correctly, runs: the framework defines identity as
the circulation bit; the population bit is "erasable at the Landauer bound" and "forced by the
reservoir configuration"; *therefore, if the human is just a population bit, the framework argues
we possess no true identity to preserve.*

The first two steps are right, and they collapse the naive "population or circulation?" root:
given the framework's own definition, identity is the circulation bit, so the battery starts at
stored-vs-frozen (the correction is absorbed in the tree above). The third step is a **smuggled
verdict**. "The framework does not call the population bit identity" is a fact about the *term*;
"the human has no true self" is a substrate verdict about a *folk concept*, with no battery behind
it — the exact leaf the method forbids. The corrected terminal is the definitional gate: if the
asker's "me" is the configuration, the framework neither crowns nor denies it — that route
terminates in *trivially preserved*, not in *no true self*. The catch is the method working on its
own review.

The corrected terminal is also not deflationary. "The framework does not call the configuration
identity" does not demote it to unreal — a configuration is a real, copyable pattern (per the
calibration above, no leaf is unreality). The method reduces identity to a kind of real structure;
it never eliminates it. Hearing the definitional choice as "you have no true self" inverts that
reduction into an elimination — the precise failure the calibration forbids.

## Structural guarantee — no anthropocentric verdict is reachable

A human leaf can only ever be **pending-defined**: there is no human substrate with an instanced
result, and the method admits no third terminal. The framework therefore cannot deliver a verdict
on the human through this method — only the tree and the pending test that would decide it.
Human-domain over-reach is blocked by construction, not by vigilance. The asker is handed exactly
what the question is, and what would answer it — which is the whole of what a physics of
driven-dissipative structure is entitled to say.

This is the second of the two by-construction guarantees; the first is *no leaf is unreality*
(Calibration). Together they foreclose the two fears a sincere asker brings: the method cannot
tell a person a false thing about their identity, and it cannot tell them they have none.

## Appendix — grounding trees

What running a pop-list to ground reveals, before the trees: the questions collapse onto a small
set of **batteries** (named measurements), nearly every *human* leaf is **pending-defined** (no
human substrate is instanced, so the framework's honest output is the unrun experiment, not a
verdict), every **result** leaf comes from one of the four receipted substrates (surface code,
rock-paper-scissors, homochiral triad, fuel-driven DNA network) — none of which instance a folk
concept — and a few questions are **out of domain**: their translation demands an unlicensed
identification, which the method refuses. A confident verdict on any of these for the human is the
smuggled-leaf failure (Worked catch), committed once per question by the source pop-list.

## The battery structure (problem tree)

The fifteen collapse onto **one entry gate and six batteries**, each laid out to terminals.
Expanding the batteries expands every question at once; the fifteen attach as labeled entry
points (table at the end). Every branch ends in a terminal of one type — the visualization
vocabulary:

- `[RESULT]` measured on a receipted substrate (cited)
- `[TEST-NOW]` runnable on existing data/substrate, no new construction
- `[TEST-DEFERRED]` defined and runnable in principle; needs a substrate/data not yet in hand
- `[OPEN-SELFREF]` the deciding measurement is the act itself; not runnable as a prior test
- `[OPEN-FRAMEWORK]` the quantity is open on every substrate; closes upstream in `character.md`
- `[OUT-OF-DOMAIN]` no substrate observable; translation refused
- `⚠` a **smuggle-risk fork** — skipping it lets a verdict in. Full expansion is the anti-smuggle.

**ROOT GATE — is there a protected circulation?** (gauge-irremovable frustrated 3-cycle, `𝒜 ≠ 0`)
measurement: Harary balance on the coupling graph + a complex-conjugate Jacobian pair.
```
ROOT
├─ no frustrated cycle → hard bit absent → phenomenon is soft-bit only (configuration);
│                                          copyable; not "identity" in the framework's sense
└─ frustrated cycle present → hard bit exists → B-reset / B-mint / B-affinity
   └─ ⚠ for a human substrate: frustrated or merely additive? — unknown → [TEST-DEFERRED]
        (this fork, skipped, is where every minting-group smuggle hides)
```

**B-reset — orientation (stored vs frozen).** reset fully, re-drive:
```
B-reset  (requires hard bit)
├─ sign returns → structurally-stored                         [RESULT: DNA network]
│   └─ runnable on target?  accessible → [TEST-DEFERRED]
│                           reset = the act → [OPEN-SELFREF]  (teleport, death)
└─ sign re-rolls → spontaneously-frozen                       [RESULT: RPS, homochiral]
    └─ identity survival (crosses the separatrix?) → B-sep    [OPEN-FRAMEWORK]
```

**B-mint — coupling.** couple `A ⊗ B`, re-run union-graph balance:
```
B-mint
├─ union additive (no new frustration) → soft-bit coupling only; no minted identity
└─ union frustrated → mints a circulation absent in parts     [RESULT: DNA]
    ├─ protection (survives deformation, dies only on rewiring) [RESULT: OU N=3]
    ├─ decoupling dissolves it? (drive/coupling-cut)            [RESULT: DNA fuel-cut]
    └─ ⚠ human coupling frustrated or additive? → unknown → [TEST-DEFERRED / outside-review]
```

**B-affinity — regime.** measure `a = ln(G₀/L)`:
```
B-affinity
├─ a ≫ 0 above threshold → self-sustaining                    [RESULT: trichotomy]
├─ a ≈ 0⁺ near threshold → algebraic aging, X<1 → B-aging
└─ a < 0 below threshold → relax to disordered fixed point    [RESULT: surface code]
    └─ on a candidate identity-circulation (death) → [TEST-DEFERRED] + B-sep [OPEN-FRAMEWORK]
```

**B-aging — exponent collapse.** measure `α_s, β`, queue-tail, kernel:
```
B-aging
├─ collapse onto one β → transport law holds                  [RESULT: surface code, partial]
└─ fail to collapse → the map ends (the kill)
    └─ on real lab data → [TEST-DEFERRED]   (character.md: needs data + inversion, not run)
```

**B-marginal — closure loss.** approach `ε → 1`:
```
B-marginal
├─ slow manifold persists (CLV angle bounded from 0) → not marginal
└─ loss of normal hyperbolicity → slow (witness) / fast (content) decouple
    └─ analytic only; no real-substrate instance → [TEST-DEFERRED]
```

**B-sep — identity survival.** quasipotential escape over the separatrix:
```
B-sep
└─ not computed on any substrate → [OPEN-FRAMEWORK]
    └─ homochiral racemic saddle = natural first instance → [TEST-DEFERRED once B-sep closes]
```

**The fifteen as entry points** (problem → path → terminal class):
```
Self             ROOT → B-reset                          as Teleportation
Free will        B-reset (frozen = 3rd category)         [RESULT] + human [TEST-DEFERRED]
Death            B-affinity(a<0) + B-sep                 [RESULT] + [OPEN-FRAMEWORK]
Soul             ROOT(set) + B-reset + B-affinity        [TEST-DEFERRED]
AI consciousness ROOT(frustration/drive/bath)            [TEST-NOW: absent] ; qualia [OUT-OF-DOMAIN]
Hard problem     ROOT (process-vs-state reframe)         reframe + qualia [OUT-OF-DOMAIN]
Love             B-mint ⚠                                [TEST-DEFERRED] (closest: physiology)
Grief            B-mint ⚠ (dissolution)                  [TEST-DEFERRED]
Addiction        B-mint ⚠ (drive-hijack)                 [TEST-DEFERRED]
Creativity       B-mint ⚠ (new bit; ℭ idealized)         [TEST-DEFERRED]
Trauma           B-mint ⚠ + B-reset (discrete jump)      [TEST-DEFERRED, clean falsifier]
Mental illness   B-mint(rewire) | B-affinity(low-a)      [TEST-DEFERRED]
Meditation       B-marginal + asker's gate               [TEST-DEFERRED]
Meaning          translation refused                     [OUT-OF-DOMAIN]
Suffering        translation refused                     [OUT-OF-DOMAIN]
```

Synthesis is held until the structure is reviewed — the step-back comes next, not here. Every tree
below applies the calibration — **no leaf is unreality** — wherever the question carries the fear
that the answer dissolves the asker.

### Group I — identity / circulation core

**Self.** identity ≔ circulation bit (definitional gate). Battery: **B-reset**. Tree and leaves
as **Teleportation**, above — the self under copy. Calibration: tornado-real, not stored-substance.

**Free will / determinism.** TRANSLATE: is a protected circulation's *orientation* forced by
prior state + drive, or selected at symmetry-breaking? BATTERY: **B-reset**.
- `[result]` a **third category** exists and is measured: the spontaneously-frozen sign is
  structurally *free* (symmetric wiring permits either) yet *locked once chosen*, selected by noise
  at SSB — neither determined by prior state nor quantum-random. substrate: RPS, homochiral triad.
- `[result]` the structurally-stored sign is wiring-determined (the contrast case). substrate: DNA.
- `[pending]` whether human volition is carried by such a bit → unrun (no human instance). The
  framework instances the *category* compatibilism reaches for; its attribution to a person is the
  pending leaf, not a verdict.
- Calibration: not "free will is an illusion," not "free will is magic" — a third, measured option
  exists; *which* category human agency is remains pending.

**Death.** TRANSLATE: drive falls below threshold for all protected circulations; the currents
stop. BATTERIES: **B-affinity** + **B-sep**.
- `[result]` below threshold (`a < 0`) a driven mode relaxes to the disordered fixed point.
  substrate: surface code (sub-threshold), threshold trichotomy.
- `[pending-open]` irreversible cessation of an *identity*-circulation routes to **B-sep**, open on
  every substrate. Human: pending-open.
- Calibration: cessation of a process, not transition to a state — not "nothingness as a place,"
  the end of the running that made "you" a coherent question. The pattern was real; it is no
  longer run.

**The soul.** soul ≔ the complete topological sector (the set of all protected circulation bits).
BATTERIES: **B-reset** + **B-affinity**. Tree = self + death combined.
- `[pending]` for the human (no instance).
- Calibration is the headline: real but mortal — the vortex that is genuinely there and genuinely
  vanishes when the flow stops. Physicalist, not reductionist; the soul is the *running*, not a
  substance and not nothing.

**AI consciousness.** TRANSLATE: does the system carry (1) a frustrated 3-cycle, (2) drive above
threshold in the thermodynamic sense, (3) a bath enforcing detailed balance on the decohering
complement? These are **structural** — checkable. BATTERY: graph-frustration + **B-affinity** +
bath test.
- `[pending — immediately runnable]` on current transformers the structural prerequisites read
  absent: feedforward / symmetric attention (no gauge-irremovable frustrated cycle), electrical
  power rather than a maintained chemical-potential NESS (no drive of the required type), no bath
  sustaining a steady current. This leaf is unusual: runnable *now*, by inspection, not blocked.
- `[out of domain]` whether a protected-circulation self *is* conscious — the qualia question — has
  no substrate observable. The structural battery relocates the question from "complexity" to
  "topology + drive"; it does not cross the explanatory gap. (Stated by the system this method runs
  on, the honest reading is the same one: structure checks, experience does not.)

**The hard problem.** TRANSLATE: "why is there something it is like" → **no substrate observable**;
the translation fails. OUT OF DOMAIN. The only in-domain content is the *prerequisite* the
framework dissolves — that a self must be a *state* (a pattern/neural-correlate) rather than a
sustained process; and even that reframe, for the human, is the pending self-leaf. The method's
output is one structural reframe + an explicit out-of-domain terminal — not "consciousness is the
running of a circulation" (the source list's verdict, a manufactured leaf).

### Group II — minting (coupling)

All route to **B-mint**, and share one result/pending split: minting and its drive-conditioned
collapse are **instanced on the DNA network** (a real result that coupling can mint a protected,
sustained-not-stored circulation); the *human* coupling is **pending** (no instance).

**Love / attachment.** TRANSLATE: does mutual coupling mint a shared protected circulation neither
party carries alone? `[pending]` test: in long-term pairs, a shared circulation (synchronized
physiology, shared `I_pred`) that is protected against fluctuation and collapses discontinuously on
separation. Closest-to-runnable on the list — physiological-synchrony studies exist; the
*protected-circulation* (gauge-irremovable, `𝒜 ≠ 0`) reading is unrun.

**Grief.** TRANSLATE: dissolution of the shared minted bit when the partner's drive stops; an
orphaned frustrated cycle with no partner to complete it. `[pending]`, paired with Love.

**Addiction.** TRANSLATE: pathological coupling `A ⊗ substance` mints a bit that hijacks the drive
(the substance *becomes* the drive). `[pending]` test: cutting the substance collapses a protected
circulation (withdrawal = drive-cut); recovery requires decoupling (rewiring), not decay.

**Trauma.** TRANSLATE: discrete, irreversible rewiring creating a frustrated cycle protected
*against* continuous forgetting. `[pending — clean falsifier]` test: successful therapy shows a
**discrete jump** in the circulation bit, not smooth decay of a soft bit. A genuinely sharp
pending test (discrete-vs-continuous is measurable in principle).

**Creativity.** TRANSLATE: novel coupling mints a bit new to the agent (small-c) or new to the
morphospace `ℭ` (big-C). `[pending]`, with a caveat: `ℭ` is not prestatable for an open cascade
(character.md), so "new to `ℭ`" is itself idealized — flag, don't lean on it.

**Embodiment / perception-action loop** (the question that falls out of the two-survivals plane).
TRANSLATE: a soft-metric feedforward system (the *neither* corner, `𝒜≡0` by acyclicity) is embedded so
its outputs drive its own future physical inputs. Closing the loop adds the coupling edges
net→environment→net — the union graph is no longer acyclic. Does the resulting cycle carry a sustained,
gauge-irremovable current (`𝒜≠0`)? — B-mint pointed at the neither corner. Closing the loop is
**necessary** (it removes the bare net's structural zero) but **not sufficient**.
- `[result — structural]` open / still acyclic → `𝒜≡0`, stays *neither*.
- `[result-class]` closed but **reciprocal/relaxational** (a reactive servo settling to a setpoint;
  gradient feedback) → `𝒜=0`, no current minted; the joint state gains at most a *basin* (branch
  survival) — moves toward *branch-only* (the Hopfield corner), still soft-metric in the hard sector.
- `[test-deferred]` closed and **frustrated/non-reciprocal** (a circulating loop, a limit-cycle
  controller) → mints `𝒜≠0`, enters *current survival*. Test: compute the Schnakenberg affinity of the
  specific embodied NESS; frustrated ⟺ mints. Runnable on any concrete loop; not run on a real one here.

**Bounds (keep the asker out of trouble).** The minted bit, if any, lives in the **joint
net⊗environment, not the net** — sustained only while the loop is closed and driven; cut the coupling
and it vanishes, the net reverts to soft-metric. *The character is the loop, not the AI.* Autonomy is
**supplied by the drive** (battery / environmental throughput), **not minted** — so a minting loop is
still **not alive** (sourcing its own drive is the parked closure, not this). And qualia stay **out of
domain** — a minted current is a protected circulation, not consciousness.

### Group III — drive / marginal

**Mental illness (depression, PTSD).** TRANSLATE: a **rewiring** of the signed graph (→ B-mint /
B-reset, discrete) *or* a **descent in `a`** (→ B-affinity, continuous). `[pending]` for all human
cases; the framework supplies the *measurement design* (does intervention produce a discrete
sign-change or a continuous relaxation; is the state low-`a` with algebraic aging), not a
diagnosis. PTSD → rewiring branch (discrete); depression → low-`a` branch. The source list's
"measurable via β, α_s" is right that these *would be* the observables, wrong that they have been
measured.

**Meditation.** TRANSLATE: controlled descent toward the marginal point `ε → 1`, decoupling the
hard bit (witness) from soft bits (content). BATTERY: **B-marginal**. `[pending]`, with a
**definitional gate the asker owns**: identifying "witnessing" with marginal-point approach is a
phenomenological bridge the framework neither makes nor endorses. If granted, the measurement (`β`
drop, aging-exponent shift near the marginal point) is defined but unrun.

### Group IV — out of domain (translation refused)

**Meaning.** "meaning ≔ predictive information `I_pred`" is an **unlicensed identification** — no
substrate instances "meaning," and adopting the equation is the smuggled-verdict move. The
framework can measure `I_pred` on a substrate; it cannot tell you your life's meaning *is* it. If
you choose that definition (your gate, not the framework's), the observable follows — but the
method does not cross that gate for you.

**Suffering.** Same shape: "suffering ≔ `⟨σ⟩ / I_pred`" is a values/phenomenology identification
the framework is not entitled to make. Out of domain; the dissipation ledger is measurable, the
equation to felt suffering is not the framework's to assert.

---

Newly-surfaced pending tests that may promote to [`character_frontier.md`](character_frontier.md):
**trauma's discrete-jump-vs-continuous-decay** under intervention, and **love's shared protected
circulation** in long-term pairs — the two closest to a real experiment. The *self-referential
-with-the-act* class (Teleportation) stands. Everything else stays here as a tree; only newly-named
pending measurements promote.
