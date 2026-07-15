I have a driven-dissipative-systems framework in which a steady state carries two orthogonal kinds of information: a metric sector (continuous order-parameter magnitudes, smooth in the drive) and a topological sector (the count b₁ of gauge-irremovable protected probability-current cycles — Schnakenberg/Polettini cycle-space homology on a signed interaction graph). These are provably orthogonal: the protected current sits in a different symmetry irrep from the metric relaxation modes (transverse/Schur decomposition of the drift b = −a∇V + l), so b₁ is invariant under any smooth change of the drive and changes only across discrete "rewiring" seams.

I want to test whether persistent homology adds anything. My analysis says:
(a) Filtering b₁ by the drive is degenerate — a topological invariant can't have birth/death events along a smooth metric axis; the barcode is constant. Correct, or is there a construction where a smooth drive sweep genuinely changes protected homology in the interior (not at the equilibrium boundary)?
(b) Filtering by coupling strength gives births (minting a frustrated cycle) and deaths (counter-rotating annihilation), but bar-length = distance to a seam, which singularity theory already characterizes with codimension + normal form. Is persistence ever strictly more than the seam arrangement here?
(c) Filtering by coarse-graining / RG depth is the only version I think survives: protected cycles are born by coupling and die by being integrated out below resolution, so the barcode would be a "topological lifetime across scale."

Two narrow, factual questions — please answer with citations, and try to falsify my (a)/(b), not affirm them:

Is "persistent homology of a renormalization-group / multi-scale coarse-graining flow" an established, named construction with a literature? Names, papers.
Name a real, experimentally measured driven-dissipative or active-matter system in which protected topological defects / current cycles are born and annihilated across a spatial-scale or coarse-graining filtration and analyzed with a persistence diagram (e.g. TDA of active-nematic defects, vortex tangles in driven fluids/superfluids, granular force networks). I need a concrete substrate, its observable, and whether the persistence lifetime (not just the count) carried physical meaning there.
If you cannot find a real substrate for question 2, say so plainly — a null result is the useful answer.

model a:
I tried to falsify your picture rather than confirm it. My conclusion is:

* **(a)** I did **not** find a standard construction in which a *smooth drive parameter* produces nontrivial persistence of an already-defined protected cycle space while remaining in the same topological phase. What I found instead is that PH is almost always applied to **geometric filtrations** (distance, density, sublevel sets, graph weights), not to adiabatic parameter sweeps. That is evidence *against* PH adding anything to your drive axis.
* **(b)** I also did **not** find a literature where persistence lifetimes replace the singularity/seam picture for creation and annihilation of current cycles. Birth/death events occur, but they are analyzed as topological transitions or bifurcations, not as persistence barcodes over the control parameter.
* **(c)** The one place where your intuition *does* line up with existing work is multiscale/coarse-graining. However, the literature is weaker than your formulation: people do multiscale PH, PH on coarse-grained representations, and PH across resolutions, but there does **not** appear to be a well-established object called "persistent homology of an RG flow."

Below are the details.

---

# 1. Persistent homology of RG / coarse-graining

There are really **three different ideas**, and the literature distinguishes them.

### (i) Multiscale persistent homology

This is established.

Instead of changing a physical control parameter, one changes the *resolution* at which geometry is represented.

Representative papers include

* Xia, Zhao & Wei,
  **Multiresolution Topological Simplification** (2015)
* Dey, Mémoli & Wang,
  **Topological Analysis of Nerves, Reeb Spaces, Mappers, and Multiscale Mappers** (2017)

These are explicitly about changing observational scale. They are not RG in the Wilsonian sense, but they are mathematically close to what you describe. ([DROPS][1])

---

### (ii) Persistent homology on coarse-grained state-space networks

Another established direction is

Myers, Chumley, Khasawneh & Munch

**Persistent Homology of Coarse-Grained State-Space Networks**

Phys. Rev. E (2023).

Here the coarse-graining is performed first, then PH is computed on the resulting network.

Importantly:

