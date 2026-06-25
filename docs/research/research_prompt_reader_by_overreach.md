# Research prompt — READER-BY-OVERREACH + the offline-read corollary: defer-or-claim

**For the outbound multi-model research channel.** Self-contained; assumes no prior context. **Constraint:
open-access / freely-downloadable sources only** (open-access journals, author/lab sites, PMC, arXiv/bioRxiv,
philsci-archive, public repos). Return a unified, source-cited report.

**This is a deferral audit, not a discovery hunt.** We have a conjecture and several candidate readings. We need
to know **where each already lives in the established literature**, so we *import and cite by name* rather than
reinvent. "This is exactly Still / England / McClelland / Pattee / Eigen — here is the citation and the precise
correspondence" is the **most valuable** outcome, not a disappointing one. We want to be told what to defer to,
and to have any residue sized honestly and small.

## Background object (what the framework already has)

A driven non-equilibrium steady state (NESS) has a finite **keep** — the organization it recovers through
complete turnover of its parts — bounded by a **wall**: maintaining a heterogeneous wiring of `N` loops costs
~`N log N` to re-specify while the running dynamics repair only ~`N` per unit dissipation. Past the wall, surplus
organization must be **archived** (a standing record the dynamics consult but cannot regenerate). A **reader** is
the machinery that reconstructs the running organization from the archive. (Already imported: archive-held term =
Kolchinsky–Wolpert stored semantic information; reader-produces-reader seam = Rosen closure to efficient
causation / Pattee epistemic cut.)

## The conjecture and corollary (what we want located)

**Reader-by-overreach.** Near the keep's ceiling, a system that repeatedly *overreaches* — transiently closing
loops more heterogeneous than its turnover can re-specify — runs briefly more efficiently, then fails when
re-specification beats repair. Each failure deposits a persistent **trace** (a metric/configurational residue).
Once *consulting the trace costs less dissipation than re-minting the loop from scratch, including the reader's
own upkeep*, readout machinery is thermodynamically selected — producing the **reader**. Path:
ascent → failure → trace → archive → reader.

**The offline-read corollary.** A keep near its ceiling cannot spend all dissipation maintaining organization
*and* build/use the reader at once (finite budget; "near the ceiling" = repair ≈ capacity); and reading traces
masked by the running attractor may require *loosening* that attractor (a controlled descent into the metric
sector). So **offline reconstruction phases** (exploit → consolidate → exploit) are predicted as structural,
with a falsifiable signature: **anti-correlation between running coordination and reading**.

## The questions (ranked) — for each: the precise formal claim, the citation, the closest existing computation, and an explicit verdict (owns it / partial / doesn't)

1. **The crossover.** Is "a system stores information precisely when consulting it costs less than recomputing
   it, and readout/predictive machinery is thermodynamically *selected* for that saving" owned? Candidates:
   **Still et al., "Thermodynamics of Prediction"** (PRL 2012) + Still's later nonequilibrium-prediction work;
   **England, dissipative adaptation** (J. Chem. Phys. 2013; Perunov–Marsland–England, PRX 2016); **Bennett,
   logical depth** (1988) / thermodynamics of computation. Does *any* tie the saving to a **maintenance /
   error-correction wall** (re-specification outrunning repair) rather than prediction-in-general? Closest thing
   to "a *reader* selected by a dissipation crossover"?

2. **The trace.** Is "a driven system pushed past its maintenance capacity leaves an *informative, re-readable*
   residue — one that lowers the cost of re-reaching the prior configuration" established? Candidates: return-point
   / hysteresis memory (Sethna; Preisach), aging in glasses, eligibility traces, reservoir computing, synaptic
   tagging-and-capture. Established result on whether such residues carry *usable mutual information* with the
   configuration that produced them, vs. entropic noise? (This is the conjecture's weakest assumption — press it.)

3. **The forced alternation.** Is "a system that both runs and must reorganize from a record is *forced* to
   time-share into online/offline phases" owned? Candidates: **Complementary Learning Systems**
   (McClelland–McNaughton–O'Reilly 1995); **Synaptic Homeostasis Hypothesis** (Tononi–Cirelli); the **Wake-Sleep
   algorithm** (Hinton et al. 1995); **experience replay** (RL); the **stability–plasticity dilemma** (Grossberg);
   **Crick–Mitchison** reverse-learning & **Hopfield** "unlearning" (1983); **simulated annealing**. For each:
   functional/empirical, or is there a *thermodynamic (dissipation-budget)* derivation that offline phases are
   *necessary*? Sharpest antecedent for **"reading requires loosening the running attractor"**? Anyone reporting
   the predicted **coordination ⊥ reading anti-correlation**?

4. **The form of the archive — forced, or frozen accident?** (a) Is there a named, established argument that
   high-fidelity heritable storage is *pressed toward* discrete/digital, error-correctable encoding as the
   information it must carry grows? Candidates: **von Neumann** digital restoration / reliable computation from
   unreliable parts; **Shannon** channel coding; **Eigen's error threshold** (sustainable sequence complexity
   bounded by per-symbol copy fidelity); **Pattee's** rate-independence of the symbol. State each precisely.
   (b) **Crucially** — is the *specific* realized form (a **digital, aperiodic 1-D polymer**) regarded as
   **forced/convergent** or as a **frozen accident** (Crick; Gould's contingency)? With a single realized origin
   (`n = 1`), is necessity-vs-contingency even *decidable*? We want the established position on what is a genuine
   selective pressure (a gradient) versus contingent baggage read backward as necessity. (Place Pattee's cut at
   the **archive/keep** = genotype/phenotype boundary, *not* any within-dynamics split.)

5. **The residue.** After 1–4, what (if anything) is *not* in the literature? We suspect the framework's only
   originals are (a) anchoring the crossover specifically to the **keep's maintenance wall** (~`N log N` vs ~`N`),
   and (b) a **sector reading** — the reader as a metric→topological back-channel — that *predicts* a measured
   biological observation (JCVI-Syn3A: the genome's irreducible archive is dominated by the expression/reader
   apparatus, ≈41% of archive bits, where the circulation/archive cut blurs). Confirm or shrink: is even (a) or
   (b) already present?

6. **Disconfirmers.** What would *kill* the conjecture: a result that failed-overreach traces are generically
   uninformative; that offline reconstruction is demonstrably *not* budget-forced (routine concurrent online
   reorganization); or that the crossover dies once the reader's own maintenance cost is included.

## Output

A unified report, every claim source-cited (open-access link), organized by the six questions. For each candidate
antecedent: the one-line formal claim, the citation, and an explicit verdict — **owns it / partially / doesn't**.
End with a one-paragraph **residue statement**: the smallest honest description of what, if anything, is the
framework's own, at its true (small) size — and, for Q4, a one-line verdict on whether "the archive had to be
digital/aperiodic" is a defensible necessity, a bounded selective pressure, or an `n = 1` frozen accident.
