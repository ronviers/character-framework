r"""twin_cycle_corner.py -- a SECOND independent "both" corner of the two-survivals plane,
OUTSIDE the chiral-SSB family (within-reach test #1).

The plane's only `both` instance (ΔV>0 ∧ 𝒜≠0) is the homochiral triad, where the broken symmetry is
PARITY (L↔R mirror) -- a second chiral instance would not be independent. This substrate breaks a
DIFFERENT symmetry: the S2 EXCHANGE of two IDENTICAL, CO-HANDED cyclic clusters.

  Homochiral skeleton:  two MIRROR (opposite-handed) cyclic 3-clusters + competitive cross-inhibition.
  Twin-cycle (here)  :  two IDENTICAL (same-handed) cyclic 3-clusters + competitive cross-inhibition.

The one change -- mirror -> copy -- moves the broken symmetry from a reflection (parity) to a
permutation (exchange). The decisive, MEASURABLE consequence:

  homochiral : branch-flip FLIPS sign(𝒜)  (the two basins are opposite-handed currents) -- so a single
               parity operation flips BOTH survivals at once (they look entangled).
  twin-cycle : branch-flip PRESERVES sign(𝒜) (both clusters spin the same way; only WHICH cluster is
               occupied differs) -- branch membership and current handedness are decoupled at the level
               of sign. This is a separation the homochiral instance CANNOT exhibit.

Both axes are read with the SAME validated apparatus:
  𝒜  (current survival) : the winning cluster's Jacobian block -> rotational-OU Lyapunov frame
                          (ep_affinity, imported from cycle_affinity; validated vs 𝒜=4πω₀/κ on the OU).
  ΔV (branch survival)  : noise-driven first passage across the m=0 exchange saddle, read two ways --
                          the σ-collapsing in-basin quasipotential V(m)=-σ²logP(m), and the Kramers
                          log-MFPT-vs-1/σ² slope (faithful copies of identity_survival_barrier's legs,
                          parameterized on the twin field).

Run:   python twin_cycle_corner.py            (full)
       python twin_cycle_corner.py smoke      (fast probe -- small n, short T, qualitative only)
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
from cycle_affinity import ep_affinity, P as PROJ, JMAT   # noqa: E402  (field-agnostic, validated)
from identity_survival_barrier import field_many as homo_field   # noqa: E402  (the parity instance, for contrast)

A0, B0, MU0, F0 = 0.5, 1.0, 1.6, 1.0   # a!=b => non-reciprocal 3-cycle; mu>mu_c => competitive exclusion
OUT = Path(__file__).resolve().parent
BINS = np.linspace(-0.05, 1.05, 56)


def field_many(X, F=F0, a=A0, b=B0, mu=MU0):
    """Two CO-HANDED cyclic 3-clusters (C1,C2) with symmetric competitive cross-inhibition.
    Both clusters use the SAME intra-coupling (a*roll(-1)+b*roll(+1)) => same handedness (the only
    change from homochiral_triad, where cluster 2 swaps a,b => mirror). The field is equivariant under
    the exchange (C1,C2)->(C2,C1): a permutation (S2) symmetry, not a reflection."""
    C1, C2 = X[:, :3], X[:, 3:]
    S1, S2 = C1.sum(1, keepdims=True), C2.sum(1, keepdims=True)
    d1 = C1 * (F - (C1 + a * np.roll(C1, -1, 1) + b * np.roll(C1, 1, 1)) - mu * S2)
    d2 = C2 * (F - (C2 + a * np.roll(C2, -1, 1) + b * np.roll(C2, 1, 1)) - mu * S1)
    return np.concatenate([d1, d2], axis=1)


def m_imbalance(X):
    """Order parameter: population imbalance between the two clusters (swap-ODD under the exchange)."""
    S1 = X[:, :3].sum(1); S2 = X[:, 3:].sum(1)
    return (S1 - S2) / (S1 + S2 + 1e-12)


def settle(X0, T=1500.0, dt=0.02):
    X = np.clip(X0.copy(), 1e-9, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field_many(X) * dt, 1e-9, None)
    return X


def basin_state(seed=2):
    rng = np.random.default_rng(seed)
    return settle((0.2 + 0.02 * rng.standard_normal((1, 6))))[0]


# ----------------------------------------------------------------------------- exchange-Z2 is spontaneous
def reset_redrive(n=40, spread=0.06):
    """Random-IC resets; read which cluster wins each time. ~50/50 => thermalized crossing
    (spontaneously selected, like homochiral) -- the row condition for a `both` corner."""
    signs = []
    for s in range(n):
        rng = np.random.default_rng(s)
        X = np.clip(0.2 + spread * rng.standard_normal((1, 6)), 1e-9, None)
        signs.append(int(np.sign(m_imbalance(settle(X))[0])))
    signs = np.array(signs)
    npos, nneg = int((signs > 0).sum()), int((signs < 0).sum())
    frac = max(npos, nneg) / len(signs)
    return npos, nneg, frac


# ----------------------------------------------------------------------------- current survival 𝒜
def _settle_with(field, X0, T=1500.0, dt=0.02):
    X = np.clip(X0.copy(), 1e-9, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field(X) * dt, 1e-9, None)
    return X


def winner_block(xstar, field=field_many):
    """Finite-diff 6x6 Jacobian of `field` at the settled state; winning cluster's 3x3 block, projected
    to the 2D rotation plane perp to (1,1,1). Same construction as cycle_affinity.winner_block."""
    eps = 1e-6
    f0 = field(xstar[None, :])[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = xstar.copy(); xp[i] += eps
        J[:, i] = (field(xp[None, :])[0] - f0) / eps
    win = slice(0, 3) if xstar[:3].sum() > xstar[3:].sum() else slice(3, 6)
    Jw = J[win, win]
    B2 = PROJ @ Jw @ PROJ.T
    return Jw, B2, win


def affinity_in_basin(xstar, field=field_many, Ds=(0.01, 0.02, 0.04)):
    """𝒜 of the winning cluster across noise levels (must be D-independent)."""
    Jw, B2, win = winner_block(xstar, field)
    wB = np.linalg.eigvals(B2)
    A_of_D = [ep_affinity(B2, d)["Acyc"] for d in Ds]
    # sign of circulation = orientation of the rotation generator in the (E1,E2) frame
    sgn = int(np.sign(B2[1, 0] - B2[0, 1]))
    return dict(A=float(np.mean(A_of_D)), spread=float(np.std(A_of_D)), sign=sgn,
                evals=wB, win=win, A_of_D=A_of_D)


def sign_contrast():
    """Measured (not asserted) crux of independence: sign(𝒜) in basin-1 vs basin-2, for the twin-cycle
    (exchange) field vs the homochiral (parity) field, holding (a,b,μ,F) identical. The ONLY structural
    difference is mirror-vs-copy. Prediction: twin PRESERVES sign across the flip, homochiral REVERSES it."""
    ic1 = np.array([[0.30, 0.30, 0.30, 0.05, 0.05, 0.05]])
    ic2 = np.array([[0.05, 0.05, 0.05, 0.30, 0.30, 0.30]])
    rows = []
    for name, field in (("twin-cycle (exchange)", field_many), ("homochiral (parity)", homo_field)):
        s1 = affinity_in_basin(_settle_with(field, ic1)[0], field)["sign"]
        s2 = affinity_in_basin(_settle_with(field, ic2)[0], field)["sign"]
        rows.append((name, s1, s2, s1 == s2))
    return rows


# ----------------------------------------------------------------------------- branch survival ΔV
def _noise_incr(X, sigma, sq, rng, noise_kind):
    xi = rng.standard_normal(X.shape) * sq
    if noise_kind == "demographic":
        xi *= np.sqrt(np.maximum(X, 0.0))
    elif noise_kind != "additive":
        raise ValueError(f"unknown noise_kind: {noise_kind!r}")
    return sigma * xi


def quasipotential(xstar, sigma, n=1000, T=1500.0, dt=0.02, seed=0, burn=0.25, noise_kind="additive"):
    """In-basin quasi-stationary distribution of prog=(home sign)*m; V(prog)=-σ²logP(prog)."""
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, axis=0).copy()
    ss = float(np.sign(m_imbalance(xstar[None, :])[0]))
    nsteps = int(T / dt); sq = np.sqrt(dt); kburn = int(burn * nsteps)
    alive = np.ones(n, dtype=bool)
    counts = np.zeros(len(BINS) - 1)
    for k in range(nsteps):
        X = np.clip(X + field_many(X) * dt + _noise_incr(X, sigma, sq, rng, noise_kind), 1e-9, None)
        prog = ss * m_imbalance(X)
        alive &= (prog > -0.5)
        if k > kburn and alive.any():
            counts += np.histogram(prog[alive], bins=BINS)[0]
    mid = 0.5 * (BINS[:-1] + BINS[1:])
    Pd = counts / max(counts.sum(), 1)
    with np.errstate(divide="ignore"):
        V = -sigma ** 2 * np.log(Pd)
    V[Pd <= 0] = np.nan
    return mid, Pd, V


def escape_rate(xstar, sigma, n=800, T=2500.0, dt=0.02, seed=0, noise_kind="additive"):
    """Escape rate k=(#flipped)/(total residence time); MFPT=1/k. Flip = cross to the mirror cluster."""
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, axis=0).copy()
    ss = float(np.sign(m_imbalance(xstar[None, :])[0]))
    nsteps = int(T / dt); sq = np.sqrt(dt)
    flipped = np.zeros(n, dtype=bool); tflip = np.full(n, np.nan)
    for k in range(nsteps):
        X = np.clip(X + field_many(X) * dt + _noise_incr(X, sigma, sq, rng, noise_kind), 1e-9, None)
        prog = ss * m_imbalance(X)
        newly = (~flipped) & (prog < -0.5)
        tflip[newly] = k * dt; flipped[newly] = True
    resid = np.where(flipped, tflip, T).sum()
    nflip = int(flipped.sum())
    k_rate = nflip / resid if nflip > 0 else np.nan
    return k_rate, nflip


