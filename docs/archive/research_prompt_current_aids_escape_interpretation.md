# Outside-interpretation prompt — when does a rotational current lower a noise-induced escape barrier?

Self-contained dynamical-systems / large-deviations question for the outbound research channel. No
framework jargon by design — any strong applied-math / stochastic-dynamics model should be able to
engage. The returned report gets filed alongside and folded (after review) into
`character_frontier.md` (`current-aids-escape`) + `character_receipts.md` §Branch-survival barrier.

**Background it bears on.** An earlier round of this channel (`review_prompt_competitive_exclusion.md`)
analyzed a symmetric two-group competition model and *predicted*, for the non-gradient (current-carrying)
case, that "the optimal fluctuation path (the instanton) takes a curved trajectory that surfs the
rotational flow of the internal cycle, drastically reducing the action required to cross the saddle"
(i.e. the Freidlin–Wentzell barrier `ΔV` should fall as the internal current rises). We have now **tested
that prediction on two different substrates and gotten opposite answers** — confirmed on one, a clean null
on the other. We want help interpreting the *regime-dependence*, which may be the substantive finding.

---

## The phenomenon: a protected rotational current that lowers the escape barrier on one substrate but not another

I study driven-dissipative systems that are bistable under a spontaneously broken ℤ₂ symmetry: two
symmetry-related attractors (call the order parameter `m ∈ [−1,1]`, attractors at `±m*`) separated by a
symmetric saddle at `m = 0`. Each attractor also carries an **internal rotational current** — a
non-reciprocal cyclic flow (an asymmetric 3-cycle, strength set by an antisymmetry `a ≠ b`) that makes the
drift non-gradient. I can dial the current on/off *without changing the deterministic landscape* (see the
control below), and I measure how the **noise-induced escape barrier** `ΔV` (the L↔R basin crossing, by
Kramers/Freidlin–Wentzell first passage) depends on the current.

**Two substrates, same protocol, opposite results.**

### Substrate H — hard transcritical / competitive exclusion (boundary-supported attractors)

Six variables, two symmetry-related groups of three (`L`, `R`), each an internal asymmetric 3-cycle,
coupled by mutual inhibition through group totals:
```
dLᵢ/dt = Lᵢ ( F − [ Lᵢ + a·Lᵢ₊₁ + b·Lᵢ₋₁ ] − μ·S_R )
dRᵢ/dt = Rᵢ ( F − [ Rᵢ + b·Rᵢ₊₁ + a·Rᵢ₋₁ ] − μ·S_L )
```
`F=1`, `μ=1.6`, `a+b=1.5`. Above `μ_c=(1+a+b)/3` the symmetric state loses stability and the order
parameter jumps essentially to **full exclusion** `m* = ±1` (winner-take-all; the attractors sit on the
boundary of the positive orthant). The internal current is strong.

### Substrate A — soft supercritical pitchfork (interior attractors)

A Kondepudi–Nelson autocatalytic substrate (autocatalysis + finite-resource saturation + mutual
annihilation), again two mirror groups of three with an internal asymmetric 3-cycle of strength `ec`:
```
dLᵢ/dt = k₁ + (g−k_d)·Lᵢ·(1 − P/cap) − k₃·Lᵢ·S_R − ec·Lᵢ·(a·Lᵢ₊₁ + b·Lᵢ₋₁)     (P = S_L+S_R)
dRᵢ/dt = k₁ + (g−k_d)·Rᵢ·(1 − P/cap) − k₃·Rᵢ·S_L − ec·Rᵢ·(b·Rᵢ₊₁ + a·Rᵢ₋₁)     (mirror)
```
`g=0.70, k_d=0.50, k₃=1.0, cap=2.0, ec=0.15, a+b=1.5`. Here the symmetry breaks via a genuine
**supercritical pitchfork** (`m*² ∝ (k₁c−k₁)` linear; barrier `∝ m*⁴` quadratic), and the broken
attractors sit in the **interior** (`m* ≈ ±0.71`). The internal current is weak.

**The control (identical logic on both).** The internal cycle term `ec·(a·next + b·prev)` splits into a
symmetric part `∝ (a+b)` and an antisymmetric part `∝ (a−b)`. The antisymmetric part is the
divergence-free rotational current; the symmetric part contributes to the competition/saturation. Holding
`(a+b)` (and `ec`) fixed and dialing only `a−b` therefore changes **only the current**, leaving the
deterministic landscape fixed. I verify this directly: the racemic saddle's symmetry-breaking eigenvalue
(substrate H) and the full `m*(k₁)` pitchfork curve (substrate A) are **invariant to machine precision**
across the `a−b` sweep. So the only thing changing is the rotational current.

I quantify the current by the **cycle affinity** `𝒜` (nats per cycle) of the winning attractor — a
deterministic, noise-independent property of the drift, read from the winner's Jacobian in the rotation
plane (rotational-OU frame; `𝒜 = 0` when the relevant eigenvalues are real, i.e. no rotation). The escape
barrier `ΔV` is read from the noise-activated mean first-passage time, demographic (√x, birth–death) noise,
via `ln⟨τ⟩ = const + ΔV·(1/σ²)` (slope = `ΔV`); in the rare-flip regime I read the escape **rate by flip
count** rather than MFPT, because the MFPT estimator is contaminated by walkers censored at the simulation
horizon when flips are rare.

