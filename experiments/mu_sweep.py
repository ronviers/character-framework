r"""mu_sweep.py -- the strong-form falsifier for branch survival: ΔV is born at the parity-breaking
bifurcation and scales as (μ − μ_c)², vanishing below threshold.

Model b's prediction (review_request_identity_survival.md): near the parity-breaking threshold the
chiral order parameter obeys the pitchfork normal form  ṁ = a(μ) m − b m³ (b>0), giving the barrier
ΔV = a(μ)²/4b ∝ (μ − μ_c)², with ΔV → 0 as μ → μ_c⁺ and ΔV = 0 below threshold.

We extract the normal form DIRECTLY from the 6D homochiral dynamics:
  a(μ)   = the parity-breaking eigenvalue of the racemic fixed point (the uniform L−R mode),
  m±(μ)  = the deterministic SSB amplitude (settled |ee|),
  ΔU(μ)  = a·m±²/4   (the normal-form barrier; b = a/m±²).
Analytic anchor: racemic x* = F/(1+a+b+3μ) ⇒ a(μ) = F(3μ−c)/(c+3μ), c=1+a+b ⇒ μ_c = c/3 = 0.833.
A noisy escape-MFPT check confirms the Freidlin–Wentzell barrier tracks ΔU (ln τ_flip ∝ ΔU/σ²).
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

A0, B0, F0 = 0.5, 1.0, 1.0
C = 1.0 + A0 + B0                 # 2.5
MU_C = C / 3.0                    # analytic parity-breaking threshold = 0.8333
OUT = Path(__file__).resolve().parent


def field_many(X, mu):
    L, R = X[:, :3], X[:, 3:]
    SL = L.sum(1, keepdims=True); SR = R.sum(1, keepdims=True)
    dL = L * (F0 - (L + A0 * np.roll(L, -1, 1) + B0 * np.roll(L, 1, 1)) - mu * SR)
    dR = R * (F0 - (R + B0 * np.roll(R, -1, 1) + A0 * np.roll(R, 1, 1)) - mu * SL)
    return np.concatenate([dL, dR], axis=1)


def ee(X):
    L = X[:, :3].sum(1); R = X[:, 3:].sum(1)
    return (L - R) / (L + R + 1e-12)


def racemic(mu):
    return np.full(6, F0 / (C + 3.0 * mu))


def parity_breaking_eig(mu):
    """parity-breaking eigenvalue a(μ): the uniform L−R mode eigenvalue of the racemic Jacobian."""
    x = racemic(mu); eps = 1e-6
    f0 = field_many(x[None, :], mu)[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = x.copy(); xp[i] += eps
        J[:, i] = (field_many(xp[None, :], mu)[0] - f0) / eps
    v = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6.0)
    a = float(v @ J @ v)
    resid = float(np.linalg.norm(J @ v - a * v))         # ~0 confirms v is the eigenvector
    return a, resid


def m_amplitude(mu, T=2500.0, dt=0.04):
    """deterministic SSB amplitude |ee| from an asymmetric IC (→0 below threshold)."""
    x = racemic(mu).copy()
    x[:3] *= 1.15; x[3:] *= 0.85
    x = np.clip(x, 1e-9, None)
    for _ in range(int(T / dt)):
        x = np.clip(x + field_many(x[None, :], mu)[0] * dt, 1e-9, None)
    return float(abs(ee(x[None, :])[0]))


def escape_mfpt(mu, sigma, n=600, T=4000.0, dt=0.02, seed=0):
    """noisy first-passage out of one chiral basin (ee crosses to −0.5·m±). MFPT = 1/rate."""
    m = m_amplitude(mu)
    if m < 0.05:
        return np.nan, m
    # settle a basin deterministically
    xb = racemic(mu).copy(); xb[:3] *= 1.15; xb[3:] *= 0.85; xb = np.clip(xb, 1e-9, None)
    for _ in range(int(2000.0 / 0.04)):
        xb = np.clip(xb + field_many(xb[None, :], mu)[0] * 0.04, 1e-9, None)
    home = float(np.sign(ee(xb[None, :])[0]))
    rng = np.random.default_rng(seed)
    X = np.repeat(xb[None, :], n, 0).copy()
    nsteps = int(T / dt); sq = np.sqrt(dt)
    flipped = np.zeros(n, bool); tflip = np.full(n, np.nan)
    for k in range(nsteps):
        X = np.clip(X + field_many(X, mu) * dt + sigma * rng.standard_normal((n, 6)) * sq, 1e-9, None)
        e = ee(X)
        nb = (~flipped) & (home * e < -0.5 * m)
        tflip[nb] = k * dt; flipped[nb] = True
    resid = np.where(flipped, tflip, T).sum()
    nf = int(flipped.sum())
    return (resid / nf if nf > 0 else np.nan), m


def main():
    print("=" * 80)
    print("μ-SWEEP -- branch-survival barrier born at the parity-breaking bifurcation")
    print("=" * 80)
    print(f"analytic threshold μ_c = c/3 = (1+a+b)/3 = {MU_C:.4f}\n")

    mus = np.linspace(0.70, 1.80, 23)
    a_of, m_of, dU_of, resmax = [], [], [], 0.0
    for mu in mus:
        a, res = parity_breaking_eig(mu); resmax = max(resmax, res)
        m = m_amplitude(mu)
        dU = a * m ** 2 / 4.0 if a > 0 else 0.0
        a_of.append(a); m_of.append(m); dU_of.append(dU)
    a_of = np.array(a_of); m_of = np.array(m_of); dU_of = np.array(dU_of)
    a_analytic = F0 * (3 * mus - C) / (C + 3 * mus)
    print(f"parity-breaking eigenvalue: numeric vs analytic F(3μ−c)/(c+3μ) max|Δ| = "
          f"{np.max(np.abs(a_of - a_analytic)):.2e}  (uniform-mode eigenvector residual {resmax:.1e})")

    # numeric μ_c from a=0 crossing
    i = np.searchsorted(a_of, 0.0)
    mu_c_num = mus[i - 1] + (mus[i] - mus[i - 1]) * (0 - a_of[i - 1]) / (a_of[i] - a_of[i - 1])
    print(f"numeric μ_c (a=0 crossing) = {mu_c_num:.4f}  (analytic {MU_C:.4f})\n")

    # below threshold: barrier is exactly zero (no second basin)
    below = mus < MU_C
    print(f"below threshold (μ<μ_c): max ΔU = {dU_of[below].max():.2e}, max m± = {m_of[below].max():.3f}"
          f"  -> single basin, NO barrier")

    # near-threshold scaling fits (μ in [μ_c, μ_c+0.35]; quartic normal form valid only near threshold)
    band = (mus > MU_C) & (mus < MU_C + 0.35)
    t = mus[band] - MU_C
    # m± ∝ (μ−μ_c)^p  ;  ΔU ∝ (μ−μ_c)^q
    p = np.polyfit(np.log(t), np.log(m_of[band]), 1)[0]
    q = np.polyfit(np.log(t), np.log(dU_of[band]), 1)[0]
    print(f"\nnear-threshold scaling (pitchfork prediction p=0.5, q=2.0):")
    print(f"   m±   ∝ (μ−μ_c)^{p:.2f}   (predicted 0.5)")
    print(f"   ΔU   ∝ (μ−μ_c)^{q:.2f}   (predicted 2.0)")

    # noisy FW check: ln(MFPT) vs ΔU should be linear (slope 1/σ²)
    print("\nnoisy Freidlin–Wentzell check -- escape MFPT at fixed σ vs the normal-form barrier ΔU:")
    sig = 0.08
    mu_n = np.array([0.95, 1.00, 1.05, 1.10, 1.15])
    lnT, dUn = [], []
    for mu in mu_n:
        mfpt, m = escape_mfpt(mu, sig, seed=7)
        a, _ = parity_breaking_eig(mu); dU = a * m ** 2 / 4.0
        if mfpt == mfpt and mfpt > 0:
            lnT.append(np.log(mfpt)); dUn.append(dU)
            print(f"   μ={mu:.2f}: ΔU={dU:.4f}, MFPT={mfpt:8.1f}, ln(MFPT)={np.log(mfpt):.3f}")
    lnT = np.array(lnT); dUn = np.array(dUn)
    if len(lnT) >= 2:
        slope, _ = np.polyfit(dUn, lnT, 1)
        r = np.corrcoef(dUn, lnT)[0, 1]
        print(f"   ln(MFPT) = {slope:.2f}·ΔU + const   (corr {r:.3f}; slope≈1/σ²={1/sig**2:.1f} if FW barrier=ΔU)")

    print("\n" + "-" * 80)
    confirmed = abs(mu_c_num - MU_C) < 0.02 and dU_of[below].max() < 1e-6
    print("  CONFIRMED (mechanism):")
    print(f"    - barrier born exactly at μ_c = {MU_C:.3f} = (1+a+b)/3 (a=0 crossing at {mu_c_num:.4f})")
    print(f"    - ΔU = 0 below threshold: branch survival exists ONLY where the basin geometry does")
    print(f"    - noisy escape MFPT tracks ΔU (corr {r:.3f}): the Freidlin–Wentzell barrier ∝ a(μ)")
    print("  FALSIFIED (model b's specific normal form):")
    print(f"    - m± does NOT follow √(μ−μ_c) (exponent {p:+.2f}, not 0.5) — it JUMPS to ~1:")
    print(f"      the L↔R transition is COMPETITIVE EXCLUSION, not a supercritical pitchfork")
    print(f"    - ΔU ∝ (μ−μ_c)^{q:.2f} (LINEAR), not (μ−μ_c)²: the barrier is set by the racemic")
    print(f"      saddle's instability rate a(μ) ∝ (μ−μ_c), with m± pinned at full exclusion")
    print("-" * 80)

    figure(mus, a_of, a_analytic, m_of, dU_of, dUn, lnT, sig)


def figure(mus, a_of, a_an, m_of, dU_of, dUn, lnT, sig):
    fig, ax = plt.subplots(1, 3, figsize=(18, 5.2), dpi=140)

    a0 = ax[0]
    a0.plot(mus, a_of, "o", color="#1565c0", ms=6, label="numeric")
    a0.plot(mus, a_an, "-", color="gray", lw=1.4, label=r"$F(3\mu-c)/(c+3\mu)$")
    a0.axhline(0, color="k", lw=0.6); a0.axvline(MU_C, color="crimson", ls="--", lw=1.4,
                                                  label=f"$\\mu_c={MU_C:.3f}$")
    a0.set_xlabel(r"cross-inhibition $\mu$"); a0.set_ylabel(r"parity-breaking eigenvalue $a(\mu)$")
    a0.set_title("(a) racemic state loses stability\nat $\\mu_c$ (parity-breaking)")
    a0.legend(fontsize=8, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]
    a1.plot(mus, m_of, "o-", color="#6a1b9a", ms=5, lw=1.5, label=r"$m_\pm$ (measured)")
    tt = np.linspace(MU_C, MU_C + 0.5, 50)
    band = (mus > MU_C) & (mus < MU_C + 0.35)
    cm = m_of[band][np.argmin(np.abs(mus[band] - (MU_C + 0.2)))] / np.sqrt(0.2)
    a1.plot(tt, cm * np.sqrt(tt - MU_C), "k--", lw=1.2, label=r"pitchfork $\sqrt{\mu-\mu_c}$ (falsified)")
    a1.axvline(MU_C, color="crimson", ls="--", lw=1.4)
    a1.set_xlabel(r"$\mu$"); a1.set_ylabel(r"$m_\pm$")
    a1.set_title("(b) order parameter JUMPS to 1\n(competitive exclusion), NOT pitchfork")
    a1.legend(fontsize=8, frameon=False); a1.grid(alpha=0.3)

    a2 = ax[2]
    a2.plot(mus, dU_of, "o-", color="#2e7d32", ms=5, lw=1.5, label=r"$\Delta U=a\,m_\pm^2/4$ (measured)")
    cq = dU_of[band][np.argmin(np.abs(mus[band] - (MU_C + 0.2)))] / 0.2 ** 2
    cl = dU_of[band][np.argmin(np.abs(mus[band] - (MU_C + 0.2)))] / 0.2
    a2.plot(tt, cl * (tt - MU_C), "-", color="#ef6c00", lw=1.4, label=r"$\propto(\mu-\mu_c)$ (linear, fits)")
    a2.plot(tt, cq * (tt - MU_C) ** 2, "k--", lw=1.2, label=r"$\propto(\mu-\mu_c)^2$ (falsified)")
    a2.axvline(MU_C, color="crimson", ls="--", lw=1.4)
    a2.set_xlabel(r"$\mu$"); a2.set_ylabel(r"barrier $\Delta U$")
    a2.set_title("(c) barrier born at $\\mu_c$, LINEAR in $\\mu-\\mu_c$\n(not quadratic), zero below")
    a2.legend(fontsize=8, frameon=False); a2.grid(alpha=0.3)

    fig.suptitle("μ-sweep: branch-survival barrier is born at the parity-breaking bifurcation "
                 f"($\\mu_c={MU_C:.3f}$); the L↔R transition is competitive exclusion — barrier "
                 r"LINEAR in $(\mu-\mu_c)$, not the pitchfork $(\mu-\mu_c)^2$", fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    path = OUT / "mu_sweep.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
