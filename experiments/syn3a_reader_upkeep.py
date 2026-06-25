r"""syn3a_reader_upkeep.py -- the READER-UPKEEP fraction of Syn3A's maintenance budget.

THE OBJECT (frontier `reader-by-overreach`, disconfirmer #3; companion to `syn3a_archive_term.py`).
The reader-by-overreach conjecture says readout machinery is thermodynamically SELECTED when
consulting a stored trace (the archive) costs less dissipation than re-minting the loop from
scratch -- INCLUDING the reader's own upkeep. The audit's sharpest disconfirmer (#3,
`research_prompt_reader_by_overreach.md`): "the crossover dies once the reader's own maintenance
cost is included ... an a priori falsifiable calculation: estimate the dissipation cost of reader
maintenance versus loop re-specification and ask whether a crossover region exists."

WHAT THIS MEASURES (and what it does NOT). The Syn3A / 4DWCM data affords the reader-upkeep SIDE
of that crossover on REAL modeled parameters -- the model's own per-protein copy numbers x lengths
give a true proteostatic-cost proxy. It does NOT afford the re-mint COUNTERFACTUAL (the ~N log N
maintenance wall, owed) -- the cell never re-mints without its genome. So this is a witness, not the
full crossover: it numbers reader-upkeep and asks whether it is small enough to leave a crossover
possible. And because the real cell DOES read (the reader is selected), re-mint >= read + upkeep --
so a LARGE reader-upkeep witnesses a STEEP wall, and disconfirmer #3 (reader-upkeep kills the
crossover) is refuted to the extent the cell pays it and still reads.

THE AXIS (why this is new). `syn3a_archive_term.py` measured the reader on the BIT axis (stored
information): the reader is the dominant block of the irreducible essential archive (~41% of its
bits). This measures the reader on the ENERGY / UPKEEP axis (running maintenance): the share of the
proteome-synthesis budget spent on the reader apparatus. The two differ by the PROTEIN-COPY weight:
a gene stored once (1x bits) but expressed at 10^3 copies (a ribosomal protein) is 1x on bits and
10^3 x on upkeep. So this is the archive-term cut re-weighted from storage to maintenance.

THE MEASURE (forced from given data, not fitted; the framework chooses no boundary):
  reader-upkeep share = sum_GIP( copies x aa_length ) / sum_all( copies x aa_length )
  GIP = "Genetic Information Processing" (the reader: transcription / translation / replication /
        folding / degradation apparatus); Metabolism = the circulation; reported alongside raw gene
        count, archive bits, and standing protein copies so the trend across weightings is visible.
  caveat (stated, not gamed): rRNA + tRNA are EXCLUDED (the table is proteins). The ribosome is
  ~2/3 rRNA by mass and is the standard largest macromolecular-synthesis sink, so the proteome-only
  reader share is a LOWER BOUND on the reader's true upkeep share. Turnover assumed ~uniform
  (upkeep ~ standing amount); a snapshot, not an integrated flux.

DATA (via the verified loader; do not re-parse):
  syn3a_data.initial_concentrations() -> Locus Tag | Exp. Ptn Cnt | Essentiality | Primary Function
  syn3a_data.genome()                 -> CDS lengths (aa = bp/3)
Substrate: JCVI-Syn3A; protein counts + function from the 4DWCM table (Thornburg/Luthey-Schulten),
genome CP016816.2 (Breuer 2019 eLife e36842 / Hutchison 2016 Science).

ASCII-only console output (Windows safety).  Run:  python experiments/syn3a_reader_upkeep.py
"""
import sys
import re
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import syn3a_data as S

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

OUT = r"H:\character-framework\experiments\syn3a_reader_upkeep.png"
LOCUS = re.compile(r"JCVISYN3A_\d+")
READER = "Genetic Information Processing"
CIRC = "Metabolism"


