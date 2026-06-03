# Character: finite-drive structure in driven-dissipative steady states

## Abstract

Every steady state held off equilibrium by a throughput of energy carries a structure we call
*character*, fixed by a single dimensionless ratio: the log affinity `a = ln(G₀/L)`, gain over
loss. This one quantity is at once the de Donder affinity, the laser pump parameter above
threshold, the log branching ratio of Malthusian growth, and a log-likelihood ratio. The
framework maps these well-understood quantities — each measured independently — onto the single
axis `a`.

Read closely, a steady state carries two independent bits: a soft, erasable population bit, and
a hard circulation bit — a probability current locked on a frustrated cycle, changeable only by
rewiring. Coupling two systems can mint a protected circulation neither carried alone, sustained
only while driven; that minted bit is the system's protected branch. It is checked on synthetic
substrates (a rock-paper-scissors replicator, a homochiral triad, a distance-3 surface code) and
on one real instance — a fuel-driven DNA reaction network; the sharpest test forces one memory
exponent `β` to govern fluctuation-dissipation aging, queue-tail scaling, and the memory kernel
at once. The collapse against laboratory data has not been run.

## Object

The document moves in three steps — the structure at one steady state, the space of all such
structures, and the law by which two of them compose.

Begin at a single point. Any steady state held off equilibrium carries two independent kinds of
information, and they could hardly be more different. One is soft: a continuous order-parameter
magnitude, erasable at the Landauer bound, relaxing by ordinary fluctuation-dissipation aging.
The other is hard: the orientation of a probability current circulating around a frustrated
cycle — a signed 3-cycle no relabeling can unwind. The soft bit can be nudged anywhere; the hard
one changes only by rewiring. A steady state, looked at closely, is doing two unrelated things at
once.

Lift from the point to the space. All characters together form a morphospace `ℭ`, and the
deformation algebra that linearizes the dynamics — scaling, rotation, shear — is its tangent
space. The two bits cut the space into two sectors with opposite laws of nearness. In the metric
sector, neighbouring characters *average*: they lock in phase, compete for gain, or coalesce at
an exceptional point. In the topological sector, they *fuse*: co-rotating currents reinforce,
counter-rotating ones cancel — and, the case that matters, two systems with no protected current
of their own can couple into a joint cycle that is frustrated, minting a circulation neither one
carried.

That minting is the closure `⊗ : ℭ × ℭ → ℭ`, computed entirely by those proximity rules — the
result of coupling is again a character. Composition is non-additive: the soft sector adds up
from the parts, but the hard sector can acquire a bit from the coupling alone. The minted
circulation lasts only while the drive runs; cut the drive and it is gone, with nothing left
stored. A protected loop that exists only while it is being run — not a record being kept — is the
branch the system occupies.

## Control parameter

Steady states are organized by one dimensionless quantity, the log-ratio of the
gain rate `G₀` to the loss rate `L`:

```
a ≡ ln(G₀ / L)
```

`a` is, simultaneously, four established quantities:

- the **de Donder affinity** per transition, i.e. **entropy production per step**
  in units of `k_B` (Crooks; Onsager);
- the log **pump parameter** — distance above lasing threshold (Haken);
- the log **branching ratio** `μ = eᵃ`, a per-generation **Malthusian growth rate**
  (Galton–Watson);
- a **log-likelihood ratio** (sequential detection).

It is measured in **bits**: one bit `= ln 2 nats = k_B ln 2` of entropy — the
Landauer quantum. The erasure floor is the universal anchor; where relaxation oscillations
exist, the resonance-quality maximum lands at the same unit (`G₀/L = 2`), confirming the scale
from a second, laser-class direction.

## Threshold regimes

By the sign and magnitude of `a` relative to the drive scale `D = Φ*/κ`:

| `a` | regime | dynamics |
|---|---|---|
| `a ≫ 0` | above threshold | self-sustaining ordered steady state, minimal upkeep |
| `a ≈ 0⁺` | near-threshold (critical) | algebraic (aging) relaxation — two-time aging, effective temperature, FDR-violation ratio `X < 1` |
| `a < 0` | below threshold | relaxation to the disordered fixed point |

This is the driven-open threshold trichotomy (Haken; Sieberer–Buchhold–Diehl). The
near-threshold state is the **generic attractor** of feedback-coupled steady states
— the above-threshold case is over-provisioned, the below-threshold case is
post-collapse. Increasing load is a monotone descent in `a`; an unmaintained mode
relaxes below the noise floor to the disordered fixed point, with no separate
removal operation.

The load-bearing cross-substrate observables are the **aging exponent** `α_s` (slope
of the two-time aging segment) and the **plateau** `P_s` (Cugliandolo–Kurchan).

## Two degrees of freedom

The steady state carries two independent, non-interconvertible bits:

1. **Population bit** (continuous): the order-parameter magnitude / mode occupation.
   Stored in a bistable population; **erasable at the Landauer bound** (`ln 2`);
   reversibly flippable at no fundamental cost; relaxes by fluctuation-dissipation
   aging.