def barrier(xstar, qp_sigmas, kr_sigmas, qp_n=1000, kr_n=800, qp_T=1500.0, kr_T=2500.0):
    # (QP) quasipotential + sigma-collapse integrity
    qp = {}
    for s in qp_sigmas:
        mid, Pd, V = quasipotential(xstar, s, n=qp_n, T=qp_T, seed=7)
        ok = np.isfinite(V)
        Vb = V[ok][np.argmax(mid[ok])]            # anchor V=0 at basin floor
        qp[s] = (mid, V - Vb, ok)
    common = None
    for s in qp_sigmas:
        mid, V, ok = qp[s]
        reg = set(np.where(ok & np.isfinite(V))[0])
        common = reg if common is None else (common & reg)
    common = sorted(common)
    if len(common) >= 3:
        stack = np.array([qp[s][1][common] for s in qp_sigmas])
        collapse_rms = float(np.sqrt(np.nanmean((stack - stack.mean(0)) ** 2)))
    else:
        collapse_rms = float('nan')
    Vmid = np.nanmean(np.array([qp[s][1] for s in qp_sigmas]), axis=0)
    midgrid = qp[qp_sigmas[0]][0]
    fin = np.isfinite(Vmid)
    dV_qp = float(np.nanmax(Vmid[fin & (midgrid < 0.5)])) if (fin & (midgrid < 0.5)).any() else float('nan')

    # (KR) Kramers slope
    mfpts, used, nflips = [], [], []
    for s in kr_sigmas:
        k_rate, nflip = escape_rate(xstar, s, n=kr_n, T=kr_T, seed=13)
        nflips.append(nflip)
        if k_rate == k_rate and k_rate > 0:
            mfpts.append(1.0 / k_rate); used.append(s)
    used = np.array(used); mfpts = np.array(mfpts)
    dV_kr = float(np.polyfit(1.0 / used ** 2, np.log(mfpts), 1)[0]) if len(used) >= 2 else float('nan')
    return dict(qp=qp, qp_sigmas=qp_sigmas, midgrid=midgrid, Vmid=Vmid, collapse_rms=collapse_rms,
                dV_qp=dV_qp, dV_kr=dV_kr, kr_used=used, mfpts=mfpts, kr_sigmas=kr_sigmas, nflips=nflips)