**Results.**

| substrate | mechanism | attractor `m*` | current `𝒜` range | escape barrier vs current |
|---|---|---|---|---|
| **H** (transcritical) | hard / boundary | `±1.0` (full exclusion) | `0 → 21.8` nats | `ΔV` **falls monotonically**, `0.328 → 0.295 → 0.284 → 0.272` (3.0σ, R²>0.99); barrier highest at `𝒜=0` |
| **A** (pitchfork) | soft / interior | `±0.71` | `0 → 2.3` nats | **no effect**: flip counts identical within Poisson across the whole activated window (2→127 / 1000), `𝒜=0` and `𝒜=2.3` indistinguishable |

So on **H** the rotational current demonstrably **lowers** the FW escape barrier (the predicted
instanton-surfing effect, confirmed at 3σ with the deterministic landscape held fixed). On **A** the same
protocol shows **no detectable effect** — and not merely because `𝒜` is smaller: if H's per-nat
sensitivity (`≈0.0026` in `ΔV` per nat) applied to A's `Δ𝒜 = 2.3`, the predicted barrier drop would give a
**~10× excess escape rate** at the measured noise level, whereas the observed excess is ~0 (≲0.3σ).

**The three confounds (I cannot separate them with these two substrates).** H and A differ simultaneously in
(i) **bifurcation/normal-form type** — hard transcritical vs soft supercritical pitchfork; (ii) **attractor
geometry** — boundary face (`m*=±1`, on the orthant boundary, escape path is long and runs along/near the
boundary) vs interior (`m*=±0.71`, escape path is short and interior); (iii) **current magnitude** —
`𝒜≈21.8` vs `≈2.3` nats.

---

## Questions

1. **Is current-assisted escape expected to be regime-dependent like this?** Is the lowering of the FW
   quasipotential by a solenoidal (divergence-free) drift component a *generic* feature of non-gradient
   bistable escape, or does it require a specific geometric condition — e.g. that the rotational flow be
   **aligned with the unstable direction of the escape (instanton) path**? My intuition is that on H the
   boundary-supported, full-exclusion escape path runs in a direction the 3-cycle current can "push along,"
   whereas on A the short interior path may be nearly orthogonal to the current, so the solenoidal part
   does little. Is there a principled statement of *when* a rotational current aids vs is irrelevant to
   basin escape?

2. **Is there a controlling dimensionless group?** Should the size of the effect scale with the current
   relative to the gradient/relaxation drift (a Péclet-like ratio), so that A's `𝒜≈2.3` is simply below the
   threshold where the instanton meaningfully tilts? If so, what is the right dimensionless combination,
   and roughly where is the crossover? (I want to know whether A's null is "structural" — the geometry
   forbids it — or "sub-threshold" — the current is just too weak.)

3. **How would you disentangle the three confounds cleanly?** Can you suggest a *single* substrate or a
   parameter family in which I can vary one feature at a time — e.g. move the attractors continuously from
   the boundary (`m*→1`) into the interior at fixed current and fixed bifurcation type, or hold geometry
   fixed and sweep the current through the suspected crossover? What is the minimal model that isolates the
   geometric-alignment hypothesis from the current-magnitude hypothesis?

4. **Optimal-path diagnostics.** Short of a full quasipotential solve, is there a cheaper diagnostic that
   predicts the sign/size of the effect from the deterministic data alone — e.g. the angle between the
   rotational drift `J` and the minimum-action (instanton) tangent along the escape path, or the
   antisymmetric part of the drift's Jacobian projected onto the saddle's unstable manifold? I will likely
   compute the instanton via gMAM on H (to get the exact barrier and *see* the path tilt with the flow);
   what should I measure on A to confirm whether the path is simply insensitive to its (weak) current?

5. **Rare-event estimator.** In the rare-flip regime my flip-count readout is robust but low-resolution.
   For pinning a *small* barrier difference between two nearly-identical systems (the A case), what is the
   right tool — adaptive multilevel splitting / forward-flux sampling, transition-path / committor methods,
   or direct gMAM action differences? I want a method whose null ("no barrier difference") is trustworthy,
   not just an underpowered MFPT.

6. **Literature anchors** for: the role of the antisymmetric/solenoidal drift component in the
   Freidlin–Wentzell quasipotential and when it lowers vs raises the barrier (Maier–Stein geometry of the
   optimal escape path; Bouchet/Reygner; Vanden-Eijnden/Heymann gMAM); current-assisted vs current-opposed
   noise-induced transitions in NESS; and any results on escape from boundary-supported (competitive
   -exclusion) attractors vs interior attractors.

---

<!-- returned model reports get pasted below this line, as model a / model b / model c -->

model a:
This looks much less like a contradiction than a classic "solenoidal drift is not the quasipotential" result.

The shortest version of my interpretation is:

> A rotational current does **not** generically lower the Freidlin–Wentzell barrier. It lowers the barrier only insofar as it changes the geometry of the optimal fluctuation path. If the instanton can exploit the current, ΔV falls; if the instanton is largely orthogonal to the current, the quasipotential is nearly unchanged even though the stationary state carries a nonzero circulation.

Your two substrates are almost a textbook demonstration of that distinction.

---