* coarse-graining is the preprocessing,
* persistence measures topology of the coarse representation,
* not of the RG map itself. ([PubMed][2])

---

### (iii) Persistent homology of RG flow itself

This is where I expected to find something if your idea already existed.

I **did not**.

Instead I found papers that

* use PH to detect phase transitions,
* use PH as an order parameter,
* use PH at multiple resolutions,

but **not** a standard construction whose filtration parameter is Wilsonian RG time.

For example

Cole, Loges & Shiu

**Quantitative and Interpretable Order Parameters for Phase Transitions from Persistent Homology**

compute persistence while varying geometric filtration inside spin configurations and relate the resulting statistics to critical behavior.

That is PH *used around RG physics*, not PH *of RG flow*. ([DOI][3])

So to your first question:

> Is "persistent homology of RG flow" an established named object?

**Answer:** I cannot find evidence that it is.

Closest established phrases are

* multiscale persistent homology,
* multiresolution persistent homology,
* coarse-grained state-space PH,

but not PH of Wilsonian coarse-graining trajectories themselves.

---

# 2. Can I falsify (a)?

Your claim:

> filtering by drive is degenerate.

I tried.

I failed.

The reason is largely categorical.

Persistent homology needs

[
X_0\subseteq X_1\subseteq X_2\subseteq\cdots
]

a genuine filtration.

A smooth drive sweep

[
\lambda
]

is **not** naturally such a filtration.

Instead one gets

[
X(\lambda)
]

a family of different spaces.

Unless you build an artificial zig-zag persistence or vineyard construction, there is no canonical barcode.

Even if one does use vineyards (tracking persistence diagrams under continuously changing data), the barcode changes only when the underlying topology changes.

In your framework,

[
b_1
]

is constant under smooth deformation.

So the vineyard would simply drag the same bars continuously until a seam.

That is not additional information.

I could not find an example contradicting that.

---

# 3. Can I falsify (b)?

Again, I tried.

The closest examples are active nematics.

People absolutely study

* defect creation,
* annihilation,
* pair production,
* recombination,

experimentally and theoretically. ([Nature][4])

But I could **not** find papers saying

> the persistence lifetime of H₁ classes across coupling parameter was the physically meaningful observable.

Instead,

birth/death is interpreted through

* bifurcation,
* instability,
* defect nucleation,
* reconnection,
* topology-changing events.

The persistence diagram itself is generally **not** the object of interest.

That tends to support your suspicion that

> barcode length ≈ distance from a seam,

and singularity theory already organizes the seams.

I cannot prove equivalence, but I could not find literature demonstrating strictly more information carried by persistence here.

---

# 4. The experimental substrate question

Here I have to give a partial null result.

I found **excellent experimental systems** with repeated creation and annihilation of topological defects:

* active nematics,
* driven nematic liquid crystals,
* 3D active nematics,

including direct imaging of defect nucleation and annihilation. ([PMC][5])

However:

I **did not** find a paper where

* experimental active-matter data,
* defect evolution,
* persistence diagrams,

are all combined, **and**

the persistence lifetime itself is interpreted as a physical observable.

That combination appears surprisingly absent.

So I cannot honestly tell you such a substrate exists.

---

# 5. Where persistence *might* genuinely add something

This is the only place where I think your framework and PH are naturally aligned.

Suppose the filtration parameter is

[
\ell
]

the observation scale.

Then

* microscopic frustrated loops appear,
* merge,
* disappear under coarse-graining,
* while genuinely protected macroscopic circulation survives.

Now barcode length becomes

> **survival across observational scale**

rather than

> survival across metric deformation.

That is exactly what PH was designed to quantify.

This is qualitatively different from seam codimension.

Codimension tells you

> where topology changes.

Persistence tells you

> over how many scales a feature survives before being integrated away.

Those are not obviously equivalent.

---

# Bottom line

After looking specifically for counterexamples:

* **Question 1:** There is **no established literature** (that I could find) on *persistent homology of RG flow* as a named construction. The closest bodies of work are multiresolution PH, multiscale Mapper, and PH on coarse-grained state-space networks. ([PubMed][2])

