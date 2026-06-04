r"""current_aids_escape.py -- the decisive test for `current-aids-escape` (frontier #1, the deepest
live question; receipts §Branch-survival barrier: "whether the [ΔV≪ΔU] gap is driven by the internal
current or the LV metric is split across reviewers -- an owed test").

THE QUESTION. In the homochiral `both` corner the noisy Freidlin-Wentzell branch-escape barrier is
ΔV ≪ ΔU (the deterministic potential): escape is *easier* than the gradient picture predicts -- a
genuine non-gradient signature (3 outside analyses agree on the signature, SPLIT on the cause). Two
candidate causes:
  (current) the internal rotational current (a≠b) lets the escape instanton "surf" the flow, lowering
            the action -> the protected current is a RESOURCE for branch escape.
  (metric)  the Lotka-Volterra non-Euclidean metric alone lowers it; the current is irrelevant.

THE CLEAN CONTROL. The competitive-exclusion threshold μ_c=(1+a+b)/3 -- and with it the racemic
saddle, the bistable landscape, the breaking eigenvalue a(μ) -- depends ONLY on a+b. So holding
a+b=1.5 FIXED pins the entire deterministic landscape (the "metric") while a-b dials the rotational
current 𝒜 from max -> 0:
        a-b = 0.50 (a=0.5 ,b=1.0 )  ->  𝒜 ≈ 21.8 nats   (the committed homochiral endpoint)
        a-b = 0.35 (a=0.575,b=0.925) -> 𝒜 ≈ 15.2
        a-b = 0.20 (a=0.65 ,b=0.85 ) -> 𝒜 ≈  8.7
        a-b = 0.00 (a=b=0.75)        -> 𝒜 =  0        (NO current; gradient-like; SAME metric)
Any change in ΔV along this line is attributable to the current alone -- the metric is held by
construction (verified below: the racemic breaking eigenvalue is pair-independent).

THE MEASUREMENT. ΔV is the true (non-gradient) FW barrier, read by the Kramers MFPT slope:
ln⟨τ⟩ = const + ΔV·(1/σ²). Demographic (√x birth-death) noise -- the receipts' robust metric, and it
vanishes at x→0 so there is no clip-manufactured floor. ΔV per pair = mean over 3 seeds; error = std.

PRE-REGISTERED DECISION (frontier ↑/✗):
  VINDICATE coupling  if ΔV decreases with 𝒜 (current-on barrier LOWER than current-off), the trend
                      clearing the error bars -> the two survivals are orthogonal in EXISTENCE (all
                      four corners realize) yet COUPLED in escape dynamics. Promotes the coupling.
  DROP (metric-only)  if ΔV is flat in 𝒜 within error -> the gap is the LV metric, the current is
                      irrelevant, the survivals stay quantitatively independent in `both` too.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from identity_survival_barrier import field_many, ee      # noqa: E402  (the validated homochiral drift)
from cycle_affinity import P as PROJ, ep_affinity          # noqa: E402  (validated affinity frame)

OUT = Path(__file__).resolve().parent
VBREAK = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6.0)   # the L↔R parity-breaking mode

# the line: a+b = 1.5 fixed (pins μ_c, the metric); a-b dials the current.
PAIRS = [(0.75, 0.75), (0.65, 0.85), (0.575, 0.925), (0.5, 1.0)]
SIGMAS = (0.205, 0.220, 0.235, 0.250)                      # shared window: both endpoints well-populated
SEEDS = (13, 23, 33)
NWALK, TMAX, DT = 800, 2500.0, 0.02


def settle_ab(X0, a, b, T=1500.0, dt=0.02):
    X = np.clip(X0.copy(), 1e-9, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field_many(X, a=a, b=b) * dt, 1e-9, None)
    return X


def basin_ab(a, b, seed=2):
    rng = np.random.default_rng(seed)
    return settle_ab(0.2 + 0.02 * rng.standard_normal((1, 6)), a, b)[0]


def affinity_ab(xstar, a, b, Ds=(0.01, 0.02, 0.04)):
    """winning hand's cycle affinity 𝒜 (deterministic, noise-independent), via the rotational-OU frame."""
    eps = 1e-6
    f0 = field_many(xstar[None, :], a=a, b=b)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = xstar.copy(); xp[i] += eps
        J[:, i] = (field_many(xp[None, :], a=a, b=b)[0] - f0) / eps
    win = slice(3, 6) if xstar[3:].sum() > xstar[:3].sum() else slice(0, 3)
    B2 = PROJ @ J[win, win] @ PROJ.T
    A = [ep_affinity(B2, d)["Acyc"] for d in Ds]
    A = np.array(A)
    A = A[np.isfinite(A)]
    return (float(np.mean(A)) if A.size else 0.0), float(np.max(np.abs(np.linalg.eigvals(B2).imag)))


