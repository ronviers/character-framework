# Outside-review prompt — competitive exclusion vs supercritical pitchfork

Self-contained dynamical-systems / large-deviations question for the outbound research channel. No
framework jargon by design — any strong applied-math model should be able to engage. The returned
report gets filed alongside and folded into `character_receipts.md` §Branch-survival barrier (the open
review question) + the `ΔV/ΔU` prefactor item in the handoff.

Background it bears on: the homochiral / twin-cycle branch-survival result — `μ_c=(1+a+b)/3=0.833`, the
order parameter jumps (competitive exclusion), `ΔV∝(μ−μ_c)` linear (not the pitchfork `(μ−μ_c)²`), and
the handedness-blindness of `a(μ)` across parity/exchange (`twin_mu_sweep.py`).

---

## Competitive exclusion vs. supercritical pitchfork in a symmetric, parity-related Lotka–Volterra competition — and the Freidlin–Wentzell barrier scaling

I have a deterministic-plus-noise dynamical model with a spontaneously broken ℤ₂ symmetry and I want a
rigorous check on (i) the bifurcation type, (ii) the noise-activated barrier scaling, and (iii) the right
way to pin the large-deviation prefactor.

**Model.** Six variables in two symmetry-related groups of three, `L = (L₀,L₁,L₂)` and `R = (R₀,R₁,R₂)`,
indices mod 3, with `S_L = ΣLᵢ`, `S_R = ΣRᵢ`:

```
dLᵢ/dt = Lᵢ ( F − [ Lᵢ + a·Lᵢ₊₁ + b·Lᵢ₋₁ ] − μ·S_R )
dRᵢ/dt = Rᵢ ( F − [ Rᵢ + b·Rᵢ₊₁ + a·Rᵢ₋₁ ] − μ·S_L )
```

Parameters `F = 1`, `a = 0.5`, `b = 1`, `μ ≥ 0`; let `c ≡ 1+a+b = 2.5`. Each group is an internal
asymmetric 3-cycle (a≠b); the two groups inhibit each other through their totals. The `R` group swaps
`a↔b` — i.e. it is the mirror of `L` (parity). A co-handed variant (both groups use `a·next + b·prev`, an
exchange/permutation symmetry instead of mirror) gives identical results for everything below.

**What I observe (deterministic + noisy, `dx = drift·dt + σ·dW`).**
- The symmetric ("racemic") fixed point has all six components equal to `x* = F/(c+3μ)`.
- Its symmetry-breaking mode (uniform `L−R`) has eigenvalue `a(μ) = F(3μ−c)/(c+3μ)`, crossing zero at
  `μ_c = c/3 ≈ 0.833`.
- Below `μ_c`: one symmetric basin, no broken state.
- Above `μ_c`: the order parameter `m = (S_L−S_R)/(S_L+S_R)` jumps essentially to ±1 (winner-take-all /
  competitive exclusion) — it does **not** grow as `√(μ−μ_c)`.
- The noise-activated barrier `ΔV` for an `L↔R` basin crossing scales **linearly**, `ΔV ∝ (μ−μ_c)`,
  tracking the deterministic `ΔU = a(μ)·m²/4` with `m` pinned at full exclusion — **not** the
  supercritical-pitchfork `ΔV ∝ (μ−μ_c)²`.
- `a(μ)` and `μ_c` are identical to machine precision whether the two groups are mirror images (parity)
  or identical copies (exchange), because the breaking mode is uniform within each group and blind to the
  internal cyclic structure.

**Questions.**
1. Is winner-take-all competitive exclusion the correct generic reduction for this symmetric two-group LV
   competition above the coexistence-instability threshold, or is there a parameter regime where a genuine
   **supercritical pitchfork** (soft, continuous `|m| ∝ √(μ−μ_c)`) appears? I know bare symmetric 2-species
   LV competition (`ẋ=x(1−x−αy)`, `ẏ=y(1−y−αx)`) is bistable/winner-take-all for `α>1` with a degenerate
   (transcritical-like) transition at `α=1` — does the internal 3-cycle structure, or near-threshold
   coupling to the internal modes, change that picture?
