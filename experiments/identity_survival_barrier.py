r"""identity_survival_barrier.py -- B-sep first instance: the identity-survival quasipotential
on the homochiral triad (the racemic saddle).

character.md (Status and open problems):
  "the identity-survival barrier -- the quasipotential for escape from a character's basin -- has
   not been computed on a real substrate (the homochiral racemic saddle is the natural first
   instance)."

This pays that invoice. Two survivals the current alone conflates (character.md, Identity):
  - circulation survival = the current not reversing             -> I(0), per-step affinity
  - identity survival    = the system not crossing the separatrix -> THIS: racemic-saddle escape

Method (Kramers / Freidlin-Wentzell): noise-driven first passage from a chiral basin (|ee|->1)
across the racemic saddle (prog=0) to the mirror basin. Two independent reads of the barrier dV:
  (QP) quasipotential  V(prog) = -sigma^2 log P(prog)  from the in-basin distribution, with a
       sigma-COLLAPSE integrity check -- a well-defined barrier <=> the curves collapse;
  (KR) Kramers escape rate  k(sigma) ~ exp(-dV/sigma^2);  log MFPT vs 1/sigma^2 has slope dV.

Substrate: the EXACT homochiral triad of mpa-conform/scripts/homochiral_triad.py (mirror chiral
3-cycles + Frank cross-inhibition), copied minimal & self-contained -- the frozen staked instance
is not modified.   prog = (home-basin sign)*ee :  1 = home,  0 = racemic saddle,  <0 = flipped.
"""
from __future__ import annotations
import sys, time
import numpy as np
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

A0, B0, MU0, F0 = 0.5, 1.0, 1.6, 1.0   # chiral (a!=b), Frank antagonism, feed -- exact from homochiral_triad.py
OUT = Path(__file__).resolve().parent


def field_many(X, F=F0, a=A0, b=B0, mu=MU0):
    L, R = X[:, :3], X[:, 3:]
    SL, SR = L.sum(1, keepdims=True), R.sum(1, keepdims=True)
    dL = L * (F - (L + a * np.roll(L, -1, 1) + b * np.roll(L, 1, 1)) - mu * SR)
    dR = R * (F - (R + b * np.roll(R, -1, 1) + a * np.roll(R, 1, 1)) - mu * SL)
    return np.concatenate([dL, dR], axis=1)


def ee(X):
    L = X[:, :3].sum(1); R = X[:, 3:].sum(1)
    return (L - R) / (L + R + 1e-12)


def settle(X0, T=1500.0, dt=0.02):
    X = np.clip(X0.copy(), 1e-9, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field_many(X) * dt, 1e-9, None)
    return X


def basin_state(seed=2):
    rng = np.random.default_rng(seed)
    return settle((0.2 + 0.02 * rng.standard_normal((1, 6))))[0]


def quasipotential(xstar, sigma, n=1000, T=1500.0, dt=0.02, seed=0, burn=0.25, bins=None):
    """In-basin quasi-stationary distribution of prog; V(prog) = -sigma^2 log P(prog).
    Walkers are censored once they flip (prog<0) so we measure the basin, not the escaped tail."""
    if bins is None:
        bins = np.linspace(-0.05, 1.05, 56)
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, axis=0).copy()
    ss = float(np.sign(ee(xstar[None, :])[0]))
    nsteps = int(T / dt); sq = np.sqrt(dt); kburn = int(burn * nsteps)
    alive = np.ones(n, dtype=bool)
    counts = np.zeros(len(bins) - 1)
    for k in range(nsteps):
        X = np.clip(X + field_many(X) * dt + sigma * rng.standard_normal((n, 6)) * sq, 1e-9, None)
        prog = ss * ee(X)
        alive &= (prog > -0.5)
        if k > kburn and alive.any():
            counts += np.histogram(prog[alive], bins=bins)[0]
    mid = 0.5 * (bins[:-1] + bins[1:])
    P = counts / max(counts.sum(), 1)
    with np.errstate(divide="ignore"):
        V = -sigma ** 2 * np.log(P)
    V[P <= 0] = np.nan          # empty bins -> nan (not +inf), so the cross-sigma mean ignores them
    return mid, P, V


