# Outbound-research prompt — where the shell people keep their quantitative data

Data-sourcing question for the outbound channel. Companion to `research_prompt_chirality_sector_independence.md`
(that one poses a hypothesis; this one hunts for the **datasets** that could feed it and several related tests).
The primary use is now the **within-shell growth trajectory** — especially its two endpoint shapes (heteromorph
/ non-self-similar growth, and determinate growth run to cessation), which probe a single shell as a recorded
cascade.
The aim is to find data with a specific *shape* — specimen-resolved, quantitative, and ideally resolved over
growth-time (a trajectory) — not summary statistics or qualitative description. Malacology / conchology /
geometric-morphometrics / sclerochronology / theoretical-morphology expertise. No framework jargon. Returned
reports file alongside.

---

## Locating quantitative, specimen-resolved gastropod-shell datasets

Accretionary shells are unusually rich recorders: a shell is a frozen growth history, and the community
measuring them is large and meticulous. I'm looking for **machine-readable, specimen-level** datasets of a few
specific shapes, and I want to know who holds them and where they live. I care much more about *quantitative,
stage- or time-resolved* data than about taxonomy or descriptions. The single most valuable property is that the
data resolve **how form changes as the animal grows** — a path, not just an adult endpoint.

Five data shapes, in rough priority order. For each: do such datasets exist in numeric, specimen-resolved form;
who curates them; in what repository/format; and how accessible?

**1. Ontogenetic growth trajectories (highest value).** Series of shape measurements taken at *successive growth
stages of the same shell* — whorl-by-whorl, or continuously from apex to aperture — capturing how the form
changes *as the animal grows*, not just the adult shape. (Raup parameters W/D/T measured per whorl; landmark or
outline/Fourier morphometrics tracked along ontogeny; or 3D/CT-scanned shells from which a growth path can be
reconstructed.) Which studies, monographs, or 3D-scan repositories (e.g. MorphoSource) hold *ontogenetic series*
rather than single adult shapes?

**2. Time-resolved growth-rate records (sclerochronology).** Growth-increment widths and/or isotope
(δ¹⁸O, δ¹³C) series measured *along* a shell that resolve growth rate over calendar time — daily/tidal/seasonal
increments — ideally paired with the environment the animal experienced (temperature, food, latitude). This is
the closest thing to a time-series of "how fast it was building," against a known driver. Where do these archives
live (PANGAEA, sclerochronology / paleoclimate-proxy databases), and how much is gastropod vs bivalve?

**3. Morphospace-occupancy datasets (theoretical morphology).** Raup-tradition parametric measurements across
many species/specimens, especially studies mapping *which regions of the theoretical form-space are occupied vs
empty*. Who holds the underlying numeric tables (not just the published scatterplots) — successors to Raup,
David, McGhee, Cortie, Okamoto (heteromorph ammonites)?

**4. Discrete-state and reversal data.** Specimens labeled by **chirality** (dextral/sinistral) with shape
measured (links to the companion prompt); plus anything on chirality *reversals* — teratological flips,
scalariform/aberrant coiling, lineages that flipped hand — and breeding/inheritance records of chirality (lab
*Lymnaea*, *Partula*, *Euhadra*). The reversals and inheritance records are the rare events I most want: they are
the moments the discrete state actually changes.

**5. Perturbation-and-recovery data.** Shell damage-and-repair records, regeneration experiments, or
developmental perturbations (temperature shock, gene knockdown — e.g. the *Lsdia1* / formin work) with
*quantitative* before/after form or growth-program recovery. How completely, and how measurably, does the growth
program (including handedness) recover after a disturbance?

**6. Trajectory endpoints — non-convergent and self-terminating growth (now the priority pair).** Two trajectory
*shapes* matter most. **(a) Heteromorph / aberrant coiling** — forms whose growth does *not* settle to a constant
logarithmic spiral (irregular, uncoiling, or meandering growth; heteromorph ammonites à la Okamoto's
growing-tube model; scalariform gastropods), measured *as trajectories* so the **departure from self-similarity**
is quantified, not just described. Do datasets exist that distinguish "never converged to a spiral" from
"converged then deviated"? **(b) Determinate growth run to cessation** — series capturing the *approach to and
arrival at* growth stop (the terminal lip/flare, size-at-maturity), ideally with growth rate declining toward
zero, so the **stopping point** is resolved. Is there data relating the cessation point (size / whorl-count at
maturity) to growth rate or an energetic budget — does growth stop at a *characteristic*, predictable point, and
is that point recoverable from a gain-vs-cost balance rather than only from age or reproductive status?