2. Is the **linear** `ΔV ∝ (μ−μ_c)` the right Freidlin–Wentzell quasipotential scaling here (a degenerate /
   hard-saturating normal form), or is the quadratic pitchfork scaling recoverable in some limit?
3. **FW barrier vs. deterministic potential.** My noisy escape-MFPT gives `ln(MFPT) ∝ ΔU` but with a slope
   (≈7.5) far below `1/σ²` (≈156) in the shallow-barrier regime — i.e. the true FW barrier ≠ the
   deterministic `ΔU`. For a non-gradient (genuinely non-equilibrium, NESS) system like this, what is the
   correct way to compute / pin the FW-barrier prefactor?
4. **Literature anchors** you would point me to: symmetric LV competition normal forms and the
   competitive-exclusion-vs-coexistence bifurcation type; May–Leonard; replicator / payoff-symmetric
   dynamics; Kondepudi–Frank chiral symmetry breaking; and large-deviation barriers for noise-induced
   transitions between symmetry-related attractors.

model a:
Short version: what you are seeing is exactly what I would expect from a symmetric Lotka–Volterra competition system whose post-threshold attractors lie on (or very near) the boundary of the positive orthant. The key issue is that the symmetry-breaking instability and the eventual saturation mechanism are not the same thing. The linear FW barrier scaling is a strong hint that the broken branches are already essentially at full exclusion when they first become dynamically admissible.

---

# 1. Is this a pitchfork or competitive exclusion?

The first thing to separate is:

* **local bifurcation of the symmetric fixed point**
* **global geometry of the attracting branches**

Your calculation of the symmetry mode is straightforward:

[
x^*=\frac{F}{c+3\mu},
\qquad
a(\mu)=\frac{F(3\mu-c)}{c+3\mu},
]

with

[
\mu_c=\frac c3.
]

The crossing of a single (L\leftrightarrow R)-odd eigenvalue through zero in a (\mathbb Z_2)-equivariant system means that the center-manifold normal form is generically

[
\dot m
======

## a(\mu)m

b,m^3
+
O(m^5).
]

That is the standard pitchfork normal form.

The question is whether the cubic coefficient (b) is finite and positive.

If (b>0), then

[
|m_*|
\sim
\sqrt{\frac{a}{b}}
\sim
\sqrt{\mu-\mu_c},
]

and one obtains a genuine supercritical pitchfork.

---

## Why you are instead seeing (m\approx\pm1)

Your system has a very special property:

[
\dot L_i
========

L_i(\cdots),
\qquad
\dot R_i
========

R_i(\cdots),
]

so every coordinate hyperplane is invariant.

Once one group wins, the other is driven toward the boundary

[
R_i=0
]

or

[
L_i=0.
]

Those boundary equilibria are exact solutions.

The broken states therefore naturally live on the faces of the positive orthant.

This is precisely the same mechanism as classical symmetric LV competition

[
\dot x=x(1-x-\alpha y),
\qquad
\dot y=y(1-y-\alpha x).
]

For (\alpha>1),

[
(1,0),,(0,1)
]

are the attractors and coexistence is unstable.

There is no small-amplitude branch.

The order parameter jumps rapidly toward

[
m=\pm1.
]

That is the winner-take-all regime.

---

## Does the 3-cycle rescue a soft pitchfork?

Not generically.

Your internal cyclic structure affects the stable transverse modes.

However, your unstable symmetry mode is

[
(L_i-R_i)\propto(1,1,1),
]

which is uniform within each group.

Therefore the instability does not "see" the cyclic orientation at linear order.

That explains why parity-related and exchange-related versions give identical

[
a(\mu)
]

and identical

[
\mu_c.
]

The internal modes only matter if they become nearly critical simultaneously.

In center-manifold language:

[
\dot m
======

## a m

b m^3
+
\sum_j c_j m q_j + \cdots
]

with (q_j) internal modes.

If every (q_j) remains strongly stable at (\mu_c), they can be slaved away and merely renormalize (b).

Then you recover ordinary LV competition.

So the answer to Question 1 is:

> The local codimension-one symmetry-breaking bifurcation is mathematically a pitchfork, but the physically relevant attracting branches can immediately run into boundary-supported competitive-exclusion states. In that regime the observable order parameter behaves as winner-take-all rather than as a soft (\sqrt{\mu-\mu_c}) pitchfork.

The way to obtain a genuine soft pitchfork is to modify the nonlinear saturation so that both groups remain positive after bifurcation. In ecology this corresponds to coexistence-preserving competition rather than exclusion.

---

# 2. Why does the FW barrier scale linearly?

This is the most interesting part.

For the canonical supercritical pitchfork

[
\dot m
======

## a m

b m^3,
]

the effective potential is

[
U(m)
====

-\frac a2 m^2
+
\frac b4 m^4.
]

The minima occur at

[
m_*=\pm\sqrt{\frac ab}.
]

The barrier is

[
\Delta U
========

\frac{a^2}{4b}.
]

Hence

[
\Delta U
\propto
(\mu-\mu_c)^2.
]

That quadratic law is universal for a soft pitchfork.

---

In your simulations the minima are essentially fixed at

[
m=\pm1.
]

Then

[
\Delta U
\approx
\frac a2
]

(up to conventions).

Since

[
a(\mu)
\sim
\mu-\mu_c,
]

you obtain

[
\Delta U
\propto
(\mu-\mu_c).
]

Therefore the observed linear scaling is exactly what one expects when the branch amplitude does not scale as (\sqrt{\mu-\mu_c}) but instead remains (O(1)).

So:

* soft pitchfork → quadratic barrier;
* hard-saturating exclusion branch → linear barrier.

Your numerical observation is internally consistent.

---

# 3. Why is the MFPT slope not (1/\sigma^2)?

Because in a non-gradient system the deterministic "potential" is not the FW quasipotential.

For

[
dx=f(x),dt+\sigma,dW,
]

with isotropic additive noise,

Freidlin–Wentzell gives

[
\text{MFPT}
\asymp
A,
\exp!\left(
\frac{\Delta V}{\sigma^2}
\right),
]

where

[
\Delta V
]

is the quasipotential.

Only for gradient systems

[
f=-\nabla U
]

does

[
\Delta V
========

2\Delta U
]

(up to convention).

For a genuine NESS,

[
f=-D\nabla\Phi + J,
]

with

[
\nabla!\cdot J=0,
\qquad
J\neq0,
]

the rotational component (J) changes the optimal escape trajectory.

The escape path is not the time-reverse of deterministic relaxation.

Consequently

[
\Delta V \neq \Delta U.
]

The ratio

[
\frac{\Delta V}{\Delta U}
]

can easily be much smaller than one.

That is exactly the situation suggested by your factor

[
7.5
\quad\text{vs}\quad
156.
]

The discrepancy is too large to be a prefactor issue alone.

It points to

[
\Delta V \ll \Delta U.
]

---

## How to compute the actual FW barrier

The correct object is the minimum action

[
\Delta V
========

\inf_{\phi}
\frac12
\int_0^T
|\dot\phi-f(\phi)|^2,dt .
]

The minimizer is the instanton (minimum-action path).

Standard numerical methods are:

* geometric minimum action method (gMAM),
* adaptive minimum action method,
* string methods,
* ordered-upwind/Hamilton–Jacobi solvers.

For your six-dimensional system, gMAM is probably the cleanest route.

Then

[
\ln(\mathrm{MFPT})
==================

\frac{\Delta V}{\sigma^2}
+
\ln A
+
o(1).
]

The slope determines (\Delta V); the prefactor only affects the intercept.

Therefore a slope mismatch by a factor of ~20 is not something the Kramers prefactor fixes.