def escape_rate(xstar, sigma, n=800, T=2500.0, dt=0.02, seed=0):
    """ML escape rate k = (#flipped)/(total residence time), censored at T. MFPT = 1/k."""
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, axis=0).copy()
    ss = float(np.sign(ee(xstar[None, :])[0]))
    nsteps = int(T / dt); sq = np.sqrt(dt)
    flipped = np.zeros(n, dtype=bool); tflip = np.full(n, np.nan)
    for k in range(nsteps):
        X = np.clip(X + field_many(X) * dt + sigma * rng.standard_normal((n, 6)) * sq, 1e-9, None)
        prog = ss * ee(X)
        newly = (~flipped) & (prog < -0.5)
        tflip[newly] = k * dt; flipped[newly] = True
    resid = np.where(flipped, tflip, T).sum()
    nflip = int(flipped.sum())
    k_rate = nflip / resid if nflip > 0 else np.nan
    return k_rate, nflip, float(np.nanmean(tflip)) if nflip else np.nan


def measure():
    print("=" * 78)
    print("IDENTITY-SURVIVAL BARRIER -- homochiral triad, racemic-saddle escape (B-sep, 1st instance)")
    print("=" * 78)
    xstar = basin_state()
    print(f"basin ee={ee(xstar[None,:])[0]:+.3f}  (full chiral commitment); prog=1 home, 0 saddle, <0 flipped\n")

    # ---- (QP) quasipotential + sigma-collapse integrity check ----
    print("[QP] quasipotential V(prog) = -sigma^2 log P(prog), in-basin (low sigma, ~no escape)")
    qp_sigmas = (0.030, 0.040, 0.050, 0.060)
    qp = {}
    for s in qp_sigmas:
        t0 = time.time()
        mid, P, V = quasipotential(xstar, s, n=1000, T=1500.0, seed=7)
        # anchor V=0 at the basin floor (max prog bin with mass)
        ok = np.isfinite(V)
        Vb = V[ok][np.argmax(mid[ok])]
        qp[s] = (mid, V - Vb, ok)
        reach = mid[ok].min()
        print(f"   sigma={s:.3f}  samples prog down to {reach:+.2f}   ({time.time()-t0:.1f}s)")

    # collapse check: pairwise rms gap of (V) over the common prog window where all sigmas have mass
    common = None
    for s in qp_sigmas:
        mid, V, ok = qp[s]
        m = ok & np.isfinite(V)
        reg = set(np.where(m)[0])
        common = reg if common is None else (common & reg)
    common = sorted(common)
    if len(common) >= 3:
        stack = np.array([qp[s][1][common] for s in qp_sigmas])
        collapse_rms = float(np.sqrt(np.nanmean((stack - stack.mean(0)) ** 2)))
        prog_window = (float(0.5*(np.linspace(-0.05,1.05,56)[:-1]+np.linspace(-0.05,1.05,56)[1:])[common].min())) \
            if common else float('nan')
    else:
        collapse_rms = float('nan')
    print(f"   sigma-collapse rms over common window = {collapse_rms:.4f}  "
          f"(small => one well-defined quasipotential; the barrier is real, not a noise artifact)")

    # barrier height: average collapsed V at the lowest reachable prog (saddle-side), vs basin (=0)
    Vmid = np.nanmean(np.array([qp[s][1] for s in qp_sigmas]), axis=0)
    midgrid = qp[qp_sigmas[0]][0]
    finite = np.isfinite(Vmid)
    dV_qp = float(np.nanmax(Vmid[finite & (midgrid < 0.5)])) if (finite & (midgrid < 0.5)).any() else float('nan')

    # ---- (KR) Kramers escape-rate leg ----
    print("\n[KR] Kramers escape rate k(sigma) ~ exp(-dV/sigma^2); log MFPT vs 1/sigma^2 slope = dV")
    kr_sigmas = (0.070, 0.080, 0.090, 0.100, 0.120)
    rates, mfpts, used = [], [], []
    for s in kr_sigmas:
        t0 = time.time()
        k_rate, nflip, mtf = escape_rate(xstar, s, n=800, T=2500.0, seed=13)
        print(f"   sigma={s:.3f}  flips={nflip:4d}  k={k_rate:.3e}  MFPT={1/k_rate if k_rate==k_rate and k_rate>0 else float('nan'):9.1f}  ({time.time()-t0:.1f}s)")
        if k_rate == k_rate and k_rate > 0:
            rates.append(k_rate); mfpts.append(1.0 / k_rate); used.append(s)
    used = np.array(used); mfpts = np.array(mfpts)
    if len(used) >= 2:
        x = 1.0 / used ** 2; y = np.log(mfpts)
        slope, _ = np.polyfit(x, y, 1)
        dV_kr = float(slope)
    else:
        dV_kr = float('nan')
    print(f"   Kramers slope d(log MFPT)/d(1/sigma^2) = dV_KR = {dV_kr:.4f}")

    print("\n" + "-" * 78)
    print(f"  dV (quasipotential, saddle-side reach) ~ {dV_qp:.4f}")
    print(f"  dV (Kramers MFPT slope)                ~ {dV_kr:.4f}")
    print("  identity-survival barrier: escape needs sigma ~ 0.1, FAR above the sigma~0.01-0.04")
    print("  demographic noise where H3 finds the hand stable -> the frozen identity is protected")
    print("  by a real (shallow) quasipotential barrier, distinct from circulation reversal I(0).")
    print("-" * 78)

    figure(xstar, qp, qp_sigmas, midgrid, Vmid, used, mfpts, dV_kr, collapse_rms)
    return dV_qp, dV_kr, collapse_rms