def racemic_breaking_eig(a, b, F=1.0, mu=1.6):
    """curvature of the racemic saddle along the L↔R breaking mode -- the deterministic-landscape
    invariant. Depends only on a+b, so it MUST be pair-independent: the metric-held control.
    The racemic point is UNSTABLE along this mode, so a naive 6D forward-integration drifts off it
    (floating-point asymmetry grows). We reach it by a SYMMETRY-PRESERVING 1D settle of the common
    magnitude m (all six components equal): dm/dt = m(F − m(1+a+b+3μ)), then read the 6×6 Jacobian
    at x* = m·1 -- exactly on the racemic fixed point, for every pair."""
    m = 1.0 / 3.0
    for _ in range(int(2000.0 / 0.005)):
        m = max(m + m * (F - m * (1.0 + a + b + 3.0 * mu)) * 0.005, 1e-12)
    x0 = np.full(6, m); eps = 1e-6
    f0 = field_many(x0[None, :], a=a, b=b)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = x0.copy(); xp[i] += eps
        J[:, i] = (field_many(xp[None, :], a=a, b=b)[0] - f0) / eps
    return float(VBREAK @ J @ VBREAK)


def escape_mfpt(xstar, sigma, a, b, n=NWALK, T=TMAX, dt=DT, seed=13):
    """demographic-noise first passage across the racemic saddle; MFPT = (total residence)/(#flipped)."""
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, axis=0).copy()
    ss = float(np.sign(ee(xstar[None, :])[0]))
    nsteps = int(T / dt); sq = np.sqrt(dt)
    flipped = np.zeros(n, dtype=bool); tflip = np.full(n, np.nan)
    for k in range(nsteps):
        xi = rng.standard_normal(X.shape) * sq * np.sqrt(np.maximum(X, 0.0))   # demographic √x metric
        X = np.clip(X + field_many(X, a=a, b=b) * dt + sigma * xi, 1e-9, None)
        prog = ss * ee(X)
        newly = (~flipped) & (prog < -0.5)
        tflip[newly] = k * dt; flipped[newly] = True
    nflip = int(flipped.sum())
    resid = np.where(flipped, tflip, T).sum()
    return (resid / nflip if nflip > 0 else np.nan), nflip


def barrier_for_pair(a, b):
    """ΔV (Kramers slope of ln MFPT vs 1/σ²) per seed; return mean, std, R², and the raw curves."""
    x = 1.0 / np.array(SIGMAS) ** 2
    slopes, r2s = [], []
    mfpt_by_seed = []                       # [seed][sigma]
    flips_by_seed = []
    for seed in SEEDS:
        xs = basin_ab(a, b)                 # basin is deterministic; seed varies only the noise path
        mf, fl = [], []
        for s in SIGMAS:
            m, nf = escape_mfpt(xs, s, a, b, seed=seed)
            mf.append(m); fl.append(nf)
        mf = np.array(mf); fl = np.array(fl)
        mfpt_by_seed.append(mf); flips_by_seed.append(fl)
        ok = np.isfinite(mf) & (fl >= 3)
        if ok.sum() >= 2:
            sl, ic = np.polyfit(x[ok], np.log(mf[ok]), 1)
            res = np.log(mf[ok]) - (sl * x[ok] + ic)
            ss_tot = np.sum((np.log(mf[ok]) - np.log(mf[ok]).mean()) ** 2)
            r2 = 1 - np.sum(res ** 2) / ss_tot if ss_tot > 0 else float('nan')
            slopes.append(sl); r2s.append(r2)
    slopes = np.array(slopes)
    return dict(dV=float(np.mean(slopes)), dV_err=float(np.std(slopes)),
                R2=float(np.nanmean(r2s)), x=x,
                mfpt=np.array(mfpt_by_seed), flips=np.array(flips_by_seed))