It means the barrier itself differs.

---

# 4. Relation to parity versus exchange symmetry

Your observation is expected.

The unstable mode is

[
(1,1,1,-1,-1,-1).
]

That vector lives entirely in the subspace of group totals

[
(S_L,S_R).
]

The distinction

[
(a,b)
\leftrightarrow
(b,a)
]

exists only inside the internal cyclic modes.

Therefore

[
\mu_c
]

and

[
a(\mu)
]

must coincide for the parity and exchange constructions.

The difference could only appear through nonlinear center-manifold coefficients or through noise-induced effects involving the internal modes.

The onset itself is blind to chirality.

---

# Literature anchors

For the deterministic bifurcation side:

* James D. Murray, *Mathematical Biology* (competition and LV bifurcations).
* Robert M. May and Warren S. Leonard on cyclic competition.
* Josef Hofbauer & Karl Sigmund, *Evolutionary Games and Population Dynamics*.
* Steven H. Strogatz for equivariant bifurcation and pitchfork normal forms.

For chiral symmetry breaking:

* Dilip Kondepudi and Frank J. K. Frank.
* The Frank model is particularly relevant because it also produces symmetry-related homochiral attractors via mutual inhibition.

For large deviations:

* Mark I. Freidlin & Alexander D. Wentzell, *Random Perturbations of Dynamical Systems*.
* Michael I. Dykman on optimal fluctuation theory.
* Eric Vanden-Eijnden for practical computation of quasipotentials.
* Maria K. Cameron for numerical quasipotential calculations.

My overall assessment is that your observations are more consistent with a **symmetry-breaking instability feeding directly into competitive exclusion** than with a classical supercritical pitchfork. The decisive evidence is not the eigenvalue crossing (which both scenarios possess) but the simultaneous observations that (m) saturates near (\pm1) and that (\Delta V) scales linearly rather than quadratically. Those two facts fit together mathematically and point toward a boundary-supported exclusion branch rather than a soft-amplitude pitchfork branch.

model b:
This is a beautifully constructed model. By coupling two May–Leonard-style intransitive 3-cycles via a $\mathbb{Z}_2$-symmetric mutual antagonism, you have hit upon a rich intersection of competitive exclusion, non-gradient stochastic dynamics, and symmetry breaking.

Your observations are entirely correct, and your intuition that the barrier scaling and transition type differ from a standard supercritical pitchfork is spot on. Here is a rigorous breakdown of the bifurcation, the barrier scaling, and the large-deviation mechanics.

---

### 1. The Bifurcation: Winner-Take-All vs. Pitchfork

**Winner-take-all (competitive exclusion) is the correct generic reduction here.** There is no parameter regime in this specific bare Lotka-Volterra (LV) form where a genuine continuous supercritical pitchfork ($m \propto \sqrt{\mu - \mu_c}$) appears.

Here is why: the internal 3-cycle structure is completely slaved to the mean field. Because $a+b = 1.5 < 2$, the internal May–Leonard modes are strictly stable (they do not undergo a Hopf bifurcation). Thus, the groups rapidly synchronize internally, and we can map the system perfectly to the totals $S_L$ and $S_R$. Defining $\alpha = c/3$, the exact reduced deterministic dynamics on the invariant manifold are:


$$\dot{S}_L = S_L (F - \alpha S_L - \mu S_R)$$

$$\dot{S}_R = S_R (F - \alpha S_R - \mu S_L)$$

If we change variables to the total population $S = S_L + S_R$ and the order parameter $m = (S_L - S_R)/S$, the equation for $m$ (assuming $S$ equilibrates rapidly) becomes:


$$\dot{m} = \frac{1}{2} (\mu - \mu_c) S m (1 - m^2)$$

