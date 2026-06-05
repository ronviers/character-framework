"""
T2 — the REAL normal endpoint (Ron's data-in-hand gate).

The calibrated apparatus (shell_t2_anchor / shell_t2_volume) tests a SYNTHETIC
normal (constant E,C,T, self-similar by construction) against a REAL heteromorph
(Misaki, T crosses zero). That contrast is asymmetric: the normal side is
self-similar by fiat. This script fills the missing endpoint with REAL normal
shells and asks the falsifiable question directly:

    Do real normal gastropod shells converge to a self-similar fixed point
    along their own growth trajectory?

Data: Collins et al. 2021 `S_Table_3_hangle_output.csv` — 184 normal-gastropod
shells, each 4-21 growth stages, aperture outline as an 18-component HARMONIC-
ANGLE shape vector (scale- and rotation-invariant by construction). For a
perfectly self-similar (gnomonic) shell the outline shape is identical at every
stage => the 18-vector is CONSTANT along growth; any drift is departure from
self-similarity. So self-similarity is read directly off the trajectory, no
generator fit needed.

Readouts (all intra-shell, falsifiable):
  (1) within-shell dispersion / pooled dispersion  — is the shell a *point* in
      morphospace? (self-similar => << 1)
  (2) settling ratio = mean(late-third step)/mean(early-third step) — do the
      stage-to-stage increments SHRINK toward a fixed point? (<1 => converging)
  (3) aggregate increment-vs-phase profile, REAL vs STAGE-SHUFFLED null — proves
      the ordering is a smooth flow (a trajectory) and exposes the apex transient
      and any terminal maturity flare.

Contrast panel: Misaki morphotype I (real heteromorph) generator E,C,T(s) — the
lost fixed point. Same dataset family used by the calibrated anchor.

Falsifier: if normal shells do NOT converge (increments don't shrink; within ~
pooled; real profile == shuffled), the "normal converges / heteromorph loses"
premise of cross-stratum-transduction T2 is wrong.
"""
import sys, csv
from pathlib import Path
from collections import defaultdict
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = Path(r"H:\character-framework\data\shell")
COLLINS = ROOT / "doi_10_5061_dryad_p5hqbzknw__v20210113" / "S_Table_3_hangle_output.csv"
MISAKI = ROOT / "doi_10_5061_dryad_q573n5tnz__v20230815" / \
    "Data_2_Parameter_values_of_the_growing_tube_model_for_each_morphotype.csv"
OUT = Path(r"H:\character-framework\experiments")
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- load Collins
rows = list(csv.reader(open(COLLINS)))
hdr = rows[0]
vcol = [hdr.index(f"V{i}") for i in range(1, 19)]
cid, cap = hdr.index("ID"), hdr.index("Aperture")
shells = defaultdict(list)  # id -> list of (stage, 18-vec)
for r in rows[1:]:
    shells[r[cid]].append((int(r[cap]), np.array([float(r[c]) for c in vcol])))
traj = {}  # id -> (S,18) sorted by stage
for k, v in shells.items():
    v.sort(key=lambda t: t[0])
    traj[k] = np.array([x for _, x in v])
ids = list(traj)
X = np.vstack([traj[k] for k in ids])               # (1474,18) all stage-vectors
gmean = X.mean(0)
print(f"Collins: {len(ids)} normal shells, {len(X)} aperture stages, 18-dim shape vectors")

# size leakage check: is shape-vector magnitude correlated with stage within shells?
cors = []
for k in ids:
    t = traj[k]; st = np.arange(len(t))
    mag = np.linalg.norm(t - gmean, axis=1)
    if mag.std() > 0:
        cors.append(np.corrcoef(st, mag)[0, 1])
print(f"  size-leakage check: median corr(|shape-vec|, stage) = {np.median(cors):+.3f} "
      f"(near 0 => descriptor is scale-free, as designed)")

# ---------------------------------------------------------------- (1) within / pooled dispersion
V_pool = np.mean(np.sum((X - gmean) ** 2, axis=1))        # pooled variance about global mean
within = []
for k in ids:
    t = traj[k]; m = t.mean(0)
    within.append(np.mean(np.sum((t - m) ** 2, axis=1)))
within = np.array(within)
ratio_wp = within / V_pool
print(f"\n(1) within-shell / pooled dispersion: median = {np.median(ratio_wp):.3f}  "
      f"(self-similar => << 1; each shell ~ a point in morphospace)")