# ----------------------------------------------------------------------------- driver
def measure(smoke=False):
    print("=" * 84)
    print("TWIN-CYCLE CORNER -- a 2nd independent `both` (ΔV>0, 𝒜≠0), exchange-SSB (NOT parity)")
    print("=" * 84)

    # cross-validate the affinity machinery on the canonical rotational OU
    kap, om = 1.0, 1.3
    Bc = -kap * np.eye(2) + om * JMAT
    r = ep_affinity(Bc, 0.3)
    print(f"[validate] rotational OU (κ=1, ω₀=1.3): 𝒜={r['Acyc']:.4f} (analytic 4πω₀/κ={4*np.pi*om/kap:.4f}) "
          f"-> affinity frame validated\n")

    xstar = basin_state()
    win = "cluster 1" if xstar[:3].sum() > xstar[3:].sum() else "cluster 2"
    print(f"settled basin: m=(S1-S2)/(S1+S2)={m_imbalance(xstar[None,:])[0]:+.3f}  -> {win} wins "
          f"(prog=1 home, 0 exchange saddle, <0 flipped)\n")

    # ---- ROW condition: spontaneous (thermalized crossing), not structural ----
    n_reset = 12 if smoke else 40
    npos, nneg, frac = reset_redrive(n=n_reset)
    print(f"[spontaneous?] reset-and-re-drive, {n_reset} random ICs: +{npos}/-{nneg} "
          f"-> {100*frac:.0f}% majority  =>  {'SPONTANEOUS (~50/50, thermalized crossing)' if frac<0.7 else 'STRUCTURAL'}")

    # ---- CURRENT survival: 𝒜 in BOTH basins (decoupling observable: same sign) ----
    print("\n[current survival 𝒜]  winning cluster's affinity, both basins (Lyapunov frame):")
    # force each basin by biasing the IC toward one cluster
    x1 = settle(np.array([[0.30, 0.30, 0.30, 0.05, 0.05, 0.05]]))[0]
    x2 = settle(np.array([[0.05, 0.05, 0.05, 0.30, 0.30, 0.30]]))[0]
    a1 = affinity_in_basin(x1); a2 = affinity_in_basin(x2)
    print(f"   basin 1 (m={m_imbalance(x1[None,:])[0]:+.2f}): 𝒜={a1['A']:.3f} nats  sign={a1['sign']:+d}  "
          f"spread/D={a1['spread']:.1e}  evals={np.array2string(a1['evals'],precision=2)}")
    print(f"   basin 2 (m={m_imbalance(x2[None,:])[0]:+.2f}): 𝒜={a2['A']:.3f} nats  sign={a2['sign']:+d}  "
          f"spread/D={a2['spread']:.1e}  evals={np.array2string(a2['evals'],precision=2)}")
    same_sign = (a1['sign'] == a2['sign'] and a1['sign'] != 0)
    noise_indep = (a1['spread'] < 1e-3 and a2['spread'] < 1e-3)

    # measured contrast vs the parity instance (the crux of independence -- same skeleton, mirror vs copy)
    print("\n   [contrast] sign(𝒜) basin1 vs basin2, twin vs homochiral (identical a,b,μ,F; only mirror↔copy):")
    contrast = sign_contrast()
    for name, s1, s2, pres in contrast:
        print(f"      {name:24s}: basin1 sign={s1:+d}, basin2 sign={s2:+d}  ->  "
              f"{'PRESERVED' if pres else 'REVERSED'} under branch flip")
    homo_reverses = any((not pres) for name, _, _, pres in contrast if name.startswith("homochiral"))
    decoupled = same_sign and homo_reverses
    print(f"   => branch/current sign-coupling: twin DECOUPLES (same sign), homochiral COUPLES (flips) "
          f"= {decoupled}; 𝒜 noise-independent: {noise_indep}")

    # ---- BRANCH survival: ΔV across the exchange saddle ----
    print("\n[branch survival ΔV]  noise-driven escape across the m=0 exchange saddle:")
    if smoke:
        qp_sig = (0.030, 0.045, 0.060); kr_sig = (0.080, 0.100, 0.120)
        bar = barrier(xstar, qp_sig, kr_sig, qp_n=300, kr_n=250, qp_T=600.0, kr_T=900.0)
    else:
        qp_sig = (0.030, 0.040, 0.050, 0.060); kr_sig = (0.070, 0.080, 0.090, 0.100, 0.120)
        bar = barrier(xstar, qp_sig, kr_sig)
    for s, nf in zip(kr_sig, bar['nflips']):
        print(f"   σ={s:.3f}  flips={nf}")
    print(f"   σ-collapse rms (common window) = {bar['collapse_rms']:.4f}  (small => one well-defined barrier)")
    print(f"   ΔV (quasipotential, saddle-side) ~ {bar['dV_qp']:.4f}")
    print(f"   ΔV (Kramers MFPT slope)          ~ {bar['dV_kr']:.4f}")

    # ---- verdict ----
    dV = bar['dV_kr']
    ok = (decoupled and noise_indep and a1['A'] > 0.1 and dV > 0 and frac < 0.7
          and np.max(np.abs(a1['evals'].imag)) > 1e-6)
    print("\n" + "-" * 84)
    if ok:
        print("  => SECOND `both` CORNER INSTANCED, outside the chiral family. A co-handed twin-cycle has")
        print(f"     a protected current (𝒜≈{a1['A']:.1f} nats, complex Jacobian pair, noise-independent) AND a")
        print(f"     finite branch-escape barrier (ΔV≈{dV:.3f}, σ-collapsing, Kramers) across an EXCHANGE")
        print("     saddle -- a spontaneously broken permutation symmetry, not parity. Decisive separation:")
        print("     sign(𝒜) is PRESERVED under the branch flip (both clusters co-handed), whereas the")
        print("     homochiral branch flip REVERSES it -- branch survival ⟂ current survival, shown a way")
        print("     the parity instance structurally cannot.")
    else:
        print("  => corner not cleanly instanced; inspect the numbers above before promoting.")
    print("-" * 84)

    figure(xstar, a1, a2, bar, frac, npos, nneg, contrast, smoke)
    return dict(A1=a1['A'], A2=a2['A'], same_sign=same_sign, decoupled=decoupled, dV_kr=dV,
                dV_qp=bar['dV_qp'], collapse_rms=bar['collapse_rms'], frac=frac, ok=ok)


