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
