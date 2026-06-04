# Outbound-research prompt — is shell chirality independent of shell shape?

Landscape question for the outbound channel. Tests one structural prediction — that two visible features of a
snail shell, its **handedness** and its **continuous coiling shape**, are statistically independent — against
the malacology / morphometrics literature and available datasets. No framework jargon; answerable by an
evolutionary-biology / geometric-morphometrics / malacology expert. Returned reports file alongside. Pairs with
the `cross-stratum-transduction` frontier entry (snail chirality as the candidate instance; this is its
runnable falsifier).

---

## Is gastropod shell chirality statistically independent of continuous shell form?

A snail's shell carries two very different kinds of trait at once:

- **Handedness (chirality):** a discrete left/right bit — dextral vs sinistral coiling. In *Lymnaea* it is set
  by a single maternal-effect gene (the formin `Lsdia1`) at the one-cell stage, and dextral/sinistral snails
  are partly reproductively isolated by mating mechanics.
- **Shape:** the continuous geometry of the coil — Raup's parameters (whorl expansion rate `W`, generating-curve
  distance `D`, translation rate `T`), or any standard morphometric description (spire angle, aperture shape,
  etc.). These vary continuously and are typically polygenic.

I want to know whether these two are **statistically independent** — whether knowing a shell's handedness tells
you *nothing* about its continuous shape, and vice versa, once species and phylogeny are controlled for.

**Precise question.** Within a species (or a clade carrying both chiralities), is the chirality bit independent
of the continuous shape vector? Concretely: conditioning continuous morphometrics on the discrete handedness
label (controlling for phylogeny, size/allometry, and environment), is there **no** systematic shape difference
between dextral and sinistral individuals beyond a trivial mirror reflection? Equivalently, is the mutual
information between handedness and shape ≈ 0?

**Why it matters (plainly).** I'm testing whether a discrete, switch-controlled, early-set body trait
(handedness) and a continuous, growth-rate-controlled trait (shape) are *orthogonal* — set by independent
machinery, neither predictive of the other. Clean independence supports that; a real (non-mirror) shape
difference between the hands, beyond what the chirality gene mechanically forces, refutes it.

**Specific sub-questions:**

1. Are there published morphometric datasets recording **both** chirality and continuous shape for the same
   individuals/species — ideally clades with naturally co-occurring dextral and sinistral forms (e.g.
   *Amphidromus*, *Partula*, *Euhadra*, certain Clausiliidae)?
2. In such data, do sinistral and dextral forms differ in continuous shape *beyond* a mirror reflection — any
   real (non-mirror) shape covariance with handedness?
3. Is chirality known to be **developmentally/genetically coupled** to any shape parameter (does the chirality
   locus pleiotropically affect coil geometry), or is it cleanly modular from shape?
4. At the macroevolutionary scale: across gastropods, do sinistral lineages occupy the **same** region of shape
   morphospace as dextral lineages, or is one hand confined to a sub-region?
5. Phylogenetic-comparative caveats: the right way to control for shared ancestry and for the rarity of
   sinistral lineages when testing this independence (sign tests, phylogenetic MANOVA, paired chiral-dimorphic
   contrasts).

**What would settle it:** a dataset (or meta-analysis) with chirality and continuous morphometrics measured on
the same shells, plus a phylogeny-controlled test of independence. Pointers to such data, or to the closest
existing analyses, are exactly what I need. A clean independence (or its failure) is the result either way —
the failure is the more interesting outcome.