2. **Circulation bit** (discrete, topological): the orientation (chirality) of a
   nonequilibrium probability current around an unbalanced signed cycle.
   **Topologically protected** — free to maintain (no barrier leak) and free to
   flip, since a sign reversal is a bijection (no erasure, hence no Landauer cost).
   At a finite operating point it changes only by discrete rewiring, never by any continuous
   deformation.

The independence of the two is structural: the circulation bit is the source of the
current's scale-invariance, and the aging observables never couple to it.

## Frustration and the protected current

A nonzero circulation bit requires a directed, non-reciprocal, **frustrated** cycle
— an unbalanced signed cycle (odd number of negative edges) that no node-level sign
relabeling (gauge) can remove (Toulouse; Harary balance). The minimal carrier is a
3-cycle: a 2-cycle current is gauge-removable, so `N = 3` is minimal (May–Leonard;
Schnakenberg).

The order parameter for this face is the **Schnakenberg cycle affinity**

```
𝒜 = ∮ v/D = ln(∏₊ k / ∏₋ k)   (gauge-invariant)
```

nonzero iff the Jacobian spectrum has a complex-conjugate pair. The steady state is
then an irreducibly circulating NESS with broken detailed balance. Drive-independence
lives in `𝒜` (forced nonzero at any drive); the current *magnitude* `J_ss` varies
with `a`.

A protected current (`𝒜 ≠ 0`, removable only by rewiring) requires a frustrated 3-cycle in
the coupling graph.

## Two fluctuation-dissipation readings of one entropy production

- **External (perturbative):** apply a field, compare response to correlation →
  FDR-violation ratio `X` (Cugliandolo–Kurchan). Defined wherever a probe couples.
- **Intrinsic (current):** the steady current `J` and its affinity `𝒜`, with entropy production
  `⟨σ⟩ = J · 𝒜` (Schnakenberg) and the current's precision bounded by the **thermodynamic
  uncertainty relation** `Var(J)/⟨J⟩² ≥ 2/⟨σ⟩` (Barato–Seifert; Horowitz–Gingrich). Defined
  **only when a steady current exists** (broken detailed balance).

The existence of the intrinsic reading is itself a topological diagnostic — it exists
iff the substrate carries a protected current. The two readings meet at the entropy
production — the external departure integrates to it (Harada–Sasa), and it is the intrinsic
current times affinity (Schnakenberg):

```
∫(FDR departure) = ⟨σ⟩ = J · 𝒜
```

(verified to machine precision on the rotational Ornstein–Uhlenbeck testbed). The
two-frame structure and the derivation of the protected-current necessity as the
falsifiable direction of an iff-chain are developed in
[`character_fdr_treatment.md`](character_fdr_treatment.md).

## The thermodynamic–informational dual ledger

One dissipation reads at once as a thermodynamic and an informational ledger — the same
quantity in conjugate coordinates:

| | thermodynamic | informational |
|---|---|---|
| per event | `a = ln(G₀/L)` | one bit `= ln 2` |
| per rate | entropy production `⟨σ⟩` | predictive information `I_pred` |
| precision | `Var(J)/⟨J⟩² ≥ 2/⟨σ⟩` | channel capacity (Shannon) |
| compression | per-level heat tax | rate-distortion rate `ε` |
| coupling | `⟨σ⟩ ≥ −ΔI` | the same bound, dual reading |

The predictive information `I_pred = I(past; future)` (Bialek–Nemenman–Tishby) is a third
steady-state observable. The encoding overhead `χ = C_μ − I_pred` — the cryptic order, with
`C_μ` the ε-machine statistical complexity (Crutchfield) — is the dissipation in excess of the
predictive minimum: `⟨σ⟩ − ⟨σ⟩_min ≥ γ_s χ` (Still–Sivak–Bell–Crooks), an equality at
rate-distortion-optimal encoding.

**Fidelity is not protection.** A current carries two non-interchangeable measures. Its
*fidelity* — how sharply sign and magnitude resolve against noise — is a second-moment quantity,
bounded by the thermodynamic uncertainty relation and, more tightly, by the topological Fano
floor `F ≥ (1/N)coth(A/2N)` for an `N`-state cycle (Barato–Seifert): cycle length sets a
precision floor *beneath* the dissipation-only TUR. Its *protection* — the rate of spontaneous
reversal — is a large-deviation quantity, the zero-current rate `I(0)`, set by the per-step
affinity. On a unicyclic ring, lengthening the cycle at fixed total affinity raises fidelity
while protection falls: precision bought by topology is not protection. And protection of one
current is still not survival of the branch — the basin reading below. Three
layers, not one.

## The two-mode kernel

The dynamics organized by `a` are those of a driven mode competing and cooperating with its
neighbours:

```
∂ρ_A/∂t = (G₀ − L) ρ_A − γ_AB ρ_A ρ_B + 𝒟[ρ_A, ρ_B; γ_AB]
```