**Cross-cutting questions:**

- Which **museum collection databases and digital repositories** expose specimen-level *measurements*
  (MorphoSource, GBIF, iDigBio, Dryad/Zenodo supplements, PANGAEA) versus data that survives only as figures in
  PDFs or in private lab spreadsheets?
- Are there **standard digitization formats** for shell morphometry (landmark sets, elliptic-Fourier outline
  coefficients, CT meshes) that would make a multi-study dataset poolable?
- Who are the **active labs / individuals** most likely to hold "shelves" of unpublished-but-digitized
  measurement series, and what's the realistic path to access?
- If you had to name the **single richest existing dataset** for studying *how shell form evolves along
  growth-time* (not just adult form), what would it be?

The ideal find is a numeric, specimen-resolved dataset *resolved over growth-stage or calendar time* — a
trajectory — for many individuals, with discrete state (chirality) labeled where possible. I expect the abundant
data (adult morphometrics, locality records) to be the least useful, and the most useful (true growth
trajectories, time-resolved rates) to be rarer — so pointers to the closest existing thing, however partial, are
exactly what I need.

-----

model a:
This is actually a surprisingly tractable data-hunt because the shell community has three unusual advantages:

1. Shells preserve their own growth history.
2. CT scanning has become routine.
3. The theoretical-morphology tradition has always been quantitative.

The bad news is that the richest datasets are scattered across museums, supplementary tables, and lab archives rather than unified databases. The good news is that the data shapes you're after do exist.

## Executive summary: where the best data probably are

If I ranked the existing ecosystem by value for your specific question ("how does shell form evolve along growth-time?"):

| Rank | Dataset type                                                               | Richness             | Accessibility               |
| ---- | -------------------------------------------------------------------------- | -------------------- | --------------------------- |
| 1    | CT-derived ontogenetic trajectories reconstructed from individual shells   | Extremely high       | Moderate                    |
| 2    | Nautilus / ammonoid ontogenetic morphometry measured through entire conchs | Extremely high       | Good                        |
| 3    | Sclerochronological increment series                                       | High                 | Good                        |
| 4    | Chirality genetics collections (*Lymnaea*, *Partula*, *Euhadra*)           | Moderate-high        | Investigator dependent      |
| 5    | Museum CT repositories (MorphoSource)                                      | Potentially enormous | Requires extraction         |
| 6    | Classic Raup-style morphospaces                                            | Moderate             | Often buried in supplements |

The key observation is that your highest-priority object—a growth trajectory—is often not stored explicitly. It is reconstructed from a shell that already contains the trajectory.

---

# 1. Ontogenetic growth trajectories (highest value)

This is where I would concentrate effort.

Gastropod and cephalopod shells are accretionary structures. Every earlier growth stage remains preserved in later whorls. Consequently, a sufficiently detailed CT scan effectively contains an entire ontogenetic record. The challenge is extracting it. ([PMC][1])

The strongest existing trajectory tradition is actually in ammonoids and nautiloids.

A particularly useful example is the ontogenetic-trajectory literature built around *Nautilus*, where conch parameters are measured repeatedly through growth. One methodological paper explicitly analyzes how densely along ontogeny measurements must be taken and presents trajectories of whorl expansion and related quantities through development. The supplementary material contains the sort of repeated-within-shell measurements you are looking for. ([PMC][2])

### Repositories

The first place I would search is:

* [MorphoSource](https://www.morphosource.org?utm_source=chatgpt.com)

MorphoSource hosts raw CT volumes, meshes, and surface models from museum specimens. It was designed specifically for storing and distributing 3D morphology datasets. Many shell datasets are present, although often not pre-processed into growth trajectories. ([PMC][3])

The important distinction:

* Adult shell measurements → common.
* CT scans from which an ontogenetic path can be reconstructed → extremely valuable.
* Explicit per-whorl trajectory tables → rare but do exist.

### Labs to watch

For quantitative ontogeny:

* Christian Klug
* René Hoffmann
* Takashi Okamoto

These communities routinely generate growth-stage-resolved measurements.

---

# 2. Time-resolved growth-rate records (sclerochronology)

This is the most mature data infrastructure you mentioned.

The center of gravity is:

* [PANGAEA](https://www.pangaea.de?utm_source=chatgpt.com)

PANGAEA contains shell increment chronologies, isotope series, and growth-rate records linked to environmental variables. The literature is dominated by bivalves because annual and seasonal increments are easier to read and validate. ([PANGAEA DOI Resolver][4])

For your purposes, bivalves may actually be useful despite not being coiled shells:

* growth rate is resolved in time;
* environmental forcing is often known;
* isotope series can provide calendar alignment.

Gastropod sclerochronology exists but is much less standardized than bivalve work.

### What these datasets look like

Typically:

| Individual | Increment number | Width | δ18O | δ13C | Date |
| ---------- | ---------------- | ----- | ---- | ---- | ---- |

This is very close to a true growth-time series.

---

# 3. Morphospace occupancy datasets

These absolutely exist, but the underlying tables are often harder to obtain than the figures.

The modern lineage descends from:

* David Raup
* George McGhee
* Takashi Okamoto

Recent work continues to measure Raup-style parameters across large shell collections and compare occupied versus theoretically possible regions of morphospace. ([OUP Academic][5])

The frustrating reality:

* many classic datasets survive only in tables embedded in papers;
* some numerical values are recoverable from supplements;
* some must be digitized from figures.

If I were building a pooled resource, I would expect substantial figure-digitization.

---

# 4. Chirality and reversal datasets

This is probably easier than it looks.

The best-established experimental systems are:

* Lymnaea stagnalis
* Partula suturalis
* Euhadra

The *Partula* literature contains large quantitative datasets linking chirality genetics and shell shape. The raw measurements used to test genotype–shape relationships are exactly the kind of specimen-level records you're seeking. ([Nature][6])

For actual state flips, the most important modern system is the formin gene (*Lsdia1*) in *Lymnaea*. CRISPR perturbation can generate inherited chirality reversal in otherwise dextral lineages. ([PubMed][7])

The raw developmental image series and breeding records associated with these projects are likely more valuable than the published summary statistics.

### Highest-value rare-event data

I would prioritize:

1. Historical *Lymnaea* breeding datasets.
2. Modern *Lsdia1* experimental records.
3. *Partula* pedigree datasets.

Those are among the few places where the discrete state actually changes.

---

# 5. Perturbation-and-recovery datasets

These exist but are fragmented.

Two major categories:

### Developmental perturbations

The *Lsdia1* chirality work is the clearest example. Chirality is experimentally altered and downstream morphology recorded. ([PubMed][7])

### Damage-repair studies

There is a substantial literature on shell repair and regeneration, but datasets are often image-heavy rather than tabular.

Likely locations:

* supplementary datasets in developmental biology papers;
* museum CT projects;
* investigator-held morphometric spreadsheets.

This is an area where direct contact with labs is likely necessary.

---

# 6a. Heteromorph and non-self-similar growth trajectories

This may be the most interesting target in the entire search.

The heteromorph ammonite community has spent decades treating shell growth explicitly as a trajectory rather than an endpoint.

Okamoto's work on *Nipponites* and related heteromorphs models growth as a changing path through developmental space and quantitatively reproduces observed trajectories. ([CiNii][8])

Even more promising, later theoretical studies analyze departures from regular coiling and quantify changes in morphology produced by nonstationary growth processes. ([OUP Academic][9])

This is probably the strongest existing literature for distinguishing:

* converged logarithmic coiling;
* persistent deviation;
* stage-dependent regime changes.

If your interest is "did the trajectory ever settle?", heteromorph ammonites are almost certainly the best-developed quantitative testbed.

---

# 6b. Determinate growth and approach to cessation

These data exist, but are less centralized.

Look for:

* terminal lip formation;
* mature aperture development;
* whorl-count-at-maturity studies;
* growth-increment chronologies near maturity.

The challenge is that many studies record:

* maturity reached

rather than

* the entire slowdown approaching maturity.

Sclerochronological datasets are likely the best route because growth increments often visibly compress as growth slows.

I know of no major centralized database dedicated specifically to "approach-to-growth-cessation trajectories."

That may be an actual gap.

---

# Standard formats that make pooling feasible

Three formats dominate.

### Landmark coordinates

Common geometric-morphometrics format.

Usually:

```
specimen_id
landmark_x
landmark_y
landmark_z
```

### Elliptic Fourier descriptors

Widely used for shell outlines.

Usually portable across studies.

### Meshes / CT volumes

Often:

* STL
* PLY
* OBJ
* DICOM
* TIFF stacks

MorphoSource stores many of these. ([PMC][3])

The good news is that trajectories can often be extracted retrospectively from these files.

---

# Which repositories matter?

Most useful:

1. [MorphoSource](https://www.morphosource.org?utm_source=chatgpt.com)
2. [PANGAEA](https://www.pangaea.de?utm_source=chatgpt.com)
3. [Dryad](https://datadryad.org?utm_source=chatgpt.com)
4. [Zenodo](https://zenodo.org?utm_source=chatgpt.com)

Less useful than many people expect:

* [GBIF](https://www.gbif.org?utm_source=chatgpt.com)
* [iDigBio](https://www.idigbio.org?utm_source=chatgpt.com)

Those are excellent for specimen occurrence records but comparatively weak for growth trajectories.

---

# If I had to pick one richest existing resource

Not a single published table.

A collection.

**CT-scanned shell collections in MorphoSource combined with the ammonoid/nautiloid ontogenetic morphometrics literature.**

Why?

Because a shell is itself a recorded growth history. A high-resolution CT scan preserves the entire sequence from apex to aperture. With appropriate extraction, one specimen can yield hundreds or thousands of ontogenetic observations. ([PMC][3])

For the specific endpoint pair you highlighted:

* **non-convergent trajectories** → heteromorph ammonite datasets (Okamoto lineage) are probably the richest source. ([CiNii][8])
* **self-terminating trajectories** → sclerochronological growth-increment archives are probably the closest existing analogue. ([PANGAEA DOI Resolver][4])

My estimate is that the highest-value data are not hidden in a giant database. They are sitting in a few dozen CT collections and supplementary spreadsheets generated by the cephalopod ontogeny and theoretical-morphology communities. Those groups appear to be the shortest path to specimen-resolved growth trajectories.

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6452709/?utm_source=chatgpt.com "Growth and morphogenesis of the gastropod shell - PMC"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7103202/?utm_source=chatgpt.com "How many ontogenetic points are needed to accurately describe the ontogeny of a cephalopod conch? A case study of the modern nautilid Nautilus pompilius - PMC"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4736502/?utm_source=chatgpt.com "A collection of non-human primate computed tomography scans housed in MorphoSource, a repository for 3D data - PMC"
[4]: https://doi.pangaea.de/10.1594/PANGAEA.816231?utm_source=chatgpt.com "Butler, PG et al. (2010): Shell-based chronologies for the Irish Sea"
[5]: https://academic.oup.com/evolut/article/77/8/1864/7197689?utm_source=chatgpt.com "Theoretical morphological analysis of differential morphospace occupation patterns for terrestrial and aquatic gastropods | Evolution | Oxford Academic"
[6]: https://www.nature.com/articles/hdy200949?utm_source=chatgpt.com "Coil and shape in Partula suturalis: the rules of form revisited | Heredity"
[7]: https://pubmed.ncbi.nlm.nih.gov/31088796/?utm_source=chatgpt.com "The development of CRISPR for a mollusc establishes the formin Lsdia1 as the long-sought gene for snail dextral/sinistral coiling - PubMed"
[8]: https://cir.nii.ac.jp/crid/1390282679410582528?utm_source=chatgpt.com "Theoretical morphology of Nipponites : a heteromorph ammonoid | CiNii Research"
[9]: https://academic.oup.com/ptp/article/97/5/739/1932905?utm_source=chatgpt.com "Effects of the Non-Stationary Fluctuations in the Morphogenetic Evolution of Heteromorph Ammonites | Progress of Theoretical Physics | Oxford Academic"

model b:
This is a fascinating and highly specific data-hunting mission. As an AI, I don't hold these datasets internally, but I can point you exactly to where the malacology, sclerochronology, and theoretical morphology communities store them.

The blunt reality of this field is that the grand, unified "Shell Growth Trajectory Database" does not exist. However, the data *does* exist, heavily fragmented across supplementary files, specific 3D repositories, and paleo-climate databases.

Here is the map of where to hunt for your specific trajectory shapes.

---

### 1. Ontogenetic Growth Trajectories (Highest Value)

You are looking for whorl-by-whorl or continuous aperture tracking. This field has bifurcated into traditional 2D morphometrics and modern 3D micro-CT scanning.

* **Where it lives:** **MorphoSource** is the absolute epicenter for raw 3D ontogenetic data. Researchers upload micro-CT stacks and surface meshes of shells from apex to aperture. For the *extracted numeric trajectories* (e.g., Raup parameters over time, sliding semi-landmarks), you must look at **Dryad** and **Zenodo**, explicitly searching for supplementary `.csv` or `.tps` files attached to papers in journals like *Paleobiology*, *Evolution*, or *Journal of Morphology*.
* **Key Curators/Labs:** Look at the work of **Thor-Seng Liew** (Naturalis/Universiti Malaysia Sabah), who has produced incredible, specimen-resolved 3D ontogenetic models of micro-snails (like *Plectostoma*), explicitly tracking whorl expansion rates. **Séverine Urdy** does heavy mathematical lifting on continuous growth trajectories and accretionary edge modeling.

### 2. Time-Resolved Growth-Rate Records (Sclerochronology)

This is the most standardized and quantitatively rigorous data you will find, though it leans heavily toward bivalves.

* **Where it lives:** **PANGAEA** (Data Publisher for Earth & Environmental Science) and the **NOAA NCEI Paleoclimatology Database**.
* **The Data Shape:** These are literal time-series tabular datasets of $\delta^{18}$O, $\delta^{13}$C, and daily/annual increment widths.
* **Gastropod vs. Bivalve:** Bivalves (like *Arctica islandica*) dominate because their hinge plates are easier to cross-date. However, gastropods with massive shells (*Strombus*, *Conus*, *Turritella*) or heavily calcified opercula are well-represented.
* **Key Curators/Labs:** The **Bernd Schöne Lab** (Mainz) and **Donna Surge Lab** (UNC) are incredibly active. The *International Sclerochronology Conference* (ISC) proceedings and associated Zenodo uploads are your best hunting grounds.

### 3. Morphospace-Occupancy Datasets

The successors to Raup, McGhee, and Okamoto are generally moving away from purely theoretical morphospaces into empirical morphospaces populated by massive 3D landmarking.

* **Where it lives:** The **Paleobiology Database (PBDB)** holds some morphometric trait data, but it is primarily occurrence/taxonomic. The rich, numeric theoretical morphology tables are almost exclusively in **Dryad** or supplemental journal repositories.
* **Key Curators/Labs:** For ammonites (the classic heteromorphs), look to **Dieter Korn** and **Christian Klug**. For gastropods, **David Jablonski's lab** (UChicago) has done massive amounts of work on spatial and temporal morphospace occupancy, though often at the adult/species level rather than ontogenetic.

### 4. Discrete-State and Reversal Data (Chirality)

This is a niche with deep, highly specific genetic and morphological records.

* **Where it lives:** Because this blends genetics and morphology, **NCBI/GenBank** (for the gene knockdowns) cross-referenced with **Zenodo** (for the physical phenotypes) is your target.
* **Key Curators/Labs:** You want the **Angus Davison Lab** (University of Nottingham) for *Lymnaea* and *Partula* inheritance datasets. They have traced chiral genetics deeply. For the *Lsdia1* formin work and definitive lab-bred reversal tables, look to **Reiko Kuroda** (Chubu University/University of Tokyo) and **Masanori Asami**. Their supplementary datasets contain exact counts of wild-type vs. CRISPR-edited scalariform/reversed mutants.

### 5. Perturbation-and-Recovery Data

Quantifying recovery from shell breaks is notoriously difficult because the recovery is often highly irregular.

* **Where it lives:** Historically, this was categorical (e.g., Geerat Vermeij's classic work on repair frequency). For *quantitative* before/after form recovery, you are looking for micro-CT studies of repair mechanics. These are sparsely distributed in **MorphoSource** and **Dryad**.
* **Key Curators/Labs:** **Carrie Tyler** and **Gregory Dietl** have done extensive work on the paleoecology of predation and repair, pushing toward more quantitative morphometrics of scars.

### 6. Trajectory Endpoints (Heteromorphs & Determinate Growth)

* **Heteromorphs (Non-self-similar):** **Takashi Okamoto's** "growing tube model" remains the standard for ammonites that uncoil or meander. Modern datasets tracking the exact geometric departure from logarithmic spirals are rare but highly prized. **Thor-Seng Liew's** *Plectostoma* data on Zenodo/Dryad is exactly what you want here for gastropods—they explicitly track the uncoiling terminal tuba in these snails.
* **Determinate Growth (Cessation):** Lip flaring (e.g., Strombidae) or terminal apertural modifications. The data relating terminal size to growth rate (energetic budget) often lives in fisheries or marine biology databases focusing on size-at-maturity rather than paleontology. Sclerochronology (PANGAEA) is your best bet for seeing the *growth rate declining to zero* as the terminal lip forms.

---

### Cross-Cutting Answers

* **Museum vs. Analytical Databases:** Collections like GBIF, iDigBio, and standard museum catalogs are useless for your specific needs—they will give you photos and bounding-box dimensions at best. **MorphoSource, Dryad, Zenodo, and PANGAEA** are where the actual *measurements* live.
* **Standardization:** There is **no standard format**. You will encounter raw 3D meshes (`.ply`, `.stl`), landmark coordinates (`.tps`), outline coefficients (Elliptic Fourier `.csv`), and custom RData files.
* **Unpublished Shelves:** The richest hidden datasets are likely raw, unprocessed micro-CT scans sitting on the hard drives of evolutionary morphology labs (like the Davison, Jablonski, or Liew labs) waiting for PhD students to segment them.
* **The Single Richest Dataset:** If I had to name the best existing pool for *how shell form evolves along growth-time*, it would be **Thor-Seng Liew's micro-CT databases of land snails (Opisthostoma and Plectostoma)**. They are highly digitized, explicitly resolve ontogenetic time via aperture tracking, capture extreme heteromorph-like endpoints, and the raw/extracted data is largely open-access. For pure *growth-rate over time*, the **sclerochronological archives of *Arctica islandica* on PANGAEA** are unparalleled, even though they are bivalves.

Given the heavy fragmentation between raw 3D scans (MorphoSource) and extracted numeric tables (Dryad/Zenodo), are you equipped to computationally process and extract trajectories from raw micro-CT volumes, or do you strictly need pre-extracted tabular arrays (like Raup parameters or Fourier coefficients) to feed your analytical pipelines?

model c:
I'll search for the specific datasets and repositories your prompt targets. Let me run parallel queries across the key data shapes.
Let me search deeper into the specific archives and datasets.
Let me search for more specific archives, labs, and the missing data shapes.
Let me search for the remaining gaps: determinate growth, perturbation recovery, and specific repository datasets.
Let me do one final targeted sweep for the remaining gaps: determinate growth, specific sclerochronology archives, and theoretical-morphology data tables.


**Outbound research report — Quantitative, specimen-resolved gastropod-shell datasets**

Below is a field report on what exists, where it lives, and how to access it, organized by the six data shapes you requested. I flag *closest existing proxies* where the ideal dataset does not yet exist in pooled form.

---

### 1. Ontogenetic growth trajectories (highest value)

**What exists.** True whorl-by-whorl or continuous ontogenetic trajectories are methodologically mature but exist mainly as *per-study lab outputs*, not as pooled archives.

- **CT-based 3D ontogeny pipelines.** A non-destructive workflow has been established for gastropods: micro-CT → voxel segmentation → curve-skeleton extraction → successive cross-sections perpendicular to the skeleton → elliptic Fourier analysis (EFA) of whorl outlines + displacement vectors (translation/rotation between planes). This yields an *n*-dimensional morphometric trajectory for a single shell. The method was developed on helicid land snails (e.g., *Cepaea nemoralis*) at the University of Zurich and is explicitly designed to handle irregularly coiled shells without assuming a fixed coiling axis.
- **Aperture ontogeny profiles.** A complementary method tracks the aperture trajectory itself via curvature, torsion, aperture size, and aperture shape scores along the ontogeny axis. It has been applied to aberrant forms (*Opisthostoma*, *Plectostoma*) and can cluster shells by their ontogenetic path rather than by adult endpoint.
- **MorphoSource holdings.** MorphoSource now hosts >210,000 media datasets, including ~95,000 published 3D models (45,000 openly downloadable). While most are adult fossils or extant specimens, some projects include ontogenetic series. For example, the *Lymnaea stagnalis* Wnt-perturbation study deposited 3D reconstructions of control and malformed shells (Project 000636914).
- **Growing-tube model code.** Noshita has published open-source code for estimating Okamoto’s growing-tube parameters (expansion *E*, curvature *C*, torsion *T*) from 3D reconstructions, enabling trajectory quantification from CT data: `github.com/noshita/growing_tube_model_estimation`.

**Gaps.** No large repository of *pooled* ontogenetic trajectories exists. Most data are in private lab spreadsheets or buried as supplementary tables in PDFs. The Zurich group (Blanckenhorn, Urdy) and the JAMSTEC group (Noshita, Ohta) are likely sitting on unpublished-but-digitized ontogenetic series.

---

### 2. Time-resolved growth-rate records (sclerochronology)

**What exists.** Sclerochronology is heavily dominated by bivalves; gastropod studies are scattered and not centrally archived.

- **Individual gastropod studies.** High-resolution δ¹⁸O and δ¹³C series have been published for marine gastropods (*Conomurex luhuanus*, *Osilinus turbinatus*, *Hunsator solanderi*), often with growth-increment widths paired to temperature or season-of-death.
- **Freshwater mollusc review.** A 2023 review catalogued 133 publications (2000–2021) on freshwater mollusc sclerochronology, noting growth-line periodicity, isotope series, and trace-element work. The underlying data are in the original papers, not in a database.
- **PANGAEA.** PANGAEA hosts some mollusc isotope data, but the bulk of archived material is bivalve or fish otolith. No gastropod-specific sclerochronology database was found.

**Gaps.** There is no equivalent of the International Tree-Ring Data Bank for molluscs. If you need gastropod time-series, the fastest path is to mine the supplementary data of the 133 papers catalogued by Stringer & Prendergast (2023) and the marine studies cited above.

---

### 3. Morphospace-occupancy datasets (theoretical morphology)

**What exists.** Raup’s 1966 morphospace and its successors (McGhee, Cortie, Okamoto, Urdy) are overwhelmingly *conceptual* or *graphical*; the underlying numeric tables are rarely published in machine-readable form.

- **Raup parameters (W/D/T).** These are routinely recomputed per-study from linear measurements. No central digital table of the original Raup dataset was located.
- **Okamoto’s growing-tube model.** Okamoto (1988) introduced *E* (expansion), *C* (curvature), *T* (torsion) for heteromorph ammonoids. These parameters are now being extracted from 3D data (see above), but no pooled dataset of *E/C/T* trajectories across species exists.
- **Morphomechanical models.** Urdy et al. (2010, 2015) and Moulton et al. (2015) developed free-form vector and morphomechanical models that can simulate allometric growth, but again as theory/code rather than as empirical data tables.

**Gaps.** The “empty space” in morphospace is documented in scatterplots, not downloadable matrices. If you want to map occupied vs. empty regions numerically, you would need to scrape measurements from the literature or collaborate with the few labs that have large private spreadsheets.

---

### 4. Discrete-state and reversal data (chirality)

**What exists.** Chirality inheritance is classic, but specimen-resolved datasets linking chirality to quantitative shape are scarce.

- **Classic inheritance records.** *Lymnaea peregra/stagnalis* (Boycott & Diver 1930; Freeman & Lundelius 1982; Davison lab), *Partula* (Murray & Clarke 1966, 1980; Johnson 1982), *Euhadra* (Ueshima & Asami), and *Bradybaena* (maternal inheritance) have breeding records and genetic mapping data. The *Partula* genomic data (117 individuals) are on NCBI SRA (PRJNA326969) and Dryad, but this is genomic, not shell-morphometric.
- **Molecular perturbation.** CRISPR/Cas9 knockdown of *Lsdia1* (formin) in *Lymnaea stagnalis* reliably inverts shell coiling. The study tracked F0→F1→F2 phenotypes and germline transmission, but the published data are genotype/phenotype counts, not full 3D morphometric trajectories of the reversed shells.
- **Teratological reversals.** Natural sinistral mutants (“Jeremy” the snail) and lab-induced reversals exist, but are treated as anecdotal or low-*n* genetic specimens rather than as quantitative morphometric series.

**Gaps.** No large dataset links chirality (dextral/sinistral) to ontogenetic shape trajectory. Davison’s lab (University of Nottingham) and the Asami/Ueshima group are the most likely holders of unpublished breeding records with associated shell measurements.

---

### 5. Perturbation-and-recovery data

**What exists.** Quantitative before/after morphometrics are rare; most studies report presence/absence of repair or qualitative descriptions.

- **Shell regeneration.** *Pomacea dolioides* juvenile shell-repair experiments tracked daily photographic records and linear dimensions (shell length) under varying calcium concentrations, but not full 3D morphometrics.
- **Developmental perturbation with 3D recovery.** The *Lymnaea stagnalis* Wnt-activation study (BIO treatment) produced three malformed phenotypes (Cap, Hyd, Com) and reconstructed their 3D growth trajectories via CT. Controls vs. malformed individuals were compared using the growing-tube model; *Com* shells showed significantly higher torsion (*T*), while *Cap* shells showed higher expansion (*E*). This is the closest example to a quantitative perturbation-and-recovery trajectory dataset, though “recovery” was not tracked—only the endpoint malformation.
- **Ocean warming/acidification micro-CT.** A NIfTI-format dataset of marine gastropod shells exposed to warming/acidification is available for download, providing 3D image stacks suitable for morphometric extraction.

**Gaps.** No study was found that tracks the *same individual* through damage → repair → quantitative morphometric return to baseline. The *Pomacea* and *Lymnaea* studies are the best starting points.

---

### 6. Trajectory endpoints — heteromorph growth and determinate growth cessation

**What exists.** This is the shape you identified as the current priority pair. Data are fragmentary.

- **Heteromorph / non-self-similar growth.** Heteromorph ammonites (*Didymoceras*, *Nostoceras*) have been modeled as transitioning between planispiral → meandering → helicospiral stages via continuous parameter changes in stiffness and growth mismatch. The physical model predicts that a helicospiral-to-planispiral transition *must* pass through a meandering stage, which is testable against CT data. However, these are model predictions paired to a few specimens, not a pooled dataset of trajectories.
- **Scalariform/aberrant gastropods.** *Opisthostoma vermiculum* and vermetid gastropods show aberrant coiling; the aperture-ontogeny method can quantify departure from self-similarity, but no dataset distinguishes “never converged” from “converged then deviated” across many specimens.
- **Determinate growth cessation.** Strombid gastropods are the classic example: at sexual maturity they cease growing in length and switch to width growth via a flared, thickened terminal lip. This is well described qualitatively, but no dataset was found that resolves the *approach* to cessation (growth rate declining to zero) or links the stopping point to an energetic budget rather than age or reproductive status.
- **DEB model for *Lymnaea stagnalis*.** A Dynamic Energy Budget model captures the full life cycle and suggests metabolic acceleration, but it models body size, not shell accretion rate, and does not resolve the terminal lip or whorl-count at maturity.

**Gaps.** True determinate-growth trajectories—time-series of shell deposition rate as the animal approaches maturity—appear to be the rarest data shape of all. Strombid collections in natural-history museums (e.g., FMNH, NHM London) may hold the specimens, but the measurements do not appear to be digitized.

---

### Cross-cutting questions

**Museum/repository landscape**
- **MorphoSource** is the best 3D data repository for raw CT and meshes (PLY/STL). It is project-based, free, and provides DOIs. However, ontogenetic series are a minority of holdings.
- **GBIF / iDigBio** serve occurrence and taxonomic data. The Darwin Core *MeasurementOrFact* and *ExtendedMeasurementOrFact* extensions *could* host shell morphometrics, but in practice they are rarely used for specimen-level shape data; most records lack measurements.
- **Dryad / Zenodo / Figshare** host individual study supplements. Examples: *Partula* genomic data on Dryad; *Lymnaea* 3D data on MorphoSource. There is no systematic pool.
- **PANGAEA** has some marine isotope data but is not gastropod-focused.

**Standard digitization formats**
- **3D meshes:** PLY (ASCII) and STL are standard; binary PLY must be converted to ASCII for downstream R packages (e.g., `Rvcg`).
- **Landmarks:** TPS, NTS, and PLY formats are used in geometric morphometrics.
- **Outlines:** Elliptic Fourier coefficients (EFA) are standard for whorl-section outlines.
- **Trajectories:** Okamoto/Noshita growing-tube parameters (*E*, *C*, *T*) provide a 3-parameter summary of any shell form, but are not yet widely adopted as an exchange standard.

**Active labs / individuals likely holding unpublished shelves**
- **Angus Davison** (University of Nottingham): chirality, *Lymnaea*, *Partula*, *Euhadra*; likely holds breeding records and shell measurements.
- **Koji Noshita / S. Ohta** (JAMSTEC/Tohoku): growing-tube model, CT-based ontogeny, *Lymnaea* perturbation data.
- **Séverine Urdy** (ETH Zurich / formerly Zurich): morphomechanical modeling, CT ontogeny methods; discussed in the Zurich CT papers.
- **Robert Guralnick / colleagues** (University of Florida / Colorado): geometric morphometrics of *Littorina* and ontogenetic trajectory methods.
- **Wolf Blanckenhorn** (University of Zurich): CT ontogeny pipeline for helicids.
- **Doug Boyer / Julie Winchester** (Duke): MorphoSource curation; may know which museums have bulk mollusc CT series.

**Single richest existing dataset for shell form evolving along growth-time**
There is no single clear winner. The closest proxies are:
1. The **Zurich/JAMSTEC CT ontogeny pipelines** (methods mature, but data scattered across private labs).
2. The **MorphoSource mollusc holdings** (~95k 3D models), though mostly adult.
3. The **Stringer & Prendergast freshwater-sclerochronology bibliography** (133 studies), which provides a reading list but not a data pool.

If forced to name one *downloadable* resource, the **Noshita/Ohta *Lymnaea stagnalis* 3D reconstruction set on MorphoSource (Project 000636914)** is a rare example of a published, specimen-resolved, perturbation-linked 3D trajectory dataset with open code.

---

**Bottom line.** The data landscape is methodologically advanced but archivally fragmented. The tools to extract ontogenetic trajectories (CT + growing-tube models + EFA) exist and are open-source; what is missing is the *aggregation* of specimen-level trajectory data into a pooled repository. The highest-yield strategy for your project is likely a **dual approach**: (1) direct collaboration with the labs above for unpublished shelves, and (2) systematic scraping of supplementary data from the 133+ sclerochronology papers and the growing body of 3D-morphometrics studies depositing on MorphoSource/Dryad.
