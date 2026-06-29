# Research prompt — the rejection anchor: a fast intrinsic current/frame stable amid a wandering bulk (round 2)

**For the outbound channel. Self-contained.** Return **named, published results with citations**. We import
established math; we do not claim to discover. Name the object, the theorem, where it lives. Field-level
plausibility is a non-answer.

**Why round 2.** Round 1 asked whether the *barycenter of accumulated rejection on the boundary* `∂M` is a named
invariant. Answer (settled): **no** — the centroid is a derived coordinate statistic, the fundamental object is the
measure/current (Freidlin–Wentzell exit measure / Maier–Stein moments cover the boundary case), and the proposed
intrinsic form `∫_{∂M} n dσ ≡ 0` is *identically zero* (divergence theorem). This round moves the object **off the
boundary and into the interior**, and asks a **different, sharper** question — about a *separation of timescales*.

## The one-paragraph target

A dissipative flow has a state `x(t)` that wanders forever and an attractor / manifold `M(t)` that itself evolves.
Define a **rejection vector field** `V(x)` in the **interior**: the component of the flow that systematically
contracts toward / excludes from the viable region — the directions the dynamics refuses to preserve. Track the
**long-time average / invariant-measure current / frame** built from `V`. The observed phenomenon to explain:
**a small, coordinate-independent object built from `V` converges (freezes) while the bulk keeps moving** — heuristically
`μ̇(t) → 0` while `M(t)` and `x(t)` keep evolving. The hypothesis is a **separation of timescales**: the anchor
stabilizes *faster than* the substrate wanders (`τ_anchor ≪ τ_wander`), and the limiting object is an intrinsic
**current / frame / support**, not a centroid.

## What we need (rank the answer by this)

1. **A name.** Is the coordinate-independent current/frame/invariant-measure of the *contracting (rejection) part*
   of a dissipative flow — distinct from the attractor itself — a named, studied object? (Candidates: the SRB
   measure restricted to the stable/contracting foliation; the asymptotic-phase / isochron frame; an averaged slow
   current.)
2. **THE CRUX — is the timescale separation GENERIC, or special/tuned?** Is it *generically* true that this
   rejection-current converges on a **faster** timescale than the trajectory/attractor wanders (`τ_anchor ≪
   τ_wander`)? Or is "an averaged object converges while the path wanders" merely the **free, generic ergodic
   theorem** (Birkhoff / SRB) with no genuine timescale gap? We need the **discriminator**: a result that says when a
   real separation exists vs when convergence is just generic averaging.
3. **Intrinsic form.** Is the right object a **current**, a moving **frame**, a **support function**, or an invariant
   **measure** — explicitly *not* a centroid? Which is coordinate-free?
4. **Universality.** Does the limiting current/frame **recur across different dissipative systems** (a genuine
   invariant), or is it system-specific?
5. **The importable statement** — the single cleanest formal result, verbatim, with assumptions.

## Candidate homes (confirm or rule out each, with a citation)

- **Ergodic theory / SRB measures.** The empirical measure converges (coordinate-independent) while the trajectory
  wanders; SRB is smooth along the unstable foliation, with the **stable/contracting foliation** as the natural
  "rejection." Is there a **rate-of-convergence** result establishing (or denying) a genuine separation?
- **Fast–slow systems / geometric singular perturbation (Fenichel).** Genuine timescale separation, slow manifolds,
  the slow current as the stable object. Is the rejection-anchor a Fenichel slow current — and is the separation
  forced by a small parameter (tuned) or emergent (generic)?
- **Averaging theory / adiabatic invariants.** A conserved/slow quantity stable while fast variables wander.
- **Asymptotic phase / isochrons** (Guckenheimer; Winfree). The coordinate-independent phase **frame** all nearby
  trajectories converge to — a frame, not a point.
