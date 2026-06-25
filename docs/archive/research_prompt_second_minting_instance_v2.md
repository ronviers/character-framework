# Research prompt v2 — a SECOND network that mints via the *kinetic-proofreading* topology

**For the outbound multi-model research channel.** Self-contained; assumes no prior context. Return a
unified, source-cited report: a **ranked shortlist of concrete, named, published systems**, each with the
location of its **measured/fitted rate constants** (SI table, repo, fitted figure). A candidate with no
accessible kinetics is not a candidate. **Supersedes v1** — read the "what round 1 proved" section: a
prior sweep already ruled out the obvious classes, and re-proposing them is a non-answer.

## Why v2 exists — the precise structure we now know we need

We have **one** real instance (a fuel-driven DNA reaction network) and want a **second of the exact same
kind**. Round 1 swept driven reaction networks broadly and converged on a single discriminating gate that
*almost everything fails* — and understanding *why* the one instance passes tells us exactly where to
look now.

**The shape that passed, and the mechanism that makes it pass.** Reduce the system to a small cyclic
state graph. The winning instance is a 3-state quencher cycle `OQ → FQ → Q → OQ` in which:

- the **chemostatted small molecules** (a fuel strand `F`, an output strand `O`) enter **only through
  reversible binding edges**, each appearing **once forward and once backward** around the cycle — so
  they **cancel exactly** in the cycle-affinity product;
- the **dissipative drive** is an **irreversible *catalytic* step on a bound complex** — an enzyme
  (RNase H) hydrolyses the bound fuel, a step that is **unimolecular in the bound complex** (independent
  of the free fuel concentration) and sends the consumed fuel to a **waste sink outside the cycle**.

The result is that the protected cycle affinity is a **pure ratio of measured rate constants**:

```
𝒜  =  ln( k_drive / k_reverse )  ≈  14.5 nats
```

bath-independent in sign and magnitude, with the sign **locked one-way by the irreversible catalytic
step**. *That* is the minting structure — an emergent network invariant, not the raw fuel reservoir
potential. This is the **Michaelis–Menten / kinetic-proofreading** topology.

## What round 1 PROVED fails — do NOT re-propose these (this is the whole point of v2)

A broad sweep already returned, and correctly rejected, the obvious "driven cycle" candidates. They fail
**one specific gate**: their fuel is consumed **stoichiometrically on a cycle edge**, with its products
released back to **chemostatted cycle baths**, so the bath species appear **asymmetrically** and the cycle
affinity becomes `stoichiometry · Δμ_fuel` — **tethered to the reservoir**, not a network rate-constant
ratio. Named and excluded:

- **ATP-driven molecular motors** (F1-ATPase, kinesin, myosin): one ATP in, ADP + Pi out, per driving
  step → affinity = Δμ_ATP, bath-tethered. **Excluded.**
- **KaiABC circadian oscillator** (Rust et al. 2007): phosphotransfer consumes ATP stoichiometrically →
  affinity tethered to `2·Δμ_ATP`. **Excluded.**
- **Carbodiimide/EDC-fuelled dissipative self-assembly** (Boekhoven/van Esch lineage; e.g. Tena-Solsona
  2018): EDC → EDU is a bimolecular net fuel burn → affinity tethered to `[EDC]/[EDU]`. **Excluded.**
- **Goldbeter–Koshland / futile phosphorylation cycles**: ATP/ADP appear asymmetrically. **Excluded.**
- The DNA system we already have (DNA hybridization + RNase-H hydrolysis, 3-state quencher). **We own
  it — propose something else.**

These are real NESS cycles with genuine circulation; they are **not** the minting structure. Do not
return them, and do not return their close relatives unless you can show the affinity is a
**rate-constant ratio, not a reservoir Δμ**.

## The binding requirements (all six)

1. **Real & published kinetics** — measured or experimentally-fitted rate constants, accessible (SI table,
   repo, fitted time-course). A purely theoretical/illustrative-parameter model is a FAIL.
2. **A reversible binding module that is detailed-balanced when the drive is off** — turn the catalyst /
   drive off and the cycle obeys detailed balance (zero net current). This is the minting "off" baseline.
