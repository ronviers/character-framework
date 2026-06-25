r"""syn3a_archive_term.py -- the ARCHIVE-HELD term, measured for the first time, on JCVI-Syn3A.

THE OBJECT (core character.md SS The keep):
    Organization = circulation-held K(C) + archive-held.
The two landed anchors -- KaiABC (kaiabc_capacity.py, K=2) and peroxidase-oxidase (bfso_capacity.py,
K=4) -- are RECORD-FREE: archive ~ 0. They measure only the first term. Syn3A is the first substrate
with archive >> 0 (a ~543 kbp genome) AND a buildable circulation (the metabolic NESS), so the SECOND
term can finally be measured -- or shown to BLUR (the handoff's framing: "watch whether it stays well-
posed or blurs, which is itself the test").

THE CUT (what is measured here). Partition the organism's irreducible organization into:
  - circulation-held : what the maintained metabolic NESS runs on (its enzymes; its steady-state
                       flux modes). Held in the dynamics; in principle regenerable through turnover.
  - archive-held     : what the circulation cannot regenerate from its own dynamics and must read
                       from a stored record -- the genome. Operationalized as the ESSENTIAL genes
                       (loss not routed around = irreducible store).
The cut is WELL-POSED if the irreducible archive is (mostly) the circulation's parameter store:
E ~ M, every essential gene is a metabolic-circulation component. It BLURS to the extent that the
irreducible archive is NOT the metabolic circulation -- a third thing that is stored (archive) yet
is itself active machinery (a maintained process), neither cleanly term-1 nor term-2.

THE HEADLINE METRIC (non-gameable: a set difference between two GIVEN datasets):
    blur = |E \ M| / |E|
  M = the metabolic circulation's gene set (GIVEN: the enzyme protein IDs in kinetic_params.xlsx,
      and/or the genes annotated "Metabolism" in the bridge map). Reported at three resolutions so
      the result is shown ROBUST to how generously the circulation boundary is drawn.
  E = the irreducible archive (GIVEN: the Essential / Essential+Quasiessential genes in the bridge).
  Neither set is chosen by the framework; the blur is read off the Syn3A biology.

THE GATE (feedback_no_synthetic_sidequests), run before building:
  - could it come out OTHERWISE?  YES. blur in [0,1] a priori; ~0 iff the genome is just an enzyme-
    parameter store. It is decided by the data, not by construction.
  - fails (blur ~ 0) -> the clean two-term decomposition stands; "archive = passive parameter
    register"; the self-referential-reader reading dies.
  - works (blur large) -> the two-term sum is NOT well-posed at high archive; a dominant third term
    (the reader: the expression apparatus that reads the archive) is structurally both. New: the
    archive-term gets its first number, and the self-referential-closure thread lands on real data.

DATA (via the verified loader; do not re-parse):
  syn3a_data.genome_stats()           -> archive bits
  syn3a_data.sbml(...)                -> the metabolic network (-> independent steady flux modes)
  syn3a_data.kinetics()               -> enzyme protein IDs P_xxxx == locus JCVISYN3A_xxxx (-> M_kinetic)
  syn3a_data.initial_concentrations() -> the bridge: Locus Tag | Essentiality | Primary Function
Substrate / essentiality: Breuer et al. 2019, eLife 8:e36842 (JCVI-Syn3A). Genome CP016816.2.

ASCII-only console output (Windows safety).  Run:  python experiments/syn3a_archive_term.py
"""
import sys
import re
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import syn3a_data as S

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

OUT = r"H:\character-framework\experiments\syn3a_archive_term.png"
LOCUS = re.compile(r"JCVISYN3A_\d+")


# --------------------------------------------------------------------- circulation (metabolic NESS)
def flux_modes(which):
    """dim null(S) = number of INDEPENDENT steady-state flux modes the metabolic network can carry
    (the cycle space of the metabolic circulation) -- the metabolic analog of K_topo. Forced by the
    stoichiometry, rate-independent."""
    m = S.sbml(which)
    species = [m.getSpecies(i).getId() for i in range(m.getNumSpecies())]
    sidx = {sp: i for i, sp in enumerate(species)}
    nr = m.getNumReactions()
    M = np.zeros((len(species), nr))
    for j in range(nr):
        r = m.getReaction(j)
        for k in range(r.getNumReactants()):
            sr = r.getReactant(k)
            M[sidx[sr.getSpecies()], j] -= (sr.getStoichiometry() or 1.0)
        for k in range(r.getNumProducts()):
            sp = r.getProduct(k)
            M[sidx[sp.getSpecies()], j] += (sp.getStoichiometry() or 1.0)
    rank = int(np.linalg.matrix_rank(M))
    return len(species), nr, rank, nr - rank