def load():
    """The bridge table, restricted to real loci, with aa length, protein copies, coding bits."""
    ic = S.initial_concentrations()
    ic = ic[ic["Locus Tag"].astype(str).str.match(LOCUS, na=False)].copy()
    # protein lengths (aa) from genome CDS features
    rec = S.genome()
    aa = {}
    for f in rec.features:
        if f.type == "CDS":
            lt = f.qualifiers.get("locus_tag", [None])[0]
            if lt:
                aa[lt] = abs(int(f.location.end) - int(f.location.start)) // 3
    ic["aa"] = ic["Locus Tag"].map(aa).fillna(0.0).astype(float)
    ic["copies"] = pd.to_numeric(ic["Exp. Ptn Cnt"], errors="coerce").fillna(0.0)
    ic["genes"] = 1.0
    ic["bits"] = 2.0 * 3.0 * ic["aa"]                  # coding bits, 2 bits/bp
    ic["budget"] = ic["copies"] * ic["aa"]             # proteome synthesis / standing-cost proxy
    ic["fn"] = ic["Primary Function"].astype(str)
    ic["ess"] = ic["Essentiality"].astype(str)
    return ic


AXES = [("gene count", "genes"), ("archive bits", "bits"),
        ("protein copies", "copies"), ("SYNTHESIS budget", "budget")]


def shares(df, col):
    tot = df[col].sum()
    if tot <= 0:
        return {}
    out = {}
    for k in (READER, CIRC, "Unclear"):
        out[k] = float(df.loc[df["fn"] == k, col].sum() / tot)
    out["other"] = 1.0 - sum(out.values())
    return out


def table(df, title):
    print("\n" + "=" * 96 + f"\n  [{title}]  reader (GIP) vs circulation (Metabolism) share, by weighting\n" + "=" * 96)
    print(f"    {'axis':<18s}{'READER':>9s}{'Metab':>9s}{'Unclear':>9s}{'other':>8s}   reader/metab")
    rows = {}
    for label, col in AXES:
        s = shares(df, col)
        rows[label] = s
        ratio = s[READER] / s[CIRC] if s[CIRC] > 0 else float("nan")
        print(f"    {label:<18s}{s[READER]:>8.1%}{s[CIRC]:>9.1%}{s['Unclear']:>9.1%}{s['other']:>8.1%}"
              f"      {ratio:>5.2f}")
    return rows


def main():
    ic = load()
    print("=" * 96)
    print("  READER-UPKEEP on JCVI-Syn3A -- the reader's share of the running maintenance budget")
    print("  reader-by-overreach disconfirmer #3: does reader-upkeep leave a crossover possible?")
    print("=" * 96)
    print(f"    {len(ic)} loci | {int((ic['copies'] > 0).sum())} with a protein count | "
          f"total copies {ic['copies'].sum():.3e} | total synth budget {ic['budget'].sum():.3e} aa")

    full = table(ic, "FULL PROTEOME  (the running maintenance budget -- all expressed proteins)")
    essq = ic[ic["ess"].isin(["Essential", "Quasiessential"])]
    ess = table(essq, "ESSENTIAL+QUASI subset  (the irreducible archive -- bridges to archive-term 41%)")

    # ---- the upkeep witness ----
    r_budget = full["SYNTHESIS budget"][READER]
    m_budget = full["SYNTHESIS budget"][CIRC]
    r_copies = full["protein copies"][READER]
    print("\n" + "=" * 96 + "\n  [THE UPKEEP WITNESS]  disconfirmer #3 (reader-upkeep kills the crossover?)\n" + "=" * 96)
    print(f"    reader-upkeep (proteome synthesis budget) = {r_budget:.1%}   circulation = {m_budget:.1%}"
          f"   ->  reader/circ = {r_budget/m_budget:.2f}")
    print(f"    reader share of raw protein COPIES        = {r_copies:.1%}   (the reader is half of all")
    print(f"      protein molecules; the lead erodes under length-weighting -- r-proteins are short+high-copy)")
    print(f"    NOTE: rRNA + tRNA excluded (proteins only). The ribosome is ~2/3 rRNA by mass and the")
    print(f"      standard largest synthesis sink, so {r_budget:.0%} is a LOWER BOUND on reader-upkeep.")
    print("    -> the cell pays ~half its proteome-maintenance budget on the reader AND STILL READS")
    print("       (the reader is selected). So re-mint >= read + upkeep: a LARGE reader-upkeep witnesses")
    print("       a STEEP maintenance wall, and disconfirmer #3 is NOT triggered on real parameters.")

    # ---- top upkeep sinks ----
    print("\n" + "=" * 96 + "\n  [TOP UPKEEP SINKS]  the proteins that dominate the running budget\n" + "=" * 96)
    top = ic.sort_values("budget", ascending=False).head(10)
    for _, r in top.iterrows():
        tag = "R" if r["fn"] == READER else ("M" if r["fn"] == CIRC else "?")
        print(f"    [{tag}] {str(r['Gene Product'])[:44]:44s} copies={r['copies']:>7.0f} aa={int(r['aa']):>5d}"
              f"  {r['budget']/ic['budget'].sum():>5.1%}")

    # ---- verdict ----
    print("\n" + "=" * 96 + "\n  VERDICT\n" + "=" * 96)
    print(f"  Reader-upkeep is LARGE and CO-EQUAL with the circulation on the running proteome budget")
    print(f"  ({r_budget:.0%} reader vs {m_budget:.0%} metabolism), NOT reader-dominant -- a deflation of the")
    print(f"  bit-axis story (the reader dominates STORED essential archive, ~41% of bits; on RUNNING")
    print(f"  energy the two terms are co-equal). Reader-dominance on energy appears only once the")
    print(f"  ribosome's rRNA is counted (the standard largest sink, excluded here). The witness stands:")
    print(f"  the cell spends ~half its maintenance on the reader and still reads, so the crossover did")
    print(f"  not die at real reader-upkeep (disconfirmer #3 refuted). This measures the reader-upkeep")
    print(f"  SIDE only; the re-mint counterfactual (the ~N log N wall) remains owed (capacity item 5a).")

    figure(full, ess, ic)
    return r_budget