print(f"    {np.mean(ratio_wp < 0.2)*100:.0f}% of shells have within < 0.2 * pooled")

# ---------------------------------------------------------------- (2) settling ratio
def thirds_ratio(t):
    d = np.linalg.norm(np.diff(t, axis=0), axis=1)        # consecutive-stage increments
    n = len(d)
    if n < 4: return np.nan
    k = max(1, n // 3)
    early, late = d[:k].mean(), d[-k:].mean()
    return late / early if early > 0 else np.nan
settle = np.array([thirds_ratio(traj[k]) for k in ids])
settle = settle[~np.isnan(settle)]
print(f"\n(2) settling ratio late/early increment: median = {np.median(settle):.3f}  "
      f"(<1 => increments shrink => converging to a fixed point)")
print(f"    {np.mean(settle < 1)*100:.0f}% of shells converge (ratio < 1)  [n={len(settle)}]")

# ---------------------------------------------------------------- (3) increment vs phase: real vs shuffled
NB = 8
edges = np.linspace(0, 1, NB + 1)
def profile(order_fn, n_rep=1):
    acc = np.zeros((n_rep, NB)); cnt = np.zeros((n_rep, NB))
    for rep in range(n_rep):
        for k in ids:
            t = traj[k]
            if len(t) < 4: continue
            tt = order_fn(t)
            d = np.linalg.norm(np.diff(tt, axis=0), axis=1)
            d = d / d.mean() if d.mean() > 0 else d        # normalize per-shell: removes size, keeps shape of profile
            phi = (np.arange(len(d)) + 0.5) / len(d)
            idx = np.clip(np.digitize(phi, edges) - 1, 0, NB - 1)
            for b, val in zip(idx, d):
                acc[rep, b] += val; cnt[rep, b] += 1
    m = acc / np.maximum(cnt, 1)
    return m.mean(0), m.std(0)
real_prof, _ = profile(lambda t: t, 1)
shuf_prof, shuf_sd = profile(lambda t: t[rng.permutation(len(t))], 200)
# raw (un-normalized) mean increment, real vs shuffled — the "is it a smooth flow" test
def mean_raw_incr(order_fn, n_rep=1):
    vals = []
    for rep in range(n_rep):
        ds = []
        for k in ids:
            t = traj[k]
            if len(t) < 2: continue
            tt = order_fn(t)
            ds.append(np.linalg.norm(np.diff(tt, axis=0), axis=1).mean())
        vals.append(np.mean(ds))
    return np.mean(vals)
raw_real = mean_raw_incr(lambda t: t, 1)
raw_shuf = mean_raw_incr(lambda t: t[rng.permutation(len(t))], 200)
print(f"\n(3) mean raw stage-increment: REAL order = {raw_real:.4f}  vs SHUFFLED = {raw_shuf:.4f}  "
      f"(real << shuffled => stages form a smooth trajectory, not a cloud)")
print(f"    real/shuffled = {raw_real/raw_shuf:.3f}")

# ---------------------------------------------------------------- PCA for the trajectory plot
U, Sv, Wt = np.linalg.svd(X - gmean, full_matrices=False)
PC = Wt[:2]                                                # (2,18)
def proj(t): return (t - gmean) @ PC.T

# ---------------------------------------------------------------- Misaki heteromorph (contrast)
def parse_misaki(path, morph="I"):
    rs = list(csv.reader(open(path, encoding="utf-8"))); h = rs[0]
    cs = h.index(f"Morphotype {morph} (values of s)"); cv = h.index(f"Morphotype {morph} (values of E, C, T)")
    out = {"E": [[], []], "C": [[], []], "T": [[], []]}; cur = None
    for r in rs[1:]:
        if len(r) <= cv: continue
        a, b = r[cs].strip(), r[cv].strip()
        if b in ("E", "C", "T"): cur = b; continue
        if cur is None or a == "" or a.lower().startswith(("upper", "growth")): continue
        try: out[cur][0].append(float(a)); out[cur][1].append(float(b))
        except ValueError: pass
    return out
mis = parse_misaki(MISAKI, "I")

# ================================================================ figure
fig = plt.figure(figsize=(15, 10))
fig.suptitle("T2 on REAL normal shells (Collins 2021, n=184): do they converge to a self-similar fixed point?",
             fontsize=13, fontweight="bold")

# A: example trajectories in PCA shape space, colored by stage
ax = fig.add_subplot(2, 3, 1)
order = np.argsort(-within)                                # show a spread: most + least stationary
pick = [ids[i] for i in list(order[:3]) + list(order[len(order)//2-1:len(order)//2+1]) + list(order[-3:])]
for k in pick:
    p = proj(traj[k]); ph = np.linspace(0, 1, len(p))
    ax.plot(p[:, 0], p[:, 1], "-", color="0.6", lw=0.6, zorder=1)
    ax.scatter(p[:, 0], p[:, 1], c=ph, cmap="viridis", s=18, zorder=2)
ax.set_xlabel("aperture-shape PC1"); ax.set_ylabel("PC2")
ax.set_title("A. Example shell trajectories (color=growth phase)\nsettle along growth (not collapse to a point)", fontsize=10)

# B: within/pooled dispersion histogram
ax = fig.add_subplot(2, 3, 2)
ax.hist(ratio_wp, bins=30, color="tab:green", alpha=0.8)
ax.axvline(np.median(ratio_wp), color="k", ls="--", lw=1.2, label=f"median={np.median(ratio_wp):.2f}")
ax.axvline(1.0, color="tab:red", ls=":", lw=1.2, label="=1 (shell as broad as population)")
ax.set_xlabel("within-shell / pooled dispersion"); ax.set_ylabel("# shells")
ax.set_title("B. A shell spans a SUB-REGION, not a point\n(median 0.34: settles to a region, not <<1)", fontsize=10)
ax.legend(fontsize=7)

# C: settling ratio histogram
ax = fig.add_subplot(2, 3, 3)
ax.hist(np.clip(settle, 0, 3), bins=30, color="tab:blue", alpha=0.8)
ax.axvline(1.0, color="tab:red", ls=":", lw=1.2, label="=1 (no settling)")
ax.axvline(np.median(settle), color="k", ls="--", lw=1.2, label=f"median={np.median(settle):.2f}")
ax.set_xlabel("settling ratio  late/early increment"); ax.set_ylabel("# shells")
ax.set_title(f"C. Increments SHRINK along growth\n{np.mean(settle<1)*100:.0f}% of shells converge (<1)", fontsize=10)
ax.legend(fontsize=7)

# D: increment-vs-phase profile, real vs shuffled
ax = fig.add_subplot(2, 3, 4)
ctr = (edges[:-1] + edges[1:]) / 2
ax.plot(ctr, real_prof, "o-", color="tab:green", lw=2, label="REAL stage order")
ax.plot(ctr, shuf_prof, "s--", color="0.5", lw=1.2, label="stage-shuffled null")
ax.fill_between(ctr, shuf_prof - shuf_sd, shuf_prof + shuf_sd, color="0.7", alpha=0.3)
ax.set_xlabel("ontogenetic phase (apex -> aperture)"); ax.set_ylabel("normalized shape increment")
ax.set_title("D. Flow shape: apex transient -> settled middle\n(real structured; shuffle flat & higher)", fontsize=10)
ax.legend(fontsize=7)

# E: raw increment real vs shuffled (smooth-trajectory test)
ax = fig.add_subplot(2, 3, 5)
ax.bar(["REAL\norder", "shuffled\nnull"], [raw_real, raw_shuf],
       color=["tab:green", "0.6"])
ax.set_ylabel("mean raw stage increment")
ax.set_title(f"E. Stages form a smooth trajectory\nreal/shuffled = {raw_real/raw_shuf:.2f} (<<1)", fontsize=10)

# F: Misaki heteromorph contrast — the lost fixed point
ax = fig.add_subplot(2, 3, 6)
for kk, col in [("E", "tab:green"), ("C", "tab:blue"), ("T", "tab:orange")]:
    ax.plot(mis[kk][0], mis[kk][1], ".-", color=col, lw=1.2, ms=3, label=kk)
ax.axhline(0, color="k", lw=0.6)
ax.set_xlabel("growth position s"); ax.set_ylabel("generator value")
ax.set_title("F. CONTRAST: Misaki heteromorph (real)\ngenerator drifts, T crosses 0 — fixed point lost", fontsize=10)
ax.legend(fontsize=8)

fig.tight_layout(rect=[0, 0, 1, 0.96])
png = OUT / "shell_t2_collins.png"
fig.savefig(png, dpi=140)
print(f"\nsaved {png}")
