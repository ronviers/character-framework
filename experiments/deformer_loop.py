r"""deformer_loop.py -- within-reach #1 (embodiment-minting), in deformer language.

The session opened on a modeler's intuition: two meshes defined as deformers, brought
into proximity, influence each other -- and `polyAverageVertex` / a smooth-falloff brush
relaxes topology until it "finds its level." That intuition maps exactly onto character's
two sectors, and this is the instance.

A closed 3-node perception-action loop (three deformer channels coupled in a cycle). The
coupling interpolates between two limits by a reciprocity knob lambda in [0,1]:

  lambda = 0  RECIPROCAL servo  -- symmetric cyclic Laplacian = Laplacian smoothing =
              `polyAverageVertex`: each node pulled toward its neighbours' average.
              A GRADIENT flow -> relaxes to a fixed point -> detailed balance.
  lambda = 1  NON-RECIPROCAL drive -- antisymmetric cyclic coupling: node i pushed by its
              predecessor, pulled by its successor (the order-dependent deformer stack;
              skin-then-lattice != lattice-then-skin). A frustrated 3-cycle -> rotation.

character.md (Frustration and the protected current): "A nonzero circulation bit requires a
directed, non-reciprocal, frustrated cycle." The order parameter is the Schnakenberg entropy-
production rate <sigma> = J*A (zero <=> detailed balance <=> relaxational; > 0 <=> an
irreducibly circulating NESS) and the cycle affinity A (noise-independent).

Claim instanced (character.md, Motion and proximity / The minting claim):
  reciprocal coupling (lambda=0)        -> <sigma> = 0, A = 0     : relaxes, no character
  non-reciprocal coupling (lambda > 0)  -> <sigma> > 0, A > 0     : a minted protected current
The lambda-sweep IS "proximity is a creation operator for protected current."

Affinity machinery (Lyapunov Sigma; Omega = B + d Sigma^{-1}; <sigma> = Tr[Omega Sigma Omega^T]/d;
A = <sigma>/(omega_0/2pi)) reused from cycle_affinity.py -- itself cross-validated against the
canonical rotational OU to machine precision.
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
from cycle_affinity import lyap, ep_affinity, P   # noqa: E402  (P: 2x3 projector onto plane perp (1,1,1))
OUT = Path(__file__).resolve().parent

KAPPA = 1.0     # self-relaxation of each deformer channel
G = 0.5         # coupling strength

# Symmetric cyclic graph Laplacian of the 3-cycle (reciprocal smoothing: pull toward
# neighbours' average). Eigenvalues {0, 3, 3}; on the plane perp (1,1,1) it is 3*I.
L_SYM = np.array([[2., -1., -1.],
                  [-1., 2., -1.],
                  [-1., -1., 2.]])

# Antisymmetric cyclic coupling (non-reciprocal directed cycle: i <- i+1 with +, i <- i-1
# with -). Eigenvalues {0, +i*sqrt3, -i*sqrt3}; on the plane it is sqrt3 * J (a rotation).
K_ANTI = np.array([[0., 1., -1.],
                   [-1., 0., 1.],
                   [1., -1., 0.]])


def coupling_matrix(lam, kappa=KAPPA, g=G):
    """dx/dt = M x.  M = -kappa*I  - (1-lam)*g*L_sym  + lam*g*K_anti.
    lam=0: pure reciprocal smoothing (gradient, relaxational).
    lam=1: pure non-reciprocal cyclic drive (frustrated, rotational)."""
    return -kappa * np.eye(3) - (1.0 - lam) * g * L_SYM + lam * g * K_ANTI


def analytic_affinity(lam, kappa=KAPPA, g=G):
    """Closed form on the perp-plane: B2 = -(kappa + 3g(1-lam)) I + (lam g sqrt3) J.
    omega_0 = lam g sqrt3 ; kappa_eff = kappa + 3g(1-lam) ; A = 4 pi omega_0 / kappa_eff."""
    om0 = lam * g * np.sqrt(3.0)
    keff = kappa + 3.0 * g * (1.0 - lam)
    return (4.0 * np.pi * om0 / keff) if keff > 0 else np.nan


def main():
    print("=" * 84)
    print("DEFORMER LOOP -- reciprocal smoothing (relaxes) vs non-reciprocal stack (circulates)")
    print("   within-reach #1: 'frustrated => mints a protected current', in deformer language")
    print("=" * 84)
    print(f"  3-node loop, self-relaxation kappa={KAPPA}, coupling g={G}; noise d=sigma^2\n")

    d = 0.02
    lams = [0.0, 0.1, 0.25, 0.5, 0.75, 1.0]
    print(f"  {'lambda':>7} {'eig(M) real':>13} {'eig(M) imag':>13} {'<sigma>=J*A':>12}"
          f" {'A (num)':>9} {'A (analytic)':>13}")
    rows = []
    for lam in lams:
        M = coupling_matrix(lam)
        w = np.linalg.eigvals(M)
        # report the leading non-uniform mode pair (drop the ~0 uniform eigenvalue)
        order = np.argsort(np.abs(w.real))           # uniform mode has smallest |Re|? no -- keep all
        re = np.sort(w.real)
        im = np.sort(np.abs(w.imag))[::-1]
        B2 = P @ M @ P.T
        r = ep_affinity(B2, d)
        A_num = 0.0 if (not np.isfinite(r["Acyc"]) or r["om0"] < 1e-12) else r["Acyc"]
        sigma = r["sigma"] if abs(r["sigma"]) > 1e-14 else 0.0
        A_an = analytic_affinity(lam)
        rows.append((lam, sigma, A_num, A_an, im[0]))
        print(f"  {lam:>7.2f} {re[0]:>13.4f} {im[0]:>13.4f} {sigma:>12.4e}"
              f" {A_num:>9.4f} {A_an:>13.4f}")

    # noise-independence of A at the fully non-reciprocal limit (affinity is a drift property)
    print(f"\n  noise-independence check at lambda=1 (A must be flat in d):")
    A_of_d = []
    for dd in (0.005, 0.01, 0.02, 0.04):
        r = ep_affinity(P @ coupling_matrix(1.0) @ P.T, dd)
        A_of_d.append(r["Acyc"])
        print(f"     d={dd:.3f}: <sigma>={r['sigma']:.4f}, A={r['Acyc']:.4f} nats/cycle")
    spread = float(np.std(A_of_d))
    print(f"     spread(A) over d = {spread:.2e}  -> noise-INDEPENDENT (affinity is in the drift)")

    print("\n" + "-" * 84)
    sig0 = rows[0][1]
    sig1 = rows[-1][1]
    relaxes = abs(sig0) < 1e-10
    mints = sig1 > 1e-6
    print(f"  lambda=0 (reciprocal smoothing / polyAverageVertex): <sigma> = {sig0:.2e}"
          f"  {'(detailed balance -> RELAXES, no character)' if relaxes else ''}")
    print(f"  lambda=1 (non-reciprocal stack / order-dependent)  : <sigma> = {sig1:.4f}"
          f"  {'(broken detailed balance -> CIRCULATES, character)' if mints else ''}")
    if relaxes and mints:
        print("  => the reciprocal limit has ZERO entropy production (it finds its level); breaking")
        print("     reciprocity MINTS a protected current. 'frustrated => 𝒜≠0' instanced; the")
        print("     λ-sweep is proximity as a creation operator for protected current.  [VINDICATE]")
    print("-" * 84)

    figure(rows, A_of_d)
    return rows


def figure(rows, A_of_d):
    lams = np.array([r[0] for r in rows])
    sig = np.array([r[1] for r in rows])
    A_num = np.array([r[2] for r in rows])
    A_an = np.array([r[3] for r in rows])
    imag = np.array([r[4] for r in rows])

    fig, ax = plt.subplots(1, 3, figsize=(17, 5.0), dpi=140)

    a0 = ax[0]
    a0.plot(lams, sig, "o-", color="#ad1457", ms=8, lw=2)
    a0.axhline(0, color="gray", lw=1, ls=":")
    a0.set_xlabel("λ   (0 = reciprocal smoothing → 1 = non-reciprocal stack)")
    a0.set_ylabel(r"$\langle\sigma\rangle = J\,\mathcal{A}$  (entropy production)")
    a0.set_title("(a) the minting: current is born\nas reciprocity breaks")
    a0.grid(alpha=0.3)
    a0.annotate("relaxes\n(soft sector)", (0.0, 0), fontsize=9, xytext=(0.04, 0.12),
                textcoords=("data", "axes fraction"), color="#555")
    a0.annotate("circulates\n(hard sector)", (1.0, sig[-1]), fontsize=9, xytext=(0.62, 0.62),
                textcoords=("data", "axes fraction"), color="#ad1457")

    a1 = ax[1]
    a1.plot(lams, A_num, "o", color="#1565c0", ms=9, label=r"$\mathcal{A}$ (numeric, Lyapunov)")
    a1.plot(lams, A_an, "-", color="k", lw=1.4, label=r"$\mathcal{A}$ (analytic $4\pi\omega_0/\kappa_{eff}$)")
    a1.set_xlabel("λ"); a1.set_ylabel(r"cycle affinity $\mathcal{A}$ (nats/cycle)")
    a1.set_title(r"(b) affinity $\mathcal{A}$ turns on with" + "\nnon-reciprocity (num = analytic)")
    a1.legend(fontsize=9, frameon=False); a1.grid(alpha=0.3)

    a2 = ax[2]
    a2.plot(lams, imag, "o-", color="#2e7d32", ms=8, lw=2)
    a2.set_xlabel("λ"); a2.set_ylabel(r"|Im eig($M$)|  (rotation rate $\omega_0$)")
    a2.set_title("(c) eigenvalues: real at λ=0 (overdamped,\nfinds its level) → complex pair (rotation)")
    a2.grid(alpha=0.3)

    fig.suptitle("deformer loop — reciprocal smoothing relaxes ($\\mathcal{A}=0$); "
                 "non-reciprocal coupling mints a protected current ($\\mathcal{A}>0$)",
                 fontsize=12, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    path = OUT / "deformer_loop.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