In a classic supercritical pitchfork ($\dot{x} = \epsilon x - x^3$), the saturation term is independent of the bifurcation parameter, so the fixed points move continuously as $x^* = \pm\sqrt{\epsilon}$. In your LV model, the system is fundamentally a degenerate transcritical bifurcation. When $\mu = \mu_c$, the $S_L$ and $S_R$ nullclines perfectly overlap, creating a continuum of fixed points (a zero-eigenvalue line). The moment $\mu > \mu_c$, the stable fixed points jump entirely to the axes ($S_L = F/\alpha, S_R = 0$ or vice versa), meaning $m^*$ jumps instantly to $\pm 1$.

**To recover a genuine supercritical pitchfork**, you must break the bilinear structure by introducing higher-order saturation terms—for example, self-crowding terms ($S_L^2$ inside the bracket) or autocatalysis, as seen in true chiral symmetry-breaking models.

### 2. The Freidlin–Wentzell Quasipotential Scaling

**The linear scaling $\Delta V \propto (\mu - \mu_c)$ is the mathematically correct large-deviation scaling for this degenerate normal form.** It does not violate any rules; rather, it reflects the instantaneous jump of the attractors.

Because the stable states are pinned at $m = \pm 1$ regardless of how small $(\mu - \mu_c) > 0$ is, the distance in phase space between the saddle ($m=0$) and the minima ($m = \pm 1$) is constant. The effective potential barrier is the integral of the restoring force along the escape path:


$$\Delta V = -\int_{0}^{1} \dot{m} \, dm = -\frac{1}{2} (\mu - \mu_c) S \int_{0}^{1} (m - m^3) \, dm$$


Because the bounds of integration are $[0, 1]$ (fixed), the barrier height scales perfectly linearly with the prefactor $(\mu - \mu_c)$. You will only recover the quadratic pitchfork scaling $\Delta V \propto (\mu - \mu_c)^2$ if the distance to the minimum also scales with the bifurcation parameter (i.e., if the integral bounds were $[0, \sqrt{\mu-\mu_c}]$).

### 3. Pinning the FW Prefactor in a Non-Gradient NESS

Your finding that the measured barrier slope ($1/\sigma^2_{eff}$) is radically different from the deterministic 1D projection $\Delta U$ is a classic hallmark of non-equilibrium steady states (NESS).

For a non-gradient dynamical system $\dot{x} = b(x) + \sigma \dot{W}$ (where $\nabla \times b \neq 0$), the true Freidlin–Wentzell quasipotential $V(x)$ cannot be found by simply integrating the 1D deterministic heteroclinic connection. The internal asymmetric cycles ($a \neq b$) generate a rotational probability flux.

When noise is applied, the system does not climb straight up the deterministic manifold against the gradient. Instead, the optimal fluctuation path (the **instanton**) takes a curved trajectory that "surfs" the rotational flow of the 3-cycle, drastically reducing the action required to cross the saddle.

**The correct way to compute the barrier:**
You must solve the Hamilton–Jacobi equation for the FW quasipotential:


$$\nabla V \cdot b(x) + \frac{1}{2} |\nabla V|^2 = 0$$


Practically, you find the instanton by minimizing the Freidlin–Wentzell action functional $S_T = \frac{1}{2} \int |\dot{\phi} - b(\phi)|^2 dt$ subject to the boundary conditions of starting at the L-dominant fixed point and ending at the saddle. The standard numerical tool for this is the **Geometric Minimum Action Method (gMAM)**. The action $S[\phi_{opt}]$ of this curved instanton will correctly pin the prefactor and match your empirical noisy escape-MFPT.

### 4. Literature Anchors

To ground this formally in a paper or thesis, these are the exact coordinates in the literature you need:

* **Symmetric LV and Degenerate Bifurcations:** Look to Hofbauer & Sigmund, *Evolutionary Games and Population Dynamics* (1998). It details the structural instability and competitive exclusion jumps in symmetrical LV systems (often mapped to replicator equations).
* **The May–Leonard Model:** R. M. May and W. J. Leonard, *Nonlinear Aspects of Competition Between Three Species* (SIAM J. Appl. Math, 1975). Vital for explaining why your internal 3-cycles (with $a+b < 2$) are stable and thus cleanly map to the 2D exclusion model.
* **Chiral Symmetry Breaking (True Pitchforks):** The Frank Model (F. C. Frank, 1953) and the Kondepudi–Nelson models (1983, 1984). These are the gold standards for chiral transitions. They rely on cross-inhibition *plus* autocatalysis (e.g., cubic terms), which perfectly contrasts with your LV system to explain why they get pitchforks and you get a transcritical exclusion jump.
* **Large Deviations in Non-Gradient Systems (Instanton Escape):** * Maier & Stein (1993, 1997) "Escape problem for irreversible systems" / "A scaling theory of bifurcations in the symmetric weak-noise escape problem". This is the canonical reference explaining why escape paths deviate from deterministic relaxation paths and lower the barrier.
* W. E, W. Ren, and E. Vanden-Eijnden (2004) "Minimum action method for the study of rare events." This is the methodological paper you need to compute the true FW barrier via gMAM.
model c:
Here is a rigorous diagnosis of your model, based on the structure you have described.

---

### 1. Bifurcation type: symmetric transcritical (hard), not pitchfork

Your six-dimensional system collapses to an effective two-dimensional Lotka–Volterra competition model for the symmetry-breaking mode.  Define the group totals $S_L=\sum L_i$, $S_R=\sum R_i$.  Because the instability mode is uniform within each group, the internal cyclic coordinates do not get excited near threshold; they are slaved to the totals.  Summing your equations gives the exact closed system

$$
\begin{aligned}
\dot S_L &= S_L\!\left(F-\frac{c}{3}S_L-\mu S_R\right),\\
\dot S_R &= S_R\!\left(F-\frac{c}{3}S_R-\mu S_L\right),
\end{aligned}
\qquad c=1+a+b .
$$

This is the canonical symmetric two-species LV competition model with competition coefficient $\alpha=3\mu/c$.  The critical point is $\alpha_c=1$, i.e. $\mu_c=c/3$.

**Why it is transcritical, not pitchfork.**  In the positive orthant, the only fixed points with *both* groups present are the symmetric ones $S_L=S_R=3F/(c+3\mu)$.  There are no partially symmetry-broken interior fixed points with $S_L\neq S_R$ and both positive.  (Proof: at any interior fixed point the within-group structure forces uniformity, $L_i\equiv S_L/3$, $R_i\equiv S_R/3$; substituting into the total equations yields $(S_L-S_R)(c-3\mu)=0$, so asymmetry is possible only at the single parameter value $\mu=\mu_c$.)  Consequently the stable states for $\mu>\mu_c$ are the **boundary** fixed points $(S_L,S_R)=(3F/c,0)$ and $(0,3F/c)$.  These states exist for all $\mu>0$; they do not emerge continuously from the symmetric fixed point.  At $\mu_c$ they exchange stability with the symmetric fixed point in a **symmetric transcritical bifurcation** (an exchange-of-stability event constrained by the $\mathbb Z_2$ symmetry).

Because the attractors sit at finite distance ($m=\pm1$) from the bifurcation point, the order parameter jumps discontinuously — winner-take-all competitive exclusion — rather than growing continuously as $\sqrt{\mu-\mu_c}$.  The internal 3-cycle structure (whether parity or exchange) is invisible to this transition because the breaking mode is uniform and the transverse internal eigenvalues remain stable.

**Answer to Q1:** There is no parameter regime in this model that produces a genuine supercritical pitchfork with soft $|m|\propto\sqrt{\mu-\mu_c}$.  The generic reduction is hard competitive exclusion.

---

### 2. Barrier scaling: linear $\Delta V\propto(\mu-\mu_c)$ is the correct FW scaling

For a supercritical pitchfork, the symmetry-broken minima emerge at distance $\sim\sqrt{\varepsilon}$ from the bifurcation point ($\varepsilon=\mu-\mu_c$).  The quasipotential barrier is the integral of the force over that distance, giving $\Delta V\sim\varepsilon^{3/2}\times\varepsilon^{1/2}\sim\varepsilon^2$ (or, in a gradient normal form, $\Delta V\sim\varepsilon^2$).