3. **An irreversible *catalytic* drive step on a bound complex** — a unimolecular (Michaelis–Menten /
   proofreading) catalytic transformation that breaks detailed balance, foldable to a pseudo-first-order
   rate by quasi-steady-state. **Critically: the consumed fuel must be converted to NON-REBINDING waste**
   (degraded/cleaved fragments that never re-enter the cycle) — *not* a chemostatted product (like ADP/Pi)
   that rebinds on another cycle edge. A rebinding product is exactly what re-tethers the affinity to
   `Δμ_fuel` and breaks the gate.
4. **THE GATE — the cancellation.** The chemostatted small molecules enter **only via reversible binding**
   and **cancel in the cycle affinity**, so the protected affinity is `𝒜 = ln(k_drive/k_reverse)` — a
   **ratio of measured rate constants**, NOT `Δμ_fuel`. *State explicitly whether this holds and show the
   cancellation.* This is the requirement that almost everything fails.
5. **Drive-locked sign** — the sign of `𝒜` is fixed by the one-way catalytic step and cannot be flipped
   by deforming the reversible rates, only zeroed by removing the drive.
6. **A fuel/drive-cut collapse** — removing the catalyst/drive collapses the circulation to equilibrium
   (observed, or predictable from the kinetics).

## Where to look (the catalytic / proofreading class — reverse the hunt away from motors & self-assembly)

Every entry still owes a **named paper with accessible rate constants**:

1. **Enzymatic-degradation-driven networks — the win's own mechanism (STRONGEST).** A nuclease /
   exonuclease / protease *destroys* the fuel or substrate into non-rebinding fragments. **PEN-toolbox**
   DNA/enzyme oscillators and bistables (polymerase + nickase + **exonuclease**; Fujii–Rondelez,
   Montagne, Baccouche, Genot) — the exonuclease degradation is the irreversible drive to a waste sink,
   templated bindings are reversible; measured/fitted rates abound. **Protease-fuelled** peptide reaction
   networks (trypsin/chymotrypsin-driven self-assembly). RNase-driven RNA networks. Same mechanism as the
   win, distinct chemistry — this is where a clean second instance is most likely.
2. **Cytoskeletal treadmilling** (microtubule / actin) — nucleotide binds the subunit reversibly, then
   hydrolyses **unimolecularly on the bound subunit** (GTP→GDP, independent of free [GTP] once bound),
   and the GDP is carried *out with the subunit* (off-cycle), not released as a rebinding bath. Measured
   rates exist (Mitchison–Kirschner lineage). Check the cancellation explicitly, but the structure fits.
3. **Kinetic-proofreading systems — only if the spent fuel is removed.** Aminoacyl-tRNA / ribosomal
   proofreading (Rodnina–Wintermeyer measured the full rate set), aaRS editing, T-cell receptor
   (McKeithan): the canonical home of the topology, BUT standard phosphotransfer releases GDP+Pi as
   **chemostatted, rebinding** baths → affinity re-tethered to `Δμ_GTP` → FAILS the gate unless the
   products are swept/regenerated off-cycle. Treat as a candidate only with that caveat addressed.
4. **Any catalyst-driven cycle** where the catalytic step is unimolecular on a bound complex AND the
   consumed fuel becomes non-rebinding waste, with a reversible-binding detailed-balanced off-baseline.

## What a PASS must deliver (per candidate)

- **Full citation + exactly where the rate constants live** (SI table / repo / "fitted to Fig. N").
- **The reduced cyclic state graph**, identifying: (a) the **reversibly-binding chemostatted species** and
  the demonstration that they **cancel** in the cycle affinity; (b) the **irreversible catalytic drive
  step** and its **waste sink**; (c) the **detailed-balanced off-baseline**.
- **The protected affinity as a rate-constant ratio** `ln(k_drive/k_reverse)` — confirm it is NOT the raw
  fuel Δμ (requirement 4).
- **Drive-cut collapse**: observed (with timescale) / predictable / absent.
- **VERDICT: PASS / WEAK (=FAIL) / FAIL**, plus the single requirement that fails.

Rank by how cleanly requirement **4 (the cancellation)** is met from published numbers — that is the gate
the entire round-1 sweep failed. **Name the single best lead and say exactly what rate-constant data we
would download to start computing tomorrow.**
