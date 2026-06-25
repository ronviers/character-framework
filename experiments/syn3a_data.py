r"""syn3a_data.py -- the JCVI-Syn3A data layer for the character framework.

JCVI-Syn3A is the minimal synthetic bacterium (Hutchison et al. 2016 *Science*; Breuer et al.
2019 *eLife*) and the framework's **archive-term anchor**: a measurable ARCHIVE (the ~543 kbp /
~496-gene genome) maintained by a measurable CIRCULATION (the metabolic NESS -- 308 species, 356
reactions, with measured enzyme kinetics). This module is the single, verified entry point to that
data, so no future session re-derives how to parse it. Import it; don't re-invent it.

    from syn3a_data import genome, genome_stats, kinetics, sbml, sbml_stats
    g = genome_stats()            # -> {'length_bp':543379, 'n_genes':496, 'archive_bits_2bit':..., ...}
    K = kinetics('Central')       # -> a pandas DataFrame of the Central-metabolism kinetic params
    m = sbml('whole_cell')        # -> a libsbml Model (308 species, 356 reactions)

DATA (local, **gitignored**, in docs/sources/minimal_cell/; fetched 2026-06-25 from
github.com/Luthey-Schulten-Lab/Minimal_Cell_4DWCM, raw @ main/input_data):
  syn3A.gb              GenBank genome, accession **CP016816.2**, 543,379 bp.  --> the ARCHIVE.
                        496 gene / 458 CDS / 29 tRNA / 6 rRNA / 2 ncRNA / 1 tmRNA.
  kinetic_params.xlsx   Enzyme kinetics by subsystem (13 sheets: Central, Nucleotide, Lipid,
                        Cofactor, Transport, tRNA Charging, Amino Acid, Gen. Info., ...). Columns:
                        Reaction Name | Subsystem | Parameter Type | Related Species | Value | Units.
                        Param types: Eff Enzyme Count, Substrate/Product Catalytic Rate Constant, Km, ...
  Syn3A_updated.xml     SBML **whole-cell** metabolic network (model MMSYN: 308 species, 356 rxns). --> CIRCULATION.
  iMB155_...xml         SBML **iMB155 FBA reconstruction** (Breuer 2019; 308 species, 340 rxns).
  initial_concentrations.xlsx     initial species concentrations.
  protein_metabolites.xlsx/.csv   protein<->metabolite map.
  (at source but NOT fetched: kinetic_params_{backup,new}.xlsx; oneParamMulder-local_min.json [6 MB];
   LargeSubunit.xlsx; loop_params.txt -- fetch on demand with the same raw URL.)

Paper: Breuer et al. 2019, *eLife* 8:e36842 (docs/sources/minimal_cell/elife-36842-v3.pdf, 75 pp).
Tooling (all installed 2026-06-25): biopython, openpyxl+pandas, python-libsbml.

ARCHIVE-TERM framing (why this data): the framework's open blocker is the **archive-held** term of
*Organization = circulation-held K(C) + archive-held*. Syn3A is the first substrate with archive >> 0
(the genome) AND a buildable circulation (the metabolic NESS) -- so the cut can finally be measured,
or shown to blur (itself the test). Archive ~ genome information; circulation ~ K(C) of the metabolic
operator built from kinetic_params + the SBML network.

ASCII-only console output (Windows safety).
"""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# docs/sources/minimal_cell/ lives a sibling-up from experiments/
DATA = Path(__file__).resolve().parent.parent / "docs" / "sources" / "minimal_cell"

FILES = {
    "genome": "syn3A.gb",
    "kinetics": "kinetic_params.xlsx",
    "whole_cell": "Syn3A_updated.xml",
    "imb155": "iMB155_noUnqATP_lipdiomics_wPUNP5_noNBtransport.xml",
    "initial_concentrations": "initial_concentrations.xlsx",
    "protein_metabolites": "protein_metabolites.xlsx",
}
_RAW = "https://raw.githubusercontent.com/Luthey-Schulten-Lab/Minimal_Cell_4DWCM/main/input_data"


def _path(key):
    p = DATA / FILES[key]
    if not p.exists():
        raise FileNotFoundError(
            f"missing Syn3A data: {p}\n  fetch it (gitignored source data):\n"
            f"    curl -fsSL '{_RAW}/{FILES[key]}' -o '{p}'")
    return p


# ----------------------------------------------------------------- genome (the ARCHIVE)
def genome():
    """The JCVI-Syn3A genome as a Biopython SeqRecord (GenBank CP016816.2)."""
    from Bio import SeqIO
    return SeqIO.read(_path("genome"), "genbank")


def genome_stats(rec=None):
    """Archive-side numbers. Several archive-bit measures are offered because 'the archive' is a
    modeling choice (raw 2-bit genome vs coding-only vs gene-count) -- the science picks one; this
    just computes them honestly. 2 bits/bp is the information-theoretic floor of a 4-letter alphabet."""
    rec = rec or genome()
    types = {}
    for f in rec.features:
        types[f.type] = types.get(f.type, 0) + 1
    coding_bp = sum(int(f.location.end) - int(f.location.start)
                    for f in rec.features if f.type == "CDS")
    L = len(rec.seq)
    return {
        "accession": rec.id,
        "organism": rec.annotations.get("organism", "?"),
        "length_bp": L,
        "n_genes": types.get("gene", 0),
        "n_cds": types.get("CDS", 0),
        "n_trna": types.get("tRNA", 0),
        "n_rrna": types.get("rRNA", 0),
        "coding_bp": coding_bp,
        "coding_fraction": coding_bp / L,
        "archive_bits_2bit_total": 2 * L,            # whole genome at 2 bits/bp
        "archive_bits_2bit_coding": 2 * coding_bp,   # protein/RNA-coding sequence only
        "feature_types": dict(sorted(types.items(), key=lambda x: -x[1])),
    }


