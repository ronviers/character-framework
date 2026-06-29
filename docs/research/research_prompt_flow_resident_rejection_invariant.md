# Research prompt — a flow-resident invariant: the barycenter of the rejection field

**For the outbound channel. Self-contained.** Return **named, published results with citations**. We are
**not** claiming to discover anything — we expect this object is already characterized somewhere in
dynamical systems / information geometry / large deviations / RG / geometric measure theory, and we want
the citation so we can **import** it. Field-level plausibility ("this sounds like X") is a non-answer:
name the object, the theorem, and where the result lives.

## The one-paragraph target

A flow — a learning dynamics, an RG coarse-graining, or a relaxational non-equilibrium steady state —
carries states toward a manifold `M`: an attractor, a typical set, a model manifold. Projection onto `M`,
call it `P`, has an orthogonal complement `(I−P)`: the **rejection** — the directions the flow expels,
"what cannot stay on `M`." Accumulated over the flow this defines a rejection density `R_t(x) ≥ 0`
concentrated on the boundary `∂M` where projection fails. Define its **barycenter**
`μ(t) = ∫ x·R_t(x) dx / ∫ R_t(x) dx`, and the long-time object — the trajectory `μ(t)`, its time-average
`μ̄ = lim (1/T)∫₀ᵀ μ(t) dt`, or (coordinate-intrinsically) the **boundary first moment**
`J(t) = ∫_{∂M_t} n(x) dσ` over the outward normal `n`. **The question: is this object's trajectory/limit a
convergent, coordinate-intrinsic invariant — more stable than `M` itself, and possibly universal across
systems?**

## What we need (rank the answer by this)

1. **A name.** Is this object — the barycenter / first moment of the rejection-or-boundary measure under a
   coarse-graining or learning flow — a named, studied quantity? In which field?
2. **Convergence.** Is it established that the barycenter trajectory **converges** (to a point or a stable
   orbit) *while the underlying manifold / microscopic parameters keep wandering*? (Our intuition: a
   "constant stream" — a conserved current, not a conserved scalar.)
3. **Universality.** Is its limiting structure known to **recur across different systems/architectures** (a
   genuine invariant), or is it system-specific (a coordinate-dependent statistic)?
4. **The intrinsic form.** Is the coordinate-free object the boundary-normal first moment / a geometric
   **current** (rather than the coordinate-dependent centroid)?
5. **The importable statement.** The single cleanest formal result we can cite and import verbatim, with its
   assumptions.

## Candidate homes (confirm or rule out each, with a citation)

- **Information geometry** (Amari): dually-flat manifolds, e-/m-projections, the **generalized Pythagorean
  theorem** — the rigorous `x = Px + (I−P)x` with an orthogonal Bregman/KL decomposition. Is the "rejection"
  the m-projection residual, and is the residual's barycenter a studied object?
- **Large deviations / Freidlin–Wentzell** (most promising — *we already use the quasipotential / minimum
  action machinery*): the rate function, the typical set and its boundary, the most-likely **exit point /
  instanton**, the quasipotential. Is the exit-location distribution's barycenter (or its long-time
  average) a known invariant with established convergence?
- **Renormalization group**: fixed points of the coarse-graining flow; the convergence of coarse-grained
  observables while microscopic degrees of freedom wander. Is there an RG observable that **is** this
  rejection-barycenter?
- **Geometric measure theory / theory of currents**: the first moment of a boundary measure;
  `∫_{∂M} n dσ` as a current; the boundary operator on rectifiable currents.
- **Index theory / Gauss–Bonnet-type**: `∫_∂ (normal / curvature)` as a topological invariant — is `J(t)`
  of this kind?
- **Optimal transport**: Wasserstein barycenters of an evolving measure, and their convergence rates.
- **Concentration of measure / high-dimensional geometry**: the interior-`O(Volume)` vs
  boundary-`O(codim-1)` asymmetry, and whether the boundary-concentrated barycenter is the stable object.

