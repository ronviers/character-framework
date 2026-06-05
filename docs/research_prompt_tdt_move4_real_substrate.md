# Research prompt — a real substrate for TDT move 4 (v2, symmetry-first)

**For the outbound multi-model research channel.** Self-contained; assumes no prior context.
Return a unified, source-cited report. The deliverable is a *ranked shortlist of concrete, named
datasets*, each scored against a fixed four-gate test, with the failing gate named for every reject.

## What we are doing (minimal context)

We have a portable three-move test — the **transverse-decomposition test (TDT)** — for a structural
claim about driven non-equilibrium steady states (NESS): a **topologically protected circulating
current** 𝒜 is *orthogonal* to, and cannot couple to, any **metric-sector observable** B (an escape
barrier, a logical-error-rate exponent, an aging/relaxation exponent), and this orthogonality is
**symmetry-protected, not generic** — breaking the protecting symmetry turns the coupling on linearly
in a symmetry-breaking knob δ. The test has already run cleanly on a homochiral reaction triad (escape
barrier), the surface code (logical-error exponent), and a biased glassy ring (aging exponent). The
surface-code run was *synthetic*: it calibrates the test but does not vindicate it on real data.
**We want a real, measured dataset to run it on.** The claim is substrate-general — do not restrict to
a single physical domain or to human/biological framing.

## The lesson that sets the search (read before proposing anything)

A prior round taught us the two binding gates pull against each other:

- **Real quantum error correction has the cleanest symmetry but no usable δ sweep** — public datasets
  fix the error model, so the symmetry-breaking knob can't be varied. It fails gate (iv).
- **Biochemical cycle systems (circadian clocks like KaiABC, ATPase/kinesin motors, flagellar motors)
  hand you the δ sweep for free but have no clean protecting symmetry** — their "symmetry" is
  time-translation/phase, which *generates* the cycle rather than *forbidding coupling*, and their
  perturbations (mutations, ATP concentration, load) move period, amplitude, and coherence all at once.
  They fail gate (iii). A current + a sweep is **salience**, not affordance — do not propose them.

The target is the **rare intersection**: systems with a genuinely **topological** protecting symmetry
that *also* publish symmetry-breaking sweeps. Prioritize, in order:
**(1) magnetic skyrmions, (2) quantum Hall edge transport, (3) topological photonic/acoustic lattices.**

## The four gates (apply strictly; (iii) and (iv) are co-equal and both rare)

For each candidate, name the measured quantity that fills each role and score pass/fail:

- **(i) A protected current 𝒜 that varies across the data** — a topological/chiral flux, edge current,
  or skyrmion Hall drift whose magnitude differs across conditions. Not merely displayed once.
- **(ii) A metric-sector observable B on the *same* system** — a barrier, lifetime/annihilation rate,
  backscattering/breakdown rate, or relaxation exponent. Decay/escape, not circulation.
- **(iii) A *clean topological* symmetry separating 𝒜's sector from B's mode.** State which invariant
  protects it (topological charge Q, the bulk Chern/winding number, an engineered lattice symmetry).
  This is the gate the result hinges on: if the protecting symmetry is not clean, move 3 below cannot
  distinguish a symmetry-breaking turn-on from generic parameter dependence, and the test is vacuous.
  **Reject any candidate whose protecting symmetry you cannot name as a topological invariant.**
- **(iv) A knob δ that breaks that symmetry, *varied within already-published data*** — field, DMI,
  confinement geometry, sample width, edge proximity, controlled disorder. A dataset that fixes δ at
  one value fails here.

## What a PASS must deliver (no field-level plausibility)

Do **not** answer "many papers in field X sweep these knobs." For each candidate return **one concrete,
named dataset / paper** and state:

- Dataset identity + citation + **access** (fully public / on request / proprietary).
- The exact measured quantity for (i) 𝒜, (ii) B, (iii) the named topological symmetry, (iv) the δ knob.
- **Which symmetry, broken by which δ, would couple 𝒜 to B** — as a physical mechanism, so the
  predicted linear turn-on is interpretable rather than buried in generic δ-dependence.
- Whether the published data spans enough δ values *and* enough 𝒜 variation to run all three moves from
  what already exists — or what specifically would need new experiments.
- Whether 𝒜 is resolvable above measurement noise/artifact (any reported variance or SNR).
- A one-line **gate verdict**: PASS, or FAIL + the gate that fails.

Rank PASS candidates by how cleanly gates (iii) and (iv) are *jointly* satisfied from existing public
data. Two genuinely-gated datasets beat twenty that merely display a current and run sweeps.


----

model a:
x
model b:
x
model c:
x