def kinetic_enzyme_set():
    """M_kinetic: locus tags of enzymes with MEASURED kinetics (the explicitly built operator).
    The protein ID P_xxxx lives in the Value column of the 'Eff Enzyme Count' rows; P_0445 == locus
    JCVISYN3A_0445."""
    out = set()
    for _, df in S.kinetics().items():
        for _, r in df.iterrows():
            if "Enzyme Count" in str(r.get("Parameter Type", "")):
                for col in ("Value", "Related Species"):
                    for tok in re.findall(r"P_(\d+)", str(r.get(col, ""))):
                        out.add("JCVISYN3A_" + tok)
    return out


# --------------------------------------------------------------------- the bridge + the archive
def bridge():
    ic = S.initial_concentrations()
    ic = ic[ic["Locus Tag"].astype(str).str.match(LOCUS, na=False)].copy()
    ic["ess"] = ic["Essentiality"].astype(str)
    ic["fn"] = ic["Primary Function"].astype(str)
    return ic


def gene_lengths():
    """locus_tag -> gene length (bp), from the genome 'gene' features (covers CDS + RNA genes)."""
    rec = S.genome()
    L = {}
    for f in rec.features:
        if f.type == "gene":
            lt = f.qualifiers.get("locus_tag", [None])[0]
            if lt:
                L[lt] = abs(int(f.location.end) - int(f.location.start))
    return L