- **Center-of-mass / Noether currents.** The classical prototype: a frame that stays inertial regardless of internal
  chaos. Is there a dissipative analogue — a stable frame decoupled from internal motion?
- **Currents (Federer–Fleming) + support function.** The intrinsic, coordinate-free encodings (a current survives
  changes that destroy pointwise information; the support function is intrinsic where the centroid is not).

## What a PASS delivers (per candidate home)

- The **named object** + field + **citation**.
- **The discriminator (Q2):** is the timescale separation **generic / tuned / nonexistent** — with the result that
  decides it. *(This is the most important deliverable: it tells us whether there is an anchor or only the ergodic
  average.)*
- **Intrinsic form** (current / frame / support / measure).
- **Universality**: established / open.
- The single best **importable formal statement**, verbatim, with assumptions.
- If **no** established object matches: say so, name the closest, and state the gap precisely.

**Keep it substrate-general.** A generic dissipative flow + manifold. **No machine-learning, cognition, or
pop-science framing** — at most one instance, never the frame. The object is the geometry of a *fast-stabilizing
intrinsic current* of the rejected/contracting part of a flow, for the simplest structures up.

model a:
The boundary version appears to be settled: there is no canonical "rejection centroid." Moving into the interior changes the problem substantially. Here the literature *does* contain several canonical coordinate-free objects—but none are literally "the rejection current." The closest matches split into two fundamentally different regimes.

| Candidate                   | Named object                   | Intrinsic form            | Does it give a fast anchor?                 |
| --------------------------- | ------------------------------ | ------------------------- | ------------------------------------------- |
| Hyperbolic/ergodic dynamics | SRB measure + stable foliation | invariant measure         | **No generic fast timescale**               |
| Slow-fast dynamics          | Fenichel slow manifold         | invariant manifold        | **Yes—but only with explicit spectral gap** |
| Limit-cycle dynamics        | Isochrons / isostables         | invariant foliation/frame | **Yes—local exponential contraction**       |
| Koopman theory              | Dominant eigenfunctions        | intrinsic coordinates     | **Yes if spectral gap exists**              |
| Geometric measure theory    | Currents                       | coordinate-free current   | Wrong notion of "current" here              |

The key discriminator is not "rejection versus attraction." It is **whether the generator has a spectral gap (or normal hyperbolicity)**.

---

# The crux (Q2)

This turns out to have a remarkably clean answer.

There are **two mathematically distinct mechanisms** that can make an "anchor" appear to freeze while trajectories continue wandering.

### Case A — generic ergodicity

Here one only has

* Birkhoff averages
* SRB statistics
* empirical measures

The trajectory keeps wandering forever, while time averages converge.

There is **no second dynamical timescale**.

The convergence is simply

[
\frac1T\int_0^T f(x(t)),dt
\longrightarrow
\int f,d\mu.
]

Nothing says this average settles dramatically earlier than the orbit itself.

Without additional assumptions there is **no theorem giving**

[
\tau_{\rm anchor}\ll\tau_{\rm wander}.
]

That inequality is **not generic**.

---

### Case B — spectral contraction

A genuine fast anchor appears when there is

* normal hyperbolicity,
* spectral gap,
* exponential contraction,
* dominant Koopman eigenvalue.

Then

[
\tau_{\rm anchor}
\sim
\frac1{|\lambda_{\rm stable}|},
]

while motion along the remaining directions occurs on much longer scales.

This is an actual theorem—not merely ergodic averaging.

So the discriminator is:

> **Does the flow possess a hyperbolic splitting with a spectral gap?**

If yes,

the anchor freezes exponentially.

If no,

one only has ordinary ergodic averaging.

That is probably the cleanest answer to your Round-2 question. ([ScienceDirect][1])

---

# Candidate 1 — SRB measure

## Named object

SRB (Sinai–Ruelle–Bowen) measure.

Intrinsic object:

an invariant probability measure on the attractor.

Coordinate-free.

---