## What a PASS delivers (per candidate home)

- The **named object** + field + **citation** (paper / theorem / where the result lives).
- **Convergence**: established / open / false — with the result that decides it.
- **Universality**: established / open — with the result.
- The single best **importable formal statement**, verbatim, with its assumptions.
- If **no** established object matches: say so cleanly, name the closest, and state the gap precisely.

**Keep it substrate-general.** State everything for a generic flow + manifold. **No machine-learning,
cognition, or pop-science framing** — a transformer or a brain is at most *one instance*, never the frame.
The object of interest is the geometry of accumulated rejection under a flow, for the simplest structures up.

model a:
After surveying the closest established frameworks, the answer is more sharply negative—and more useful—than your prompt initially suggests.

The **exact object** you describe ("the barycenter of accumulated rejection under a flow") does **not** appear to exist as a named invariant in the literature. However, nearly every component exists separately, and there is a remarkably consistent picture across fields.

The strongest conclusion is:

> **The literature contains convergence theorems for evolving measures, boundary currents, exit distributions, and projection residuals—but not for the first moment of "rejection" itself. The closest coordinate-free objects are boundary currents and exit measures, not centroids.**

Below is the ranking I would give.

---

# 1. Large deviations / Freidlin–Wentzell

## Verdict: ★★★★★

This is by far the closest mathematical home.

Your "rejection density" is almost exactly what large-deviation theory calls an **exit distribution** (or reactive current in transition-path theory).

The canonical objects are

* quasipotential
* minimum-action path
* exit measure
* reactive current

—not their barycenter.

---

### Named object

The exit distribution

[
\mu_\varepsilon(\partial D)
]

for a diffusion leaving a metastable basin.

Freidlin & Wentzell prove that as noise vanishes,

* exit locations concentrate
* the measure converges
* often to a single point
* sometimes to finitely many saddle points.

The centroid therefore converges **only because the measure converges**, not because the centroid itself is fundamental.

This is standard Freidlin–Wentzell theory.

---

### Importable theorem

Roughly:

If

* deterministic dynamics possess an attracting domain,
* diffusion amplitude tends to zero,

then the exit measure converges to the quasipotential minimizer(s).

The limiting object is

[
\mu_{\rm exit}
]

not

[
\int x,d\mu.
]

That distinction is universal in the literature. ([SIAM][1])

---

### Universality

Very high.

The exit measure depends only on the quasipotential.

Different microscopic dynamics sharing the same quasipotential produce identical limiting exit laws.

That is genuine universality.

---

# 2. Geometric Measure Theory / Currents

## Verdict: ★★★★★

Your coordinate-free reformulation

[
J=\int_{\partial M} n,d\sigma
]

is **much closer** to existing mathematics than the centroid.

This is naturally interpreted as a boundary current.

---

### Named object

Integral current

Boundary operator

Rectifiable current

Federer–Fleming

---

The boundary

[
\partial T
]

is itself an invariant object.

Currents converge under

* flat convergence
* weak convergence
* mass convergence.

Those are rigorous convergence notions.

The first moment

[
\int x,d(\partial T)
]

exists,

but is merely a linear functional applied to the current.

It is not promoted to a distinguished invariant.

([Encyclopedia of Mathematics][2])

---

### Importable theorem

Federer–Fleming compactness:

bounded mass
+
bounded boundary mass

⇒ convergent subsequence of currents.

This is exactly the kind of theorem your proposal wants.

---

# 3. Optimal Transport

## Verdict: ★★★★☆

This field has essentially solved

> "When does the barycenter of an evolving measure converge?"

---

### Named object

Wasserstein barycenter

Fréchet barycenter

Bures–Wasserstein barycenter

---

The convergence theory is extensive.

The important point:

the measure itself is primary.

The barycenter is a derived statistic.

Convergence proofs are about

[
\mu_t
]

not about

[
\mathrm{bar}(\mu_t).
]