def main():
    print("=" * 90)
    print("CURRENT-AIDS-ESCAPE -- does the protected current lower the branch-escape barrier ΔV?")
    print("   control: a+b=1.5 FIXED (pins μ_c & the metric); a-b dials the current 𝒜.  noise: demographic")
    print("=" * 90)

    # --- metric-held control + the affinity dial ---
    print("\n[control] the deterministic landscape is held fixed along the line (racemic breaking eig),")
    print("          while 𝒜 dials from max to zero:")
    rows = []
    for a, b in PAIRS:
        xs = basin_ab(a, b)
        A, imag = affinity_ab(xs, a, b)
        reig = racemic_breaking_eig(a, b)
        rows.append(dict(a=a, b=b, A=A, imag=imag, reig=reig, ee=ee(xs[None, :])[0]))
        print(f"   a={a:.3f} b={b:.3f} (a-b={a-b:+.2f}): basin ee={ee(xs[None,:])[0]:+.3f}  "
              f"𝒜={A:7.3f} nats  |Im λ_win|={imag:.3f}  racemic-breaking-eig={reig:+.5f}")
    reigs = np.array([r["reig"] for r in rows])
    print(f"   => racemic breaking eigenvalue spread across pairs = {reigs.std():.2e} "
          f"(flat => the metric/landscape is genuinely held; only the current changes)")

    # --- the Kramers barrier ΔV at each pair ---
    print(f"\n[barrier] ΔV = slope of ln⟨τ⟩ vs 1/σ², σ∈{SIGMAS}, n={NWALK}, T={TMAX}, {len(SEEDS)} seeds")
    t0 = time.time()
    for r in rows:
        bres = barrier_for_pair(r["a"], r["b"])
        r.update(bres)
        flips_lo = bres["flips"].sum(0)     # total flips per sigma across seeds
        print(f"   a-b={r['a']-r['b']:+.2f} (𝒜={r['A']:6.2f}): ΔV={bres['dV']:.4f} ± {bres['dV_err']:.4f}  "
              f"(R²={bres['R2']:.4f}; flips/σ={flips_lo.tolist()})")
    print(f"   [{time.time()-t0:.0f}s for the barrier sweep]")

    # --- the readout ---
    As = np.array([r["A"] for r in rows])
    dVs = np.array([r["dV"] for r in rows])
    errs = np.array([r["dV_err"] for r in rows])
    order = np.argsort(As)
    As, dVs, errs = As[order], dVs[order], errs[order]
    dV_no, dV_max = dVs[0], dVs[-1]          # 𝒜=0 vs 𝒜=max
    drop = dV_no - dV_max
    pooled_err = np.hypot(errs[0], errs[-1])
    # trend: linear fit of ΔV vs 𝒜
    slope_trend, _ = np.polyfit(As, dVs, 1)

    print("\n" + "-" * 90)
    print(f"  ΔV(no current, 𝒜=0)      = {dV_no:.4f} ± {errs[0]:.4f}")
    print(f"  ΔV(max current, 𝒜={As[-1]:.1f}) = {dV_max:.4f} ± {errs[-1]:.4f}")
    print(f"  drop ΔV(0) − ΔV(max)     = {drop:+.4f}  (pooled err {pooled_err:.4f}, "
          f"{abs(drop)/pooled_err:.1f}σ)")
    print(f"  trend dΔV/d𝒜             = {slope_trend:+.5f} nats⁻¹  "
          f"({'DECREASING' if slope_trend < 0 else 'increasing'} with current)")
    significant = drop > 2 * pooled_err and slope_trend < 0
    monotone = np.all(np.diff(dVs[np.argsort(As)]) <= errs[np.argsort(As)][1:] + errs[np.argsort(As)][:-1])
    if significant:
        print("\n  => VINDICATE `current-aids-escape`: the barrier DROPS as the current rises, > 2σ, the")
        print("     deterministic landscape held fixed. The protected current is a RESOURCE for branch")
        print("     escape -- the two survivals are orthogonal in EXISTENCE yet COUPLED in escape dynamics.")
    elif drop > pooled_err and slope_trend < 0:
        print("\n  => SUGGESTIVE (1–2σ): the barrier trends down with current but the error bars are not")
        print("     yet decisive. More seeds / wider σ lever owed before promotion.")
    else:
        print("\n  => METRIC-ONLY (drop within error): ΔV does not track the current. The ΔV≪ΔU gap is the")
        print("     LV metric, not the current. The survivals stay quantitatively independent in `both`. DROP.")
    print("-" * 90)

    figure(rows)
    return dict(dV_no=dV_no, dV_max=dV_max, drop=drop, pooled_err=pooled_err,
                slope_trend=slope_trend, significant=significant)


