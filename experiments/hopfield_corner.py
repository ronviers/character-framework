r"""hopfield_corner.py -- instancing the fourth corner of the two-survivals plane:
BRANCH SURVIVAL WITHOUT CURRENT SURVIVAL (ΔV > 0, 𝒜 = 0).

A symmetric-coupling attractor net (Hopfield class) relaxes by gradient / detailed-balance descent
to fixed points: it has basins (a Kramers barrier ΔV between stored patterns → branch survival) but
no protected current (symmetric Jacobian → real spectrum, entropy production ⟨σ⟩ = 0, 𝒜 = 0 → no
current survival). This is the metastable corner — the mirror of the bare RPS triad (current
without branch survival).

2-neuron symmetric Hopfield:  ẋ_i = −x_i + w·tanh(x_{j≠i}),  W = [[0,w],[w,0]] symmetric, w>1
bistable. Two attractors (±x*, ±x*); order parameter m = (x_1+x_2)/2. The affinity/entropy-production
machinery is the same validated rotational-OU frame used for the homochiral/RPS cells.
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

W = 1.6                                   # symmetric coupling, >1 for bistability
OUT = Path(__file__).resolve().parent


def field_many(X):                        # X: (n,2);  ẋ_i = −x_i + w·tanh(x_{other})
    return -X + W * np.tanh(X[:, ::-1])


def field_one(x):
    return field_many(x[None, :])[0]


def settle(x0, T=400.0, dt=0.02):
    x = x0.copy()
    for _ in range(int(T / dt)):
        x = x + field_one(x) * dt
    return x


def jacobian(x):
    s = 1.0 / np.cosh(x) ** 2              # sech²
    return np.array([[-1.0, W * s[1]], [W * s[0], -1.0]])


def lyap(B, twoD):
    n = B.shape[0]
    K = np.kron(B, np.eye(n)) + np.kron(np.eye(n), B)
    return np.linalg.solve(K, -twoD.flatten()).reshape(n, n)


def entropy_production(J, d):
    """⟨σ⟩ = Tr[ΩSΩᵀ]/d with Ω = J + dS⁻¹ (irreversible drift). Vanishes for a gradient (symmetric) J."""
    S = lyap(J, 2 * d * np.eye(2))
    Om = J + d * np.linalg.inv(S)
    return float(np.trace(Om @ S @ Om.T) / d)


def escape_mfpt(xstar, sigma, n=600, T=3000.0, dt=0.02, seed=0):
    rng = np.random.default_rng(seed)
    X = np.repeat(xstar[None, :], n, 0).copy()
    m0 = float(xstar.mean()); home = np.sign(m0)
    nsteps = int(T / dt); sq = np.sqrt(dt)
    flipped = np.zeros(n, bool); tflip = np.full(n, np.nan)
    for k in range(nsteps):
        X = X + field_many(X) * dt + sigma * rng.standard_normal((n, 2)) * sq
        m = X.mean(1)
        nb = (~flipped) & (home * m < -0.5 * abs(m0))
        tflip[nb] = k * dt; flipped[nb] = True
    resid = np.where(flipped, tflip, T).sum(); nf = int(flipped.sum())
    return (resid / nf if nf > 0 else np.nan), nf


def main():
    print("=" * 80)
    print("HOPFIELD CORNER -- branch survival WITHOUT current survival (ΔV>0, 𝒜=0)")
    print("=" * 80)
    xstar = settle(np.array([1.0, 1.0]))
    print(f"symmetric attractor net (w={W}): attractor x* = {np.array2string(xstar, precision=3)}, "
          f"m* = {xstar.mean():+.3f}  (mirror attractor at −x*)\n")

    # ---- no current survival: symmetric Jacobian -> real spectrum, ⟨σ⟩ = 0 ----
    J = jacobian(xstar)
    ev = np.linalg.eigvals(J)
    print("[no current survival]")
    print(f"   Jacobian symmetric? max|J−Jᵀ| = {np.max(np.abs(J - J.T)):.2e}")
    print(f"   eigenvalues = {np.array2string(ev, precision=3)}  -> max|Im| = {np.max(np.abs(ev.imag)):.2e} "
          f"(real => no rotation)")
    for d in (0.01, 0.02, 0.04):
        sig = entropy_production(J, d)
        print(f"   d=σ²={d:.3f}: entropy production ⟨σ⟩ = {sig:.2e}  -> 𝒜 = 0 (detailed balance, no current)")

    # ---- branch survival: Kramers barrier ΔV between the two patterns ----
    print("\n[branch survival]  noise-driven escape between the two patterns (Kramers):")
    sigmas = np.array([0.40, 0.46, 0.52, 0.60, 0.70])
    mfpts, used = [], []
    for s in sigmas:
        mfpt, nf = escape_mfpt(xstar, s, seed=3)
        tag = f"{mfpt:8.1f}" if mfpt == mfpt else "    --"
        print(f"   σ={s:.2f}: flips={nf:4d}/600  MFPT={tag}")
        if mfpt == mfpt and mfpt > 0:
            mfpts.append(mfpt); used.append(s)
    used = np.array(used); mfpts = np.array(mfpts)
    dV = float('nan')
    if len(used) >= 2:
        slope, _ = np.polyfit(1.0 / used ** 2, np.log(mfpts), 1)
        dV = slope
        print(f"   Kramers slope d(ln MFPT)/d(1/σ²) = ΔV = {dV:.4f} > 0  -> branch survival present")

    print("\n" + "-" * 80)
    ok = (np.max(np.abs(ev.imag)) < 1e-9 and abs(entropy_production(J, 0.02)) < 1e-9 and dV > 0)
    if ok:
        print("  => FOURTH CORNER INSTANCED. A symmetric attractor net has a finite basin-escape barrier")
        print(f"     ΔV≈{dV:.3f} (branch survival) and exactly zero current (⟨σ⟩=𝒜=0, real spectrum): it")
        print("     occupies a basin and resists escape, yet does not circulate. Branch survival and")
        print("     current survival are independent — the Hopfield corner is the mirror of bare RPS.")
    else:
        print("  => corner not cleanly instanced; inspect the numbers.")
    print("-" * 80)

    figure(used, mfpts, dV)


def figure(used, mfpts, dV):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.4), dpi=140)

    a0 = ax[0]
    if len(used) >= 2:
        x = 1.0 / used ** 2
        a0.semilogy(x, mfpts, "o", ms=9, color="#6a1b9a")
        xf = np.linspace(x.min(), x.max(), 40)
        sl, ic = np.polyfit(x, np.log(mfpts), 1)
        a0.semilogy(xf, np.exp(ic + sl * xf), "k--", lw=1.5, label=f"ΔV={sl:.3f}>0 (branch survival)")
    a0.set_xlabel(r"$1/\sigma^2$"); a0.set_ylabel("escape MFPT between patterns")
    a0.set_title("Hopfield: a real Kramers barrier $\\Delta V>0$\n"
                 "yet $\\langle\\sigma\\rangle=\\mathcal{A}=0$ (no current)")
    a0.legend(fontsize=9, frameon=False); a0.grid(alpha=0.3, which="both")

    a1 = ax[1]; a1.axis("off")
    a1.set_xlim(0, 2); a1.set_ylim(0, 2)
    a1.plot([1, 1], [0, 2], color="gray", lw=1); a1.plot([0, 2], [1, 1], color="gray", lw=1)
    cells = [(0.5, 1.5, "NEITHER\nsoft-metric\nfeedforward net", "#90a4ae"),
             (1.5, 1.5, "BOTH\nspontaneously selected\nhomochiral triad", "#2e7d32"),
             (0.5, 0.5, "BRANCH ONLY\nmetastable\nHopfield  ← here", "#6a1b9a"),
             (1.5, 0.5, "CURRENT ONLY\nstructurally stored\nRPS, DNA", "#1565c0")]
    for cx, cy, t, c in cells:
        a1.text(cx, cy, t, ha="center", va="center", fontsize=9.5, color=c, weight="bold")
    a1.text(1, -0.08, r"current survival $\mathcal{A}\neq0$  →", ha="center", fontsize=9)
    a1.text(-0.08, 1, r"branch survival $\Delta V>0$  →", va="center", rotation=90, fontsize=9)
    a1.set_title("the two-survivals plane (4 corners, all realized)")

    fig.suptitle("the two-survivals plane: branch survival ($\\Delta V$) ⟂ current survival ($\\mathcal{A}$) "
                 "— the Hopfield corner instanced", fontsize=12.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "hopfield_corner.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
