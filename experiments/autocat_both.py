r"""autocat_both.py -- Step 2 of the mechanism-independent `both`: is there a window where the
autocatalytic SOFT PITCHFORK coexists with a current (𝒜≠0)?

Step 1 (autocat_pitchfork.py) isolated, current-free, a soft pitchfork + quadratic barrier (ee*²∝ε
linear, ΔU∝ee*⁴) -- a distinct universality class from the LV twin's hard/linear. Here each handedness
becomes a 3-species ring with an internal a≠b cycle (strength `ec`) that mints the current. BUT that
ring is itself a within-group LV competition (the review's HARD ingredient), so a strong cycle reicts
hard-exclusion and KILLS the soft branch (confirmed: ec=0.5 destroys breaking). The scientific question
is therefore the WINDOW: at small ec, does ee*² stay LINEAR (soft survives) while 𝒜 is clearly >0?

  dL_i = k1 + (g−kd)·L_i·(1−P/cap) − k3·L_i·S_R − ec·L_i·(a·L_{i+1}+b·L_{i-1})    P=S_L+S_R
  dR_i = k1 + (g−kd)·R_i·(1−P/cap) − k3·R_i·S_L − ec·R_i·(b·R_{i+1}+a·R_{i-1})    (mirror, parity)

`both` iff some ec>0 has BOTH: soft pitchfork (ee*²-R²>0.99, ΔU∝ee*⁴) AND current (𝒜>0.1, complex
pair, noise-indep) AND spontaneous reset (~50/50). The ec-scan maps the coexistence directly.
"""
from __future__ import annotations
import sys
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
from cycle_affinity import ep_affinity, P as PROJ   # noqa: E402  (validated affinity frame)

KD, K3, CAP, G, A0, B0 = 0.50, 1.0, 2.0, 0.70, 0.50, 1.0
VBREAK = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6.0)
OUT = Path(__file__).resolve().parent


def field(X, k1, ec, g=G, kd=KD, k3=K3, cap=CAP, a=A0, b=B0):
    L, R = X[:, :3], X[:, 3:]
    SL = L.sum(1, keepdims=True); SR = R.sum(1, keepdims=True); P = SL + SR
    sat = 1.0 - P / cap
    cycL = a * np.roll(L, -1, 1) + b * np.roll(L, 1, 1)
    cycR = b * np.roll(R, -1, 1) + a * np.roll(R, 1, 1)              # mirror (parity)
    dL = k1 + (g - kd) * L * sat - k3 * L * SR - ec * L * cycL
    dR = k1 + (g - kd) * R * sat - k3 * R * SL - ec * R * cycR
    return np.concatenate([dL, dR], axis=1)


def ee(X):
    SL = X[:, :3].sum(1); SR = X[:, 3:].sum(1)
    return (SL - SR) / (SL + SR + 1e-12)


def settle(k1, ec, bias=0.05, T=3500.0, dt=0.01):
    X = np.clip(np.array([[1 + bias, 1 + bias, 1 + bias, 1 - bias, 1 - bias, 1 - bias]]), 1e-9, None) / 3.0
    for _ in range(int(T / dt)):
        X = np.clip(X + field(X, k1, ec) * dt, 1e-9, None)
    return X[0]


def racemic_eig(k1, ec):
    x = np.full((1, 6), 1.0 / 3.0)
    for _ in range(int(2000.0 / 0.01)):
        x = np.clip(x + field(x, k1, ec) * 0.01, 1e-9, None)
    x0 = x[0]; eps = 1e-6
    f0 = field(x0[None, :], k1, ec)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = x0.copy(); xp[i] += eps
        J[:, i] = (field(xp[None, :], k1, ec)[0] - f0) / eps
    return float(VBREAK @ J @ VBREAK)


def winner_affinity(xstar, k1, ec, Ds=(0.01, 0.02, 0.04)):
    eps = 1e-6
    f0 = field(xstar[None, :], k1, ec)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = xstar.copy(); xp[i] += eps
        J[:, i] = (field(xp[None, :], k1, ec)[0] - f0) / eps
    win = slice(0, 3) if xstar[:3].sum() > xstar[3:].sum() else slice(3, 6)
    B2 = PROJ @ J[win, win] @ PROJ.T
    A_of = [ep_affinity(B2, d)["Acyc"] for d in Ds]
    return float(np.mean(A_of)), float(np.std(A_of)), np.linalg.eigvals(B2)


def linfit_pitchfork(k1s, ec):
    ee2 = np.array([ee(settle(k1, ec)[None, :])[0] ** 2 for k1 in k1s])
    broken = ee2 > 4e-4
    if broken.sum() < 4:
        return ee2, float('nan'), float('nan')
    Al, bl = np.polyfit(k1s[broken], ee2[broken], 1); k1c = -bl / Al
    r = ee2[broken] - (Al * k1s[broken] + bl)
    R2 = 1 - np.sum(r ** 2) / np.sum((ee2[broken] - ee2[broken].mean()) ** 2)
    return ee2, k1c, R2