## 1. Why the two outcomes are not actually surprising

Write the drift as

[
f(x)= -\nabla U(x)+J(x)
]

with (J) the non-gradient (solenoidal) part.

The FW quasipotential is determined by the optimal-control problem

[
\Delta V
========

\inf
\frac12
\int_0^T
|\dot x-f(x)|^2,dt .
]

The important point is:

* (J) enters the action.
* But (J) contributes only through its projection onto the chosen path.
* A large circulation that is tangent to level sets can leave (\Delta V) almost unchanged.

This is exactly what the classic non-gradient escape papers found:

* the instanton bends,
* saddle-crossing locations can move,
* uphill and downhill trajectories separate,
* but the barrier change is highly geometry dependent.

The common intuition that "more current ⇒ lower barrier" is too strong.

A better statement is:

[
\delta \Delta V
\sim
-\int_{\gamma_*}
J\cdot \tau, ds
]

as a first geometric intuition, where (\gamma_*) is the optimal path and (\tau) its tangent.

Not literally as written, but conceptually that is the object that matters: the component of the rotational drift along the escape tube.

---

## 2. Your H substrate is almost the ideal case for current-assisted escape

The striking feature is not the current.

It is the **boundary-supported winner-take-all attractor**.

You have

[
m^*=\pm1,
]

meaning the escape trajectory must dismantle an exclusion state.

That immediately creates three ingredients that favor a current effect.

### A. Long transition tube

The path from

[
m=1
\rightarrow
m=0
]

is long in state space.

A small tangential aid accumulates over a long distance.

Even if the local projection of (J) onto the instanton is modest, the integrated effect can be substantial.

---

### B. Reduced dimensionality near the boundary

Near competitive-exclusion faces, the dynamics effectively collapse onto a lower-dimensional manifold.

The optimal path often hugs the boundary.

When this happens, the rotational 3-cycle is no longer an irrelevant transverse motion.

It becomes partially aligned with the only available route.

Then the current can genuinely "carry" the escape trajectory.

---

### C. Strong non-normality

Competitive-exclusion systems with asymmetric cycles often have large antisymmetric Jacobian components.

Those components can strongly tilt the Hamiltonian characteristics that determine the instanton.

Your observed decrease

[
0.328
\rightarrow
0.272
]

is entirely plausible in that regime.

The effect is not enormous.

It is about 17%.

That is exactly the scale I would expect from path-geometry modification rather than from a wholesale change in the underlying landscape.

---

## 3. Why A may genuinely be a null

What is most interesting in your report is not that the effect is smaller.

It is that it appears statistically absent.

That suggests something stronger than mere weakness.

### Interior pitchfork geometry

For A:

[
m^*\approx0.71
]

and both attractors lie deep in the interior.

Near a supercritical pitchfork, the effective dynamics are often well approximated by a one-dimensional amplitude equation

[
\dot m
======

\alpha m
-\beta m^3 .
]

The barrier is then essentially controlled by motion along (m).

The rotational cycle lives mostly in directions transverse to (m).

If so, the instanton has almost no reason to explore those directions.

The current simply circulates around the basin.

It does not help climb toward the saddle.

That produces exactly what you observe:

* substantial stationary circulation,
* visible affinity,
* essentially unchanged escape barrier.

In other words:

> A may be showing a regime where the current is dynamically real but asymptotically irrelevant to the large-deviation channel.

That is an interesting result, not a failed one.

---

## 4. Current magnitude vs geometric alignment

You asked whether A is "sub-threshold" or "structural."

My guess:

**mostly structural.**

The strongest clue is your back-of-the-envelope argument:

* H sensitivity ≈ (2.6\times10^{-3}) barrier units per nat.
* A reaches 2.3 nats.
* H scaling would predict an easily detectable effect.
* None appears.

That argues against a universal affinity scaling.

Affinity alone is almost certainly not the correct control parameter.

---

### Better dimensionless group

I would examine something like

[
\Pi
===

\frac{|P_\gamma J|}
{|P_\gamma f_{\rm relax}|}
]

where

* (P_\gamma) projects onto the instanton tangent,
* (f_{\rm relax}) is the restoring drift.

This measures current **along the escape channel**, not total circulation.

Two systems can have the same affinity and completely different (\Pi).

My suspicion:

[
\Pi_H \gg \Pi_A.
]

---

## 5. The cleanest discriminating experiment

You want to separate:

1. current magnitude,
2. boundary/interior geometry,
3. bifurcation type.

I would not start with another biological model.

I would build the minimal non-gradient normal form.

---

### Minimal test model

Take a pitchfork coordinate (m) plus a rotational coordinate (\theta):

[
\dot m
======

\alpha m-\beta m^3
+
\varepsilon,g(m,\theta)
]

[
\dot\theta
==========

\omega .
]

Then independently vary:

* pitchfork depth ((\alpha)),
* rotation strength ((\omega)),
* coupling ((\varepsilon)).

The crucial parameter is (\varepsilon).

If (\varepsilon=0),

the rotation exists but cannot affect escape.

If increasing (\omega) at fixed (\varepsilon) lowers the barrier, you have isolated the magnitude effect.

If increasing (\omega) does nothing until (\varepsilon) becomes appreciable, you have shown that geometric coupling—not affinity itself—is the controlling factor.