In your model the attractors are at $O(1)$ distance ($m=\pm1$) for all $\mu>\mu_c$.  The only quantity that vanishes at threshold is the unstable eigenvalue of the symmetric saddle, $\lambda_u\sim\varepsilon$.  The Freidlin–Wentzell action to climb from the attractor to the saddle is therefore proportional to the saddle height times the $O(1)$ path length, i.e. $\Delta V\sim\varepsilon$.  Your observation of linear scaling is exactly the signature of a **hard/transcritical** normal form.

**Answer to Q2:** The linear scaling is the correct FW quasipotential scaling for this system.  The quadratic pitchfork scaling is not recoverable in any limit because the normal form is fundamentally different: the attractors live on the boundary of the simplex, not in its interior.

---

### 3. Prefactor: the deterministic potential $\Delta U$ is not the FW barrier

Your deterministic dynamics for $(S_L,S_R)$ is a gradient flow in the non-Euclidean metric $G=\mathrm{diag}(1/S_L,1/S_R)$ for the potential

$$
\Phi(S_L,S_R)=-F(S_L+S_R)+\frac{c}{6}(S_L^2+S_R^2)+\mu S_L S_R .
$$

However, with **additive** isotropic noise ($\sigma\,dW$ on the original variables, hence effective noise $\sigma_{\rm eff}=\sigma\sqrt{3}$ on each total), the system is **not** a gradient system in the Euclidean metric.  The Freidlin–Wentzell quasipotential $V$ satisfies the Hamilton–Jacobi equation

$$
-S_L\frac{\partial\Phi}{\partial S_L}\frac{\partial V}{\partial S_L}
-S_R\frac{\partial\Phi}{\partial S_R}\frac{\partial V}{\partial S_R}
+\frac{\sigma_{\rm eff}^2}{2}\left|\nabla V\right|^2=0,
$$

and **not** $V=2\Phi$.  The slope mismatch you observe ($\ln\tau$ vs. $\Delta U$ giving $\sim7.5$ instead of $1/\sigma^2\approx156$) is direct evidence that the true barrier is $\Delta V\ll\Delta U$; the non-gradient (metric) part of the drift creates a lower-action escape path than the naive potential climb.

**How to pin the prefactor.**  Because the effective dynamics is two-dimensional, the full FW prefactor can be computed rigorously:

1. **Compute the quasipotential.**  Use the geometric Minimum Action Method (gMAM) or solve the above HJ equation numerically to obtain $V(S_L,S_R)$.  The barrier is $\Delta V=V({\rm saddle})-V({\rm attractor})$.

2. **Quadratic expansions (Riccati equation).**  Near the attractor $\mathbf x_a$ and the saddle $\mathbf x_s$, expand $V$ to second order.  The Hessian $H_a$ at the attractor satisfies the algebraic Riccati equation
   $$
   J_a^{\!T} H_a+H_a J_a+H_a D H_a=0,
   $$
   where $J_a$ is the Jacobian of the drift at $\mathbf x_a$ and $D=(\sigma_{\rm eff}^2/2)I$.  At the saddle, $V$ has one negative and one positive curvature direction; the positive Hessian $H_s^{\rm st}$ in the stable subspace satisfies the analogous Riccati equation.

3. **Prefactor formula.**  The mean first-passage time between the two exclusion basins is
   $$
   \tau \sim \frac{2\pi}{|\lambda_s|}\sqrt{\frac{\det H_a}{|\det H_s|}}\;
   \exp\!\left(\frac{2\Delta V}{\sigma_{\rm eff}^2}\right),
   $$
   where $\lambda_s$ is the unstable eigenvalue of the deterministic drift at the saddle.  (If you plot $\ln\tau$ versus $\Delta V$, the slope should be $2/\sigma_{\rm eff}^2=2/(3\sigma^2)\approx104$ for your parameters; the remaining discrepancy between this and your observed 7.5 is exactly the factor $\Delta V/\Delta U\ll1$.)