def scan_ec(ec, k1s):
    ee2, k1c, R2 = linfit_pitchfork(k1s, ec)
    if not np.isfinite(k1c) or k1c <= 0.02:
        return dict(ec=ec, k1c=k1c, R2=R2, A=0.0, rot=False, broke=False, ee2=ee2)
    k1m = 0.5 * k1c
    A, spread, evals = winner_affinity(settle(k1m, ec), k1m, ec)
    return dict(ec=ec, k1c=k1c, R2=R2, A=A, spread=spread,
                rot=bool(np.max(np.abs(evals.imag)) > 1e-6), broke=True, ee2=ee2, k1m=k1m, evals=evals)


def barrier_collapse(ec, k1c):
    k1b = np.linspace(0.25 * k1c, 0.85 * k1c, 5)
    dU, ee4 = [], []
    for k1 in k1b:
        A = racemic_eig(k1, ec); e2 = ee(settle(k1, ec)[None, :])[0] ** 2
        dU.append(A * e2 / 4.0); ee4.append(e2 ** 2)
    dU = np.array(dU); ee4 = np.array(ee4)
    s4, i4 = np.polyfit(ee4, dU, 1); r4 = dU - (s4 * ee4 + i4)
    R2_4 = 1 - np.sum(r4 ** 2) / np.sum((dU - dU.mean()) ** 2)
    return ee4, dU, R2_4


def reset_rolls(ec, k1, n=40, spread=0.4):
    signs = []
    for s in range(n):
        rng = np.random.default_rng(s)
        X = np.clip((1.0 / 3.0) * (1 + spread * rng.standard_normal((1, 6))), 1e-9, None)
        for _ in range(int(2500.0 / 0.02)):
            X = np.clip(X + field(X, k1, ec) * 0.02, 1e-9, None)
        signs.append(int(np.sign(ee(X)[0])))
    signs = np.array(signs); npos, nneg = int((signs > 0).sum()), int((signs < 0).sum())
    return npos, nneg, max(npos, nneg) / len(signs)


def main():
    print("=" * 88)
    print("AUTOCAT `both` -- WINDOW where the soft pitchfork coexists with a current (𝒜≠0)")
    print("=" * 88)
    k1s = np.linspace(0.0, 0.5, 26)
    ecs = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50]
    print("[ec scan]  soft pitchfork (ee*²-R²>0.99) AND current (𝒜>0.1) ?")
    rows = []
    for ec in ecs:
        r = scan_ec(ec, k1s); rows.append(r)
        soft = r["broke"] and r["R2"] > 0.99
        cur = r["A"] > 0.1 and r["rot"]
        tag = "  <= BOTH (soft+current)" if (soft and cur and ec > 0) else \
              ("  branch DEAD" if not r["broke"] else ("  soft, no current" if not cur else "  current, hard"))
        print(f"   ec={r['ec']:.2f}: k1c={r['k1c']:.3f}  ee*²-R²={r['R2']:.4f}  𝒜={r['A']:.3f} nats"
              f"  complex_pair={r['rot']}{tag}")

    win = [r for r in rows if r["ec"] > 0 and r["broke"] and r["R2"] > 0.99 and r["A"] > 0.1 and r["rot"]]
    if not win:
        print("\n  => NO coexistence window: the current and the soft branch TRADE OFF on this substrate")
        print("     (the within-group cycle that mints 𝒜 is itself the hard-exclusion competition). A")
        print("     soft-pitchfork `both` is not freely realizable here -- a finding, not a failure.")
        figure(rows, None); print("-" * 88); return dict(both=False, rows=rows)

    best = max(win, key=lambda r: r["A"])          # most current inside the soft window
    ec = best["ec"]; k1c = best["k1c"]
    print(f"\n[confirm at ec={ec:.2f}]  (most current inside the soft window)")
    ee4, dU, R2_4 = barrier_collapse(ec, k1c)
    npos, nneg, frac = reset_rolls(ec, best["k1m"])
    print(f"    ee*² linear R²={best['R2']:.5f} (k1c={k1c:.3f});  ΔU∝ee*⁴ collapse R²={R2_4:.4f}")
    print(f"    𝒜={best['A']:.3f} nats (spread/D={best['spread']:.1e}); winner evals="
          f"{np.array2string(best['evals'], precision=3)}")
    print(f"    reset re-roll +{npos}/-{nneg} -> {100*frac:.0f}% ({'SPONTANEOUS' if frac < 0.7 else 'structural'})")

    both = best["R2"] > 0.99 and R2_4 > 0.98 and best["A"] > 0.1 and best["rot"] and frac < 0.7
    print("\n" + "-" * 88)
    if both:
        print(f"  => MECHANISM-INDEPENDENT `both` INSTANCED (ec={ec:.2f}). The soft pitchfork survives a")
        print(f"     current: ee*² LINEAR (R²={best['R2']:.4f}), quadratic barrier ΔU∝ee*⁴ (R²={R2_4:.4f}),")
        print(f"     with 𝒜≈{best['A']:.1f} nats (complex pair, noise-indep), spontaneously selected ({100*frac:.0f}%).")
        print("     The `both` corner now holds TWO mechanisms: hard transcritical (homochiral/twin, linear")
        print("     ΔV) AND soft pitchfork (here, quadratic ΔV) -- mechanism-independence, not just symmetry.")
    else:
        print(f"  => marginal at ec={ec:.2f} (R²_4={R2_4:.3f}, reset {frac:.2f}); inspect.")
    print("-" * 88)
    figure(rows, dict(ec=ec, k1c=k1c, R2=best["R2"], ee4=ee4, dU=dU, R2_4=R2_4, A=best["A"],
                      evals=best["evals"], npos=npos, nneg=nneg, ee2=best["ee2"], k1s=k1s))
    return dict(both=both, ec=ec, A=best["A"], R2=best["R2"], R2_4=R2_4, frac=frac)