## Does it match the rejection field?

Partially.

The stable foliation is literally the contracting ("forgotten") directions.

The SRB measure is absolutely continuous along unstable leaves while contraction along stable leaves erases transverse information.

This is exactly the statistical notion of "rejection."

But—

the SRB measure itself is **not** a current built from contraction.

It is the invariant measure surviving contraction.

([ScienceDirect][1])

---

## Timescale

This is where your question becomes precise.

Existence of an SRB measure **does not imply**

fast convergence.

Rates require

* exponential mixing
* decay of correlations
* transfer-operator spectral gap

Without those,

there is no intrinsic fast anchor.

---

## Universality

Very high.

Every uniformly hyperbolic dissipative attractor has this object.

The object is universal.

Its numerical value is system-dependent.

---

# Candidate 2 — Fenichel theory

This is the strongest match to your heuristic.

## Named object

Normally hyperbolic invariant manifold.

The slow manifold.

---

The theorem says trajectories collapse exponentially fast onto the slow manifold,

after which motion continues slowly along it.

Exactly

[
\tau_{\rm fast}
\ll
\tau_{\rm slow}.
]

Unlike ergodicity,

this is a genuine dynamical separation.

It depends on

normal hyperbolicity.

Not merely averaging.

---

## Intrinsic object

The manifold itself.

Or its stable foliation.

Coordinate independent.

---

## Generic?

Only inside the class

with singular perturbation / normal hyperbolicity.

Not generic for arbitrary dissipative flows.

---

This is probably the closest mathematical realization of

> "anchor freezes while substrate continues wandering."

---

# Candidate 3 — Isochrons

Much closer than they first appear.

Isochrons are not points.

They are invariant foliations.

Every trajectory rapidly converges onto exactly one isochron while continuing to evolve around the attractor.

The anchor is therefore

a phase coordinate,

not a location.

The stable foliation defines the frame.

([SIAM][2])

---

## Important refinement

Modern Koopman theory introduced

**isostables**.

These are arguably even closer to your proposal.

Isostables are level sets of the dominant Koopman eigenfunction.

They measure

remaining asymptotic decay.

The dominant eigenvalue fixes the slowest contraction rate.

Everything faster disappears.

So the isostable coordinate is essentially

the surviving contraction coordinate.

This is much closer to an intrinsic rejection coordinate than the SRB measure.

([Namur Research Portal][3])

---

# Candidate 4 — Koopman eigenfunctions

This may actually be the closest mathematical object to what your prompt describes.

Instead of tracking trajectories,

Koopman theory tracks observables.

Dominant eigenfunctions define

intrinsic coordinates.

Their decay rates are

the spectrum

[
e^{\lambda t}.
]

If

[
|\Re\lambda_1|
\gg
|\Re\lambda_2|,
]

then

everything except the dominant coordinate disappears rapidly.

The surviving coordinate acts exactly like a fast intrinsic frame.

This is not a centroid.

It is not a measure.

It is an intrinsic coordinate arising from the operator spectrum. ([Namur Research Portal][3])

---

# Candidate 5 — Currents

Here the answer is largely "no."

Federer–Fleming currents encode

orientation,

integration,

homology.

They are coordinate free.

But they are not dynamical contraction objects.

Nothing in classical geometric measure theory produces

a universal contracting current

whose stabilization time differs from trajectory motion.

So this appears to be the wrong mathematical home.

---

# Importable statement

The cleanest theorem matching your desired behavior is essentially Fenichel's persistence result:

> If an invariant manifold is normally hyperbolic, then it persists under sufficiently small perturbations, possesses invariant stable foliations, and trajectories in a neighborhood converge exponentially to the manifold, after which evolution proceeds on the slower dynamics induced on the manifold.

The assumptions are exactly what create the separation of timescales: normal hyperbolicity supplies a spectral gap between contraction transverse to the manifold and motion tangent to it. That gap, not ergodicity alone, is what yields a genuine "fast anchor, slow wander." ([Namur Research Portal][3])