**Practical note:**  Because the attractor lies on the boundary subspace $S_R=0$, the Riccati expansion must be done in the full 2D space (not restricted to the boundary).  The noise in the $S_R$ direction is the only mechanism that lifts the system off the boundary; the deterministic flow then carries it to the saddle or back to the attractor.  The effective 1D reduction along the instanton path is valid only after the full 2D quasipotential has been identified.

---

### 4. Literature anchors

| Topic | Key references |
|-------|----------------|
| **Symmetric LV competition & the transcritical/coexistence threshold** | The 2D reduction you derived is the standard symmetric competition model.  See Murray, *Mathematical Biology* (3rd ed., §3.5) or Edelstein-Keshet, *Mathematical Models in Biology* (Ch. 6).  The degenerate transcritical nature of the $\alpha=1$ threshold is discussed in the context of the "competitive exclusion principle" by MacArthur & Levins (1967) and in the bifurcation-theory literature as a symmetric transcritical (e.g. Guckenheimer & Holmes, *Nonlinear Oscillations*, §7.4). |
| **May–Leonard cyclic competition** | May & Leonard, *SIAM J. Appl. Math.* **32**, 243 (1975).  Your within-group 3-cycle is a May–Leonard-like motif, but because the groups are coupled through totals, the heteroclinic cycle behavior of pure May–Leonard is suppressed. |
| **Replicator / payoff-symmetric dynamics** | Hofbauer & Sigmund, *Evolutionary Games and Population Dynamics* (Cambridge, 1998).  The symmetric LV model is a replicator equation with payoff matrix $A=\begin{pmatrix}1&\alpha\\\alpha&1\end{pmatrix}$; the $\alpha>1$ regime is the "hawk-dove" competitive exclusion case. |
| **Chiral symmetry breaking in non-equilibrium systems** | Kondepudi & Nelson, *Phys. Rev. Lett.* **50**, 1023 (1983); Kondepudi & Prigogine, *Modern Thermodynamics* (Wiley, 1998).  Their models exhibit a soft pitchfork when the order parameter is unconstrained, but hard/transcritical behavior when the dynamics is confined to a simplex (as in population dynamics). |
| **FW quasipotentials & non-gradient prefactors** | Freidlin & Wentzell, *Random Perturbations of Dynamical Systems* (Springer, 1984).  For 2D non-gradient escapes and the non-differentiability of $V$: Maier & Stein, *Phys. Rev. E* **48**, 931 (1993); **50**, 3682 (1994).  For numerical computation of $V$ in population models: Bouchet & Reygner, *J. Stat. Phys.* **162**, 793 (2016); for gMAM: Heymann & Vanden-Eijnden, *Commun. Pure Appl. Math.* **61**, 596 (2008). |
| **WKB / large-deviation treatments of stochastic LV** | Assaf, Meerson & co-workers have computed quasipotentials and MFPTs for competitive LV using the WKB method; see e.g. Assaf & Meerson, *Phys. Rev. E* **81**, 021116 (2010) and follow-up work on extinction and switching in predator-prey/competition systems. |

---

### Bottom line

Your model is a **six-dimensional wrapper around a two-dimensional symmetric transcritical bifurcation**.  The internal cyclic structure is a red herring for the symmetry-breaking transition; the totals obey the classic competitive-exclusion LV equations, and the jump to $m=\pm1$ with linear barrier scaling is the generic, unavoidable behavior.  To get the prefactor right, abandon the deterministic potential $\Delta U$ and compute the true FW quasipotential $\Delta V$ for the $(S_L,S_R)$ subsystem — the slope of $\ln\tau$ versus $\Delta V$ will then lock to $2/(3\sigma^2)$, and the prefactor follows from the Riccati Hessians at the attractor and saddle.