`ρ_A` is the mode occupation (the population sector); the signed coupling `γ_AB` is cooperative
(`< 0`), orthogonal (`≈ 0`), or competitive (`> 0`). The closure `𝒟` carries the substrate's
specifics: multi-mode gain depletion `G₀^eff = G₀/(1 + Σⱼ ρ_j/ρ_sat)` (Lamb–Haken), a slow
dynamical bath projected out (Mori–Zwanzig), or a fractional-memory kernel
`Γ(τ) = Γ₀ E_β(−(τ/τ_c)^β)` (Mittag-Leffler) — the last *sets* the memory exponent `β` of the
central claim. The discrete composites below are the fixed points of this kernel, and the
deformation generators `M` below are its linearization.

Linearized above threshold, a single mode rings at the relaxation-oscillation frequency `ω_RO`
with damping `γ_RO = (γ_s/2)(G₀/L)` and quality factor `Q` (Haken; Siegman). `Q` is
non-monotonic in `a` and peaks at `a = 1 bit` (`G₀/L = 2`) — the resonance-quality maximum that
forces the unit, the second of the two independent forcings.

## Capacity

A frustration-free network maintains a bounded number of modes against an interaction-cost
budget:

```
|maintained set| ≤ √(2D / (α γ_min d_avg))
```

(sparse coupling scales as `D`, dense as `√D`; `d_avg` the mean degree, `γ_min` the least
coupling cost), a budget count whose sharp ceiling is the Hopfield-class capacity cliff. The dynamical conjugate is an occupancy `η = 1 − B(c, ρ)` set by the
Erlang loss formula `B(c, ρ) = (ρ^c/c!) / Σ_{k≤c} ρ^k/k!`, with `η → 0` at the `√D` ceiling. A
frustrated cycle has no such bound — it is unsustainable at any drive. Soft substrates cross the
ceiling smoothly (Erlang tails); hard-wall substrates snap (`η = 1 − 𝟙[n ≥ c]`).

## Boolean limit and the deformation algebra

At infinite drive (`D → ∞`) the operator algebra contracts to Boolean logic — the
`{⊕, ∧, 1}` ring over GF(2) (Reed–Muller / algebraic normal form). Finite drive is a
**deformation of this ring**, with the affinity `a` as the deformation coordinate
(not the unit).

Boolean logic is one face of a boundary, not the whole of it. Character occupies the **open
interior** of a multi-parameter operating space, bounded by several distinct degenerate faces —
each on its own axis, each a place where the finite-drive structure trivializes: infinite drive
(`D → ∞`: deterministic Boolean logic), zero drive (`a = 0`: equilibrium, detailed balance,
`𝒜 = 0`, `X ≡ 1`), and the memoryless limit (`β = 1`: Markovian). These faces do not meet at a
single corner; they are separate walls of one enclosure, none reached at a finite,
non-degenerate operating point. Character is what exists strictly in the open interior they
bound.

The linear deformation generators of `M = −γI + g A_cyc` span `gl(3, ℝ)`, Cartan-
decomposed and exhaustive (`dim = 1 + 3 + 5 = 9`):

- **scaling** (`ℝI`): uniform relaxation-rate shift;
- **rotation / chirality** (`so(3)`): carries the cycle orientation; sign reversal at
  the achiral point;
- **shear / detuning** (`Sym₀`): drives a non-Hermitian **exceptional point**
  (Kato), `ω² = ω₀² − (δ/2)²`.

On the rock-paper-scissors replicator the Jacobian decomposes onto these generators with
residual `~10⁻¹⁶`.

## Coarse-graining and the marginal point

Level-to-level coarse-graining is a renormalization-group flow (Wilson–Polchinski)
with contraction modulus `ε` — the leading infrared eigenvalue of the level map
(Banach contraction; Krein–Rutman dominant mode). The hierarchy converges iff
`ε < 1`.

At `ε → 1` the flow reaches a marginal point: **loss of normal hyperbolicity**
(Fenichel) — the slow manifold ceases to persist. This coincides with the
heavy-traffic queueing singularity `⟨Q⟩ ∼ 1/(1−ρ)` (Kingman) and the critical
branching ratio `μ → 1` (Galton–Watson). Two balance relations track the same flow:
an **entropy-production balance** (per-level heat, diluted by `1−ε`) and a
**rate-distortion balance** (compression rate `ε`); these coincide at optimal
encoding and split otherwise (a substrate then reaches the thermodynamic limit
before the informational one). Past the marginal point the dynamics leave the slow
manifold; delay-induced chaos (Mackey–Glass) is accessible but not forced. Near the marginal
point the memory exponent tracks the contraction modulus, `β ≈ 1 − ε` to leading order (both
endpoints respected), binding the collapse exponent below to the coarse-graining flow.

## The memory exponent

