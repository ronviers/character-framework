# outbound prompt (Phase A — send this)

---

### Identification/derivation prompt — is the cycle-affinity sign a *universal invariant* with a classification theory?

Self-contained nonequilibrium-statistical-mechanics / topology / category-theory question for the
outbound research channel. **No domain jargon by design** — any strong stochastic-thermodynamics,
algebraic-topology, singularity-theory, or category-theory model should engage cold. **The goal is
identification, then a forced classification** (or a clean negative). We have a candidate invariant of
driven systems and one question: is it *universally* the invariant of a single classifying structure,
with genuine equivalence classes, or merely a substrate-by-substrate quantity sharing a name? We want
the **named established structure + the explicit classifying object** so we can import it — or a clear
"there is none; it is substrate-specific," which is equally usable.

#### 0. The setup (plain)

A driven, dissipative stochastic system sits in a nonequilibrium steady state. Its drift splits into a
relaxational (gradient) part and a circulating (transverse) part,

```
b(x) = −a(x) ∇V(x)  +  𝒜 · l(x) ,     ⟨l, ∇V⟩ = 0 ,
```

and `𝒜 ≥ 0` measures the steady circulation (the cycle affinity; `𝒜 = 0` is equilibrium / detailed
balance). The object of interest is **`sign(𝒜)`** — the *sense* of the circulation. Three established
facts about it (the part we already have):

- **Gauge-irremovable.** `sign(𝒜)` is invariant under relabeling the states and under any smooth
  retuning of the rates or the drive strength. It flips only when the cycle is **rewired** (a
  transition added, cut, or reversed) or driven through `𝒜 = 0`.
- **A signed-graph invariant.** A nonzero affinity is exactly a *frustrated* (Harary-unbalanced) signed
  cycle; `sign(𝒜)` is the gauge-irremovable sign of that unbalance (Kolmogorov irreversibility).
- **Sub-integer, and superselected.** It is a sign, not an integer winding number (its holonomy is
  sub-integer). And it is *barred from the leading large-deviation observables* of the relaxational
  sector (the quasipotential / escape barrier is invariant under `𝒜`; transverse-decomposition,
  Graham–Haken, Freidlin–Wentzell): the metric sector can **modulate** it but cannot **create or
  destroy** it — a superselection rule.

The same structure is read off systems that share nothing else: chemical reaction networks, Brownian
gyrators, driven colloids on a ring, quantum error-correcting codes, aging glasses.

#### 1. The question

**Is `sign(𝒜)` — the gauge-irremovable cycle-affinity sign — universally (model-independently) the
invariant of a single classifying structure, with substrate-independent equivalence classes of
protected circulations, or merely the leading analytic/topological label of each substrate taken
separately?**

By "classifying structure" we mean: a setting in which protected circulations fall into equivalence
classes such that (i) two circulations are in the same class iff connected by a structure-preserving
deformation that does **not** cross the singular set `𝒜 = 0`; (ii) crossing `𝒜 = 0`, or rewiring,
moves between classes; (iii) the classes are the *same objects* across substrates. Candidate homes:

- **signed-graph / gauge cohomology** (the balance class of a signed graph; `sign(𝒜)` as an element of
  `H¹(·, ℤ₂)` or the graph's balance group);
- **homotopy** — `π₀` of the space of admissible drift fields with the `𝒜 = 0` locus removed (classes
  = path-components);
- **cobordism / a fusion (monoidal) algebra** — circulations that can be born, **merge** (coalescence),
  and **split** (minting), giving a creation/annihilation or fusion structure on the classes;
- **singularity / catastrophe theory** — the classes as strata, the `𝒜 = 0` events as their bounding
  singularities (Thom/Arnold/Golubitsky–Schaeffer);
- **a category of characters** — objects = protected circulations, morphisms = structure-preserving
  maps, a (symmetric monoidal) composition = coupling/minting;
- **a large-deviation universality class** — substrates sharing one rate function / quasipotential,
  indexed by `sign(𝒜)` (the metric sector identical, the topological sector the label).

#### 2. Tasks (be specific; cite)

1. **Name the structure, or state there is none.** Is there an established, model-independent
   classification of protected nonequilibrium circulations under which `sign(𝒜)` is the universal
   invariant? If yes: the theorem, its hypotheses, the **explicit classifying object** (which
   group/space/category, what the classes are), and the canonical reference. If no single result, say
   which candidate above applies under what conditions, and where universality fails.
2. **The invariant's range.** Is the protected bit `ℤ₂` (a sign), `ℤ` (an integer winding), or richer?
   We have evidence it is gauge-irremovable but **sub-integer** — so an integer-invariant classification
   (Chern/winding) is the wrong import unless justified. Confirm or correct.
3. **The morphisms (deformation / transport).** Characterize the structure-preserving maps that
   **preserve** a class and the singular events that **change** it. Do coarse-graining (scale) and
   cross-substrate maps preserve `sign(𝒜)`? State what a "structure-preserving map" between two
   different substrates' circulations *is*.
4. **Composition.** Minting (coupling creates a protected bit **neither part carried**) and coalescence
   (merging). Is there an algebra / monoidal / fusion structure on the classes (creation–annihilation,
   or a tensor of characters)? Named precedent?
5. **Which manifold.** Does the classification live on the **state space** (the circulation geometry at
   a fixed operating point) or the **parameter / control space** (as couplings are swept)? Distinguish
   sharply; do not conflate.
6. **The single importable statement — or the negative.** Distil to one citable proposition: either
   *"protected nonequilibrium circulations are classified by [named structure], with `sign(𝒜)` the
   universal invariant [Author, Year, Thm N]"* (with hypotheses + a cross-substrate check), **or**
   *"there is no model-independent classification; the cycle-affinity sign is a substrate-specific
   quantity (a family of analogies, not one invariant)."* A clean negative is a fully acceptable,
   expected outcome — say so plainly if that is the truth.

#### 3. Constraints / what makes a report unusable

- **Forced, not fitted.** A classification reverse-engineered to reproduce a chosen set of examples is
  the failure we are guarding against. The structure must come from a named result and *then* be checked
  against the substrates.
- **Substrate-independence is the bar.** A scheme that classifies only within one substrate family
  (only reaction networks, only codes) does not answer the question — it confirms the negative.
- **Sub-integer, not integer.** Do not assume an integer topological invariant; the object is a
  gauge-irremovable sign. If you claim an integer, justify it.
- **Modulation, not generation.** The metric sector cannot create or destroy the bit (superselection).
  Any construction in which local/metric structure *generates* the protected class is wrong.
- **State the manifold.** Leaving state-space vs parameter-space ambiguous, or bridging them silently,
  makes the report unusable (Task 5 is load-bearing).
- **Be honest about a negative.** If `sign(𝒜)` is generically substrate-specific with no universal
  classifying structure, say so — that retires the framework's central bet cleanly, which is a result,
  not a disappointment.


model a:
This is a very strong outbound prompt. It does something that many framework-originated questions fail to do: it forces the responder to either identify an existing mathematical object or return a clean negative.

A few observations before sending it.

### 1. The strongest part is the forced negative

The most valuable sentence in the entire prompt may be:

> "A clean negative is a fully acceptable, expected outcome."

Without that, respondents will tend to "find" a classification by stretching analogies.

Your prompt instead asks:

> Is there actually a known classifying object?

That is exactly the right question.

---

### 2. The likely outcome is not "one universal structure"

Based on the mathematics already identified around your framework, I would assign high prior probability to the following answer:

> There is no known universal classifying structure for all nonequilibrium circulations.

Instead, different mathematical structures appear in different regimes:

| Regime                        | Classifying object                                         |
| ----------------------------- | ---------------------------------------------------------- |
| Finite Markov networks        | cycle space / graph cohomology                             |
| Signed networks               | Harary balance, ℤ₂ classes                                 |
| Continuous stochastic flows   | homology of current loops                                  |
| Geometric pumping             | Berry-type holonomies                                      |
| Parameter-space singularities | catastrophe strata                                         |
| Fusion/merging processes      | monoidal categories, operads, reaction-network composition |

Those are all real mathematical structures.

The difficult question is whether they are shadows of **one deeper object**.

I do not know a standard theorem that says they are.

---

### 3. The biggest hidden assumption is here

You currently write:

> The same structure is read off systems that share nothing else: chemical reaction networks, Brownian gyrators, driven colloids on a ring, quantum error-correcting codes, aging glasses.

A strong respondent may immediately challenge this.

Not because the examples are wrong, but because:

> "same sign appears"

does not imply

> "same equivalence class exists."

That distinction is exactly what the prompt is trying to settle.

I might strengthen the wording slightly:

> "A quantity playing the role of a gauge-irremovable circulation sign appears in systems that otherwise share little structure..."

That prevents respondents from attacking the premise rather than answering the classification question.

---

### 4. The deepest issue is Task 4

Task 4 is where your framework either becomes mathematics or remains analogy.

You ask:

> Minting and coalescence.

This is essentially asking:

> Do protected circulations form a monoidal category?

or

> Do they form a fusion algebra?

or

> Are they objects in a cobordism theory?

That is not a routine NESS question.

It is probably the most original part of the prompt.

If a respondent can identify an existing composition law, that would be an important import.

If they cannot, that is also highly informative.

---

### 5. The state-space / parameter-space distinction is load-bearing

You were right to make this a dedicated task.

Many people unconsciously slide between:

**State-space topology**

* loops of probability current
* cycle spaces
* homology

and

**Parameter-space topology**

* Berry phases
* pumping cycles
* bifurcation structure
* catastrophe strata

These are different manifolds.

A large fraction of apparent "topological" classifications in nonequilibrium physics actually live in parameter space, not state space.

If respondents fail Task 5, the report is probably unusable.

---

### 6. The one mathematical import I suspect may emerge

If I had to guess where the investigation ends, it would be somewhere near:

> path components of the space of admissible irreversible generators with the detailed-balance locus removed.

In other words,

[
\mathcal M
==========

{\text{admissible driven systems}}
\setminus
{\mathcal A=0}.
]

Then

[
\pi_0(\mathcal M)
]

becomes the natural classifier.

That would make your protected bit literally a connected-component label.

Notice how much of your framework immediately follows:

* smooth deformation preserves class,
* crossing (\mathcal A=0) changes class,
* rewiring changes class,
* sign behaves like a superselection label.

That is mathematically clean.

The question is whether anybody has already proved and named it.

Your prompt is precisely designed to find out.

---

### 7. One thing I would add

I would insert a final forced question:

> **7. Minimal counterexample.**
>
> If you claim no universal classification exists, provide two explicit driven systems with identical nonzero `sign(𝒜)` that cannot be placed in the same class under your proposed structure-preserving maps.

That prevents a weak negative of the form:

> "there is no universal theory"

without demonstrating where universality actually breaks.

It forces the respondent to exhibit the obstruction.

---

Overall, this is one of the better "identification" prompts you've produced. It is not asking respondents to validate Character. It is asking them to identify a known mathematical object—or prove that no such object exists. That is exactly the kind of question that can actually kill or strengthen a framework.

model b:
I appreciate the clarity and strict parameters of your prompt. As an AI, I do not have personal stakes in any framework, so I can give you the unvarnished mathematical reality of this problem.

To answer your overarching question immediately: **There is no established, model-independent classifying structure for which $\text{sign}(\mathcal{A})$ serves as a universal invariant.** While the transverse/circulating sector is a rigorous feature of nonequilibrium steady states (NESS), elevating its *sign* to a substrate-independent topological or categorical phase invariant is an analogy, not a recognized mathematical fact. The structural apparatus you are hunting for—a universal category or cobordism ring of protected circulations—does not currently exist in the literature.

Here is the precise breakdown of your tasks, grounded strictly in established stochastic thermodynamics and algebraic topology.

### 1. Name the Structure, or State There is None

**There is no universal classifying structure.** The cycle-affinity sign is a substrate-specific quantity.

The closest established framework is **Graph Cohomology (Schnakenberg Network Theory)**, but it fails the substrate-independence test. Under Schnakenberg theory (and its continuous analogs via discrete exterior calculus or de Rham cohomology), the affinities are classified as elements of the first cohomology group of the **specific state space**.

* **The Object:** $\mathcal{A}$ is an element of $H^1(\mathcal{X}; \mathbb{R})$, where $\mathcal{X}$ is the state-space manifold or Markov graph.
* **Where Universality Fails:** Because the homology depends entirely on the topology of $\mathcal{X}$, the classification is strictly intra-substrate. There is no universal "space of admissible drift fields" that unifies the state space of a chemical reaction network with the state space of a Brownian gyrator. The $\mathcal{A} = 0$ locus is not a universal bounding singularity; it is simply the detailed-balance hyperplane in the specific thermodynamic force space of that particular system.

### 2. The Invariant's Range

The invariant is indeed **sub-integer** (specifically, a $\mathbb{Z}_2$ label mapping to $\{+, -\}$), but it is crucial to recognize *why*.

$\mathcal{A}$ itself is a continuous, real-valued thermodynamic force ($\mathcal{A} \in \mathbb{R}$) representing entropy production per cycle. Taking $\text{sign}(\mathcal{A})$ reduces this to a $\mathbb{Z}_2$ observable indicating the direction of the mean probability current. It is sub-integer because it is fundamentally not a topological winding number (like a Chern number, which requires a periodic parameter space or Brillouin zone). It is merely an inequality indicator regarding a dissipative current. Confirming your suspicion: any attempt to import integer-invariant classifications (like K-theory for topological insulators) is mathematically unjustified here.

### 3. The Morphisms (Deformation / Transport)

Because there is no universal category, there are no established **cross-substrate** structure-preserving maps. You cannot map the circulation of a colloidal ring onto a quantum error-correcting code in a way that mathematically "preserves" the $\mathbb{Z}_2$ sign through a formal functor.

For **intra-substrate** maps (within the same model):

* **Structure-Preserving Maps:** These are smooth deformations of the transition rates (or the potential landscape $V(x)$) that do not cross the detailed-balance manifold ($\mathcal{A} \neq 0$).
* **Singular Events:** Rewiring the graph (changing the Betti number of the state space) or retuning parameters such that the macroscopic affinity crosses zero.
* **Coarse-Graining:** Decimation of states preserves the macroscopic affinity (and its sign) *only if* the target cycle is not traced out. If the coarse-graining traces over the loop carrying the circulation, the macroscopic affinity is projected out into effective equilibrium or localized noise, destroying the $\mathbb{Z}_2$ bit.

### 4. Composition

**There is no established monoidal, fusion, or tensor algebra for these classes.** While you can physically couple two driven systems (minting) or merge cycles (coalescence), this operation is handled entirely via standard graph-cartesian products (for discrete states) or tensor products of the underlying Fokker-Planck operators. There is no named precedent or "fusion category of nonequilibrium signs" that abstracts this process away from the messy metric details of the Fokker-Planck or Master equations.

### 5. Which Manifold

This is the most critical distinction: **The established classification (Graph Cohomology) lives strictly on the STATE SPACE.** The first Betti number, the cycles, and the orientations are geometric properties of the transition network or physical space at a *fixed* operating point. The $\mathbb{Z}_2$ sign does not live on the parameter/control space. Conflating the state-space loops (which generate $\mathcal{A}$) with parameter-space loops (which generate geometric phases or Berry curvatures) is a common failure point in attempting to build a topological thermodynamics.

### 6. The Single Importable Statement

*"There is no model-independent classification; the gauge-irremovable cycle-affinity sign is a substrate-specific quantity—a local property of state-space graph cohomology, representing a family of physical analogies rather than a single universal invariant."*

**Final Assessment:** Your framework's central bet—that $\text{sign}(\mathcal{A})$ is the shadow of a universal, cross-domain classifying structure—should be cleanly retired. The metric sector indeed modulates it without destroying it (superselection), but this robustness comes from the algebraic rigidity of the state-space graph (Schnakenberg theory), not from a universal category of protected circulations.

"If you claim no universal classification exists, provide two explicit driven systems with identical nonzero sign(𝒜) that cannot be placed in the same class under your proposed structure-preserving maps."

This is the exact right challenge. If a universal classification exists, having identical $\text{sign}(\mathcal{A})$ must guarantee that two systems belong to the same path-connected component in some overarching classifying space, mapped to one another without destroying the state space or passing through detailed balance ($\mathcal{A} = 0$).

Here are two explicit, ubiquitous nonequilibrium systems that both possess a steady, strictly positive circulation ($\text{sign}(\mathcal{A}) = +1$), yet are separated by an impenetrable topological and algebraic wall.

### 1. The Two Systems

**System A: A Discrete Chemical Reaction Cycle (Schnakenberg Graph)**
Consider a well-mixed chemical system undergoing a sequence of three elementary transitions: $X_1 \rightleftharpoons X_2 \rightleftharpoons X_3 \rightleftharpoons X_1$.

* **State Space ($\mathcal{X}_A$):** A discrete graph consisting of 3 vertices and 3 edges (a 1-dimensional simplicial complex).
* **Dynamics:** A continuous-time Markov jump process governed by a finite $3 \times 3$ transition rate matrix $W$.
* **The Affinity:** Determined by the macroscopic cycle product of the rates:

$$\mathcal{A}_A = \ln \left( \frac{W_{12} W_{23} W_{31}}{W_{21} W_{32} W_{13}} \right)$$



Assume we drive the system such that $\mathcal{A}_A > 0$. Therefore, $\text{sign}(\mathcal{A}_A) = +1$.

**System B: A Continuous Driven Colloid on a Ring**
Consider an overdamped Brownian particle driven by a non-conservative constant force $F$ along a periodic one-dimensional ring of circumference $L$, subject to thermal noise.

* **State Space ($\mathcal{X}_B$):** A continuous 1-manifold, the circle $S^1$.
* **Dynamics:** A continuous Langevin/Fokker-Planck process governed by an unbounded differential operator $\mathcal{L} = \partial_x (D \partial_x - \mu F)$.
* **The Affinity:** Determined by the work done by the non-conservative force over the thermal energy:

$$\mathcal{A}_B = \frac{F L}{k_B T}$$



Assume $F > 0$. Therefore, $\text{sign}(\mathcal{A}_B) = +1$.

---

### 2. The Obstructions to a Structure-Preserving Map

To place these two systems in the same equivalence class under a universal structure, there must exist a continuous deformation—a structure-preserving map or homotopy—connecting the matrix $W$ to the differential operator $\mathcal{L}$ such that $\mathcal{A}$ remains strictly positive throughout the deformation.

This is impossible for three rigorous mathematical reasons:

#### A. Topological Incompatibility (The State Space Barrier)

A structure-preserving map must be a homeomorphism (or at least a continuous, invertible map) between the underlying domains. You cannot continuously deform a set of 3 discrete points into a continuous circle $S^1$. The topology of the state spaces is fundamentally distinct. To transform System A into System B, you must take a continuum limit (e.g., let the number of discrete states $N \to \infty$ while the lattice spacing $a \to 0$). This limit is highly singular; the state space literally changes dimension and cardinality.

#### B. Algebraic Incompatibility (The Operator Barrier)

System A is governed by a bounded operator (a finite matrix). System B is governed by an unbounded differential operator on an infinite-dimensional Hilbert space ($L^2(S^1)$). There is no continuous path in any shared functional space connecting a bounded matrix to an unbounded differential operator that preserves the algebraic definition of the affinity. The definition of $\mathcal{A}$ must undergo a discontinuous translation from a discrete sum of logarithmic rate ratios to a continuous spatial integral of thermodynamic forces.

#### C. The "Embedding" Failure

One might attempt to bypass the topological wall by embedding both systems into a larger, universal "space of all possible probability measures." However, when coarse-graining System B onto a 3-state lattice to match System A, or taking the continuum limit of System A to match System B, you inevitably introduce effective memory (non-Markovianity) or divergent transition rates. A map that forces a system to lose its Markovian property or pass through a divergence is, by definition, a singularity. It violently breaks the structure-preserving requirement.

---

### The Verdict

Both systems definitively share the label $\text{sign}(\mathcal{A}) = +1$. They both exhibit Kolmogorov irreversibility and broken detailed balance.

However, they cannot be placed in the same equivalence class because **they do not live in the same classifying space to begin with.** System A's affinity belongs to the first cohomology group of a discrete triangle graph; System B's affinity belongs to the first de Rham cohomology group of the continuous circle.

The fact that they share a $+1$ sign is a profound physical analogy regarding entropy production, but it is not a shared topological invariant of a unified mathematical structure.

model c:

I'll analyze this research prompt carefully and search for the relevant mathematical and physical literature to address whether `sign(𝒜)` — the cycle-affinity sign — admits a universal classifying structure.

Let me search for the key concepts involved: signed graph theory in nonequilibrium statistical mechanics, gauge cohomology of Markov processes, and topological classification of nonequilibrium steady states.
Now I have gathered sufficient material. Let me compose the research report addressing all six tasks in the prompt.

---

## Research Report: Is `sign(𝒜)` a Universal Invariant with a Classifying Structure?

---

### Executive Summary

**The clean negative is the honest answer.** There is **no established, model-independent classification** of protected nonequilibrium circulations under which `sign(𝒜)` is a universal invariant with substrate-independent equivalence classes. The cycle-affinity sign is a **substrate-specific quantity** — a family of deep analogies across substrates, not one invariant under a single classifying structure. What *does* exist are powerful but **substrate-dependent** frameworks (gauge cohomology of Markov processes, signed-graph switching theory, large-deviation cycle theory) that each capture `sign(𝒜)` within their domain, but none unify across substrates with the required universality.

---

### Task 1: Name the Structure, or State There Is None

**There is none — as a single universal classifying structure.**

The literature reveals three candidate frameworks, each powerful within its substrate family but failing the universality bar:

| Candidate | Domain | What It Classifies | Why It Fails Universality |
|-----------|--------|-------------------|--------------------------|
| **Gauge cohomology / Wilson-loop flatness** (Polettini 2011) | Discrete-state Markov processes on finite graphs | Flat vs. non-flat connections; `sign(𝒜)` encoded in Wilson loop W(γ) = exp(∮_γ A) where A_ij = log(w_ij/w_ji) | Requires a graph structure; does not extend to continuous diffusions, quantum codes, or aging glasses without ad hoc discretization |
| **Signed-graph switching classes** (Zaslavsky, Harary) | Graphs with signed edges | Balance vs. unbalance; frustration index l(Σ); switching equivalence classes | Purely combinatorial; no dynamical content; does not see rates, drive strength, or steady-state currents |
| **Large-deviation cycle theory** (Schnakenberg 1976; Andrieux & Gaspard 2007) | Stochastic thermodynamics of Markov processes | Cycle affinities as thermodynamic forces; fluctuation theorems for currents | Rate-function universality holds for *current statistics* given fixed affinities, not for classifying affinities themselves across substrates |

The gauge-theoretic framework by Polettini  establishes that detailed balance ↔ flat connection ↔ all Wilson loops = 1. The thermodynamic force A_ij = log(w_ij/w_ji) is the gauge potential, and Kolmogorov's criterion is equivalent to flatness. However, this construction is **intrinsically tied to a discrete graph with oriented edges**. The Wilson loop W(γ) = exp(∮_γ A) lives on the **state-space graph**, not on a parameter space, and its value depends on the specific graph topology (number of cycles = |E| − |V| + 1). There is no canonical map from a Brownian gyrator or a quantum error-correcting code to this graph structure without arbitrary choices.

The signed-graph framework  provides switching equivalence classes where two signatures are equivalent iff they have the same set of negative cycles. The frustration index l(Σ) measures imbalance. But this is a **static combinatorial invariant** — it knows nothing of dynamics, dissipation, or the metric sector. It classifies graph signatures, not driven dissipative systems.

The large-deviation framework  gives fluctuation theorems for cycle currents: P({Φ_α})/P({−Φ_α}) = exp(Σ A_α Φ_α^t). The cycle affinities A_α are the parameters of the rate function. But this is a **representation theorem within a given substrate** (a fixed Markov generator), not a classification across substrates.

**Conclusion for Task 1:** No single named theorem, group, space, or category classifies `sign(𝒜)` universally. The quantity is substrate-specific.

---

### Task 2: The Invariant's Range

**The protected bit is ℤ₂ (a sign), not ℤ.**

The evidence is overwhelming:

- The cycle affinity itself is a **real number** ℱ_c = Σ ln(R_ji/R_ij) ∈ ℝ ∪ {∞}. Its sign is the gauge-irremovable information.
- The **winding number** ω_c(u) = ||(1/2π) Σ arg(u_j/u_i)||_nc ∈ {1, ..., ⌈n_c/2⌉ − 1} is an integer, but it is **not** the invariant in question — it characterizes eigenvector structure, not the circulation sense .
- The Wilson loop W(γ) = exp(∮_γ A) ∈ ℝ⁺ is a positive real. Its deviation from 1 (W ≠ 1) signals nonequilibrium, but the **sign of log W = ℱ** is the ℤ₂ invariant. There is no integer "winding" of the affinity itself — the affinity is a real circulation, not a quantized topological charge.
- In the gauge theory, the gauge group is (ℝ⁺, ×), not U(1). There is no periodicity that would allow integer winding. The connection is real-valued, not complex-phased.

The prompt's observation that the invariant is "sub-integer" is correct and crucial. An integer classification (Chern number, winding number in the topological-insulator sense) would require a **compact fiber** or **periodic structure** (e.g., U(1) gauge group, Bloch bands). The thermodynamic gauge group (ℝ⁺, ×) is non-compact. The only discrete remnant is the sign of the affinity, which is ℤ₂.

**Correction to candidate imports:** Do not import Chern/winding number theory. The correct import is **signed-graph balance theory** (Harary 1953) or **gauge-flatness detection** (Polettini 2011), both of which yield ℤ₂-classification at the level of `sign(𝒜)`.

---

### Task 3: The Morphisms (Deformation / Transport)

**Within a substrate:** Structure-preserving maps that preserve `sign(𝒜)` are **gauge transformations** (local rescalings of the probability density) combined with **smooth retuning of rates** that do not cross ℱ_c = 0. In Polettini's framework , a gauge transformation is ρ'_i = e^{−φ_i} ρ_i, with corresponding rate transformation w'_ij = e^{φ_j} w_ij. This leaves currents invariant and preserves all Wilson loops. The singular event that changes `sign(𝒜)` is crossing ℱ_c = 0 (a **stalling bifurcation**) or **rewiring** (adding/cutting/reversing a transition, changing the graph topology).

**Across substrates:** There is **no established notion** of a "structure-preserving map" between, say, a chemical reaction network and a quantum error-correcting code that preserves `sign(𝒜)`. The analogies are heuristic:
- Both have cycles with directed flow
- Both violate detailed balance
- Both have a "sense" of circulation

But there is no functor, no natural transformation, no homomorphism that maps the cycle affinity of one to the other while preserving the sign. The substrates share **phenomenology**, not **mathematical structure**.

**Coarse-graining:** Under coarse-graining of Markov chains , effective affinities are "dressed" by hidden degrees of freedom. The effective affinity Q_μ satisfies an integral fluctuation relation, but it is **not** simply the original `sign(𝒜)`. The hidden time-reversal dynamics flips the sign of affinities for cycles containing the coarse-grained edge . Thus coarse-graining does **not** preserve `sign(𝒜)` in any simple sense — it transforms the entire affinity structure.

---

### Task 4: Composition

**No established fusion / monoidal / creation-annihilation algebra exists on the classes of `sign(𝒜)`.**

The prompt asks about:
- **Minting:** coupling creates a protected bit neither part carried
- **Coalescence:** merging circulations
- **Fusion rules** or **tensor of characters**

There are **no named precedents** for this in the literature on nonequilibrium steady states. The closest analogues are:

1. **Mandelstam identity for Wilson loops** : W(γ₁ ∘ γ₂) = W(γ₁) W(γ₂). This is a **multiplicative composition of loops on the same graph**, not a fusion of distinct systems. It does not create a new protected bit from nothing.

2. **Cycle decomposition of entropy production** : σ = Σ_γ J_γ A_γ. The sum is over fundamental cycles. But adding two NESSs does not yield a simple rule for their affinity signs — the affinities add only if the systems are **non-interacting** and the cycles are independent.

3. **Signed graph homomorphisms** : There is a categorical product and coproduct of signed graphs, and the homomorphism order is a lattice. But this is **combinatorics**, not thermodynamics. The product of two switching classes does not correspond to coupling two physical systems.

4. **Dynamic Balance / Golden Ratio Möbius transformations** : This work proposes modular transformations (S_φ, T_φ) on a nonequilibrium parameter α, with fusion-like structure in an E₈ framework. But this is a **highly specific model** (Ising-like systems with antisymmetric Onsager coupling), not a universal composition law for `sign(𝒜)`.

**Conclusion:** The composition structure asked for does not exist in the literature. There is no known way to "add" two protected circulation signs to get a third, or to create one from nothing via coupling. The ℤ₂ nature of `sign(𝒜)` would suggest a ℤ₂ fusion rule (0+0=0, 0+1=1, 1+1=0), but this has no physical derivation in nonequilibrium thermodynamics.

---

### Task 5: Which Manifold

**This is load-bearing, and the answer is: both, but they are not the same object, and conflating them is the error to avoid.**

| Space | What lives there | What `sign(𝒜)` means there |
|-------|---------------|---------------------------|
| **State space** (the graph / manifold of microstates) | The gauge potential A_ij, the Wilson loops W(γ), the cycle affinities ℱ_c | `sign(𝒜)` is a **property of the connection** on the state-space graph. It is computed from the rates w_ij at a fixed operating point. Polettini's gauge theory lives here . |
| **Parameter / control space** (the space of drive strengths, temperatures, chemical potentials) | The bifurcation locus ℱ_c = 0, the stalling manifold, the nonequilibrium phase transition surface | `sign(𝒜)` is a **label of a connected component** of parameter space minus the singular set. Crossing ℱ_c = 0 is a bifurcation that flips the sign. |

**Critical distinction:** In the gauge-theoretic framework, the classification lives on **state space**. The Wilson loops are computed by circulating around cycles *on the graph*. The "moduli space" of flat vs. non-flat connections is a space of connections modulo gauge, but this is **not** the parameter space of the experimentalist.

In the **parameter space**, the singular set ℱ_c = 0 is a codimension-1 hypersurface (for each independent cycle). The sign of ℱ_c labels which side of this wall the system is on. This is the setting for **nonequilibrium phase transitions**  and **singularity theory** . But here, the classification is of **parameter regimes**, not of circulations themselves.

The prompt's superselection rule — that the metric sector can modulate but not create/destroy the bit — is consistent with the **state-space** picture: the quasipotential (metric sector) depends smoothly on parameters but is blind to `sign(𝒜)` . The bit is "topological" on state space and "superselected" in the large-deviation sense.

**Do not bridge them silently.** A map from parameter space to state space (assigning a connection to each parameter point) is a **section of a bundle**, not an identity. The classification on one does not automatically transport to the other.

---

### Task 6: The Single Importable Statement — The Negative

> **"There is no model-independent classification; the cycle-affinity sign is a substrate-specific quantity (a family of analogies, not one invariant)."**

This is the clean negative, and it is a **result**, not a disappointment. The frameworks that do exist are powerful but **domain-bound**:

1. **For discrete-state Markov processes on graphs:** `sign(𝒜)` is classified by the **gauge cohomology of the connection** (Polettini 2011) — flat (detailed balance) vs. non-flat (nonequilibrium), with the sign of the Wilson loop exponent as the ℤ₂ label. The classifying object is the **space of connections modulo gauge**, with the flat connections forming a single equivalence class. Reference: Polettini, *Nonequilibrium thermodynamics as a gauge theory*, EPL 97, 30003 (2012) [arXiv:1110.0608].

2. **For signed graphs (combinatorial skeleton):** `sign(𝒜)` corresponds to the **balance class** of the signed graph (Harary 1953; Zaslavsky). The classifying object is the **switching class** [Σ], characterized by the set of negative cycles. The frustration index l(Σ) quantifies imbalance. Reference: Zaslavsky, *Signed graphs*, Discrete Appl. Math. 4, 47–74 (1982).

3. **For stochastic thermodynamics (large deviations):** `sign(𝒜)` indexes the **asymmetry of the rate function** for cycle currents. The fluctuation theorem P({Φ})/P({−Φ}) = exp(Σ A_α Φ_α) holds, but this is a **representation**, not a classification. Reference: Andrieux & Gaspard, *Fluctuation theorem for currents and Schnakenberg network theory*, J. Stat. Phys. 127, 107–131 (2007).

4. **For eigenvalue localization:** `sign(𝒜)` > 0 is necessary for nonreal eigenvalues; the winding number ω_c(u) ∈ ℤ is an additional integer invariant of the eigenmode, but it is **not** `sign(𝒜)` itself. Reference: [arXiv:2605.15884] (2026).

**None of these frameworks agree on the classifying object across substrates.** The gauge theory needs a graph; the signed-graph theory needs a signature; the large-deviation theory needs a Markov generator; the eigenvalue theory needs a rate matrix. There is no **natural transformation** between these structures that would make `sign(𝒜)` a universal invariant.

---

### Final Assessment

The bet that `sign(𝒜)` is the universal invariant of a single classifying structure **does not pay off** with the current state of knowledge. The quantity is:

- **Gauge-irremovable** ✓ (within each substrate)
- **A signed-graph invariant** ✓ (within combinatorial structures)
- **Sub-integer (ℤ₂)** ✓ (not an integer winding)
- **Superselected** ✓ (metric sector cannot create/destroy it)

But it is **not substrate-independent**. The frameworks that capture it are **analogous** across domains, not **unified** under one theorem. The negative is clean and usable: it tells you that any framework claiming universality must first construct the cross-substrate map that no one has yet built.

---

### References (Key Sources)



- Polettini, M. *Nonequilibrium thermodynamics as a gauge theory*, arXiv:1110.0608 [cond-mat.stat-mech] (2011).
- [arXiv:2605.15884] *Cycle affinity and winding localize eigenvalues of Markov generators* (2026).
- Polettini, M. & Esposito, M. *Effective fluctuation and response theory*, J. Stat. Phys. 176, 94 (2019) [arXiv:1803.03552].
- Halaseh et al., *Geometry of nonequilibrium reaction networks*, arXiv:2208.01290.
- Andrieux, D. & Gaspard, P. *Fluctuation theorem for currents and Schnakenberg network theory*, J. Stat. Phys. 127, 107 (2007).
- Zaslavsky, T. *Signed graphs*, Discrete Appl. Math. 4, 47 (1982).
- Harary, F. *On the notion of balance of a signed graph*, Michigan Math. J. 2, 143 (1953).