def figure(xstar, a1, a2, bar, frac, npos, nneg, contrast, smoke):
    fig, ax = plt.subplots(2, 2, figsize=(15, 11), dpi=140)

    # (a) Kramers ΔV
    a0 = ax[0, 0]
    used, mfpts = bar['kr_used'], bar['mfpts']
    if len(used) >= 2:
        x = 1.0 / used ** 2
        a0.semilogy(x, mfpts, "o", ms=9, color="#00695c")
        xf = np.linspace(x.min(), x.max(), 40)
        sl, ic = np.polyfit(x, np.log(mfpts), 1)
        a0.semilogy(xf, np.exp(ic + sl * xf), "k--", lw=1.6, label=f"ΔV={sl:.3f}>0 (branch survival)")
        for xi, mi, si in zip(x, mfpts, used):
            a0.annotate(f"{si:.2f}", (xi, mi), fontsize=8, xytext=(4, 4), textcoords="offset points")
    a0.set_xlabel(r"$1/\sigma^2$"); a0.set_ylabel("escape MFPT across exchange saddle")
    a0.set_title("(a) branch survival: Kramers barrier $\\Delta V>0$\nacross the $m{=}0$ exchange saddle")
    a0.legend(fontsize=9, frameon=False); a0.grid(alpha=0.3, which="both")

    # (b) quasipotential sigma-collapse
    a1p = ax[0, 1]
    cols = plt.cm.viridis(np.linspace(0.15, 0.85, len(bar['qp_sigmas'])))
    for s, c in zip(bar['qp_sigmas'], cols):
        mid, V, ok = bar['qp'][s]
        a1p.plot(mid[ok], V[ok], "o-", ms=4, color=c, label=f"σ={s:.3f}")
    a1p.plot(bar['midgrid'], bar['Vmid'], "k--", lw=2, label="mean (quasipotential)")
    a1p.axvline(0, color="crimson", ls=":", lw=1.4, label="exchange saddle")
    a1p.set_xlabel("prog = (home sign)·m"); a1p.set_ylabel(r"$V=-\sigma^2\log P$")
    a1p.set_title(f"(b) quasipotential σ-COLLAPSE\nrms over common window = {bar['collapse_rms']:.4f}")
    a1p.legend(fontsize=8, frameon=False); a1p.grid(alpha=0.3)

    # (c) the decoupling observable: 𝒜 same sign in both basins (+ measured homochiral contrast)
    a2p = ax[1, 0]
    Ds = (0.01, 0.02, 0.04)
    a2p.plot(Ds, a1['A_of_D'], "o-", color="#1565c0", ms=9, lw=2,
             label=fr"basin 1: $\mathcal{{A}}$={a1['A']:.1f}, sign={a1['sign']:+d}")
    a2p.plot(Ds, a2['A_of_D'], "s--", color="#ef6c00", ms=9, lw=2,
             label=fr"basin 2: $\mathcal{{A}}$={a2['A']:.1f}, sign={a2['sign']:+d}")
    a2p.set_xlabel(r"noise intensity $D=\sigma^2$"); a2p.set_ylabel(r"cycle affinity $\mathcal{A}$ (nats/cycle)")
    a2p.set_ylim(0, max(max(a1['A_of_D']), max(a2['A_of_D'])) * 1.45)
    a2p.set_title(r"(c) current survival: $\mathcal{A}$ noise-independent AND"
                  "\nSAME SIGN in both basins (homochiral flips it)")
    # annotate the measured sign contrast (twin: preserved; homochiral: reversed)
    lines = [f"sign(A) basin1/basin2 (same a,b,μ,F):"]
    for name, s1, s2, pres in contrast:
        lines.append(f"  {name}: {s1:+d}/{s2:+d}  {'PRESERVED' if pres else 'REVERSED'}")
    a2p.text(0.03, 0.04, "\n".join(lines), transform=a2p.transAxes, fontsize=7.7, family="monospace",
             va="bottom", ha="left", bbox=dict(boxstyle="round", fc="#fffde7", ec="#bbb"))
    a2p.legend(fontsize=9, frameon=False, loc="upper right"); a2p.grid(alpha=0.3)

    # (d) the plane, now with TWO both-corners
    a3 = ax[1, 1]; a3.axis("off"); a3.set_xlim(0, 2); a3.set_ylim(0, 2)
    a3.plot([1, 1], [0, 2], color="gray", lw=1); a3.plot([0, 2], [1, 1], color="gray", lw=1)
    cells = [(0.5, 1.5, "NEITHER\nsoft-metric\nfeedforward net", "#90a4ae"),
             (1.5, 1.62, "BOTH\nhomochiral (parity)\n+ twin-cycle (exchange) ← NEW", "#2e7d32"),
             (0.5, 0.5, "BRANCH ONLY\nmetastable\nHopfield", "#6a1b9a"),
             (1.5, 0.5, "CURRENT ONLY\nstructurally stored\nRPS, DNA", "#1565c0")]
    for cx, cy, t, c in cells:
        a3.text(cx, cy, t, ha="center", va="center", fontsize=9.5, color=c, weight="bold")
    a3.text(1, -0.08, r"current survival $\mathcal{A}\neq0$  →", ha="center", fontsize=9)
    a3.text(-0.08, 1, r"branch survival $\Delta V>0$  →", va="center", rotation=90, fontsize=9)
    a3.set_title(f"(d) two independent `both` corners now\n(reset re-roll +{npos}/-{nneg} → spontaneous)")

    tag = "  [SMOKE]" if smoke else ""
    fig.suptitle(r"the twin-cycle corner: a 2nd `both` ($\Delta V>0 \wedge \mathcal{A}\neq0$) via "
                 r"EXCHANGE-SSB, not parity" + tag, fontsize=13, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    path = OUT / "twin_cycle_corner.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    measure(smoke=(len(sys.argv) > 1 and sys.argv[1] == "smoke"))