([Proceedings of Machine Learning Research][3])

---

# 4. Information Geometry

## Verdict: ★★★☆☆

Your projection picture is already formalized.

---

### Named theorem

Generalized Pythagorean theorem

for Bregman divergence.

The decomposition

[
x=P(x)+(I-P)x
]

becomes

orthogonal decomposition in divergence geometry.

Amari,
Csiszár,
Matúš,
etc.

---

But:

the residual

[
(I-P)x
]

is **never accumulated into a new invariant measure**.

It remains a divergence residual.

So your "rejection field"

is mathematically legitimate,

yet nobody studies

its centroid.

([arXiv][4])

---

# 5. Renormalization Group

## Verdict: ★★★☆☆

Very close philosophically.

Not close mathematically.

RG studies

* relevant directions
* irrelevant directions

which is almost literally

accepted
vs
rejected perturbations.

But the invariant is

the fixed point,

not

the center of irrelevant directions.

No standard observable corresponds to your barycenter.

---

# 6. Differential Geometry / Gauss–Bonnet

## Verdict: ★★☆☆☆

Your proposed

[
\int_{\partial M} n,d\sigma
]

is **not** a topological invariant.

In Euclidean space,

[
\int_{\partial M} n,d\sigma =0
]

for every compact smooth body,

by the divergence theorem.

So this integral is actually trivial in the simplest setting.

To obtain a nontrivial invariant one must weight the normal by curvature or another geometric quantity.

Thus the unweighted normal current cannot be the universal object you hoped.

---

# 7. Concentration of Measure

## Verdict: ★★☆☆☆

Very useful background.

Not your object.

One finds results showing

boundary concentration,
thin shells,
isoperimetry,

but not boundary first moments.

---

# Overall answer to your five questions

## (1) Is there a name?

No.

Not for the barycenter of accumulated rejection.

Closest names are

* exit measure
* reactive current
* boundary current
* Wasserstein barycenter
* projection residual.

None coincide with your construction.

---

## (2) Is convergence known?

Yes—

for the underlying measures.

Not for the barycenter as an independently meaningful invariant.

Whenever convergence occurs,

it is inherited from

[
\mu_t
\rightarrow
\mu_\infty.
]

---

## (3) Universality?

Exit measures:

yes.

Reactive currents:

yes.

Currents:

yes.

Centroids:

generally no.

Centroids are coordinate dependent.

---

## (4) Is the intrinsic object really a current?

This is the biggest surprise.

I think **yes**.

Everything in the mature literature points toward

the measure

or

the current

being fundamental,

while the centroid is merely a coordinate statistic extracted afterward.

Your instinct to replace

[
\bar x
]

with

a boundary current

is mathematically aligned with geometric measure theory.

---

## (5) Best importable theorem

The cleanest statement is **not** about barycenters.

It is the Federer–Fleming compactness theorem:

> A sequence of integral currents with uniformly bounded mass and uniformly bounded boundary mass admits a flat-convergent subsequence whose boundary converges as well. ([Encyclopedia of Mathematics][2])

Combined with Freidlin–Wentzell:

> Under small-noise assumptions, exit measures converge to measures supported on quasipotential minimizers.

Together they give exactly the architecture your proposal needs:

* define a rejection measure,
* prove it converges as a current or measure,
* only then take moments (such as a barycenter) if desired.

---

### The precise gap

The literature has no established notion of a **flow-resident barycenter of rejection** that is itself treated as a universal invariant. The invariant objects are instead the **evolving measure/current** (exit measure, reactive current, boundary current) together with convergence theorems for those objects. The first moment of that measure is available as a derived observable, but there is no general theorem elevating it to a coordinate-intrinsic or universal quantity. In other words, if there is a fundamental object to import, it is almost certainly **the rejection current or measure**, not its centroid. That is where the mature theory already exists.