That would directly test the "alignment" hypothesis.

---

## 6. What I would measure before running gMAM

The most informative deterministic quantity is not affinity.

It is the projection of the rotational drift onto the unstable escape direction.

At the saddle compute:

[
\chi
====

\frac{
|J(x_s)\cdot e_u|
}{
|J(x_s)|
}
]

where (e_u) is the unstable eigenvector.

Interpretation:

* (\chi\approx0): current mostly transverse → little barrier effect expected.
* (\chi\approx1): current aligned with escape → strong effect possible.

Then extend this along the heteroclinic/most-likely path and integrate.

That gives a deterministic predictor of the sign.

For H I would expect substantial overlap.

For A I would not be surprised if it is nearly zero everywhere.

---

## 7. What gMAM is likely to show

If your interpretation is correct:

### H

As affinity increases:

* instanton visibly bends,
* path acquires circulation,
* action decreases.

You should literally see the path "surfing" the cycle.

---

### A

As affinity increases:

* instanton remains nearly unchanged,
* path remains almost one-dimensional in the order parameter,
* action changes only at higher order.

That would make the null result mechanistically transparent.

---

## 8. Estimator choice

For the A case I would stop relying on direct rare-flip counting.

The best return on effort is probably:

1. gMAM (direct action difference),
2. adaptive multilevel splitting (AMS) as an independent check.

AMS is excellent for resolving small differences between nearly identical rare-event systems.

If gMAM predicts

[
\Delta(\Delta V)\approx0,
]

and AMS sees no statistically significant rate ratio, that is a very strong null.

Forward-flux sampling is also reasonable, but for your specific question—tiny action differences between two closely related drifts—the combination of gMAM plus AMS is hard to beat.

---

My overall read is that the most likely emerging principle is not

> "rotational current lowers barriers"

but rather

> "rotational current lowers barriers only when it has substantial projection onto the large-deviation escape channel."

The H/A pair is exactly the sort of evidence that would push me toward that stronger geometric formulation. H appears to satisfy the alignment condition; A appears not to. If future gMAM calculations show a strongly tilted instanton in H and an essentially unchanged instanton in A, that would be a remarkably clean confirmation of the hypothesis.

model b:
This is a fascinating set of results. The fact that you have isolated the rotational current while holding the deterministic landscape (and specifically the symmetry-breaking eigenvalue) invariant to machine precision gives you an incredibly clean controlled experiment. As an AI, I don’t run my own wet-labs or simulations, but I can help you parse the dynamical systems theory, the macroscopic fluctuation theory, and the stochastic thermodynamics at play here.

Your instincts about the geometry of the escape path are spot on. The divergence between Substrate H and Substrate A is almost certainly a structural consequence of how the Freidlin–Wentzell (FW) instanton interacts with the solenoidal (divergence-free) component of the drift in different geometries.

Here is a breakdown of why this regime-dependence occurs, how to quantify it, and how to disentangle the confounds.

---

### 1. Regime Dependence: Alignment vs. Irrelevance

Current-assisted escape is highly regime-dependent. The lowering of the FW quasipotential by a solenoidal drift is **not generic**; it is strictly governed by the geometric alignment between the solenoidal field and the gradient (relaxation) field.

In a purely gradient system ($\dot{x} = -\nabla U$), the optimal escape path (the instanton) is exactly the time-reversed deterministic relaxation path from the saddle to the attractor. When you add a solenoidal rotational field $l(x)$, the drift becomes non-gradient: $f(x) = -\nabla U(x) + l(x)$. The instanton must now deviate from the time-reversed relaxation path to minimize the FW action functional:


$$S_T = \frac{1}{2} \int_0^T || \dot{x} - f(x) ||^2 dt$$

* **Substrate H (Boundary/Transcritical):** The attractors are pinned at the boundary of the positive orthant. The deterministic relaxation path from the saddle to the attractor likely follows the edges of this boundary. If the 3-cycle current generates a flow that runs "along" or parallel to this boundary, the instanton can wildly deviate into the interior to "surf" the current on the way back up to the saddle. The solenoidal flow performs positive work along this curved path, sharply reducing $\Delta V$.
* **Substrate A (Interior/Pitchfork):** The attractors are in the interior, and the escape path is short. Near a soft supercritical pitchfork, the dominant dynamic is the relaxation along the 1D slow manifold connecting the attractors through the saddle. In this region, a rotational flow is typically **transverse** (orthogonal) to the slow manifold. If the current is perfectly orthogonal to the unperturbed path, the first-order perturbation to the FW action is zero. The instanton is simply too short and constrained to build a "detour" that harvests the weak rotational current.

### 2. The Controlling Dimensionless Group

The structural null in Substrate A is likely a combination of both geometry *and* being sub-threshold. The controlling dimensionless group here is the ratio of the rotational flow timescale to the deterministic relaxation timescale along the escape path.

You can define a local **Péclet-like rotational number** ($\text{Pe}_{rot}$):


$$\text{Pe}_{rot} = \frac{\omega}{\lambda_+}$$


Where $\omega$ is the characteristic angular frequency of the rotational current (proportional to your cycle affinity $\mathcal{A}$) and $\lambda_+$ is the unstable eigenvalue of the saddle (the relaxation rate down the manifold).