## Overall assessment

Your "fast intrinsic rejection anchor" does not appear to exist in the literature under that name. The closest established structures divide cleanly:

* If the phenomenon is **purely statistical**, the canonical object is the **SRB/invariant measure**, and there is generally **no guaranteed fast separation of timescales** beyond ergodic convergence.
* If the phenomenon is **dynamical**, the canonical objects are **normally hyperbolic invariant manifolds**, **stable foliations**, **isochrons/isostables**, and **Koopman eigenfunctions**. In that setting, a fast-stabilizing anchor is a standard consequence of a **spectral gap** or **normal hyperbolicity**.

The main conceptual shift from Round 1 is therefore: the most fundamental interior object is probably **not a current at all**, but an **intrinsic foliation or Koopman coordinate**. The distinction between "anchor" and "bulk" is governed by **spectral structure** rather than by averaging.

[1]: https://www.sciencedirect.com/science/article/pii/S0022039616300316?utm_source=chatgpt.com "SRB measures for a class of partially hyperbolic attractors in Hilbert spaces - ScienceDirect"
[2]: https://epubs.siam.org/doi/10.1137/090777244?utm_source=chatgpt.com "Continuation-based Computation of Global Isochrons | SIAM Journal on Applied Dynamical Systems"
[3]: https://researchportal.unamur.be/en/publications/isostables-isochrons-and-koopman-spectrum-for-the-action-angle-re/?utm_source=chatgpt.com "Isostables, isochrons, and Koopman spectrum for the action-angle representation of stable fixed point dynamics - the Research Portal - University of Namur"

model b:
Here is the formal assessment of your candidate homes and the precise mathematical objects that govern the "rejection anchor" you are describing.

The short answer: The object you seek exists as an intrinsic **frame** and a family of conditional **measures**, not as a current. The timescale separation between the stabilization of this rejection frame and the wandering of the bulk is **real and generic**, provided we define "stabilization" as tangent-space alignment (which is strictly exponential) and "wandering" as ergodic measure convergence (which is statistical and bounded by mixing rates).

Here is the breakdown by your requested criteria.

---

### 1. The Discriminator: Is the Timescale Separation Generic or Tuned?

The timescale separation $\tau_{anchor} \ll \tau_{wander}$ is **generic**, but it manifests as a fundamental difference in *types* of convergence, determined by two distinct spectra in ergodic theory:

* **Fast timescale (The Anchor / Rejection Frame):** Governed by the **Lyapunov spectrum**. Trajectories align to the intrinsic contracting directions (the stable frame) at an exponentially fast rate dictated by the strictly negative Lyapunov exponents $\lambda_i < 0$. This is pointwise, geometric, and exponentially fast.
* **Slow timescale (The Wandering Bulk):** Governed by the **Pollicott–Ruelle resonances / Spectral Gap** of the transfer operator. The convergence of the empirical path to the invariant measure (Birkhoff ergodic averaging) is subject to statistical fluctuations. By the Central Limit Theorem for dynamical systems, the bulk wandering converges at a rate of $1/\sqrt{t}$ (or $e^{-\gamma t}$ for correlation decay, where the spectral gap $\gamma \ll |\lambda_i|$ generically).

**The Discriminator:** If the system is uniformly or non-uniformly hyperbolic, the exponential alignment to the stable frame *generically* outpaces the $1/\sqrt{t}$ convergence of the ergodic average. However, if you require a strict, bounded gap where the anchor freezes entirely while the bulk operates on an $O(1)$ timescale, you must move to Fenichel theory, where the separation is explicitly **tuned** by a small parameter $\epsilon$.

---

### 2. Candidate Homes Evaluated

#### Ergodic Theory / SRB Measures (The Winning Candidate)

