# Identity-survival on a homochiral triad, and the structural/spontaneous distinction — findings for independent review

*Companion to `character.md`. Submitted for an outside opinion.*

## Purpose

This note reports computational results obtained against two substrates named in `character.md` —
the homochiral reaction triad and the rock-paper-scissors (May–Leonard) replicator — and proposes
(a) one correction to `character.md` §Identity and (b) a mechanism for the distinction that section
draws. The underlying physics is standard (Kramers escape, Freidlin–Wentzell quasipotential,
Lyapunov steady states, Schnakenberg cycle affinity, May–Leonard cyclic competition); it can be
checked without accepting the framework's interpretive layer. Review questions are at the end.

The framework context, in one line: `character.md` §Identity holds that a driven 3-cycle carries a
*protected chirality sign* (the orientation of a non-equilibrium probability current), and
distinguishes two ways that sign acquires its value — **structurally stored** (set by the wiring,
flips only by rewiring) vs **spontaneously frozen** (set by symmetry breaking, re-chosen at random
on reset).

## Setup (standard terms)

Both substrates are 3-cycle cyclic-competition NESS under additive demographic noise.

**RPS (May–Leonard), one species per node:**
```
dx_i/dt = x_i (1 − x_i − α x_{i+1} − β x_{i−1}),   i mod 3
```
Coexistence `x* = 1/(1+α+β)`; Jacobian eigenvalues `{ −x*(1+α+β),  −x*[1−(α+β)/2] ± i x*(√3/2)(α−β) }`.
With `α=0.5, β=1.0`: a stable focus with a complex pair → a sustained rotational NESS. Chirality
sign `= sign(α−β)`, fixed by the parameters.

**Homochiral triad (Frank/Kondepudi class), two mirror cyclic triads `L, R` with mutual cross-inhibition:**
```
dL_i/dt = L_i (F − L_i − a L_{i+1} − b L_{i−1} − μ S_R)
dR_i/dt = R_i (F − R_i − b R_{i+1} − a R_{i−1} − μ S_L),    S_L=ΣL, S_R=ΣR
```
Parity `P:(L↔R, cycle-reverse)` is an exact symmetry. With `a=0.5, b=1.0, μ=1.6, F=1.0` the racemic
state `L=R` is unstable; one hand wins by spontaneous symmetry breaking.

**Reduction (used below).** With the loser hand extinct (`S_R→0`), the winning hand obeys
`dL_i/dt = L_i(F − L_i − a L_{i+1} − b L_{i−1})` — *identical* to RPS under `F↔1, a↔α, b↔β`. Same
fixed point (`0.4`), same eigenvalues (`[−1, −0.1±0.173i]`), same cycle affinity. The two hands are
each other's `α↔β` rewiring (opposite chirality).

## Measured results (direct simulation)

**R1 — identity-survival barrier.** Noise-driven first passage between the two mirror basins (across
the racemic saddle; order parameter `ee=(L−R)/(L+R)`) is Kramers-activated: `ln(MFPT)` is linear in
`1/σ²` with slope `ΔV ≈ 0.018`. Independently, the in-basin quasipotential `V(ee) = −σ² ln P(ee)`
**collapses across σ** (rms `4.6·10⁻³`), confirming a well-defined Freidlin–Wentzell barrier, not a
noise artifact. The chiral sign is stable at the `σ ≈ 0.01–0.04` demographic noise where prior tests
hold; escape requires `σ ≈ 0.1`.

**R2 — two distinct survivals.** The within-cycle current-reversal rate `I(0)` is governed by the
cycle affinity `𝒜`, computed via the rotational-OU frame: Lyapunov steady covariance `Σ`
(`MΣ+ΣMᵀ+2DI=0`); entropy-production rate `⟨σ⟩ = Tr[ΩΣΩᵀ]/D` with irreversible drift `Ω = M + DΣ⁻¹`;
`𝒜 = ⟨σ⟩ / (ω₀/2π)`. For the winning hand `𝒜 ≈ 21.77 nats`, **noise-independent to machine
precision** (the machinery was validated against the canonical 2D rotational OU, recovering
`⟨σ⟩ = 2ω₀²/κ`, `𝒜 = 4πω₀/κ` exactly). Because `𝒜` (an affinity, noise-independent) and `ΔV` (a
quasipotential, entering as `exp(−ΔV/σ²)`) have **categorically different noise-scaling**, they
cannot be the same quantity — the two survivals are distinct observables.