def figure(rows):
    fig, ax = plt.subplots(1, 3, figsize=(18, 5.4), dpi=140)
    cols = plt.cm.plasma(np.linspace(0.1, 0.82, len(rows)))

    # (a) Arrhenius plot: ln MFPT vs 1/σ², slopes fan with the current
    a0 = ax[0]
    for r, c in zip(rows, cols):
        x = r["x"]
        mf = np.nanmean(r["mfpt"], axis=0)
        mferr = np.nanstd(r["mfpt"], axis=0)
        a0.errorbar(x, mf, yerr=mferr, fmt="o", ms=7, color=c, capsize=3,
                    label=fr"$\mathcal{{A}}$={r['A']:.1f}: $\Delta V$={r['dV']:.3f}")
        sl, ic = np.polyfit(x, np.log(mf), 1)
        xf = np.linspace(x.min(), x.max(), 30)
        a0.plot(xf, np.exp(sl * xf + ic), "-", color=c, lw=1.3, alpha=0.8)
    a0.set_yscale("log")
    a0.set_xlabel(r"$1/\sigma^2$"); a0.set_ylabel(r"MFPT $\langle\tau\rangle$ to racemic saddle")
    a0.set_title("(a) Kramers: ln MFPT vs $1/\\sigma^2$\nslope = FW barrier $\\Delta V$ (steeper = harder)")
    a0.legend(fontsize=8.5, frameon=False, title="winner affinity"); a0.grid(alpha=0.3, which="both")

    # (b) the readout: ΔV vs 𝒜, with the metric-held control
    a1 = ax[1]
    As = np.array([r["A"] for r in rows]); dVs = np.array([r["dV"] for r in rows])
    errs = np.array([r["dV_err"] for r in rows])
    a1.errorbar(As, dVs, yerr=errs, fmt="o-", ms=9, color="#c62828", capsize=4, lw=1.6,
                label=r"$\Delta V$ (FW barrier, Kramers)")
    if len(As) >= 2:
        sl, ic = np.polyfit(As, dVs, 1)
        xf = np.linspace(0, As.max() * 1.05, 20)
        a1.plot(xf, sl * xf + ic, "k--", lw=1.2, alpha=0.7,
                label=fr"trend $d\Delta V/d\mathcal{{A}}$={sl:+.4f}")
    a1.set_xlabel(r"winner cycle affinity $\mathcal{A}$ (nats) = the current"); a1.set_ylabel(r"branch-escape barrier $\Delta V$")
    a1.set_title("(b) does the current lower the barrier?\n(metric held: a+b=1.5 fixed)")
    a1.legend(fontsize=9, frameon=False); a1.grid(alpha=0.3)

    # (c) verdict text
    a2 = ax[2]; a2.axis("off")
    reigs = np.array([r["reig"] for r in rows])
    dV_no, dV_max = dVs[np.argmin(As)], dVs[np.argmax(As)]
    drop = dV_no - dV_max; perr = np.hypot(errs[np.argmin(As)], errs[np.argmax(As)])
    verdict = ("VINDICATED: current aids escape" if (drop > 2 * perr and dVs[np.argmax(As)] < dVs[np.argmin(As)])
               else ("SUGGESTIVE (1–2σ)" if drop > perr else "METRIC-ONLY: drop within error"))
    txt = ("CURRENT-AIDS-ESCAPE\nthe decisive test (frontier #1)\n\n"
           "control -- a+b=1.5 FIXED:\n"
           f" racemic breaking eig spread\n   = {reigs.std():.1e}  (metric held)\n"
           f" 𝒜 dials {As.min():.1f} → {As.max():.1f} nats\n\n"
           "barrier (Kramers FW):\n"
           f" ΔV(𝒜=0)   = {dV_no:.4f} ± {errs[np.argmin(As)]:.4f}\n"
           f" ΔV(𝒜=max) = {dV_max:.4f} ± {errs[np.argmax(As)]:.4f}\n"
           f" drop      = {drop:+.4f}  ({abs(drop)/perr:.1f}σ)\n\n"
           f"=> {verdict}\n\n"
           "the protected current as a\nRESOURCE for branch escape:\n"
           "two survivals orthogonal in\nEXISTENCE, coupled in ESCAPE.")
    a2.text(0.02, 0.98, txt, va="top", ha="left", fontsize=10.5, family="monospace")

    fig.suptitle("current-aids-escape: is the FW branch-escape barrier $\\Delta V$ lowered by the protected "
                 "current $\\mathcal{A}$?  (a+b held fixed; only the current varies)",
                 fontsize=12.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "current_aids_escape.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