* **The Named Object:** The **Oseledets Stable Bundle** $E^s(x)$ spanned by **Covariant Lyapunov Vectors (CLVs)**, and the **conditional measures** $\mu_x^s$ of the SRB measure disintegrated along the stable foliation.
* **Intrinsic Form:** A measurable invariant **frame** (a subbundle of the tangent space $TM$) and a family of conditional **measures**. It is strictly coordinate-independent and covariant with the flow.
* **Universality:** **Established** (via Pesin theory) for all smooth dissipative flows admitting an SRB measure with non-zero Lyapunov exponents (non-uniform hyperbolicity).
* **The Importable Statement:** > **Oseledets Multiplicative Ergodic Theorem (1968) / Pesin Stable Manifold Theorem (1977).** Let $f^t$ be a $C^{1+\alpha}$ flow on a compact Riemannian manifold $M$ preserving an ergodic probability measure $\mu$. Then, for $\mu$-almost every $x$, the tangent space splits equivariantly into coordinate-free Oseledets spaces: $T_x M = E^s(x) \oplus E^c(x) \oplus E^u(x)$. Furthermore, the tangent vectors align to $E^s(x)$ at an exponential rate $e^{\lambda_s t}$ ($\lambda_s < 0$), while the empirical measure $1/T \int_0^T \delta_{f^t(x)} dt$ converges to $\mu$ at a rate governed by the Central Limit Theorem for flows, establishing a generic timescale gap between geometric frame contraction and statistical measure convergence.

#### Fast–Slow Systems / Geometric Singular Perturbation (Fenichel)

* **The Named Object:** The **Normally Hyperbolic Invariant Manifold (NHIM)** and its stable foliation $\mathcal{W}^s(M_\epsilon)$.
* **Intrinsic Form:** A smooth invariant **foliation** (a geometric frame/structure).
* **The Crux (Q2):** The timescale separation here is strictly **tuned**. It requires a small singular perturbation parameter $0 < \epsilon \ll 1$ in the vector field $\dot{x} = f(x,y), \dot{y} = \epsilon g(x,y)$.
* **Universality:** **System-specific.** It only applies to flows explicitly possessing a slow manifold structure, not generic dissipative systems.
* **The Importable Statement:**
> **Fenichel's First Theorem (1971).** If $M_0$ is a compact, normally hyperbolic invariant manifold for the unperturbed flow ($\epsilon=0$), then for sufficiently small $\epsilon > 0$, there exists a perturbed NHIM $M_\epsilon$ with an associated stable foliation $\mathcal{W}^s(M_\epsilon)$. The contraction along the fibers of $\mathcal{W}^s(M_\epsilon)$ (the rejection anchor) occurs on the $O(1)$ fast timescale, while the flow on $M_\epsilon$ (the wandering bulk) evolves on the $O(1/\epsilon)$ slow timescale.



#### Asymptotic Phase / Isochrons (Guckenheimer; Winfree)

* **The Gap:** Isochrons are a beautiful coordinate-free **frame**, but they are restricted *only* to systems where the attractor is a simple periodic orbit (limit cycle). They do not generalize to the chaotic wandering bulk you specified. They are a specific, low-dimensional instance of the stable foliation mentioned above.

#### Currents (Federer–Fleming) + Support Function

* **The Gap:** In dynamical systems, Federer-Fleming currents are realized as **Ruelle-Sullivan currents** or **Schwartzman asymptotic cycles**. While these are deeply intrinsic, coordinate-free objects, they encode the homology of the *attractor itself* (the accepted, wandering bulk). They do not isolate the *rejection* (contracting) directions. There is no standard "stable current" because the stable directions dissipate volume and do not form closed homological cycles.

#### Center-of-mass / Noether Currents / Averaging Theory

* **The Gap:** All three of these frameworks require conservative dynamics or symmetries (Hamiltonian mechanics, continuous Lie group symmetries, or Hamiltonian adiabatic invariants). Generic dissipative flows break Noether symmetries; there is no globally conserved inertial frame that completely decouples from internal chaotic motion without external forcing.