**R3 — controlled embedding.** The bare RPS triad (= the homochiral winning hand) has `𝒜 = 21.77`
and **no** `ΔV` (one basin; chirality flips only by rewiring `α↔β`). Embedding it in the `L↔R`
mirror adds `ΔV = 0.018` **without changing 𝒜**. Circulation affinity and identity barrier are
orthogonal: the embedding acts on one and leaves the other untouched. (This is a clean before/after
on a single triad, not a comparison across two unrelated substrates.)

**R4 — reset-and-re-drive discriminator.** 40 random-IC resets per substrate, protected sign read
each time: homochiral re-rolls `+20 / −20` (50/50 — spontaneous); RPS returns the **same** sign
`+0 / −40` (structural). The control (homochiral 50/50) confirms the apparatus can detect
spontaneity; RPS simply lacks it.

## Proposed correction to `character.md` §Identity

§Identity lists "the rock-paper-scissors **and** homochiral triads" as spontaneously frozen. R4
shows RPS does not re-roll (40/40), and its sign `= sign(α−β)` is wiring-set and flips only by
rewiring — which is §Identity's own *definition* of structurally stored. The classification was
**internally inconsistent**: §Identity's definition and the receipts entry (which already states RPS
"flips only by rewiring") both make RPS structural; only the §Identity list called it spontaneous.
The proposed correction moves RPS to structurally stored (with the DNA network), leaving the
homochiral triad as the sole spontaneously-frozen instance. This is independent of R1–R3 (the
barrier results do not depend on RPS's class).

## Proposed mechanism (interpretation, not yet independently tested)

R3 plus the field-equation reduction suggest the two "kinds" are **one chirality bit with two
flip-modes**:

- A bare triad's chirality lives in the drift (`sign(α−β)`); its only symmetry (`α=β`) is the
  achiral, current-free point. So "symmetric" and "running" are mutually exclusive — there is no
  *maintained* symmetric state to break, and the sign can change only by an external rewiring.
- Coupling the triad to its `α↔β`-rewired mirror (= the homochiral construction) supplies a parity
  symmetry whose symmetric state (racemic) is **still current-carrying** — both wirings run,
  balanced — and, above the cross-inhibition threshold, unstable. The rewiring that would flip a
  bare triad's sign becomes an **internal population shift** across the racemic saddle: a
  noise-crossable barrier of height `ΔV`.

So: **spontaneously frozen = structurally stored with the mirror wiring present as a coexisting,
competing population**, which thermalizes the discrete rewiring into a finite quasipotential
barrier. The drive merely maintains the currents (fungible — any sustained flow); the second copy is
essential only because both wirings must coexist for the flip to be a population crossing rather
than an external edit.

Confidence: the field-equation identity (homochiral hand = RPS) and the `α↔β`-mirror relation are
facts readable from the equations; the "thermalized rewiring" reading is interpretation, forced by
R3 but not yet independently tested.

## Predictions / falsifiers (cheap, runnable)

- **μ-threshold (the single-knob test).** Lower Frank cross-inhibition `μ` through its threshold:
  the racemic state restabilizes, and the mechanism predicts `ΔV → 0` and resets stop re-rolling at
  the *same* `μ`. Confirms "a maintained-unstable symmetric state is the whole requirement."
- **Multiplicity.** Three mirror copies (`Z₃`) → three basins; reset distribution ≈ 1/3 each.
- **Maintenance fungibility.** Drive the same structure with a structurally different sustained flow
  → SSB, `ΔV`-scaling, and `𝒜` unchanged.

## Questions for review

1. Are **R1–R2** sound as stated — the Kramers/quasipotential extraction and σ-collapse; the
   affinity computation and its noise-independence; and the inference that different noise-scaling
   precludes `ΔV = I(0)`?
2. Is the **RPS reclassification** (structurally stored, not spontaneously frozen) correct? Is there
   a standard reading of cyclic-competition systems under which a single RPS triad's chirality is
   *spontaneously* broken — i.e., is anything being missed?
3. Is the proposed **mechanism** ("spontaneous = structural + a coexisting rewired mirror; the
   embedding thermalizes the rewiring into a quasipotential barrier") (a) a known/standard result
   that should simply be cited, (b) novel and plausible, or (c) flawed?
4. Does this warrant **restating §Identity's "two kinds" as one bit with two flip-modes**, or is the
   existing dichotomy framing preferable for other reasons?

## Reproduction

| result | script | key output |
|---|---|---|
| R1 | `experiments/identity_survival_barrier.py` | `ΔV ≈ 0.018`; σ-collapse rms `4.6e-3` |
| R2 | `experiments/cycle_affinity.py` | `𝒜 = 21.77` nats, D-independent; canonical-OU validation |
| R3 | `experiments/rps_affinity.py` | RPS `𝒜 = 21.77` = homochiral winner; no `ΔV` |
| R4 | `experiments/reset_redrive_test.py` | homochiral 20/20; RPS 40/40 |

Substrate definitions (canonical instances): `experiments/homochiral_triad.py`,
`experiments/rps_triad.py` (with `rps_two_bits.py` and `two_frame_magnitude.py` — the full instance
and validation scripts, copied into this repo from the legacy `mpa-conform` so it is self-verifying;
they run standalone). All runs are direct simulation (no fitting, no inversion pipeline); the
`ΔV`/`𝒜` separation and the reclassification rest only on the four session scripts above.


-----------------------
model a:

### Formalizing the $\Delta V$ Collapse

The vanishing of the quasipotential barrier $\Delta V$ as the system drops below the cross-inhibition threshold can be mapped by projecting the dynamics onto the slow manifold. For a homochiral network, we define the order parameter as the enantiomeric excess, $x = (L-R)/(L+R)$.

Near the critical cross-inhibition threshold $\mu_c$, the deterministic drift governed by the difference in competing reaction rates reduces to the normal form of a supercritical pitchfork bifurcation:


$$\dot{x} = \gamma(\mu - \mu_c) x - \kappa x^3$$


where $\gamma$ and $\kappa$ are positive constants derived from the bare reaction rates.

The Freidlin–Wentzell quasipotential $V(x)$, which governs the Kramers escape rate, relates to the deterministic drift via $dV/dx \propto -\dot{x}$. Integrating this gives the landscape:


$$V(x) = -\frac{\gamma(\mu - \mu_c)}{2} x^2 + \frac{\kappa}{4} x^4$$

Above threshold ($\mu > \mu_c$), the system possesses an unstable racemic saddle at $x_0 = 0$ and two stable chiral basins at $x_\pm = \pm \sqrt{\gamma(\mu - \mu_c)/\kappa}$. The identity-survival barrier $\Delta V$ is the energy difference between the basin minimum and the saddle:


$$\Delta V = V(0) - V(x_\pm) = \frac{\gamma^2}{4\kappa} (\mu - \mu_c)^2$$

This formalizes the proposed mechanism: as $\mu \downarrow \mu_c$, the competing mirror basins coalesce into a single basin at $x=0$, and the barrier $\Delta V$ smoothly scales to zero following a quadratic power law. Below threshold ($\mu \leq \mu_c$), the symmetric running state is stable, symmetry breaking is lost, and the barrier ceases to exist.

---

### Proposed Revision: §Identity

*Here is the redrafted §Identity section, integrating the single-bit / two-flip-modes structure and correcting the RPS alignment.*

## Identity

Identity is not a property of one character read in isolation; it is a **relation between a point and the manifold** — which coordinates the boundary conditions leave free, and the trajectory taken through them. Concretely, identity is the **circulation-bit / topological sector**: the substructure the reservoir configuration permits but does not force.

Hold two things apart. The bit's **reality** — an actually-circulating current — is always *sustained*: no drive, no current, and at zero drive the sector dissolves. Its **value** — which way it circulates — is carried not by the flow but by the wiring, drive-independently.

There is only one kind of circulation bit, but it possesses **two flip-modes**, dictated by how the boundary conditions treat the complementary wiring:

1. **External Rewiring (Structurally stored).** The edge-rate asymmetry fixes the sign, so the direction is recoverable — stop the drive and restart it and the same circulation returns. The bare triad occupies a single basin; there is no maintained symmetric state to break. The fuel-driven DNA reaction network and the rock-paper-scissors (RPS) triad are this mode: the sign is set by the wiring (e.g., $sign(\alpha-\beta)$), and flipping it requires a discrete external edit to the structure.
2. **Thermalized Crossing (Spontaneously frozen).** The system is structurally symmetric: it embeds the primary wiring alongside a coexisting, competing mirror wiring. Both wirings run, but cross-inhibition renders their balanced state (the racemic saddle) unstable. The homochiral triad is this mode: parity is exact, so which hand wins is chosen by spontaneous symmetry breaking, lost on a full reset. The embedding thermalizes the discrete rewiring operation into an internal population shift, crossable by a noise-driven fluctuation.

Either way the topological sector is the **irreducible residue**: the metric sector is forced by the reservoir configuration — exactly as rare as that configuration, and regenerable from it — while the protected sign is not. From the reservoirs alone it cannot be recovered; an asymmetric wiring regenerates it, a broken symmetry never does.

Geometrically, identity is **membership in a basin** of the morphospace, and its protection is the **rate of escape** from that basin — the quasipotential barrier over the separatrix. The two modes are two basin geometries: a structurally-stored bit occupies a single basin whose mirror is not thermally reachable, so escape demands rewiring; a spontaneously-frozen bit occupies one of two mirror basins split by a saddle, and escapes by crossing a finite quasipotential barrier $\Delta V$. This separates two survivals the current alone conflates: *circulation* survival is the current not reversing ($I(0)$); *identity* survival is the system not crossing the separatrix. The separatrix, not zero current, is the boundary that matters.

model b:
The strongest part of the proposed revision is not actually the numerical value ΔV ≈ 0.018. It's the **structural claim that ΔV is born at the pitchfork/parity-breaking bifurcation and disappears when the racemic state becomes stable again.**

the μ-threshold prediction should not be phrased merely as an empirical expectation ("ΔV → 0"). It should be elevated into the actual geometric mechanism behind the structural/spontaneous distinction.

Mathematically, the reduction is standard.

Near the parity-breaking threshold, define the chiral order parameter

[
m \equiv \frac{S_L-S_R}{S_L+S_R}
]

with (m=0) the racemic state.

Because the system has exact (L\leftrightarrow R) symmetry, the deterministic normal form near threshold must be odd in (m):

[
\dot m
======

## a(\mu)m

b,m^3
+
O(m^5),
\qquad b>0.
]

The bifurcation occurs at

[
a(\mu_c)=0.
]

For (\mu<\mu_c),

[
a(\mu)<0,
]

and the racemic state is stable.

For (\mu>\mu_c),

[
a(\mu)>0,
]

and two chiral fixed points appear at

[
m_\pm
=====

\pm\sqrt{\frac{a(\mu)}{b}}.
]

The corresponding Freidlin–Wentzell quasipotential is

[
V(m)
====

-\frac{a(\mu)}{2}m^2
+
\frac{b}{4}m^4.
]

The barrier separating one chiral basin from the other is

[
\Delta V
========

# V(0)-V(m_\pm)

\frac{a(\mu)^2}{4b}.
]

Therefore

[
\Delta V
\propto
(\mu-\mu_c)^2
]

close to threshold.

This immediately gives:

[
\Delta V \to 0
\qquad\text{as}\qquad
\mu\to\mu_c^+.
]

and

[
\Delta V = 0
\qquad\text{for}\qquad
\mu\le \mu_c.
]

The Kramers escape time then becomes

[
\tau_{\rm flip}
\sim
\exp!\left(\frac{\Delta V}{\sigma^2}\right)
===========================================

\exp!\left(
\frac{C(\mu-\mu_c)^2}{\sigma^2}
\right).
]

So the spontaneous identity bit is not merely "weaker" near threshold; the basin geometry itself disappears.

---


> **Refined mechanism.** The distinction between structurally stored and spontaneously frozen chirality is not primarily a distinction of current structure but of basin geometry. A bare RPS triad possesses a protected circulation sign but no parity-symmetric competing basin; its mirror state exists only under rewiring, so no finite quasipotential barrier is defined. Coupling the triad to its opposite-handed mirror introduces an exact parity symmetry and a racemic fixed point. Above the Frank cross-inhibition threshold this racemic state becomes unstable through a parity-breaking bifurcation, creating two mirror basins separated by a Freidlin–Wentzell barrier (\Delta V). The barrier scales continuously from zero at threshold and governs identity survival through Kramers escape. In this reading, spontaneous freezing is not a different kind of chirality but a structural chirality embedded in a parity-symmetric manifold whose basin geometry permits noise-driven transitions between mirror realizations.

Then modify the prediction section:

> **μ-threshold prediction (strong form).** Let (\mu_c) denote the parity-breaking threshold. Near threshold the chiral order parameter obeys the pitchfork normal form
>
> [
> \dot m = a(\mu)m-bm^3 ,
> ]
>
> yielding a quasipotential barrier
>
> [
> \Delta V = \frac{a(\mu)^2}{4b}
> \propto (\mu-\mu_c)^2 .
> ]
>
> Therefore the identity-survival time must satisfy
>
> [
> \ln\tau_{\rm flip}
> \propto
> \frac{(\mu-\mu_c)^2}{\sigma^2}.
> ]
>
> Observation of a nonzero (\Delta V) after restoration of racemic stability, or failure of (\Delta V) to collapse continuously to zero at (\mu_c), would falsify the proposed basin-geometry mechanism.

This is a substantially stronger statement than the current draft because it converts "the barrier should vanish when symmetry is restored" from an intuition into a specific normal-form prediction with a scaling law. If your simulations already contain μ-sweeps, fitting (\Delta V(\mu)) to a quadratic near threshold would be the natural next check.

---

## μ-sweep result (run)

The μ-threshold prediction has been run (`experiments/mu_sweep.py`). The mechanism is **confirmed**; the specific normal form is **corrected**.

- **Threshold confirmed exactly.** The racemic state's parity-breaking eigenvalue `a(μ) = F(3μ−c)/(c+3μ)` (`c = 1+a+b`) crosses zero at **`μ_c = c/3 = 0.833`** (numeric `0.8337`; uniform-mode eigenvector residual `~10⁻¹¹`). `ΔV = 0` below threshold — branch survival exists only above the bifurcation. The basin-geometry mechanism is confirmed; the strong-form falsifier (nonzero `ΔV` after racemic restabilization) does **not** fire.
- **Not a pitchfork — competitive exclusion.** The order parameter `m±` does **not** follow `√(μ−μ_c)`; it **jumps** to full exclusion (`≈ 1`) immediately above threshold — the loser wiring is driven to zero. So `ΔV ∝ a(μ) ∝ (μ−μ_c)` — **linear**, not the predicted `(μ−μ_c)²` (the noisy escape MFPT tracks `a(μ)`, corr `0.98`). Model b's quadratic normal form is superseded by competitive exclusion.

This does not weaken the branch-membership reading — it sharpens it: above threshold the system is *fully* in one branch (binary occupancy), which is precisely what "branch membership" means, rather than a continuously-growing order parameter. Revised question for review: **is the competitive-exclusion (degenerate / hard-saturating) normal form, with `ΔV` linear in `(μ−μ_c)`, the correct reduction for the symmetric Lotka–Volterra L↔R competition — and does it supersede the supercritical-pitchfork derivation, or coexist with it in a different parameter regime?**