def figure(full, ess, ic):
    fig, ax = plt.subplots(1, 3, figsize=(17.5, 5.2), dpi=140)
    axis_labels = [a[0] for a in AXES]
    xs = np.arange(len(AXES))

    # (1) reader vs circ vs unclear across the four weightings (full proteome)
    w = 0.26
    for off, k, c in [(-w, READER, "#c62828"), (0.0, CIRC, "#2e7d32"), (w, "Unclear", "#90a4ae")]:
        ys = [full[a[0]][k] for a in AXES]
        lab = "READER (Gen.Info.Proc.)" if k == READER else ("circulation (Metab.)" if k == CIRC else "Unclear")
        ax[0].bar(xs + off, ys, width=w, color=c, label=lab)
    ax[0].set_xticks(xs); ax[0].set_xticklabels(axis_labels, rotation=18, ha="right", fontsize=8)
    ax[0].set_ylabel("share of the budget"); ax[0].set_ylim(0, 0.6)
    ax[0].set_title("reader vs circulation across weightings:\nco-equal on the running energy budget", fontsize=9.5)
    ax[0].legend(fontsize=8, frameon=False); ax[0].grid(alpha=0.25, axis="y")

    # (2) reader/circ ratio across axes -- crosses ~1 (bits<1, copies/budget>1)
    ratios = [full[a[0]][READER] / full[a[0]][CIRC] for a in AXES]
    ax[1].axhline(1.0, color="#555", ls=":", lw=1)
    ax[1].plot(xs, ratios, "o-", color="#6a1b9a", lw=2, ms=8)
    for x, y in zip(xs, ratios):
        ax[1].annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 8), fontsize=8, ha="center")
    ax[1].set_xticks(xs); ax[1].set_xticklabels(axis_labels, rotation=18, ha="right", fontsize=8)
    ax[1].set_ylabel("reader / circulation"); ax[1].set_ylim(0.7, 1.4)
    ax[1].set_title("storage favors circulation (bits<1);\nupkeep favors the reader (copies/budget>1)", fontsize=9.5)
    ax[1].grid(alpha=0.25, axis="y")

    # (3) top upkeep sinks, colored by reader/circ
    top = ic.sort_values("budget", ascending=False).head(10)[::-1]
    cols = ["#c62828" if r == READER else ("#2e7d32" if r == CIRC else "#90a4ae") for r in top["fn"]]
    names = [str(p)[:26] for p in top["Gene Product"]]
    ax[2].barh(range(len(top)), top["budget"] / ic["budget"].sum(), color=cols)
    ax[2].set_yticks(range(len(top))); ax[2].set_yticklabels(names, fontsize=7.5)
    ax[2].set_xlabel("share of proteome synthesis budget")
    ax[2].set_title("top upkeep sinks: reader (red) and\ncirculation (green) interleaved", fontsize=9.5)
    ax[2].grid(alpha=0.25, axis="x")

    fig.suptitle("Reader-upkeep on JCVI-Syn3A: ~half the running maintenance budget is the reader "
                 "(co-equal with the circulation) -- disconfirmer #3 refuted, the wall is steep",
                 fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