def figure(rows, best):
    fig, ax = plt.subplots(1, 3, figsize=(18, 5.3), dpi=140)
    ecs = np.array([r["ec"] for r in rows])
    R2s = np.array([r["R2"] if r["broke"] else np.nan for r in rows])
    As = np.array([r["A"] for r in rows])

    a0 = ax[0]
    a0.plot(ecs, R2s, "o-", color="#00695c", ms=7, label="ee*² linear $R^2$ (soft)")
    a0.axhline(0.99, color="#00695c", ls=":", lw=1, alpha=0.6)
    a0.set_xlabel("internal-cycle strength $ec$"); a0.set_ylabel("ee*² linear $R^2$", color="#00695c")
    a0.tick_params(axis="y", labelcolor="#00695c"); a0.set_ylim(0.9, 1.005)
    a0b = a0.twinx()
    a0b.plot(ecs, As, "s--", color="#c62828", ms=6, label=r"$\mathcal{A}$ (current)")
    a0b.axhline(0.1, color="#c62828", ls=":", lw=1, alpha=0.6)
    a0b.set_ylabel(r"$\mathcal{A}$ (nats)", color="#c62828"); a0b.tick_params(axis="y", labelcolor="#c62828")
    a0.set_title("(a) coexistence WINDOW: soft ($R^2{>}0.99$)\nAND current ($\\mathcal{A}{>}0.1$) vs $ec$")
    if best is not None:
        a0.axvline(best["ec"], color="gray", ls="-", lw=1, alpha=0.5)
    a0.grid(alpha=0.3)

    a1 = ax[1]
    if best is not None:
        a1.plot(best["k1s"], best["ee2"], "o", color="#00695c", ms=6)
        br = best["ee2"] > 4e-4
        Al, bl = np.polyfit(best["k1s"][br], best["ee2"][br], 1)
        xf = np.linspace(best["k1s"].min(), best["k1c"], 30)
        a1.plot(xf, np.maximum(Al * xf + bl, 0), "k--", lw=1.4, label=fr"linear $R^2$={best['R2']:.4f}")
        a1.axvline(best["k1c"], color="crimson", ls=":", lw=1.2)
        a1.legend(fontsize=9, frameon=False)
    a1.set_xlabel("racemic input $k_1$"); a1.set_ylabel(r"$ee_*^2$")
    a1.set_title("(b) pitchfork SURVIVES the current\n$ee_*^2$ still linear at the chosen $ec$")
    a1.grid(alpha=0.3)

    a2 = ax[2]
    if best is not None:
        a2.plot(best["ee4"], best["dU"], "o", color="#2e7d32", ms=9)
        s4, i4 = np.polyfit(best["ee4"], best["dU"], 1); xf = np.linspace(0, best["ee4"].max() * 1.05, 20)
        a2.plot(xf, s4 * xf + i4, "k--", lw=1.4, label=fr"$\Delta U\propto ee_*^4$, $R^2$={best['R2_4']:.4f}")
        a2.legend(fontsize=9, frameon=False)
        a2.set_title(fr"(c) quadratic barrier SURVIVES ($\mathcal{{A}}$={best['A']:.1f},"
                     f" reset +{best['npos']}/−{best['nneg']})")
    else:
        a2.text(0.5, 0.5, "no coexistence window\n(current ⟂ soft trade off)", ha="center", va="center",
                fontsize=12, transform=a2.transAxes)
        a2.set_title("(c) no soft-pitchfork `both` here")
    a2.set_xlabel(r"$ee_*^4$"); a2.set_ylabel(r"barrier $\Delta U$"); a2.grid(alpha=0.3)

    fig.suptitle(r"autocatalytic `both`: does the soft pitchfork ($ee_*^2$ linear, $\Delta U\propto ee_*^4$) "
                 r"survive a current $\mathcal{A}\neq0$?  (ec-scan maps the coexistence window)",
                 fontsize=12.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "autocat_both.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