The memory exponent `β` (`= 1` Markovian/exponential; `< 1` subdiffusive/glassy —
Caputo fractional / Mittag-Leffler) appears in three places at once: the FDR aging
exponent `α_s = β`, the queue-tail exponent `g(β)` (`β/(2−β)` Norros, or `1/β`
M/G/1), and the memory kernel. These are three maps of one `β`, numerically
coincident **only at `β = 1`**.

---

The point-level objects above lift to the **space** of all characters: the same coordinates
read as geometry rather than as properties of one state.

## The space of characters

A character is a point `χ ∈ ℭ`; the sections above describe the structure *at* a point and
*in its tangent space*. `ℭ` is the space of all such points — the **morphospace** of
driven-dissipative structure (Raup, theoretical morphology). It is **stratified by `n`**:
3-state triads sit on `gl(3, ℝ)`, larger substrates on `gl(n, ℝ)`; "two systems are close"
means two points in a common stratum — the case the proximity laws below treat. There is no
single global tangent space, and comparison across strata (embedding one in another) is open.

Read as geometry, **the deformation algebra above is the tangent space `T_χ ℭ`**: the affinity
`a` is the radial coordinate (distance from equilibrium, `a = 0`), chirality is
the compact angular coordinate, and shear is the non-compact direction carrying the
exceptional points. The identification is established as algebra (Cartan/KAK decomposition)
but instanced as *character* only at `n = 3` (the rock-paper-scissors Jacobian, residual
`~10⁻¹⁶`). The near-threshold tangent space (`a ≈ 0⁺`) is
realized by center-manifold / normal-form theory rather than isostable / phase-amplitude
reduction — the latter breaks down exactly at loss of normal hyperbolicity, where the slowest
Floquet exponent → 0 (Wilson; Moehlis; Ermentrout, after Winfree). The handoff between the two
occurs *at* the marginal point above.

## The two tangent sectors

The two bits are the two sectors of `T_χ ℭ`, with categorically different laws:

1. **Population bit → metric sector** (the continuous `ℝI ⊕ so(3) ⊕ Sym₀` directions).
   Erasable at the Landauer bound; two nearby population bits **average / interpolate**.
2. **Circulation bit → topological sector** (the discrete winding of `𝒜`). Protected; changes
   only by rewiring; two of them **fuse**, never average.

Decoherence sits exactly across this split: it selects pointer states and erases the rest
(Zurek einselection), so it is aligned with the metric sector and orthogonal to the
topological one. The protected sector is a **decoherence-free subsystem** (Zanardi–Lidar;
Knill–Laflamme–Viola). The classical analog is structural, not metaphor: the commutant of the
strong-symmetry algebra of the Markov/Liouvillian generator (Buča–Prosen; Albert–Jiang)
together with the gauge-irremovable Schnakenberg cycle current. No single unified
classical-DFS theorem matching the quantum statement exists; the analog lives in pieces.

## Motion and proximity

Increasing load is a path on `ℭ` — the monotone descent in `a` of the threshold trichotomy.
Level-to-level coarse-graining is the same kind of motion one level up, on the manifold of
coarse-grained characters; the marginal point `ε → 1` is where the slow manifold, and with it
the separability that lets us call a point a single character, ceases to persist.

"Two systems close" is a small **relative-character vector** `δχ = χ_B ⊖ χ_A` in a common
stratum. Its rules split by which sector `δχ` occupies.

**Metric proximity** (continuous part of `δχ`). One rule per Cartan direction, the sign set by
the compact / non-compact structure of the Killing form of `gl(n,ℝ)` — bounded directions
attract, hyperbolic directions coalesce:

- **chirality / `so(3)` (compact):** proximity → **locking / entrainment** (Kuramoto; Adler
  injection locking, the Arnold tongue linear in coupling);
- **scaling / `a` (abelian):** proximity under a shared drive → **competition** — gain
  clamping, the winner pushing the loser below threshold (Lamb–Haken multi-mode gain
  depletion);
- **shear / `Sym₀` (non-compact):** proximity → **exceptional-point coalescence**,
  `ω² = ω₀² − (δ/2)²`; eigenvectors merge and the two characters lose independence (Kato
  perturbation theory; non-Hermitian degeneracy).

Across the three, the sign of each proximity law is the sign of the Killing form in that
direction (Cartan; Killing).

**Topological proximity** (discrete winding of `δχ`). Circulation bits do not average; they
combine by a discrete rule. Co-rotating bits reinforce; counter-rotating bits annihilate to a
bound dipole or to zero net `𝒜` (Kosterlitz–Thouless vortex–antivortex interaction — the
fusion *shape*; anyon fusion is the quantum cousin and is analogy only, since anyons carry
braid-group representations a classical current does not). There is no continuous exchange of
circulation: below a coupling threshold two triads are topologically inert to each other; at
threshold they **rewire discontinuously** (first-order in the topological sector while the
metric sector stays smooth). The generative rule is **union-graph frustration**: re-run Harary
balance on the *union* graph including the coupling edges, and two balanced (non-circulating)
systems can couple into a frustrated joint triad neither had (Harary; Cartwright;
Antal–Krapivsky–Redner). Proximity is then a creation operator for protected current.