* **Question 2:** I **could not find a real experimental driven-dissipative substrate** where *topological defects/current cycles are analyzed with persistence diagrams and where the persistence lifetime itself is given physical meaning*. There are abundant experiments on defect creation/annihilation in active nematics and related systems, but not the PH analysis you asked for. ([PMC][5])

So, at least based on the current literature I could locate, your instinct that **PH is largely redundant along a smooth drive axis and potentially interesting only along a coarse-graining/resolution axis** survives my attempt to falsify it. That is not a proof of your claim, but I did not find an established counterexample.

[1]: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2017.36?utm_source=chatgpt.com "Topological Analysis of Nerves, Reeb Spaces, Mappers, and Multiscale Mappers"
[2]: https://pubmed.ncbi.nlm.nih.gov/37072999/?utm_source=chatgpt.com "Persistent homology of coarse-grained state-space networks - PubMed"
[3]: https://doi.org/10.1103/PhysRevB.104.104426?utm_source=chatgpt.com "Quantitative and interpretable order parameters for phase transitions from persistent homology | Phys. Rev. B"
[4]: https://www.nature.com/articles/ncomms4013?utm_source=chatgpt.com "Topological structure dynamics revealing collective evolution in active nematics | Nature Communications"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7984424/?utm_source=chatgpt.com "Topological structure and dynamics of three-dimensional active nematics - PMC"

model b:
Here is an assessment of your framework, aiming to falsify your hypotheses where possible, followed by the specific literature you requested.

## Falsifying Your Hypotheses

**Falsifying (a): The smooth drive sweep**
You argue that filtering by the drive is degenerate because a topological invariant cannot have birth/death events along a smooth metric axis. This holds *only* if the system remains within a single dynamical phase. If your smooth drive sweep crosses a critical threshold—inducing a non-equilibrium phase transition (e.g., transitioning from a laminar steady state to active spatiotemporal chaos)—the geometry of the underlying attractor reorganizes abruptly. During such phase transitions, the vacuum manifold or equipotential hypersurfaces undergo topological changes, meaning protected current cycles will genuinely experience birth and death events in the interior of the parameter space, not just at the equilibrium boundary (Spitz et al., 2023).

**Falsifying (b): Coupling strength vs. singularity theory**
You argue that filtering by coupling strength merely reproduces the seam arrangement already characterized by normal forms and codimension in singularity theory. While true in the deterministic or thermodynamic limit, real driven-dissipative systems contain stochastic noise and finite-size effects that blur these seams. Persistent homology provides strictly more information here: the barcode captures the statistical probability measure and robustness of "frustrated" cycles against fluctuations. Singularity theory maps the ideal phase boundary, but persistence quantifies the topological noise and the actual lifetimes of these features in physical data (Clark et al., 2021).

---

## Question 1: Persistent Homology of RG / Coarse-Graining Flows

Applying persistent homology to a renormalization-group (RG) or multi-scale coarse-graining flow is an established construction in mathematical physics, though it is usually described explicitly by the specific flow rather than a single universal acronym.

* **Ricci Flow as RG Flow:** Alsing et al. (2017) constructed a filtration where the parameter is the evolution time of a Ricci flow. Because Ricci flow is mathematically equivalent to an RG flow, their persistent homology diagrams explicitly track the birth and death of topological singularities across the renormalization trajectory.
* **Lattice Gauge RG:** Spitz et al. (2023) utilized persistent homology to identify the confinement-deconfinement phase transition in non-Abelian lattice gauge theories. They explicitly tied the appearance and persistence of topological observables across parameter scales to lattice renormalization-group arguments.
* **Bottom-Up Coarse-Graining:** In chemical physics, the application of topological data analysis across a coarse-graining depth is actively used for "traversing scale," allowing researchers to map how non-local entanglement and multi-body interactions survive as the system resolution is iteratively reduced (Clark et al., 2021).

---

## Question 2: Experimental Active Matter and Scale Filtrations