---

### Summary for your Outbound Channel

If you require the separation of timescales to be a free, natural property of all chaotic dissipative flows, your object is the **Oseledets Stable Bundle** (a frame) living in **Ergodic/Pesin Theory**. The separation is generic, driven by the gap between exponential frame alignment (Lyapunov spectrum) and statistical measure convergence (spectral gap).

If you require the bulk to functionally "freeze" relative to the rejection contraction, your object is the **Stable Foliation of a NHIM** living in **Geometric Singular Perturbation Theory (Fenichel)**. However, this separation is strictly tuned by a small parameter and is not universal.

The concept of a "rejection current" as a Federer-Fleming object does not exist in the standard literature, because contracting directions do not close into invariant cycles; they must be modeled as measurable tangent frames or conditional measures.
model c:
I'll conduct a systematic search across the candidate homes to identify whether this "rejection anchor" — a fast-stabilizing intrinsic current/frame of the contracting part of a dissipative flow — is a named object, and whether the timescale separation is generic or tuned.


**Verdict.** There is **no single named invariant** in the literature that exactly matches the “rejection anchor” — a coordinate-free current/frame of the *contracting* part that freezes while the attractor and trajectory wander. However, the object sits at the intersection of three established homes, and the sharpest match is the **stable foliation of a normally hyperbolic invariant manifold** (Fenichel theory). The critical discriminator is that the timescale separation is **not generic** for arbitrary dissipative flows: it is either **tuned** (explicit small parameter) or **generic only within a restricted hyperbolic class**. Without such structure, “an averaged object converges while the path wanders” collapses to the bare ergodic theorem with no genuine gap.

---

### 1. The name — what is the object?

The “rejection vector field” \(V(x)\) — the component that contracts toward / excludes from the viable region — is the **stable distribution** \(E^{s}\) transverse to the attractor. The object built from it is the **stable foliation** \(W^{s}\) (or in the limit-cycle case, the **isochron foliation**). In geometric terms this is a **foliation cycle / current**: the stable lamination can be viewed as a de Rham–Federer–Fleming current by integrating differential forms over the stable leaves. It is explicitly *not* a centroid; it is a frame (the field of tangent spaces to the stable leaves) or equivalently a current of integration.

- **Special case (limit cycles):** The stable foliation is the **isochron foliation** of Guckenheimer and Winfree — the level sets of asymptotic phase \(\Theta(x)\). The gradient \(\nabla\Theta\) is the coordinate-free frame, and the isochrons are precisely the manifolds of points that share the same “rejected” transverse dynamics.
- **General case (manifolds):** For a normally hyperbolic invariant manifold \(M\), the stable foliation \(W^{s}(M)\) is invariantly fibered by stable leaves \(W^{s}(p)\) for \(p \in M\), with \(T_{p}W^{s}(p) = E^{s}_{p}\).

No standard term combines “current of the contracting part + freezing while bulk wanders” into one named object. The closest named construct is the **stable foliation** (or **isochron foliation** in the periodic case).

---

### 2. The crux — is the timescale separation generic, tuned, or nonexistent?

**Answer: TUNED for Fenichel; GENERIC-WITHIN-HYPERBOLICITY for Ruelle resonances; NONEXISTENT for generic dissipative flows without extra structure.**

