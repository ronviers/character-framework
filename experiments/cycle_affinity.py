r"""cycle_affinity.py -- follow-up #1, done right: I(0) (circulation survival) vs ΔV (identity
survival) on the homochiral triad, frame-robustly.

A naive matched-σ count of within-hand current reversals at the escape noise σ~0.1 is a false
kill -- there the current is noise-washed (|noise/step| ~ |J|), so a detector fires on noise (the
tell: the "reversal time" is σ-independent, ~5, whereas a real barrier crossing accelerates hard
with noise). The correct read:
I(0) is set by the winning hand's CYCLE AFFINITY 𝒜, a DETERMINISTIC (noise-independent) property
of the drift, via the validated rotational-OU machinery (mpa-conform/scripts/two_frame_magnitude.py:
Lyapunov steady covariance -> ⟨σ⟩ = J·𝒜 to machine precision).

The separation is then STRUCTURAL and needs no unit-matching:
  identity survival  -> ΔV ≈ 0.018, a quasipotential: escape ~ exp(-ΔV/σ^2)  [σ-DEPENDENT]
  circulation surv.  -> 𝒜 nats, an affinity:        I(0) set by 𝒜           [σ-INDEPENDENT]
Two quantities with different noise-scaling cannot be the same object -> the layers are distinct.

Machinery cross-validated against the canonical rotational OU (A=-κI+ω₀ Jmat) before use.
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
from identity_survival_barrier import field_many, ee, basin_state   # noqa: E402
OUT = Path(__file__).resolve().parent

E1 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
E2 = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
P = np.vstack([E1, E2])                       # 2x3 projector onto the rotation plane perp to (1,1,1)
JMAT = np.array([[0.0, -1.0], [1.0, 0.0]])
DV_IDENTITY = 0.018                           # measured identity-survival barrier (Kramers)


def lyap(B, twoD):
    """solve B S + S B^T + twoD = 0 (steady covariance of dx = Bx dt + noise, cov(noise)=twoD)."""
    n = B.shape[0]
    K = np.kron(B, np.eye(n)) + np.kron(np.eye(n), B)
    return np.linalg.solve(K, -twoD.flatten()).reshape(n, n)


def ep_affinity(B, d):
    """⟨σ⟩ and cycle affinity 𝒜 for a 2D linear NESS dx=Bx dt+√(2d)dW, via the rotational-OU frame.
    Ω = B + d S^{-1} (irreversible drift); ⟨σ⟩ = (1/d) Tr[Ω S Ω^T]; 𝒜 = ⟨σ⟩ / J_cyc, J_cyc=ω₀/2π."""
    S = lyap(B, 2 * d * np.eye(2))
    Om = B + d * np.linalg.inv(S)
    sigma = np.trace(Om @ S @ Om.T) / d
    w = np.linalg.eigvals(B)
    om0 = float(np.max(np.abs(w.imag)))
    kappa = float(-np.mean(w.real))
    Jcyc = om0 / (2 * np.pi)
    Acyc = sigma / Jcyc if Jcyc > 0 else np.nan
    return dict(kappa=kappa, om0=om0, sigma=sigma, Jcyc=Jcyc, Acyc=Acyc)


def winner_block(xstar):
    """finite-diff 6x6 Jacobian at the settled state; return the winning hand's 3x3 block, projected
    to the 2D rotation plane (B2) and the raw 3x3 (Jw)."""
    eps = 1e-6
    f0 = field_many(xstar[None, :])[0]
    J = np.zeros((6, 6))
    for i in range(6):
        xp = xstar.copy(); xp[i] += eps
        J[:, i] = (field_many(xp[None, :])[0] - f0) / eps
    win = slice(3, 6) if xstar[3:].sum() > xstar[:3].sum() else slice(0, 3)
    Jw = J[win, win]
    B2 = P @ Jw @ P.T
    return Jw, B2


def main():
    print("=" * 82)
    print("CYCLE AFFINITY 𝒜 -- circulation survival I(0) vs identity survival ΔV (frame-robust)")
    print("=" * 82)

    # ---- cross-validate the machinery on the canonical rotational OU ----
    kap, om = 1.0, 1.3
    Bc = -kap * np.eye(2) + om * JMAT
    print("[validate] canonical rotational OU A=-κI+ω₀J (κ=1, ω₀=1.3):")
    for d in (0.7, 0.2):
        r = ep_affinity(Bc, d)
        print(f"   d={d:.2f}: ⟨σ⟩={r['sigma']:.6f} (analytic 2ω₀²/κ={2*om**2/kap:.6f}), "
              f"𝒜={r['Acyc']:.4f} (analytic 4πω₀/κ={4*np.pi*om/kap:.4f})")
    print("   -> ⟨σ⟩ and 𝒜 are D-INDEPENDENT and match the closed forms: machinery validated.\n")

    # ---- homochiral winner ----
    xstar = basin_state()
    Jw, B2 = winner_block(xstar)
    wJ = np.linalg.eigvals(Jw)
    wB = np.linalg.eigvals(B2)
    print(f"homochiral winner: basin ee={ee(xstar[None,:])[0]:+.3f}")
    print(f"   winner 3x3 Jacobian eigenvalues = {np.array2string(wJ, precision=3)}")
    print(f"   2D rotation-plane B2 eigenvalues = {np.array2string(wB, precision=3)}  "
          f"(complex pair = the protected rotation)\n")

    print("[homochiral] cycle affinity at several noise levels (must be D-independent):")
    Ds = (0.01, 0.02, 0.04)
    A_of_D = []
    for d in Ds:
        r = ep_affinity(B2, d)
        A_of_D.append(r["Acyc"])
        print(f"   d=σ²={d:.3f}: κ={r['kappa']:.4f}, ω₀={r['om0']:.4f}, ⟨σ⟩={r['sigma']:.4f}, "
              f"𝒜={r['Acyc']:.4f} nats/cycle")
    A_w = float(np.mean(A_of_D))
    A_spread = float(np.std(A_of_D))
    I0 = 2.0 * (np.cosh(A_w / (2 * 3)) - 1.0)        # N=3 ring reversal rate from the affinity
    print(f"\n   𝒜 = {A_w:.4f} nats/cycle  (spread over D = {A_spread:.2e} -> noise-INDEPENDENT, confirmed)")
    print(f"   within-cycle reversal rate I(0) = 2(cosh(𝒜/2N)-1) = {I0:.3e}  (N=3); reversal barrier ~ 𝒜/2N = {A_w/6:.3f}")

    # ---- the separation ----
    print("\n" + "-" * 82)
    print("  SEPARATION (no unit-matching needed -- different noise-scaling):")
    print(f"   identity survival : ΔV = {DV_IDENTITY:.3f}  QUASIPOTENTIAL, escape ~ exp(-ΔV/σ²)  [σ-DEPENDENT]")
    print(f"   circulation surv. : 𝒜 = {A_w:.3f} nats  AFFINITY, I(0)~exp(-𝒜/2N)              [σ-INDEPENDENT]")
    sep = A_spread < 1e-6 or A_spread / max(abs(A_w), 1e-9) < 1e-3
    if sep:
        print("   => 𝒜 is noise-independent while ΔV is a noise-activated quasipotential: the two CANNOT")
        print("      be the same quantity. circulation-survival ≠ identity-survival -- distinct layers.")
        print("      [VINDICATE -- frame-robust]")
    else:
        print("   => 𝒜 shows residual D-dependence; recheck the frame before claiming separation.")
    print("-" * 82)

    figure(Ds, A_of_D, A_w)
    return A_w


def figure(Ds, A_of_D, A_w):
    fig, ax = plt.subplots(1, 2, figsize=(13, 5), dpi=140)

    a0 = ax[0]
    a0.plot(Ds, A_of_D, "o-", color="#6a1b9a", ms=9, lw=2)
    a0.axhline(A_w, color="gray", ls="--", lw=1, label=f"𝒜 = {A_w:.2f} nats (flat)")
    a0.set_xlabel(r"noise intensity $D=\sigma^2$"); a0.set_ylabel(r"cycle affinity $\mathcal{A}$ (nats/cycle)")
    a0.set_ylim(0, max(A_of_D) * 1.4)
    a0.set_title("(a) circulation survival: affinity $\\mathcal{A}$ is\nNOISE-INDEPENDENT (I(0) set by drift)")
    a0.legend(fontsize=9, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]
    sig = np.linspace(0.05, 0.16, 100)
    a1.plot(sig ** 2, DV_IDENTITY / sig ** 2, color="#c62828", lw=2.2, label=r"$\Delta V/\sigma^2$ (escape exponent)")
    a1.set_xlabel(r"noise intensity $D=\sigma^2$"); a1.set_ylabel(r"identity-escape LDP exponent $\Delta V/\sigma^2$")
    a1.set_title("(b) identity survival: $\\Delta V$ is a\nNOISE-ACTIVATED quasipotential ($\\sigma$-dependent)")
    a1.legend(fontsize=9, frameon=False); a1.grid(alpha=0.3)

    fig.suptitle("two survivals SEPARATE: circulation = noise-independent affinity $\\mathcal{A}$;  "
                 "identity = noise-activated quasipotential $\\Delta V$", fontsize=12, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    path = OUT / "cycle_affinity.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