If $\text{Pe}_{rot} \ll 1$, the pull of the gradient field overwhelmingly dominates. The instanton remains stiff and straight, the transverse current is integrated out, and the barrier reduction scales as $\mathcal{O}(\text{Pe}_{rot}^2)$—effectively invisible in your flip-count data. If $\text{Pe}_{rot} \gtrsim 1$, the instanton snaps, bends into the flow, and you get an $\mathcal{O}(\text{Pe}_{rot})$ reduction in $\Delta V$, as seen in Substrate H.

### 3. Disentangling the Confounds

To isolate the geometric-alignment hypothesis from the current-magnitude hypothesis, you need a single continuous model. I recommend modifying **Substrate H** by introducing a tunable interior-pulling term.

Take your standard mutual inhibition model and add a weak, saturating self-limitation (a generalized Allee effect or carrying capacity) that pulls the attractors off the boundary $\pm \mathbf{1}$ and into the interior, without changing the network topology:


$$dL_i/dt = L_i ( F - [ L_i + a \cdot L_{i+1} + b \cdot L_{i-1} ] - \mu \cdot S_R ) - \kappa L_i^3$$


By dialing $\kappa$ from **0** (boundary attractors, hard exclusion) to a larger positive value (interior attractors, soft competition), you can continuously sweep the attractor location $m^*$ from **1.0** to **0.5** while holding the asymmetric cyclic strength ($a-b$) fixed.

### 4. Optimal-Path Diagnostics

You do not need a full gMAM solve to predict the sign and magnitude of the effect. You can use first-order perturbation theory on the unperturbed (purely symmetric) deterministic path.

1. Set $a = b$ so the drift is purely symmetric (gradient-like).
2. Compute the deterministic heteroclinic trajectory $x_0(t)$ from the saddle to the attractor.
3. Calculate the purely solenoidal field $l(x)$ by taking the difference between your full drift field and the symmetric drift field.
4. Compute the line integral of the solenoidal field along the unperturbed path:

$$W = \int l(x_0) \cdot dx_0$$