| Home | Separation? | Discriminator |
|------|-------------|---------------|
| **Fenichel / NHIM** | Genuine: \(\tau_{\text{anchor}} \ll \tau_{\text{wander}}\) | **TUNED** — requires explicit small parameter \(\varepsilon \ll 1\) (fast-slow structure) or normal hyperbolicity with spectral gap. The stable foliation converges exponentially in the fast time while the slow manifold drifts on the slow time. |
| **Ruelle–Pollicott resonances** | Genuine: spectral gap gives exponential convergence to equilibrium | **GENERIC within mixing Anosov/hyperbolic systems** — the transfer operator has a spectral gap, so statistical properties (the SRB measure, and dually the stable foliation encoded in left eigenfunctions) converge exponentially fast. But this is *not* generic across all dissipative flows; it requires uniform or nonuniform hyperbolicity + mixing. |
| **Bare ergodic theory (SRB)** | No separation | **GENERIC but trivial** — Birkhoff/SRB guarantees convergence of time averages for a.e. initial condition, but provides *no* rate and no timescale gap. The “anchor” and the “wander” are on the same timescale. |

**The precise gap:** For a generic dissipative flow that is *not* normally hyperbolic and *not* uniformly hyperbolic, there is **no theorem** guaranteeing that a current built from the stable distribution converges faster than the attractor drifts. The observation that “\(\dot{\mu}(t) \to 0\) while \(M(t)\) and \(x(t)\) keep evolving” is, in full generality, merely the free ergodic theorem. A genuine separation \(\tau_{\text{anchor}} \ll \tau_{\text{wander}}\) requires either:
- an **explicit timescale parameter** (Fenichel: \(\varepsilon \to 0\)), or
- **hyperbolicity + mixing** (Ruelle spectral gap).

---

### 3. Intrinsic form — current, frame, support, or measure?

The right object is a **current** (or equivalently a **foliation / frame**), not a measure and not a centroid.

- **Current:** The stable foliation \(W^{s}\) defines a current \(T_{W^{s}}\) by integration of compactly supported differential forms over the stable leaves. This is coordinate-free and survives perturbations that destroy pointwise information. In the limit-cycle case, the isochron current is the level-set current of \(\Theta\).
- **Frame:** The field of stable subspaces \(E^{s}(x)\) (or the gradient frame \(\nabla\Theta\) for isochrons) is a moving frame. For limit cycles, the isochron frame is coordinate-free up to a constant phase shift.
- **Support function:** The support of the stable current is the basin of attraction. The support function of the stable foliation is intrinsic where the centroid is not.
- **Measure:** The SRB measure is a 0-current, but it is smooth along the *unstable* foliation and singular along the stable foliation. The “rejection” part is not captured by the SRB measure alone; it is captured by the *geometry* of the stable foliation.

---

### 4. Universality — does it recur?

- **Within normally hyperbolic systems:** Yes. The stable foliation of a NHIM is a universal feature — it persists under \(C^{1}\)-small perturbations and its existence is guaranteed by normal hyperbolicity (an open condition).
- **Within hyperbolic systems:** Yes. The stable lamination and its associated Ruelle–Sullivan-type current are universal for Anosov and Axiom A attractors.
- **Across all dissipative systems:** **No.** Normal hyperbolicity and uniform hyperbolicity are *not* dense in the space of all dissipative flows. The rejection anchor is not a universal invariant of arbitrary dissipative dynamics.

---

### 5. The importable statement

**For the tuned case (Fenichel / NHIM):** This is the single cleanest result that captures the “anchor freezes while substrate wanders” phenomenon.

> **Fenichel’s First Theorem** (Fenichel 1971; Hirsch–Pugh–Shub 1977).  
> Let \(M_{0} \subset \mathbb{R}^{n}\) be a compact, connected, \(C^{r}\) normally hyperbolic invariant manifold for a \(C^{r}\) flow, with stable normal bundle \(E^{s}\). Then there exists \(\varepsilon_{0} > 0\) such that for the fast-slow system
> \[
> \varepsilon \dot{x} = f(x,y,\varepsilon), \quad \dot{y} = g(x,y,\varepsilon),
> \]
> with \(0 < \varepsilon \leq \varepsilon_{0}\), there is a locally invariant \(C^{r}\) slow manifold \(M_{\varepsilon}\) within \(O(\varepsilon)\) of \(M_{0}\), normally hyperbolic with the same stability type. Moreover, the stable foliation \(W^{s}(M_{\varepsilon})\) satisfies: for each \(p \in M_{\varepsilon}\), every \(q \in W^{s}_{\text{loc}}(p)\) converges to the orbit of \(p\) exponentially fast in the fast time:
> \[
> \|\varphi^{t}(q) - \varphi^{t}(p)\| \leq C_{s} e^{\lambda_{s} t}, \quad \lambda_{s} < 0,
> \]
> while the flow on \(M_{\varepsilon}\) evolves on the slow time \(t = \varepsilon \tau\).