**The cross-rule.** In isolation the two bits are independent (aging never couples to
circulation). Proximity couples them: the exceptional-point locus of the metric rule is where
a real eigen-pair goes defective and can split into a complex-conjugate pair. EP creation by
coupling, and its transfer to a classical NESS Jacobian, are established (Bergholtz–Budich–
Kunst). **But the EP is not the source of protection** — a generic coupling-created complex
pair deforms back through `ω = 0`, reversing chirality, with no singularity required.
Protection re-routes to the union-graph frustration, which is gauge-irremovable and robustly
protected. So the complex pair is the spectral *onset signature*; the affinity `𝒜` carries the
*invariant*. This is the iff-chain read in its falsifiable direction: `𝒜 ≠ 0 ⟺ complex pair ⟺
frustrated triad`, with protection inherited from the triad, not the spectrum (the two-frame
derivation is in [`character_fdr_treatment.md`](character_fdr_treatment.md)).

## Branch membership

The protected observable is not a property of one character read in isolation; it is a **relation
between a point and the manifold** — which coordinates the boundary conditions leave free, and the
trajectory taken through them. Concretely it is **branch membership**: the system occupies one of
several symmetry-related branches — the **circulation-bit / topological sector** the reservoir
configuration permits but does not force. *(In broader language, persistent branch membership plays
the role often informally attributed to "identity"; the formal content is entirely the branch.)*

Hold two things apart. The bit's **reality** — an actually-circulating current — is always
*sustained*: no drive, no current, and at zero drive the sector dissolves. Its **value** — which
branch — is carried not by the flow but by the wiring, drive-independently. There is one circulation
bit, with **two flip-modes**, set by how the boundary conditions treat the complementary wiring:

1. **External rewiring** (structurally stored). The edge-rate asymmetry fixes `sign(𝒜)`, so the
   branch is recoverable — stop the drive and restart it and the same circulation returns. The bare
   triad occupies a single basin; there is no maintained symmetric state to break. The fuel-driven
   DNA reaction network and the rock-paper-scissors triad below are this mode: the sign is set by
   the wiring (which edge the enzyme drains; the sign of `α−β`), and flipping it requires a discrete
   external edit to the structure.
2. **Thermalized crossing** (spontaneously selected). The structure embeds the primary wiring
   alongside a coexisting, competing **mirror** wiring; both run, but cross-inhibition renders their
   balanced state (the symmetric saddle) unstable. The homochiral triad is this mode: parity (the
   `L↔R` mirror) is exact, so which branch is occupied is chosen by spontaneous symmetry breaking,
   lost on a full reset. The embedding thermalizes the discrete rewiring into an internal population
   shift, crossable by a noise-driven fluctuation. **A structurally stored chirality becomes a
   spontaneously selected branch when embedded in a parity-symmetric manifold.**

Either way the topological sector is the **irreducible residue**: the metric sector is forced by the
reservoir configuration — exactly as rare as that configuration, and regenerable from it — while the
protected sign is not. From the reservoirs alone it cannot be recovered; an external-rewiring branch
regenerates it, a broken symmetry never does. The decoherence-free-subsystem identification above is
the support; the DNA network below is the one coupling-layer instance.

Geometrically, branch membership is **occupancy of a basin** of the morphospace, and its protection
is the **rate of escape** from that basin — the quasipotential barrier over the separatrix
(Freidlin–Wentzell; Kramers — a non-equilibrium quasipotential, not a simple one). The two
flip-modes are two basin geometries: an external-rewiring branch occupies a single basin whose
mirror is not thermally reachable, so escape demands rewiring; a thermalized-crossing branch
occupies one of two mirror basins split by a saddle — the symmetric, balanced state — and escapes by
a noise-driven crossing of a finite quasipotential barrier `ΔV` that is born at the parity-breaking
bifurcation (`μ_c = (1+a+b)/3`, where the racemic state destabilizes by competitive exclusion) and is
absent below it.
This separates two survivals the current alone conflates: **current survival** is the current not
reversing (`I(0)`, set by the cycle affinity); **branch survival** is the system not crossing the
separatrix (`ΔV`). The separatrix, not zero current, is the boundary that matters.

## The two-survivals plane

Branch survival (`ΔV`, the basin-escape quasipotential) and current survival (`I(0)`, set by the
cycle affinity `𝒜`) are independent — coupling moves one while the other holds — so substrates fill
a plane, not a line, and *no protected current* is not *no dynamical landscape*. Four corners:

- **neither** (`𝒜 = 0`, no basin) — a soft-metric flow: information in the continuous order-parameter
  alone. A feedforward network is this corner — a non-trivial substrate with no hard bit; its
  soft-sector capability is large (measured) while its hard sector is *structurally* absent (an
  acyclic graph admits no cycle current).