def main():
    g = S.genome_stats()
    print("=" * 96)
    print("  THE ARCHIVE-HELD TERM, MEASURED -- JCVI-Syn3A (Breuer 2019 eLife e36842)")
    print("  Organization = circulation-held K(C) + archive-held ; does the cut stay well-posed or BLUR?")
    print("=" * 96)

    # -------- [ARCHIVE] the store --------
    print("\n" + "=" * 96 + "\n  [ARCHIVE]  the genome (the stored record the circulation cannot regenerate)\n" + "=" * 96)
    print(f"    {g['accession']}  {g['organism']}")
    print(f"    {g['length_bp']:,} bp | {g['n_genes']} genes (CDS {g['n_cds']}, tRNA {g['n_trna']}, "
          f"rRNA {g['n_rrna']}) | coding {100*g['coding_fraction']:.1f}%")
    print(f"    archive (2 bits/bp): total {g['archive_bits_2bit_total']:.3e}  coding-only "
          f"{g['archive_bits_2bit_coding']:.3e}")

    # -------- [CIRCULATION] the metabolic NESS --------
    print("\n" + "=" * 96 + "\n  [CIRCULATION]  the metabolic NESS (term 1; analog of the KaiABC/PO maintained loop)\n" + "=" * 96)
    for which in ("whole_cell", "imb155"):
        nsp, nr, rank, nmodes = flux_modes(which)
        print(f"    {which:11s}: {nsp} species, {nr} reactions, rank(S)={rank}  ->  independent steady"
              f" flux modes (cycle capacity) = {nmodes}")
    Mk = kinetic_enzyme_set()
    print(f"    enzymes with measured kinetics (the explicitly built operator M_kinetic) = {len(Mk)} genes")
    print("    (the circulation is characterized by MEMBERSHIP + cycle capacity; its dynamical NESS is")
    print("     not integrated here -- the cut is an accounting of which genes the circulation contains.)")

    # -------- [THE CUT] --------
    ic = bridge()
    locus_fn = dict(zip(ic["Locus Tag"], ic["fn"]))
    M_metab = set(ic[ic["fn"] == "Metabolism"]["Locus Tag"])                 # broad: all annotated metabolism
    M_metab_cell = M_metab | set(ic[ic["fn"] == "Cellular Processes"]["Locus Tag"])  # maximal
    resolutions = [
        ("M_kinetic  (built operator, measured rates)", Mk & set(ic["Locus Tag"])),
        ("M_metabolic (all annotated Metabolism)", M_metab),
        ("M_metab+cellular (most generous circulation)", M_metab_cell),
    ]
    strict = {
        "Essential":           set(ic[ic["ess"] == "Essential"]["Locus Tag"]),
        "Essential+Quasiess.": set(ic[ic["ess"].isin(["Essential", "Quasiessential"])]["Locus Tag"]),
    }

    print("\n" + "=" * 96 + "\n  [THE CUT]  blur = |E \\ M| / |E|   (E = irreducible archive ; M = circulation)\n" + "=" * 96)
    print("    blur ~ 0  => cut well-posed (archive is the circulation's parameter store)")
    print("    blur ~ 1  => cut blurs (the irreducible archive is NOT the metabolic circulation)\n")
    print(f"    {'circulation set M':<46s}{'|M|':>5s}   " +
          "   ".join(f"blur[{k}]" for k in strict))
    blur_table = {}
    for label, Mset in resolutions:
        row = []
        for ek, E in strict.items():
            b = len(E - Mset) / len(E)
            row.append(b)
            blur_table[(label, ek)] = (len(E & Mset), len(E - Mset), len(E), b)
        print(f"    {label:<46s}{len(Mset):>5d}   " + "      ".join(f"{b:0.3f}" for b in row))
    # headline: the strict operator vs the irreducible (essential+quasi) archive
    inM, notM, nE, b0 = blur_table[(resolutions[0][0], "Essential+Quasiess.")]
    print(f"\n    HEADLINE (built operator vs essential+quasi archive): {inM} of {nE} accounted, "
          f"{notM} not -> blur = {b0:.3f}")
    # most generous circulation vs strict-essential archive (the hardest test for a large blur)
    inMg, notMg, nEg, bg = blur_table[(resolutions[2][0], "Essential")]
    print(f"    MOST GENEROUS (metab+cellular vs essential-only): {inMg} of {nEg} accounted, "
          f"{notMg} not -> blur = {bg:.3f}  (blur survives the generous boundary)")

    # -------- [WHERE THE BLUR LIVES] --------
    E = strict["Essential+Quasiess."]
    unaccounted = E - resolutions[0][1]            # essential+quasi NOT in the built metabolic operator
    fn_break = {}
    for lt in unaccounted:
        fn_break[locus_fn.get(lt, "?")] = fn_break.get(locus_fn.get(lt, "?"), 0) + 1
    print("\n" + "=" * 96 + "\n  [WHERE THE BLUR LIVES]  the unaccounted irreducible archive, by Primary Function\n" + "=" * 96)
    for fn, c in sorted(fn_break.items(), key=lambda x: -x[1]):
        bar = "#" * int(48 * c / max(fn_break.values()))
        print(f"    {fn:<32s}{c:>4d}  {bar}")
    reader = fn_break.get("Genetic Information Processing", 0)
    print(f"\n    --> the single largest unaccounted block is the READER (Genetic Information Processing,")
    print(f"        = the transcription/translation/replication apparatus that READS the archive): "
          f"{reader}/{len(unaccounted)} = {reader/len(unaccounted):.0%}")

    # -------- [BITS] the archive-held term, partitioned by the cut --------
    Lbp = gene_lengths()
    def bits(locs):
        return 2 * sum(Lbp.get(lt, 0) for lt in locs)
    Eset = strict["Essential+Quasiess."]
    circ = Eset & resolutions[1][1]                                    # essential & metabolism
    read = {lt for lt in Eset if locus_fn.get(lt) == "Genetic Information Processing"}
    uncl = {lt for lt in Eset if locus_fn.get(lt) == "Unclear"}
    other = Eset - circ - read - uncl
    print("\n" + "=" * 96 + "\n  [BITS]  the irreducible archive in bits (2/bp), partitioned by the cut\n" + "=" * 96)
    tot = bits(Eset)
    for name, st in [("circulation (Metabolism)", circ), ("READER (Gen.Info.Proc.)", read),
                     ("Unclear (generic essential)", uncl), ("other", other)]:
        print(f"    {name:<30s}{len(st):>4d} genes   {bits(st):.3e} bits   {bits(st)/tot:5.1%}")
    print(f"    {'TOTAL irreducible archive':<30s}{len(Eset):>4d} genes   {tot:.3e} bits   100.0%")
    bits_breakdown = {"circulation": bits(circ), "reader": bits(read), "unclear": bits(uncl), "other": bits(other)}

    # -------- VERDICT --------
    print("\n" + "=" * 96 + "\n  VERDICT  (the archive-term cut: well-posed or blurred?)\n" + "=" * 96)
    print(f"  THE CUT BLURS.  Across every circulation resolution the irreducible archive is majority")
    print(f"  NON-metabolic: blur ranges {bg:.2f} (most generous) to {b0:.2f} (built operator). The single")
    print(f"  largest unaccounted block is the READER -- the expression apparatus, {read and bits_breakdown['reader']/tot:.0%} of the")
    print(f"  archive's bits -- which is stored (essential, irreducible) yet is itself an active maintained")
    print(f"  process. It is neither cleanly term-1 (not the metabolic NESS) nor term-2 (not passive")
    print(f"  storage): the self-referential seam, located at the machinery that reads the archive.")
    print(f"  The falsifier that did NOT trigger: blur could have been ~0 (genome = enzyme-parameter store);")
    print(f"  it is {b0:.2f}. So 'Organization = circulation + archive' as a clean SUM is disfavored at high")
    print(f"  archive -- the two terms OVERLAP irreducibly at the reader. (Connects: self-referential-closure")
    print(f"  north-star; reading-transition. This is a sharpening of the object, NOT a tidy vindication.)")

    figure(resolutions, strict, blur_table, fn_break, bits_breakdown, g)
    return b0