If this "work" integral $W \approx 0$, the rotational current is orthogonal to the escape path, and the first-order barrier reduction will be strictly zero (Substrate A's null). If $W$ is large, the current aligns with the path, and you will see a first-order drop in $\Delta V$ (Substrate H).

### 5. Rare-Event Estimators

For Substrate A, your flip counts are underpowered to detect an $\mathcal{O}(\text{Pe}_{rot}^2)$ barrier difference.

* **Do not use MFPT or flip-counts** for resolving micro-differences in barriers; the variance from the Poisson statistics will always swallow the signal.
* **Adaptive Multilevel Splitting (AMS):** This is the gold standard for continuous-time, high-dimensional stochastic trajectories. It is strictly superior to Forward-Flux Sampling (FFS) here because it does not require you to pre-define stiff intermediate interfaces, which is crucial when the rotational current is actively twisting the optimal path.
* **Direct gMAM:** Honestly, if you want a trustworthy null, compute the gMAM action for Substrate A at $\mathcal{A}=0$ and $\mathcal{A}=2.3$. It removes the noise parameter entirely and yields the deterministic $T \to \infty$ zero-noise action. If gMAM shows $\Delta S < 10^{-4}$, you have your definitive "structural null."

### 6. Literature Anchors

* **Maier and Stein (1993, 1997):** Their seminal papers on escape in non-gradient systems are exactly what you need. They describe how the instanton "bows out" to exploit the transverse/solenoidal field. Look specifically at *Escape problem for irreversible systems* (1993).
* **Bouchet and Reygner (2016):** *Generalisation of the Eyring-Kramers Transition Rate Formula to Irreversible Diffusion Processes*. They rigorously treat the solenoidal component's contribution to the prefactor and the FW action.
* **Vanden-Eijnden and Heymann (2008):** *The geometric minimum action method: A least action principle on the space of curves*. Essential reading for understanding why the geometric (reparameterized) formulation allows the path to bend independently of the time-parameterization.
* **Ping Ao (2004):** *Potential in stochastic dynamics and its gauge field*. Details the orthogonal decomposition of stochastic drift into gradient and divergenceless (solenoidal) components.

---

Have you already attempted to extract the unperturbed deterministic heteroclinic connection for Substrate A to check if the rotational field is, in fact, perfectly orthogonal to the slow manifold?
model c:
I'll analyze this research prompt carefully. It's a sophisticated dynamical systems/stochastic dynamics question about when rotational currents lower noise-induced escape barriers in non-gradient systems. Let me search for relevant literature and then provide a thorough
  
  
     
 Now I have gathered substantial literature. Let me synthesize a comprehensive research report addressing all six questions in the prompt.

---

## Research Report: Regime-Dependence of Rotational-Current-Assisted Noise-Induced Escape

### Executive Summary

The observed regime-dependence — barrier lowering on substrate H (hard transcritical/boundary) but no effect on substrate A (soft pitchfork/interior) — is **expected and principled**, not anomalous. The effect is governed by the **alignment geometry** between the instanton escape path and the rotational drift, modulated by a Péclet-like dimensionless group comparing current strength to gradient relaxation. The three confounds (bifurcation type, attractor geometry, current magnitude) can be disentangled through a controlled parameter family. Below I address each question systematically.

---

### 1. Is Current-Assisted Escape Expected to Be Regime-Dependent?

**Yes — and the geometry of alignment is the controlling principle.**

The Freidlin–Wentzell quasipotential $V(x_1, x_2) = \inf_{T>0} \inf_{\varphi} S_T[\varphi]$ is constructed from the action functional:

$$S_T[\varphi] = \int_0^T \|\dot{\varphi}(t) - b(\varphi(t))\|^2 \, dt$$

For a drift decomposition $b(x) = -\nabla U(x) + J(x)$ where $J$ is the solenoidal (rotational, divergence-free) component, the instanton equation in the Hamiltonian picture reads:

$$\dot{\varphi} = b(\varphi) + p = -\nabla U(\varphi) + J(\varphi) + p$$

where $p$ is the conjugate momentum (the "noise force"). The key insight from the orthogonal decomposition literature is that **the instanton follows the rotational component** $J$ **but goes against the potential component** $-\nabla U$ .

This means the instanton path is *tilted* by the rotational flow. Whether this tilt reduces the action (barrier) depends on whether the rotational flow pushes the trajectory **toward** the saddle/escape gateway or **away from it** — i.e., whether $J$ has a component **aligned with the unstable direction** of the escape path.

**Your geometric-alignment intuition is correct:**

- **Substrate H (boundary, $m^* = \pm 1$):** The escape path from a boundary-supported attractor is long, running along/near the boundary face. The 3-cycle current circulates *within* the winning group's simplex, and the escape toward the symmetric saddle involves motion that the current can "push along" — the rotational flow has a significant projection onto the escape tangent. The instanton "surfs" the current, reducing the required noise force $p$ and thus the action.

- **Substrate A (interior, $m^* = \pm 0.71$):** The escape path is short and direct through the interior. The weak 3-cycle current (𝒜 ≈ 2.3 nats vs. 21.8) circulates in a plane nearly **orthogonal** to the escape direction (which is primarily along the order-parameter axis $m$). The instanton receives little assistance; the solenoidal component does negligible work along the escape path.

**Principled statement:** A rotational current lowers the FW barrier **if and only if** the current has a positive projection onto the instanton tangent vector field along the escape path — specifically, when $\int_{\text{path}} J(\varphi) \cdot \dot{\varphi} \, ds > 0$ in a sense that reduces the required $p \cdot \dot{\varphi}$. If $J \perp \dot{\varphi}$ everywhere along the path, the current is geometrically irrelevant to the escape action.

This is consistent with the Maier–Stein model results: when the non-gradient parameter $\beta \gg 1$, the instanton deviates significantly from the heteroclinic orbit, "surfing" the rotational flow to reduce action; when $\beta \approx 1$ (gradient limit), the instanton coincides with the heteroclinic and the rotational component vanishes .

---

### 2. Is There a Controlling Dimensionless Group?

**Yes — a Péclet-like number governing the "instanton tilt."**

The natural dimensionless group is the **ratio of rotational drift to gradient relaxation** along the relevant escape direction. Define:

$$\Pi = \frac{|J_{\parallel}|}{|\nabla U|_{\text{eff}}} \cdot \frac{L_{\text{rot}}}{L_{\text{esc}}}$$

where:
- $|J_{\parallel}|$ = projection of rotational current onto the escape path tangent
- $|\nabla U|_{\text{eff}}$ = effective gradient strength (barrier height / escape distance)
- $L_{\text{rot}}$ = characteristic length scale of rotational circulation
- $L_{\text{esc}}$ = characteristic escape path length

Alternatively, in terms of your measured quantities:

$$\Pi \sim \frac{\mathcal{A}}{\Delta V_{\text{grad}}} \cdot \frac{\lambda_{\text{rot}}}{\lambda_{\text{unstable}}}$$

where $\mathcal{A}$ is the cycle affinity (nats/cycle), $\Delta V_{\text{grad}}$ is the gradient-only barrier, and $\lambda_{\text{rot}}/\lambda_{\text{unstable}}$ compares the rotational eigenvalue to the saddle's unstable eigenvalue.

**For your substrates:**

| Substrate | $\mathcal{A}$ | $\Delta V$ | Path geometry | $\Pi$ (estimated) | Effect |
|-----------|--------------|------------|---------------|-------------------|--------|
| **H** | 21.8 | 0.328 | Long, boundary-aligned, current-parallel | $\gg 1$ | Strong barrier reduction |
| **A** | 2.3 | $\sim$0.1 (interior, soft) | Short, interior, current-orthogonal | $\ll 1$ | No detectable effect |

**Crossover prediction:** The effect becomes significant when $\Pi \gtrsim 1$, i.e., when the rotational current can advect the system a distance comparable to the escape path length during one relaxation time. For substrate A, even if you increased $\mathcal{A}$ to match H's 21.8 nats, the **geometric orthogonality** (short interior path vs. circulating current) would still suppress the effect — suggesting the null on A is **structural** (geometry forbids it) rather than merely **sub-threshold** (current too weak).

However, you cannot definitively separate these with only two substrates. A's $\mathcal{A} = 2.3$ may also be below threshold even if geometry were favorable. The controlled experiment in Question 3 resolves this.

---

### 3. How to Disentangle the Three Confounds Cleanly

**Proposed minimal model: A tunable 4-parameter family that isolates geometry from current magnitude.**

Take a **generalized Lotka–Volterra competitive system** with $N$ species in two groups, or better: a **reduced-order effective model** in the $(m, c)$ plane where $m$ is the order parameter and $c$ is a "circulation coordinate" capturing the internal 3-cycle phase.

**Minimal model suggestion:**

$$\dot{m} = -\partial_m U(m; \mu) + \epsilon J_m(m, c)$$
$$\dot{c} = \omega(m) + \epsilon J_c(m, c)$$

where:
- $U(m; \mu)$ is a tunable potential: transcritical-like ($U \sim -|m|^3$ near 0) for boundary behavior, or pitchfork-like ($U \sim m^4$) for interior behavior
- $\mu$ controls attractor location: $m^* \in [0.5, 0.99]$ (interior → boundary)
- $\epsilon$ controls current strength independently
- $J = (J_m, J_c)$ is divergence-free, with $J_m$ controllable to test alignment

**Specific protocol to isolate each confound:**

| Experiment | Vary | Hold Fixed | Tests |
|------------|------|------------|-------|
| **(a) Geometry sweep** | $m^*$ from 0.6 → 0.99 (move attractor toward boundary) | Bifurcation type (keep pitchfork), $\mathcal{A}$ fixed | Is boundary geometry sufficient? |
| **(b) Bifurcation type** | Potential shape: $U \sim m^4$ vs. $U \sim |m|^3$ | $m^*$, $\mathcal{A}$, geometry | Is transcritical vs. pitchfork the difference? |
| **(c) Current magnitude** | $\mathcal{A}$ from 0 → 25 | Geometry, bifurcation type | Is there a threshold $\mathcal{A}_c$? |

**Implementation on your existing substrates:**

On **substrate A**, you can artificially push the attractor toward the boundary by increasing $k_1$ (the inflow) or reducing $cap$ — but this changes the bifurcation type. Instead, **add a symmetry-breaking field** $h$ (like an external bias) that tilts the pitchfork into an imperfect bifurcation, moving $m^*$ toward $\pm 1$ while keeping the supercritical structure. Then measure $\Delta V$ vs. $\mathcal{A}$ at fixed $m^*$.

On **substrate H**, you can soften the transcritical by adding a saturating term that rounds the boundary, making attractors interior at $m^* \approx \pm 0.7$.

**The critical test:** If you move substrate A's attractor to $m^* = 0.9$ (near boundary) at fixed $\mathcal{A} = 2.3$ and see barrier reduction appear, the effect is **geometric**. If you increase $\mathcal{A}$ on A at fixed $m^* = 0.71$ and see no effect until $\mathcal{A} \sim 10$, it's **sub-threshold**. If neither works, the **bifurcation type** (hard vs. soft) matters via the barrier's structural dependence on $m^*$.

---

### 4. Optimal-Path Diagnostics Without Full Quasipotential Solve

**Yes — several cheap deterministic diagnostics predict the sign/size of the effect.**

**Diagnostic 1: Alignment angle $\theta(s)$ along the heteroclinic orbit**

Compute the deterministic relaxation path from the saddle to the attractor (the heteroclinic orbit $\gamma_{\text{det}}(s)$). At each point, compute:

$$\cos\theta(s) = \frac{J(\gamma(s)) \cdot \dot{\gamma}_{\text{esc}}(s)}{|J||\dot{\gamma}_{\text{esc}}|}$$

where $\dot{\gamma}_{\text{esc}}$ is the tangent to the *reverse* path (attractor → saddle, the escape direction). The **instanton surfing index**:

$$\mathcal{S} = \int_0^1 \cos\theta(s) \, |J(\gamma(s))| \, ds \Big/ \int_0^1 |\nabla U(\gamma(s))| \, ds$$

If $\mathcal{S} > 0$ and large, expect barrier reduction. If $\mathcal{S} \approx 0$, expect null effect. This requires only the deterministic drift, no stochastic simulation.

**Diagnostic 2: Saddle unstable-manifold projection**

At the saddle point $x_s$, compute the unstable eigenvector $e_u$ (the escape direction). Project the rotational current:

$$\mathcal{P} = \frac{J(x_s) \cdot e_u}{|e_u|}$$

If $\mathcal{P} > 0$, the current pushes *out* of the basin at the saddle, assisting escape. If $\mathcal{P} \approx 0$, no assistance. This is the **linearized alignment predictor**.

**Diagnostic 3: gMAM on H, then compare to A**

Run gMAM on substrate H at two $\mathcal{A}$ values (0 and 21.8). Measure:
- The action difference $\Delta S = S_{\mathcal{A}=0} - S_{\mathcal{A}=21.8}$
- The path deflection angle $\delta\theta$ between the two instantons

Then on substrate A, compute the **same** diagnostics from the deterministic data alone (Diagnostics 1 & 2). If the alignment angle on A is $\sim 90°$ (orthogonal) while on H it's $\sim 0°$ (parallel), this confirms the geometric hypothesis.

**What to measure on A to confirm insensitivity:**

Compute the **instanton-equation residual** with the current turned off: if the heteroclinic orbit already satisfies the instanton equation to good approximation (i.e., $p \approx 0$ along the path), then adding weak current cannot significantly improve (lower) the action. The current is "prey to diminishing returns" — the path is already optimal without it.

---

### 5. Rare-Event Estimator for Small Barrier Differences

**For pinning a small $\Delta V$ difference on substrate A, use gMAM action differences directly, not MFPT or flip counts.**

Your current flip-count readout has Poisson noise $\sim \sqrt{N_{\text{flips}}}$. For rare flips (2–127 per 1000 trials), the relative error on the rate is $\sim 1/\sqrt{N_{\text{flips}}}$, making it impossible to resolve a $\sim 10\%$ barrier difference (which would give only $\sim 10\%$ rate change, buried in noise).

**Recommended hierarchy:**

1. **Best: Direct gMAM action comparison** — Compute the geometric action $S[\varphi^*]$ for the instanton at $\mathcal{A}=0$ and $\mathcal{A}=2.3$. The action difference $\Delta S$ *is* the barrier difference $\Delta V$ (up to the noise strength factor). This is deterministic, noise-free, and gives a trustworthy null: if the two actions agree to machine precision, the barrier is genuinely invariant. 

2. **Second: Adaptive Multilevel Splitting (AMS)** — If you need the actual rate (including prefactor), AMS splits trajectories at interfaces, giving unbiased rate estimates with controlled variance. It works for non-equilibrium systems without detailed balance. 

3. **Third: Forward-Flux Sampling (FFS)** — Similar to AMS but uses forward-only integration, making it robust for non-reversible systems. FFPilot optimizes interface placement to control sampling error. 

4. **Avoid: MFPT estimators** in the rare-flip regime — censored walkers at the simulation horizon bias the estimator downward, and the variance is dominated by the tail.

**Specific recommendation for A:** Run gMAM (or sgMAM) from the attractor to the saddle at $\mathcal{A}=0$ and $\mathcal{A}=2.3$. If the actions differ by $< 10^{-4}$ (relative), you have a trustworthy null at the quasipotential level. If you also need the prefactor, follow with a short AMS run seeded by the gMAM paths.

---

### 6. Literature Anchors

**Freidlin–Wentzell quasipotential & solenoidal drift:**

- **Santolin, Freitas, Esposito & Falasco (2024):** Bridge FW theory with stochastic thermodynamics; derive iterative expansion of quasipotential around detailed-balance solution; prove escape rate is bounded by dissipation along instanton and relaxation paths. Key: the orthogonal decomposition $b = -a\nabla V + l$ with $\langle l, \nabla V \rangle = 0$ .

- **Grigorio et al. (2024):** Use SINDy to learn the orthogonal decomposition from a single instanton trajectory; show the rotational component $l(x)$ is the correction to exponential decay of transition rates .

**Eyring–Kramers prefactor for non-reversible systems:**

- **Bouchet & Reygner (2016):** Generalize EK formula to irreversible diffusion; prefactor includes correction for non-Gibbsianness along the instanton. The quasipotential replaces the potential; the prefactor depends on the drift divergence at the saddle .

**gMAM / instanton computation:**

- **Heymann & Vanden-Eijnden (2008):** Original gMAM paper; reformulates action on space of curves; tests on Maier–Stein model showing instanton deviation from heteroclinic as non-gradient parameter increases .

- **Grafke, Schäfer & Vanden-Eijnden (2017):** Simplified gMAM (sgMAM) requiring only first-order Hamiltonian derivatives; applied to Maier–Stein, Allen–Cahn, Burgers–Huxley, etc. .

- **Simonnet et al. (2022):** Deep gMAM using neural networks; emphasizes that in non-gradient systems, instantons need not cross saddle points, and multiple instantons with different actions can exist .

**Macroscopic Fluctuation Theory (Bertini–De Sole–Gabrielli–Jona-Lasinio–Landim):**

- **Bertini et al. (2015):** Reviews MFT; quasipotential as natural extension of availability; Hamilton–Jacobi equation for non-equilibrium steady states; symmetric/antisymmetric current decomposition .

**Rare-event sampling methods:**

- **Allen, Frenkel & ten Wolde (2006):** Original FFS for non-equilibrium systems .

- **Berryman & Schilling (2010):** FFS for nonstationary systems .

- **Cérou & Guyader (2007); Lelièvre et al.:** Adaptive Multilevel Splitting (AMS); unbiased estimators for non-normalized quantities; non-intrusive .

**Stochastic thermodynamics & cycle affinity:**

- **Falasco et al. (2025):** Macroscopic stochastic thermodynamics; connects dissipation along deterministic and escape trajectories to FW quasipotential .

- **Gaspard & Andrieux:** Schnakenberg network theory; cycle affinities as global thermodynamic forces .

---

### Bottom-Line Interpretation

Your result is **not contradictory** — it reveals a **geometric selection rule** for current-assisted escape:

> **The solenoidal drift lowers the FW barrier only when the rotational current has a non-zero projection onto the instanton escape path. On boundary-supported attractors with long escape trajectories, the internal cycle can "surf" the escape; on interior attractors with short, direct escape paths, the current is geometrically decoupled from the escape mode.**

The regime-dependence is the substantive finding. The three confounds are disentangled by a geometry sweep at fixed current (Question 3a), which I predict will show barrier reduction emerging as $m^* \to 1$ even at weak $\mathcal{A}$.