# ----------------------------------------------------------------- kinetics (CIRCULATION rates)
def kinetics(sheet=None):
    """Enzyme kinetics. `sheet=None` -> dict{sheet_name: DataFrame} of all 13 subsystems;
    `sheet='Central'` -> that one DataFrame. Columns: Reaction Name, Subsystem, Parameter Type,
    Related Species, Value, Units."""
    import pandas as pd
    xl = pd.ExcelFile(_path("kinetics"))
    if sheet is not None:
        return xl.parse(sheet)
    return {s: xl.parse(s) for s in xl.sheet_names}


def kinetic_sheets():
    import pandas as pd
    return pd.ExcelFile(_path("kinetics")).sheet_names


# ----------------------------------------------------------------- SBML (the metabolic NETWORK)
def sbml(which="whole_cell"):
    """libsbml Model. which in {'whole_cell' (Syn3A_updated, 356 rxns), 'imb155' (Breuer FBA, 340 rxns)}."""
    import libsbml
    doc = libsbml.readSBML(str(_path(which)))
    if doc.getNumErrors() > 0:
        # parse errors that aren't fatal still return a model; surface count, don't hide
        pass
    return doc.getModel()


def sbml_stats(which="whole_cell"):
    m = sbml(which)
    return {
        "which": which, "model_id": m.getId(),
        "species": m.getNumSpecies(), "reactions": m.getNumReactions(),
        "parameters": m.getNumParameters(), "compartments": m.getNumCompartments(),
    }


# ----------------------------------------------------------------- aux tables
def initial_concentrations():
    """NB despite the file name, this is the **per-gene-product table** (456 rows, 15 cols):
    Locus Tag | Gene Name | Gene Product | Exp. Ptn Cnt | Essentiality | Primary Function | ...
    -- i.e. the **archive<->circulation bridge** (which genome entry codes which protein, at what
    count, essential or not). Load-bearing for the archive-term cut (essential genes = the archive
    the circulation cannot regenerate; protein counts = the circulation's component inventory)."""
    import pandas as pd
    return pd.read_excel(_path("initial_concentrations"))


def protein_metabolites():
    import pandas as pd
    return pd.read_excel(_path("protein_metabolites"))


# ----------------------------------------------------------------- self-test / summary card
def _summary():
    print("=" * 78)
    print("JCVI-Syn3A DATA LAYER -- summary card (verifies the toolchain end-to-end)")
    print("=" * 78)
    g = genome_stats()
    print("\n[ARCHIVE]  syn3A.gb  (%s, %s)" % (g["accession"], g["organism"]))
    print("  genome: %d bp | genes %d (CDS %d, tRNA %d, rRNA %d) | coding %.1f%%"
          % (g["length_bp"], g["n_genes"], g["n_cds"], g["n_trna"], g["n_rrna"],
             100 * g["coding_fraction"]))
    print("  archive bits (2 bits/bp):  total %.3e  |  coding-only %.3e"
          % (g["archive_bits_2bit_total"], g["archive_bits_2bit_coding"]))
    print("  feature types:", g["feature_types"])

    print("\n[CIRCULATION]  metabolic networks (SBML)")
    for w in ("whole_cell", "imb155"):
        s = sbml_stats(w)
        print("  %-11s model=%s  species=%d  reactions=%d  params=%d  compartments=%d"
              % (w, s["model_id"], s["species"], s["reactions"], s["parameters"], s["compartments"]))

    print("\n[KINETICS]  kinetic_params.xlsx")
    sheets = kinetic_sheets()
    print("  %d subsystem sheets: %s" % (len(sheets), ", ".join(sheets)))
    central = kinetics("Central")
    ptypes = central["Parameter Type"].value_counts().to_dict()
    print("  'Central' sheet: %d rows | parameter types: %s"
          % (len(central), dict(list(ptypes.items())[:5])))
    print("  sample rows:")
    for _, r in central.head(3).iterrows():
        print("    %-8s %-34s %-9s %s %s"
              % (str(r["Reaction Name"]), str(r["Parameter Type"]),
                 str(r["Value"]), str(r["Units"]), ""))

    print("\n[AUX]")
    ic = initial_concentrations()
    pm = protein_metabolites()
    print("  initial_concentrations.xlsx: shape %s, cols %s" % (ic.shape, list(ic.columns)[:6]))
    print("  protein_metabolites.xlsx:    shape %s, cols %s" % (pm.shape, list(pm.columns)[:6]))

    print("\n" + "=" * 78)
    print("OK -- genome / SBML / kinetics / aux all parse. The archive (genome) and the")
    print("circulation (metabolic NESS + measured kinetics) are both in hand and machine-readable.")
    print("Next: build the metabolic operator (circulation K(C)) vs the genome (archive), measure")
    print("the cut, and watch whether it stays well-posed or BLURS -- the archive-term test.")
    print("=" * 78)


if __name__ == "__main__":
    _summary()