[1]: https://epubs.siam.org/doi/10.1137/21M1449282?utm_source=chatgpt.com "Computing the Conformal Barycenter | SIAM Journal on Applied Algebra and Geometry"
[2]: https://encyclopediaofmath.org/wiki/Geometric_measure_theory?utm_source=chatgpt.com "Geometric measure theory - Encyclopedia of Mathematics"
[3]: https://proceedings.mlr.press/v125/chewi20a.html?utm_source=chatgpt.com "Gradient descent algorithms for Bures-Wasserstein barycenters"
[4]: https://arxiv.org/abs/1202.0666?utm_source=chatgpt.com "Generalized minimizers of convex integral functionals, Bregman distance, Pythagorean identities"

model b:
This is a structurally compelling construction. You are looking for a singular, unifying theoretical object that tracks the "exhaust" of a projection operator under a flow, hypothesizing that the boundary-accumulation of this exhaust is more fundamentally stable than the manifold itself.

I must be candid: **the exact composite object you are describing—a universally named "rejection barycenter" that acts as a fully coordinate-intrinsic, convergent invariant across all these fields—does not currently exist in the literature.** However, the theoretical machinery you are looking for is distributed primarily across two fields: **Large Deviations** (which formalizes the accumulation of expelled measure on a boundary) and **Geometric Measure Theory** (which formalizes the coordinate-free boundary moments).

Before breaking down your candidate homes, a necessary mathematical correction regarding your intrinsic form: for a closed bounded domain $M_t \subset \mathbb{R}^d$, the exact integral of the outward normal $\int_{\partial M_t} n(x) d\sigma$ is identically zero by the Divergence Theorem (since $\nabla \cdot I = 0$). If you are looking for a non-trivial boundary first moment, the geometrically rigorous object is the flux of the position vector, or in the language of currents, the **first variation of the boundary**.

Here is the systematic breakdown of your candidate homes, identifying exactly what can be imported, what fails, and the gaps that remain.

---

## Candidate Homes: Evaluation & Pass/Fail

### 1. Large Deviations / Freidlin–Wentzell Theory

**Verdict:** **PASS (Closest Match for the Dynamical Density)**
The closest established object to your "rejection density accumulating on the boundary" is the **Exit Measure** (or harmonic measure in the limit of vanishing noise), and its convergence to the **Instanton** (the most probable exit path/point).

* **The Named Object:** The Exit Measure (distribution of the exit point on $\partial M$) and the Quasipotential Minimum.
* **Convergence:** **Established.** As the noise parameter $\epsilon \to 0$ (or time $t \to \infty$ for the accumulated flow), the exit measure weakly converges to a Dirac measure concentrated at the global minimum of the quasipotential on the boundary.
* **Universality:** **False (System-Specific).** The limiting object depends entirely on the system's specific drift field and diffusion matrix; it is a coordinate-dependent statistic, not a universal topological invariant.
* **The Gap:** FW theory assumes a stochastic perturbation causing the exit, whereas your framing relies on the deterministic orthogonal complement of a projection operator.
* **Citation:** Freidlin, M. I., & Wentzell, A. D. (1984). *Random Perturbations of Dynamical Systems*. Springer.

### 2. Geometric Measure Theory (GMT)

**Verdict:** **PASS (Closest Match for the Intrinsic Form)**
If you want the coordinate-free, geometric version of "the forces pushing off the manifold," GMT houses this as the variation of a varifold.