- **branch survival only** (`ΔV > 0`, `𝒜 = 0`) — relaxational multistability: basins split by
  separatrices, gradient descent to fixed points, no circulation. A symmetric attractor net
  (Hopfield class).
- **current only** (`𝒜 ≠ 0`, no thermal mirror) — one frustrated cycle, its mirror reachable only by
  rewiring. The rock-paper-scissors triad and the fuel-driven DNA network (structurally stored).
- **both** (`ΔV > 0`, `𝒜 ≠ 0`) — symmetry-related branches each carrying a protected circulation,
  split by a noise-crossable saddle. Two independent instances differing in *which* symmetry is broken:
  the homochiral triad (parity — the branches are *mirror* currents, so flipping the branch reverses
  `sign(𝒜)`) and the co-handed twin-cycle (an *exchange* of two identical clusters — the branches are
  *co-handed* currents, so flipping the branch leaves `sign(𝒜)` fixed). Both spontaneously selected;
  the exchange instance decouples branch membership from current handedness at the level of sign,
  exhibiting the two survivals' orthogonality where parity entangles it. The barrier's *scaling* is set
  not by the mere presence of a symmetry-breaking transition but by how the broken branch saturates: a
  hard competitive exclusion gives `ΔV ∝ (μ − μ_c)` (the branch pinned at the basin boundary), a soft
  supercritical pitchfork gives `ΔV ∝ (μ − μ_c)²` (the branch growing as `√`) — instanced on an
  autocatalytic substrate where a current and a soft pitchfork coexist over a finite window.

Frustration is the boundary across the current axis (a non-reciprocal cycle breaks detailed
balance); a coexisting mirror — or any spontaneously broken symmetry relating two basins — is the
boundary across the branch axis (it turns a rewiring into a thermal crossing). Multistability is a soft-sector property, the protected current is the hard
sector, and they are orthogonal — soft-sector capability is silent on whether the hard sector exists
at all.