**For the generic-within-hyperbolicity case (Ruelle resonances):**

> **Spectral Gap for Transfer Operators** (Ruelle 1986; Pollicott 1985; Liverani 2004; Dyatlov–Zworski 2019).  
> Let \(f: M \to M\) be a transitive \(C^{1+\alpha}\) Anosov diffeomorphism. The transfer operator \(\mathcal{L}_{f}\) acting on an appropriate anisotropic Banach space has essential spectral radius strictly less than 1. The eigenvalue \(1\) is simple and corresponds to the SRB measure \(\mu_{\text{SRB}}\). The remainder of the spectrum lies in a disk of radius \(\rho < 1\), yielding exponential decay of correlations: for Hölder observables \(\varphi, \psi\),
> \[
> \left| \int (\varphi \circ f^{n}) \psi \, d\mu_{\text{SRB}} - \int \varphi \, d\mu_{\text{SRB}} \int \psi \, d\mu_{\text{SRB}} \right| \leq C \rho^{n}.
> \]
> The stable foliation is encoded in the left eigenspaces (dual to the SRB measure), and the spectral gap provides the exponential rate at which statistical properties “freeze.”

---

### Candidate homes — confirm or rule out

| Candidate | Verdict | Reason |
|-----------|---------|--------|
| **Ergodic theory / SRB measures** | **Ruled out as direct home** | The SRB measure governs statistics but is smooth along the *unstable* foliation, singular along the stable. It provides no intrinsic “rejection current” and no timescale gap without mixing/hyperbolicity. |
| **Fast–slow / Fenichel (GSPT)** | **Confirmed — closest match** | The stable foliation of the slow manifold is exactly the rejection anchor. The timescale separation is genuine but **tuned** via \(\varepsilon \ll 1\). |
| **Averaging / adiabatic invariants** | **Ruled out** | Adiabatic invariants are conserved/slow quantities built from the *slow* variables, not from the contracting/rejection vector field. |
| **Asymptotic phase / isochrons** | **Confirmed — special case** | For limit cycles, the isochron foliation is the coordinate-free rejection frame. It generalizes to slowly varying cycles but the non-autonomous convergence theory is less complete. |
| **Center-of-mass / Noether currents** | **Ruled out** | These are Hamiltonian/conservative constructions. The dissipative analogue is the inertial/slow manifold, not a Noether current. |
| **Currents (Federer–Fleming) + support** | **Confirmed — intrinsic form** | The stable foliation is naturally a geometric current. The support function is intrinsic. But the convergence-while-wandering theorem lives in Fenichel/Ruelle, not in GMT alone. |

---

### Summary

The rejection anchor is **not a single named invariant**. Import it as the **stable foliation of a normally hyperbolic invariant manifold** (Fenichel) or, in the periodic case, as the **isochron foliation** (Guckenheimer–Winfree). The timescale separation \(\tau_{\text{anchor}} \ll \tau_{\text{wander}}\) is **real but tuned** in Fenichel theory (via \(\varepsilon\)), and **generic only within hyperbolic systems** via the Ruelle–Pollicott spectral gap. For a generic dissipative flow with no explicit small parameter and no hyperbolicity, the separation is **nonexistent** — convergence is the bare ergodic average.