* **The Named Object:** The **First Variation of a Varifold** (which defines the generalized mean curvature measure).
* **Convergence:** **Established (Conditional).** Under mean curvature flow, singularities and limiting behaviors of the generalized mean curvature measure are rigorously characterized (e.g., Huisken's monotonicity formula).
* **Universality:** **False.** The limit depends on the initial geometry.
* **The Gap:** GMT tracks the local geometry of the manifold as it flows, not the "rejection" field of states failing to project onto it.
* **Citation:** Simon, L. (1983). *Lectures on Geometric Measure Theory*. Australian National University.

### 3. Information Geometry (Amari)

**Verdict:** **FAIL (Conceptual Gap)**

* While the Generalized Pythagorean Theorem elegantly decomposes a state via dual connections, the residual (the difference between the state and its m-projection) is simply an error vector in the dual coordinates.
* **The Gap:** There is no literature establishing the *barycenter* of this residual integrated over a dynamic flow as a tracked, stable invariant. The field focuses on the static geometric structure of the manifolds, not the macroscopic flow of the residuals.

### 4. Renormalization Group (RG)

**Verdict:** **FAIL (Conceptual Gap)**

* The "rejection" in RG consists of the high-momentum degrees of freedom integrated out of the partition function.
* **The Gap:** While the flow of the effective action converges to fixed points, the "barycenter" of the integrated-out variables is not tracked as a geometric or statistical invariant. RG observables are operators, not spatial barycenters of discarded measure.

### 5. Optimal Transport / Index Theory / Concentration of Measure

**Verdict:** **FAIL (Scope Mismatch)**

* **Optimal Transport:** Wasserstein barycenters apply to families of probability measures, not the continuous rejection density of a single flow.
* **Index Theory:** Tracks purely topological invariants (Euler characteristic, Chern classes) which are strictly discrete. Your $J(t)$ is continuous.
* **Concentration:** Describes static probability spaces (e.g., the Gaussian isoperimetric inequality), not dynamical invariants of a flow.

---

## The Importable Statement

If your core mechanical goal is to import a theorem proving that an expelled/rejected density under a flow converges to a highly stable, specific location on a boundary while the interior parameters wander, you must import from **Large Deviations**.

Here is the cleanest formal result you can adapt (The Freidlin-Wentzell Exit Location Theorem):

> **Theorem (Freidlin-Wentzell):** Let $X_t^\epsilon$ be a diffusion process in a domain $D \subset \mathbb{R}^d$ governed by $d X_t^\epsilon = b(X_t^\epsilon) dt + \epsilon d W_t$, where $b(x)$ has a single stable attractor at $O \in D$. Let $V(x)$ be the quasipotential (the minimum action required to reach $x$ from $O$ against the flow $b$). Let $\tau^\epsilon$ be the first exit time from $D$. If there exists a unique point $x^* \in \partial D$ such that $V(x^*) = \min_{x \in \partial D} V(x)$, then for any $\delta > 0$,
> $$\lim_{\epsilon \to 0} \mathbb{P}_{x_0} \left( \| X_{\tau^\epsilon}^\epsilon - x^* \| > \delta \right) = 0$$
> 
> 

**Assumptions required to import this:** 1. Your flow can be formulated as having a deterministic drift $b(x)$ toward $M$.
2. Your "rejection" mechanism can be modeled as a small perturbation $\epsilon$ that causes mass to hit the boundary $\partial D$ (where the projection $P$ fails).
3. The accumulation density $R_t(x)$ is equivalent to the exit distribution (the harmonic measure) on the boundary.

**Summary:** You will not find the "barycenter of the projection rejection" as a named, off-the-shelf invariant in geometry. You must either build the geometric definition from scratch using GMT (First Variations), or import the dynamical concentration mechanism from Freidlin-Wentzell (The Exit Measure).
model c:
Based on extensive search across the candidate homes you identified, here is the assessment. The short answer is: **no established object matches your exact construction**, but there are closely related objects in two fields, and the gap is precisely characterizable.

---

## 1. The Steiner Point (Convex Geometry) — CLOSEST NAMED RELATIVE

**Named object:** The **Steiner point** (also called the **Steiner curvature centroid** or **surface-area centroid**).

**Field:** Convex geometry / Brunn–Minkowski theory.

**Definition:** For a convex body $K \subset \mathbb{R}^n$, the Steiner point is:
$$s(K) = \frac{1}{\kappa_n} \int_{S^{n-1}} u \, h_K(u) \, d\sigma(u) = \frac{1}{n} \int_{S^{n-1}} u \, dS_K(u)$$
where $h_K$ is the support function and $S_K$ is the **surface area measure** on the unit sphere (the pushforward of boundary $(n-1)$-measure under the Gauss map). For $C^2_+$ bodies, equivalently:
$$s(K) = \int_{\partial K} x \, H_{n-1}(x) \, d\mathcal{H}^{n-1}(x) \bigg/ \int_{\partial K} H_{n-1}(x) \, d\mathcal{H}^{n-1}(x)$$
where $H_{n-1}$ is the Gauss–Kronecker curvature.

**Connection to your object:** Your $J(t) = \int_{\partial M_t} n(x) \, d\sigma$ is, for convex bodies, the **first moment of the surface area measure with respect to the normal direction**—a close relative of the Steiner point construction. The Steiner point is the centroid weighted by curvature (the "infinitesimal content" of boundary patches), while your rejection barycenter weights by accumulated flux/rejection density.

**Convergence:** The Steiner point is **continuous** with respect to Hausdorff convergence of convex bodies (Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, §1.7). However, this is static convergence of bodies, not dynamical convergence under a flow while the interior "wanders."

**Universality:** The Steiner point is **Minkowski-additive and equivariant under rigid motions**—a genuine geometric invariant. But it is defined for convex bodies, not general manifolds under flow.

**The gap:** Your object accumulates rejection *over time* from a dynamical flow, whereas the Steiner point is a static geometric functional. There is no established "dynamical Steiner point" that tracks the barycenter of time-accumulated boundary flux.

---

## 2. The Exit Location Distribution (Freidlin–Wentzell Theory) — CLOSEST DYNAMICAL ANALOGUE

**Named object:** The **exit location distribution** / **most probable exit point** (MPEP).

**Field:** Large deviations theory / stochastic exit problems.

**Key result (Maier & Stein 1997):** For a stochastic system perturbed by noise of strength $\epsilon$ in a domain $\Omega$ with attractor $S$, as $\epsilon \to 0$, the exit location distribution $p_\epsilon(x) \, dx$ on $\partial\Omega$ concentrates near the saddle point $H$ where the quasipotential $W$ attains its minimum. The distribution's moments—including its barycenter/expected offset from $H$—have been computed explicitly. For the expected offset $E\hat{\Theta}_\epsilon = \int s \, p_\epsilon(s) \, ds$ along the boundary:

$$E\hat{\Theta}_\epsilon \sim [A\Gamma(1+\mu/2)]\epsilon^{\mu/2} \quad (\mu < 1)$$
$$E\hat{\Theta}_\epsilon \sim c\left[\sqrt{\frac{2}{\pi}}\frac{1}{\mu^2-1} + \frac{B(1/2,\mu/2)}{4\sqrt{\pi}(\mu-1)}\right]\epsilon^{1/2} \quad (\mu > 1)$$

where $\mu = |\lambda_s(H)|/\lambda_u(H)$ is the eigenvalue ratio at the saddle.

**Connection to your object:** This is the barycenter of a boundary-concentrated measure under a flow (the stochastic flow perturbed by small noise). The quasipotential $W$ plays the role of your "rejection field"—it measures the "difficulty" of reaching any boundary point.

**Convergence:** In the $\epsilon \to 0$ limit, the exit location distribution converges to a **delta measure at the quasipotential minimizer** $H$. The barycenter converges to $H$. However, this is asymptotic concentration, not convergence of a time-averaged barycenter while the interior wanders.

**Universality:** The limiting distribution (Weibull with shape $2/\mu$ for $\mu < 1$, or Gaussian-like for $\mu > 1$) is **universal** across systems sharing the same eigenvalue ratio $\mu$ at the saddle.

**The gap:** The FW exit barycenter is defined for **stochastic exit from a fixed domain**, not for a time-evolving manifold $M_t$ under a deterministic or learning flow. The "rejection" in FW theory is probabilistic (noise-driven exit), not geometric (projection residual). There is no established result for the barycenter of accumulated rejection from a *deterministic* flow onto a *time-varying* manifold.

---

## 3. Information Geometry — RULED OUT

The e-/m-projection framework (Amari, *Information Geometry and Its Applications*) gives orthogonal decompositions of KL divergence, but the "residual" $(I-P)x$ is not a measure and has no barycenter construction. The m-projection residual is a **vector in the tangent space**, not a density on a boundary. No named object matches.

---

## 4. Geometric Measure Theory / Currents — RULED OUT

The first moment $\int_{\partial M} n \, d\sigma$ as a current is the **boundary operator applied to the current $[M]$**:
$$\partial [M](\omega) = \int_{\partial M} \langle \omega, n \rangle \, d\sigma$$

This is standard (Federer, *Geometric Measure Theory*, 4.1.7). But the boundary current is a **functional on forms**, not a point in space. Its "barycenter" would require a vector-valued current evaluation, which is not a standard construction. The **mean curvature vector** $\int_{\partial M} n \, d\sigma / \text{Area}(\partial M)$ appears in mean curvature flow, but this is not an invariant—it's the velocity of the flow, not a convergent barycenter.

---

## 5. Renormalization Group — RULED OUT

RG fixed points are characterized by **relevant/irrelevant operator dimensions**, not by a barycenter of "rejected" degrees of freedom. The Wilsonian effective action integrates out high modes, but the "rejection" (integrated-out modes) has no geometric boundary measure whose barycenter is studied. The closest concept is the **anomalous dimension** of the trace of the stress tensor, which is a scalar, not a barycenter.

---

## 6. Optimal Transport / Wasserstein Barycenters — RULED OUT

Wasserstein barycenters (Agueh & Carlier, 2011) are defined for **probability measures on a fixed space**, not for boundary measures of evolving manifolds. The convergence theory (Kim & Pass, 2017) concerns stability under measure perturbation, not under geometric flow. No named object matches the rejection-barycenter construction.

---

## SUMMARY: The Verdict

| Criterion | Status |
|-----------|--------|
| **Name** | **No exact match.** Closest: Steiner point (static geometry), FW exit distribution (stochastic dynamics). |
| **Convergence** | **Open / unstudied** for the exact object. FW exit barycenter converges to quasipotential minimizer, but for stochastic exit from fixed domain. |
| **Universality** | **Partial:** FW exit distribution shape is universal (eigenvalue-ratio dependent), but no result for deterministic flow rejection. |
| **Intrinsic form** | The boundary-normal first moment $J(t)$ is a natural geometric current, but its convergence theory is **undeveloped**. |
| **Importable statement** | **None verbatim.** The gap is precise. |

---

## The Gap (Precise Statement)

Your object requires a theory of **dynamical boundary measure barycenters** under flows where:
- The manifold $M_t$ evolves (not fixed, as in FW);
- The "rejection" is deterministic (projection residual, not stochastic noise);
- The accumulation is over time (not an asymptotic $\epsilon \to 0$ limit).

This combination—**time-accumulated deterministic rejection from a flow-resident manifold**—does not appear to have been characterized. The closest mathematical infrastructure is:

1. **Steiner point theory** (for the geometric construction of curvature-weighted boundary centroids), and
2. **Freidlin–Wentzell exit theory** (for the convergence of boundary-concentrated measures to distinguished points).

A synthesis would require extending FW-type exit measure analysis to deterministic flows with time-varying domains, or dynamicalizing the Steiner point construction—neither of which appears in the literature under the names you seek.

**Recommendation:** If you need a citation to import, the **Steiner point** (Schneider, *Convex Bodies*, §1.7) provides the geometric template, and **Maier–Stein** (1997, *J. Stat. Phys.*) provides the dynamical template. But you will need to derive the convergence of your specific object; it is not yet a theorem in either field.