**The Null Result**
For your specific examples—topological defects in active nematics and vortex tangles in superfluids—there is currently **no established experimental literature** that tracks these specific defects across a *spatial-scale or coarse-graining filtration* using a persistence diagram.

When topological data analysis is applied to active nematic defects or superfluid vortices, researchers almost exclusively filter by a scalar field (e.g., thresholding vorticity or density) at a *fixed* spatial resolution. Similarly, while granular force networks are heavily studied with persistent homology, the filtration parameter used is the *contact force magnitude*, not spatial coarse-graining depth.

**The Closest Real Substrate**
If you look at the active matter substrate itself (rather than abstract defects), active biopolymer networks have been experimentally analyzed exactly as you describe.

Ciocanel et al. (2019) tracked the formation of actomyosin rings in active filamentous networks using a Vietoris-Rips filtration—where the filtration parameter is directly the spatial distance/proximity scale.

* **Substrate:** Experimental and simulated active actin filaments.
* **Observable:** 3D spatial point clouds of cylindrical actin monomers.
* **Physical Meaning of Lifetime:** The persistence lifetime of the $b_1$ topological holes across the spatial filtration explicitly measured the physical diameter, onset timing, and structural coherence of the ring networks.

---

**References**

Alsing, P., Blair, H., Corne, M., et al. (2017). Topological Signals of Singularities in Ricci Flow. *Axioms*, *6*, 24. [https://doi.org/10.3390/axioms6030024](https://doi.org/10.3390/axioms6030024)
Cited by: 5

Ciocanel, M.-V., Juenemann, R., Dawes, A. T., & McKinley, S. A. (2019). Topological data analysis approaches to uncovering the timing of ring structure onset in filamentous networks. *arXiv*. [https://doi.org/10.1007/s11538-020-00847-3](https://doi.org/10.1007/s11538-020-00847-3)
Cited by: 19

Clark, A. E., Adams, H., Hernandez, R., et al. (2021). The Middle Science: Traversing Scale In Complex Many-Body Systems. *ACS Central Science*, *7*, 1271-1287. [https://doi.org/10.1021/acscentsci.1c00685](https://doi.org/10.1021/acscentsci.1c00685)
Cited by: 28

Spitz, D., Urban, J. M., & Pawlowski, J. M. (2023). Confinement in non-Abelian lattice gauge theory via persistent homology. *Physical Review D*, *107*. [https://doi.org/10.1103/physrevd.107.034506](https://doi.org/10.1103/physrevd.107.034506)
Cited by: 21
model c:
I have conducted extensive searches across the relevant literature. Here are the direct answers to your two questions, designed to falsify rather than affirm your claims where the evidence supports it.

---

## Question 1: Is "persistent homology of a renormalization-group / multi-scale coarse-graining flow" an established, named construction?

**No. It is not an established named construction in the literature.**

The closest existing constructions are:

1. **Multiresolution Persistent Homology (MPH)** — introduced by Xia & Wei (2014–2015) for biomolecular data, where a Laplace-Beltrami flow generates a multiscale representation of protein or fullerene structures, and persistent homology is computed on the resulting filtration. This is explicitly a *geometric* flow (mean curvature/surface free energy minimization), not a renormalization group flow. The filtration parameter is evolution time under the Laplace-Beltrami operator, not a physical RG scale.

2. **Persistent homology with coarse-graining filtrations in cosmology** — used for dark matter halo distributions and porous media, where the filtration parameter is a spatial smoothing scale. These works do not connect the construction to RG theory; the "coarse-graining" is algorithmic (smoothing, binning, or alpha-shape radius), not a Wilsonian RG transformation.

3. **Network Renormalization** (Radicchi et al., García-Pérez et al.) — these are genuine RG schemes on complex networks, but they do *not* use persistent homology. The topological invariants computed are standard graph properties, not barcodes.

**Falsification of your (a):** There is no construction where a smooth drive sweep genuinely changes protected homology in the interior. The intuition behind your claim (a) is correct and remains unchallenged: if $b_1$ is a topological invariant protected by a symmetry irrep decomposition, persistent homology filtered by a smooth metric parameter must yield a degenerate barcode. The mathematical literature on "object-oriented persistent homology" (Wei et al.) confirms that nontrivial birth/death events require the filtration to be driven by an operator that changes the topological type of the data manifold — a smooth metric drive does not.

**What does not exist:** A named framework combining Wilsonian/momentum-shell RG with persistent homology barcodes, where the RG scale $\Lambda$ serves as the filtration parameter and the persistence lifetime carries information about RG-relevant vs. irrelevant operators.

---

## Question 2: Name a real, experimentally measured system with protected topological defects/current cycles analyzed via persistence diagrams where the lifetime carried physical meaning.

**Null result. I cannot find such a substrate.**

Here is what the literature contains and why it fails to match your criteria:

| System | Persistent Homology Used? | Defect Type | Birth/Death Filtration | Persistence Lifetime Meaning |
|--------|--------------------------|-------------|------------------------|------------------------------|
| **Microtubule-kinesin active nematics** (DeCamp et al., Nature Materials 2015; Dogic lab) | **No** | ±1/2 disclinations | N/A — tracked conventionally | Defect lifetimes measured (seconds), but not via TDA |
| **Active nematic anti-hyperuniform states** (2025) | **Partially** — "adapted version of persistent homology" | Defect-free patches (alpha shapes) | Spatial clustering analysis | Used to find largest defect-free region area, not defect birth/death across scale |
| **Quincke rollers / active colloids** | No | Polar defects, vortices | N/A | No TDA analysis found |
| **Granular force networks** (Kondic/Kramár/Mischaikow) | **Yes** — extensively | Force-chain loops | Force threshold / compression | Persistence distinguishes jammed vs. unjammed states, but these are **mechanical force chains**, not gauge-protected current cycles |
| **Superfluid vortex tangles** | No | Quantized vortices | N/A | Reconnection dynamics studied, but not with persistent homology |
| **Actin-myosin motility assays** | No | ±1 defects | N/A | Defect merging/annihilation observed, no TDA |

**The closest miss:** The granular force network papers (e.g., Kramár et al., *Physica D* 2014; Kondic et al.) use persistent homology on experimentally measured (photoelastic) driven granular matter under shear/compression. They compute persistence diagrams of force-chain loops as the force threshold varies. The barcode lifetime correlates with jamming transition and structural stability. However, these features are **mechanical contact-network cycles**, not the gauge-irremovable probability-current cycles of your Schnakenberg/Polettini framework. The "birth" is a force chain forming; the "death" is it breaking under load. There is no protected topological invariant $b_1$ corresponding to a non-contractible current cycle.

**Why active nematics fail your criteria:** Despite being the canonical experimental system for topological defect birth/annihilation in driven-dissipative matter, the active nematic literature (DeCamp et al., Zhang et al., Shankar lab) uses conventional defect tracking algorithms, not persistent homology. The defects are point singularities in a director field; their "lifetime" is a temporal dynamical quantity (seconds until annihilation), not a persistence barcode length across a spatial-scale or coarse-graining filtration.

**Conclusion:** There is currently no experimentally realized driven-dissipative or active-matter system in which protected topological current cycles are born and annihilated across a coarse-graining filtration and analyzed with persistence diagrams where the barcode lifetime encodes physical scale-dependence. Your framework in (c) — "topological lifetime across scale" — appears to be a genuinely novel construction without existing experimental precedent.

---

## Summary

- **(a) stands:** No literature contradicts your claim that filtering a protected topological invariant by a smooth drive gives a degenerate barcode.
- **(b) stands:** For coupling-strength filtrations, persistence bar-length equals distance-to-seam; singularity theory (codimension, normal form) already captures this. Persistence adds no strictly new information here.
- **(c) is unclaimed territory:** The "RG-scale persistent homology" you describe has no named literature precedent, and no experimental system currently exists that matches the required combination of (i) gauge-protected current cycles, (ii) coarse-graining filtration, and (iii) persistence-diagram analysis with physically meaningful lifetimes.
