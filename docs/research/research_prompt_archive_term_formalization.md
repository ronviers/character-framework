# Research prompt — is the ARCHIVE-HELD term already formalized? (defer-or-claim)

**For the outbound multi-model research channel.** Self-contained; assumes no prior context. **Constraint:
open-access / freely-downloadable sources only** (no paywalled articles — prefer open-access journals,
author/lab sites, PMC, arXiv/bioRxiv, philsci-archive, public repos). Return a unified, source-cited report.

**This is a deferral audit, not a discovery hunt.** We have a measurement and a candidate reading. We need to
know **where that reading already lives in the established literature**, so we *import and cite* rather than
reinvent. A finding of "this is exactly Kolchinsky–Wolpert / Rosen / X, here is the citation and the precise
correspondence" is the **most valuable** outcome, not a disappointing one. We want to be told what to defer to.

## The object and the measurement (what we have)

We decompose biological/physical organization as:

> **Organization = circulation-held `K(C)` + archive-held.**

- **circulation-held `K(C)`** — the organization a running non-equilibrium steady state (NESS) recovers after
  **complete turnover of its parts** (no static record beyond replacement of generic components). Measured as
  `K_topo (= b₁, protected cycle count) + K_metric (slow-manifold dimension)`. Anchored on two record-free
  substrates (a circadian clock, a chemical oscillator).
- **archive-held** — the distinctions whose fidelity requirement **exceeds** the circulation's self-specifying
  capacity: the standing high-dimensional part-specification the running fluxes **consult but cannot
  regenerate** from their own state (DNA, on this reading).

**The measurement (on JCVI-Syn3A, the minimal cell — Breuer et al. 2019, eLife e36842).** We partitioned the
irreducible archive (the **essential** genes) against the metabolic circulation (the gene set of the metabolic
NESS, from the kinetic model + SBML). Headline metric `blur = |E \ M| / |E|` (E = essential genes, M =
metabolic-circulation gene set; a set difference between two given datasets). **Result: the cut blurs** — blur
≈ 0.6–0.77 across circulation definitions; the metabolic circulation accounts for under half the irreducible
archive, and the largest unaccounted block is the **expression apparatus** (transcription/translation/
replication — the machinery that *reads* the archive), ≈41% of the archive's coding bits. Our reading: the
reader is **stored yet active** — neither passive archive nor the metabolic circulation — a **self-referential
seam** where the two-term sum fails. We suspect this is **not novel** and want it located.

## The questions (ranked)

1. **Is the archive-held term Kolchinsky–Wolpert "stored semantic information"?** (Kolchinsky & Wolpert 2018,
   *Interface Focus*; arXiv:1806.08053 — semantic information = the information a system holds about its
   environment that is **causally necessary to maintain its existence**, with a **stored** vs **observed**
   split.) Precisely: does their "stored semantic information" formalize "the distinctions the circulation
   cannot regenerate but must consult to persist"? What exactly do they define and measure? **Has anyone
   applied it to a genome / metabolic network / FBA model / minimal cell** — i.e. is our blur an instance of a
   measure someone has already computed on biological data? Give the closest existing computation.

2. **Does Rosen's (M,R) systems / closure to efficient causation already own "the reader that produces the
   reader"?** State the precise formal claim (the `β = B` closure that terminates the regress). Is our
   "⊗-fixed-point re-entering its own input set" identical to it? What is the **current standing** of this work
   (including the contested non-computability claims of *Life Itself*) — is it considered rigorous, fringe, or
   superseded? What, if anything, would a topological/transverse-symmetry reading add that (M,R) does not have?

3. **Where do the autocatalysis/closure formalisms bound the claim?** For each — RAF theory (Hordijk–Steel),
   the hypercycle (Eigen–Schuster), the chemoton (Gánti), autopoiesis (Maturana–Varela), and the von Neumann
   constructor/tape — state in one line what it formalizes about the archive↔reader coupling and whether it
   makes our "blur" trivial/expected. We already cite RAF, hypercycle, von Neumann; we want the **gaps** and
   the **sharpest** antecedent for *the non-separability of metabolism from its own expression machinery*.

4. **Has the metabolism-vs-expression-vs-unknown essential-gene split been framed information-theoretically
   before?** Independently of our framework: is there published work (minimal-cell, systems-biology,
   origin-of-life, or info-theory of cells) that quantifies **what fraction of a cell's irreducible/essential
   complement is its own information-processing machinery vs its metabolism**, or that treats the genome as
   "information the dynamics cannot regenerate"? Name it. (We expect Breuer 2019 / Hutchison 2016 / Thornburg
   2022 already report the gene-category split; we want whether anyone has given it the *archive-held / stored-
   information* reading.)

5. **The deferral verdict.** Synthesize: **which existing formalism is the right home for the archive-held
   term**, what the framework must **import and cite** (with citations), and what — if anything — is **genuinely
   open** (an unclaimed gap a topological/transverse reading could occupy) vs **already solved**. If the honest
   answer is "the archive-held term is stored semantic information (KW), the reader is Rosen closure, and the
   framework adds only a re-description," **say that plainly** — that is the result we are testing for.

## Deliverable

A unified, source-cited report (open-access links only) that answers 1–5, ending with: (a) a **ranked map** of
formalism → which piece of our object it owns, with the single best citation each; (b) a clear **import list**
(what to add to `character_prior_art.md` and defer to); and (c) a one-paragraph **honest verdict** on whether
the framework's archive-term reading is an import-re-description or has an unclaimed, defensible residue.