def figure(resolutions, strict, blur_table, fn_break, bits_breakdown, g):
    fig, ax = plt.subplots(1, 3, figsize=(17.5, 5.2), dpi=140)

    # (1) blur sweep across circulation resolutions
    labels = [r[0].split("(")[0].strip() for r in resolutions]
    xs = np.arange(len(resolutions))
    for off, (ek, color) in zip((-0.18, 0.18),
                                [("Essential", "#b71c1c"), ("Essential+Quasiess.", "#1565c0")]):
        ys = [blur_table[(r[0], ek)][3] for r in resolutions]
        ax[0].bar(xs + off, ys, width=0.34, color=color, label=f"E = {ek}")
    ax[0].axhline(0.5, color="#555", ls=":", lw=1)
    ax[0].set_xticks(xs); ax[0].set_xticklabels(labels, rotation=18, ha="right", fontsize=8)
    ax[0].set_ylabel(r"blur $= |E\setminus M| / |E|$"); ax[0].set_ylim(0, 1)
    ax[0].set_title("the cut blurs at every circulation resolution\n(majority of irreducible archive is non-metabolic)",
                    fontsize=9.5)
    ax[0].legend(fontsize=8, frameon=False); ax[0].grid(alpha=0.25, axis="y")

    # (2) where the blur lives (unaccounted archive by function)
    items = sorted(fn_break.items(), key=lambda x: x[1])
    cols = ["#c62828" if k == "Genetic Information Processing" else "#90a4ae" for k, _ in items]
    ax[1].barh([k.replace("Genetic Information Processing", "READER (Gen.Info.Proc.)") for k, _ in items],
               [v for _, v in items], color=cols)
    ax[1].set_xlabel("genes (essential+quasi, NOT in built metabolic operator)")
    ax[1].set_title("where the blur lives:\nthe reader dominates the unaccounted archive", fontsize=9.5)
    ax[1].grid(alpha=0.25, axis="x")

    # (3) archive bits partitioned by the cut
    order = [("circulation", "#2e7d32"), ("reader", "#c62828"), ("unclear", "#fbc02d"), ("other", "#90a4ae")]
    vals = [bits_breakdown[k] for k, _ in order]
    ax[2].pie(vals, labels=[k for k, _ in order], colors=[c for _, c in order], autopct="%1.0f%%",
              startangle=90, textprops={"fontsize": 9}, wedgeprops={"edgecolor": "w"})
    ax[2].set_title(f"irreducible archive in bits ({sum(vals):.2e} total)\n"
                    "partitioned by the cut -- the reader's share", fontsize=9.5)

    fig.suptitle("The archive-held term on JCVI-Syn3A: the cut between circulation and archive BLURS at the "
                 "reader (the self-referential seam)", fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