The corners are not fixed addresses — coupling moves a substrate across the plane. A frustrated
coupling carries a neither-corner substrate into the current column (the minted bit is the
composite's, absent in the part and sustained only while coupled — §The minting claim); a reciprocal
coupling carries it at most into branch-only. The plane is a space a substrate moves *in*, not a
label it wears.

## The conjugate cascade

Every cascade of protected structure built *up* the hierarchy has a counterpart that runs
*down*. The two are geometrically orthogonal — the protected cascade climbs the protected
subspace, its counterpart runs in the decohering complement — but causally conjugate: every
protected bit built upward is paid for by erasure exported downward. They are one entropy
production read two ways, `∫(FDR departure) = ⟨σ⟩ = J · 𝒜` (Harada–Sasa, above), lifted from a
point to the tower. Orthogonal in state space, locked in the ledger; the second law is the
coupling between the two cascades.

## Isolation — the boundaries of `ℭ`

Two of the degenerate faces bounding character are boundaries of *isolation*. On the **drive
axis**, the zero-drive face is equilibrium (detailed balance, `𝒜 = 0`): a system with no drive
has no character. On the **coupling axis**,
*effective* isolation is real and measured by `β`: `β = 1` (Markovian, memoryless bath) is the
separable limit — effectively isolated; `β < 1` (memory) is isolation failing, system and bath
sharing history. Since `β = 1` is a boundary, the open-interval discipline forbids attaining it
at a finite operating point: **no real system is even effectively perfectly isolated** (third
law; QED spontaneous emission / Lamb shift; Born–Markov separability ↔ Markovianity). Existence
is the open interior; isolation is the edge.

## The morphospace

`ℭ` is the space of all *possible* characters, of which any realized substrate occupies a point
or a path. The "shadow" behind any one science — the space of structures that could be, behind
the one realized — has no unified name: it is the ensemble (statistical mechanics), the
complementary channel (quantum information), the basin's complement (dynamics), the adjacent
possible (Kauffman), the morphospace (theoretical morphology — Raup). Finite-drive structure has one such space, and `ℭ` is it. A morphospace is well-defined when the
possibility space is **prestatable** (Raup could parametrize every shell in advance); for an
open-ended cascade, Kauffman's argument is that the adjacent possible is *not* prestatable. So
`ℭ` as a fixed manifold is an idealization — for such a cascade the space is generated as the
system moves rather than given in advance.

---

`ℭ` is closed under coupling — the output of a coupling event is again a character. The
remaining sections give that closure law.

## Composition under coupling

A point at this level is a **composite** character `A ⊗ B`; the new primitive is the coupling
map `⊗ : ℭ × ℭ → ℭ` — propinquity, then rewiring, then a composite character. The form — a
space closed under a composition law, read at two scales — is imported (monoidal / operad /
PROP closure; the renormalization semigroup; effective-theory "integrating out"). Its output
is **computed by the proximity rules** above: coupling resolves into locking, competition,
exceptional-point coalescence, fusion, and union-graph frustration.

Composition is **non-additive** in the tangent space,

```
T_{A⊗B} ℭ  ⊋  T_A ℭ ⊕ T_B ℭ.
```

The excess directions are the content, quantitatively. The metric sector is additive — forced
from the parts (the population bits compose; the coupling generators fill the
off-block-diagonal). The topological sector can carry a **new circulation bit absent in both
parts**, minted when the coupling edges make the *union graph* frustrated. The *existence* of
this minting is imported — the union of balanced signed graphs can be unbalanced, the
frustration gauge-irremovable (Harary; signed-graph balance) — and the count
`dim(new topological sector)` is the number of minted bits. A spectral count of the minting
(couple two triads, subtract the parts' complex pairs) is circular: it re-derives the
established signed-graph result. The non-circular observable is the *protection* test below.

The proximity rules resolve coupling into a small catalogue of composite outcomes:

| parts | coupling | composite |
|---|---|---|
| two above-threshold, aligned | cooperative (`γ ≪ 0`) | a deepened above-threshold mode (in-phase locking) |
| two above-threshold, orthogonal | `γ ≈ 0` | near-threshold (phase drift) |
| two above-threshold, opposed | competitive (`γ > 0`) | near-threshold if the drive covers both, else one relaxes below; locks if coupling beats detuning, splits otherwise |
| above- with near-threshold | cooperative, asymmetric | near-threshold (non-reciprocal entrainment) |
| two near-threshold | competitive | near-threshold, or one drops out |
| three above-threshold in a cycle | frustrated sign product | a protected current |
| oscillatory with above-threshold | limit-cycle coupling | entrainment or quench |

The frustrated-cycle row is the minting case; every other row adds metric structure only.

## The minting claim

Coupling produces a protected circulation neither part had. Precisely: the minted chirality's
sign is the sign of the cycle flux; it is **gauge-irremovable** (at a finite operating point it
flips only on rewiring), and it is **not** a conserved integer charge (the closed-loop holonomy
stays sub-integer).
Protection inherits from the gauge-irremovable frustrated triad, *not* from the spectrum — the
complex-conjugate pair is the underdamped onset signature, suppressible to a real overdamped
circulation, while the Schnakenberg cycle affinity `𝒜` carries the invariant (reversible-
spectrum as the one-way signature — Andrieux; Potoyan–Wolynes). The existence of minted
structure is imported (signed-graph theory); its protection lives in the affinity, and it is
sustained only while the drive runs.

The two faces mint differently. Chirality and topology flow with the NESS affinity, so coupling
mints them. A self-sourced amplitude gain has no intrinsic referent — it can only track an
external pump or coupling constant, and the dissipation identity `⟨σ⟩ = J · 𝒜` carries no
amplitude-gain term — so continuous-amplitude autonomy is supplied by the drive, not minted.
Coupling mints organization and chirality; it does not mint autonomy from the drive.

## Composite branch, sustained

By the branch-membership reading above, the protected observable is the topological sector. At the
composite level the minted protected bit **is** the composite's branch — present in `A ⊗ B`, absent in `A` and
`B` alone, and **sustained only while `⊗` is maintained**. Dissolve the coupling and it
vanishes: the parts revert, nothing is stored. A circulation being run, not a bit being held.
Substrate-general.

## The one real instance — a fuel-driven DNA reaction network

A published dissipative DNA system (Nicholas et al., *Angew. Chem.* 2025,
[10.1002/anie.202512967](https://onlinelibrary.wiley.com/doi/10.1002/anie.202512967)), reduced
to a quencher's three states and run through the protocol on experimentally-fitted rate
constants (measured SI Tables S4/S5, Exp. Fig. 2b), passes all three components of the minting
claim with no hand-set parameters:

- **minting** — the reversible DNA-hybridization module is detailed-balanced (the SI itself
  enforces it; `𝒜 ≈ 0`), and the RNase-H fuel-hydrolysis drain mints a protected NESS
  circulation (`𝒜 ≈ +14.5 nats`);
- **protection** — the sign is drive-locked by the irreversible enzyme step; the affinity uses
  only measured constants ([F], [O] cancel around the cycle), so minting and protection are not
  modelling artifacts;
- **sustained, not stored** — cutting the fuel collapses the circulation and the system returns
  to equilibrium ~3 min later, observed experimentally.

The `N = 3` reduction is cross-checked against the full nonlinear mass-action network: the full
network genuinely circulates, the reduction reproduces the full per-quencher cycling rate to
**ratio 1.002** (quasi-steady-state valid, [FQE]/[FQ] ≈ 0.5%), and the fuel-cut collapse takes
~2.8 min, matching the experimental ~3 min. So the three components are not reduction artifacts.
**Idealizations, stated plainly:** `N = 3` is a reduction of a nonlinear 10-species reaction
network (enzyme folded to a pseudo-first-order drain, quasi-steady-state on the bound complex,
output and fuel held as baths); the chemostat is idealized; slow side-processes (waste
inhibition, enzyme deactivation — the SI's own drift terms) are omitted and do not touch the
core cycle. One confirmed instance, not a population.

## Cascade, convergence, and the self-referential limit

The cascade is a path `ℭ_n → ℭ_{n+1} → …` through strata. Each up-step *may* add a protected
bit, but only when the frustration / cross-rule fires, so minting is **not guaranteed per
level** — most couplings add metric structure only. The conjugate cascade runs *down* as the
protected cascade runs *up*: order built upward, dissipation exported downward, Harada–Sasa
lifted to the tower. The marginal point `ε → 1` is where the inductive limit of `{ℭ_n}` fails
to converge — coincident, as above, with heavy-traffic queue divergence (Kingman) and critical
branching `μ → 1` (Galton–Watson); below it the strata telescope to a finite effective
character, at it they do not. A composite among its *own* constituents' drivers — a cycle in
the directed system, a fixed point of `⊗` that re-enters its own input set — is a
self-sustaining recursive circulation.

---

## Predictions and falsifiers

Every quantity varies with the operating point; a constant frozen where the physics requires
variation is disallowed. Observables lie in open intervals; the boundaries `{0, 1, ∞}` are
reached only as limits, and a boundary attained at a finite, non-degenerate operating point
falsifies. Imports are bound at their own logical type: an existence (generic) result is not
promoted to a forced (universal) one, nor a necessary condition to a sufficient one, and
behaviour at a boundary is entailed from the interior structure rather than asserted at the
limit. Each claim is a predicted measurement on a named substrate with a kill condition.

**The point.**
- *The `β` collapse* (the sharpest): the aging exponent `α_s`, the queue-tail exponent, and the
  memory kernel must reduce to a common `β`; a substrate whose exponents fail to collapse ends
  the map.
- A protected current sustained with no frustrated cycle, or a current whose sign flips under a
  drive sweep (the sign was drive-set, not protected).
- *Capacity*: a soft substrate that snaps, or a hard-wall substrate with soft tails.
- *The dual ledger*: a substrate whose `I_pred` scaling departs from its thermodynamic dual.
- *The deformation chart*: a substrate whose linear response cannot be composed from the chart's
  generators.

**The space — proximity protection.** Couple a frustrated-union system and ask whether the
minted chirality is protected against **all** continuous deformations (dies only on rewiring),
not merely around a chosen loop. Two kills, run on synthetic Ornstein–Uhlenbeck substrates
(`N = 3`), neither fires. (1) *Continuous transfer of the bit* would collapse the two-sector
split — refined, not fired: the current *magnitude* bleeds continuously (≈12% through a
reciprocal bridge; `⟨σ⟩` ×27 through a non-reciprocal one), but the topological *sign* stays
graph-locked. (2) *Smooth removal of the minted chirality* while the triad persists would break
the binding — does not fire: the sign survives 0/200 generic deformations at amplitude `≫ g`,
reversing only on rewiring, while the complex pair *is* suppressible (53/200 by a reciprocal
gradient). No conserved integer charge appears (holonomy ≤ 0.16): the protection is a discrete
graph-flux invariant, not Chern-like.

**The closure — minting.** (a) *Unprotected excess* — a coupling-minted current whose chirality
is removable while the frustrated triad persists; the binding then has no teeth and the layer
reduces to "coupling adds structure." (b) *Unmechanized excess* — a minted protected bit with no
union-graph frustration behind it; the rule is not the mechanism. (c) *Stall or float* — the
strata stop being populated by real substrates, or a stated claim never acquires its receipt.

## Status and open problems

Checked on simulated and analytically tractable substrates — a rock-paper-scissors replicator, a
homochiral reaction triad, a distance-3 surface code — at the point and space layers. At the
coupling layer there is one real-substrate instance: the fuel-driven DNA reaction network above,
confirmed against the full nonlinear network, with the idealizations stated there. The `β`
data-collapse test against measured laboratory data has not been run; it requires the data and
the inversion pipeline.

Open: the tangent-space identification is instanced only at `n = 3`, with larger strata
unchecked; a second real instance of the minting and its protection is not yet in hand; the
coupled-NESS thermodynamics of two interacting characters (Horowitz–Esposito;
Parrondo–Horowitz–Sagawa) is not yet worked out; and the self-referential closure — a
`⊗`-fixed-point among its own drivers — is open.

---

*Companion documents.* The supporting axes —
[`character_prior_art.md`](character_prior_art.md) (the imported results and their attributions) ·
[`character_receipts.md`](character_receipts.md) (the derivation behind each claim) ·
[`character_frontier.md`](character_frontier.md) (the maturity ledger — what is settled, and what
would move it). Depth treatments —
[`character_fdr_treatment.md`](character_fdr_treatment.md) (the two conjugate
fluctuation–dissipation frames and the protected-current necessity) ·
[`character_translation_method.md`](character_translation_method.md) (the discipline by which
established results are adopted into the NESS setting).