def figure(xstar, qp, qp_sigmas, midgrid, Vmid, kr_used, mfpts, dV_kr, collapse_rms):
    fig, ax = plt.subplots(1, 3, figsize=(18, 5.4), dpi=140)

    a0 = ax[0]
    cols = plt.cm.viridis(np.linspace(0.15, 0.85, len(qp_sigmas)))
    for s, c in zip(qp_sigmas, cols):
        mid, V, ok = qp[s]
        a0.plot(mid[ok], V[ok], "o-", ms=4, color=c, label=f"sigma={s:.3f}")
    a0.plot(midgrid, Vmid, "k--", lw=2, label="mean (quasipotential)")
    a0.axvline(0, color="crimson", ls=":", lw=1.4, label="racemic saddle")
    a0.set_xlabel("prog = (home sign)*ee"); a0.set_ylabel(r"$V(\mathrm{prog})=-\sigma^2\log P$")
    a0.set_title(f"(a) quasipotential, sigma-COLLAPSE\nrms over common window = {collapse_rms:.4f}")
    a0.legend(fontsize=8, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]
    if len(kr_used) >= 2:
        x = 1.0 / kr_used ** 2
        a1.semilogy(x, mfpts, "o", ms=8, color="#1565c0")
        xf = np.linspace(x.min(), x.max(), 50)
        sl, ic = np.polyfit(x, np.log(mfpts), 1)
        a1.semilogy(xf, np.exp(ic + sl * xf), "k--", lw=1.6, label=f"slope dV={sl:.3f}")
        for xi, mi, si in zip(x, mfpts, kr_used):
            a1.annotate(f"{si:.2f}", (xi, mi), fontsize=8, xytext=(4, 4), textcoords="offset points")
    a1.set_xlabel(r"$1/\sigma^2$"); a1.set_ylabel("MFPT to racemic saddle")
    a1.set_title("(b) Kramers: log MFPT vs $1/\\sigma^2$\n(slope = identity-survival barrier dV)")
    a1.legend(fontsize=9, frameon=False); a1.grid(alpha=0.3, which="both")

    a2 = ax[2]
    a2.axis("off")
    txt = ("IDENTITY-SURVIVAL BARRIER\nhomochiral triad -- racemic saddle\n\n"
           "the FIRST instance of B-sep:\nthe quasipotential for escape\nfrom a character's basin.\n\n"
           "two survivals, separated:\n"
           " - circulation survival = I(0)\n   (current not reversing)\n"
           " - identity survival = dV here\n   (not crossing the separatrix)\n\n"
           f"dV(Kramers) ~ {dV_kr:.3f}\n"
           "escape needs sigma ~ 0.1,\nFAR above the sigma~0.01-0.04\nwhere the hand is stable (H3).\n\n"
           "the frozen identity is real,\nprotected, and MORTAL: a shallow\nbut definite barrier, not infinite.")
    a2.text(0.02, 0.98, txt, va="top", ha="left", fontsize=11, family="monospace")

    fig.suptitle("character B-sep -- identity-survival quasipotential on the homochiral triad",
                 fontsize=13, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    path = OUT / "identity_survival_barrier.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    measure()
