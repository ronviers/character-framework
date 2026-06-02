# Character: finite-drive structure in driven-dissipative steady states

## Abstract

Nonequilibrium steady states (NESS) arise across driven-dissipative systems—lasers, biochemical networks, queueing processes, and glassy materials—yet no unified framework organizes their steady-state properties under a single control parameter. We introduce *character*: the finite-drive structure of a NESS, parameterized exclusively by the dimensionless affinity \(a = \ln(G_0/L)\), the log-ratio of gain to loss. This single quantity simultaneously recovers the de Donder affinity (entropy production per step), the laser pump parameter above threshold, the log branching ratio (Malthusian growth), and a log-likelihood ratio. The framework does not propose new dynamics; it forces independently established results from stochastic thermodynamics, laser theory, Galton–Watson processes, and spin-glass aging onto \(a\) and tests their alignment by data collapse.
Two independent degrees of freedom arise: a population bit (erasable at the Landauer bound) and a topologically protected circulation bit (requiring a frustrated 3-cycle). The memory exponent \(\beta\)—from fluctuation-dissipation aging, queue-tail scaling, and the memory kernel—coincides only at \(\beta=1\), providing a sharp falsifiable test. Coarse-graining reduces to a renormalization-group contraction; the marginal point coincides with critical branching and heavy-traffic queue divergence. The framework is validated on synthetic substrates (rock-paper-scissors replicator, homochiral triad, surface code); at the coupling layer it has one real-substrate instance — a fuel-driven DNA reaction network — with the central data-collapse test still awaiting experimental data.

## Object

A coordinate system for driven-dissipative steady states. It does not introduce
dynamics; it fixes independently-derived results from laser theory, stochastic
thermodynamics, queueing, spin-glass aging, and the renormalization group onto a
single control parameter and tests the alignment by data collapse. The content is
the forcing onto one parameter and the collapse test; the constituent results are
imported.

## Control parameter

Steady states are organized by one dimensionless quantity, the log-ratio of the
gain rate `G₀` to the loss rate `L`:

```
a ≡ ln(G₀ / L)
```

`a` is, simultaneously, four established quantities — the framework's claim is that
they are one:

- the **de Donder affinity** per transition, i.e. **entropy production per step**
  in units of `k_B` (Crooks; Onsager);
- the log **pump parameter** — distance above lasing threshold (Haken);
- the log **branching ratio** `μ = eᵃ`, a per-generation **Malthusian growth rate**
  (Galton–Watson);
- a **log-likelihood ratio** (sequential detection).

It is measured in **bits**: one bit `= ln 2 nats = k_B ln 2` of entropy — the
Landauer quantum. The framework forces this unit twice from independent directions
(the resonance-quality maximum at `G₀/L = 2`, and the erasure floor), which is why
it is the natural denomination rather than a chosen one.

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
   It changes only by discrete rewiring, never by any continuous deformation.

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

Necessity statement: a protected current (`𝒜 ≠ 0`, removable only by rewiring)
implies a frustrated 3-cycle in the coupling graph. Falsified by any real substrate
sustaining a protected current with no such cycle, or by a drive sweep in which the
current's sign flips (sign was drive-set, not protected).

## Two fluctuation-dissipation readings of one entropy production

- **External (perturbative):** apply a field, compare response to correlation →
  FDR-violation ratio `X` (Cugliandolo–Kurchan). Defined wherever a probe couples.
- **Intrinsic (current):** the **thermodynamic uncertainty relation**,
  `Var(J)/⟨J⟩² ≥ 2/⟨σ⟩` (Barato–Seifert; Horowitz–Gingrich). Defined **only when a
  steady current exists** (broken detailed balance).

The existence of the intrinsic reading is itself a topological diagnostic — it exists
iff the substrate carries a protected current. The two readings are one entropy
production, joined by the Harada–Sasa identity:

```
∫(FDR departure) = ⟨σ⟩ = J · 𝒜
```

(verified to machine precision on the rotational Ornstein–Uhlenbeck testbed).

## Boolean limit and the deformation algebra

At infinite drive (`D → ∞`) the operator algebra contracts to Boolean logic — the
`{⊕, ∧, 1}` ring over GF(2) (Reed–Muller / algebraic normal form). Finite drive is a
**deformation of this ring**, with the affinity `a` as the deformation coordinate
(not the unit). The classical corner is a single degenerate point at which
`Boolean = Markovian = equilibrium = detailed balance = X ≡ 1 = 𝒜 = 0 = β = 1`.

The linear deformation generators of `M = −γI + g A_cyc` span `gl(3, ℝ)`, Cartan-
decomposed and exhaustive (`dim = 1 + 3 + 5 = 9`):

- **scaling** (`ℝI`): uniform relaxation-rate shift;
- **rotation / chirality** (`so(3)`): carries the cycle orientation; sign reversal at
  the achiral point;
- **shear / detuning** (`Sym₀`): drives a non-Hermitian **exceptional point**
  (Kato), `ω² = ω₀² − (δ/2)²`.

Each generator's forced response is a checkable prediction: a substrate whose
linear response cannot be composed from these generators falls outside the chart.
(Instanced on the rock-paper-scissors replicator: its Jacobian decomposes
onto these generators with residual `~10⁻¹⁶`.)

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
manifold; delay-induced chaos (Mackey–Glass) is accessible but not forced.

## The central testable claim

The memory exponent `β` (`= 1` Markovian/exponential; `< 1` subdiffusive/glassy —
Caputo fractional / Mittag-Leffler) appears in three places at once: the FDR aging
exponent `α_s = β`, the queue-tail exponent `g(β)` (`β/(2−β)` Norros, or `1/β`
M/G/1), and the memory kernel. These are three maps of one `β`, numerically
coincident **only at `β = 1`**. The framework's sharpest test is the **data collapse**:
a substrate whose aging and queue-tail exponents fail to reduce to a common `β`
falsifies it.

## Measurement discipline

- Every quantity varies with the operating point; a constant frozen where the
  physics requires variation is disallowed.
- Every claim is a predicted measurement on a named substrate with a kill condition.
- Observables lie in open intervals; the boundaries `{0, 1, ∞}` are reached only as
  limits. A boundary attained at a finite, non-degenerate operating point falsifies.

## Validation status

Derived and checked on simulated and analytically tractable substrates (the
rock-paper-scissors replicator, a homochiral reaction triad, a distance-3 surface
code). One real-substrate instance has been confirmed at the coupling layer — a
published fuel-driven DNA reaction network (Nicholas et al. 2025), reduced to a
three-state Markov model and cross-checked against the full nonlinear network, with
stated idealizations. The central data-collapse test against measured laboratory data
remains pending the data and the inversion pipeline.

---

## What the translation leaves standing

In this register the constituent results are visibly the standard ones — affinity,
the FDR-violation ratio, the thermodynamic uncertainty relation, the Schnakenberg
current, the RG contraction, normal hyperbolicity, data collapse. Two things do not
reduce to an existing name:

1. the **forcing** of all of them onto the single parameter `a`, and the
   **over-determination** that makes the alignment a test rather than a definition;
2. **`character`** itself — the umbrella for the finite-drive structure of a NESS,
   which has no single established name though each of its components does.

Everything else is a renaming. That is consistent with the framework's stated
posture (it imports and re-expresses; the residual is the bindings and the
falsifiers), and it is the strongest reason the coined vocabulary is optional rather
than load-bearing for a physics audience.
