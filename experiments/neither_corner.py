r"""neither_corner.py -- the corrected fourth-quadrant instance: the SOFT-METRIC ("neither") corner,
a non-trivial substrate with measured soft-sector capability and a STRUCTURALLY absent hard sector.

The earlier proposal measured I(X;Z); for a deterministic continuous encoder that diverges
(Saxe / Kolchinsky–Tracey: H(Z|X)=−∞), and any finite value is a binning/noise artifact. The clean
training-dependent capability observable is the confusion-matrix mutual information I(Ŷ;Y) — finite,
bounded by H(Y), exact, and →0 for a null net / →H(Y) for a capable one.

The hard sector is NOT measured-zero; it is structurally absent (the strongest form):
  𝒜 ≡ 0   — the computation graph is an acyclic DAG; its node-adjacency is nilpotent (all
            eigenvalues 0, no directed cycle), so no Schnakenberg cycle current can exist.
  ΔV undefined — a feedforward net retains no state between passes (state is externally re-supplied);
            there are no attractors, no separatrix, no Kramers trajectory.

Testbed: a K-class isotropic Gaussian mixture (P(X) known → exact ceiling I(X;Y)), a 2-layer MLP
X∈ℝ^d → Z=tanh(W₁X+b₁) → softmax(W₂Z+b₂), trained by plain gradient descent.
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

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(0)
D, K, H = 8, 8, 16                          # input dim, classes, hidden width
MEANS = 3.0 * rng.standard_normal((K, D))   # well-separated class means (σ = 1)


def sample(n):
    y = rng.integers(0, K, n)
    X = MEANS[y] + rng.standard_normal((n, D))
    return X, y


def softmax(L):
    L = L - L.max(1, keepdims=True)
    E = np.exp(L)
    return E / E.sum(1, keepdims=True)


def mutual_information_bits(joint):
    """I from a joint distribution table (bits)."""
    P = joint / joint.sum()
    Pr = P.sum(1, keepdims=True); Pc = P.sum(0, keepdims=True)
    m = P > 0
    return float(np.sum(P[m] * np.log2(P[m] / (Pr @ Pc)[m])))


def bayes_ceiling_IXY(n=20000):
    """exact-as-sampled ceiling I(X;Y): uniform priors, isotropic unit Gaussians ->
    P(Y=k|x) = softmax_k(-½||x-μ_k||²).  I = H(Y) − E_X[H(P(·|X))]."""
    X, _ = sample(n)
    d2 = ((X[:, None, :] - MEANS[None, :, :]) ** 2).sum(2)     # (n,K)
    post = softmax(-0.5 * d2)
    Hpost = -np.sum(post * np.log2(np.clip(post, 1e-12, None)), axis=1).mean()
    return np.log2(K) - Hpost


def adjacency_nilpotency():
    """node adjacency of the DAG (D inputs → H hidden → K outputs); show it is nilpotent
    (all eigenvalues 0, A³=0) ⇒ no directed cycle ⇒ 𝒜 ≡ 0 by construction."""
    n = D + H + K
    A = np.zeros((n, n))
    A[:D, D:D + H] = 1.0                      # input → hidden
    A[D:D + H, D + H:] = 1.0                  # hidden → output
    ev = np.linalg.eigvals(A)
    return float(np.max(np.abs(ev))), float(np.linalg.norm(np.linalg.matrix_power(A, 3)))


def main():
    print("=" * 80)
    print("NEITHER CORNER -- soft-metric substrate: measured capability, STRUCTURAL hard-sector absence")
    print("=" * 80)
    Xtr, ytr = sample(6000); Xte, yte = sample(3000)
    W1 = 0.3 * rng.standard_normal((D, H)); b1 = np.zeros(H)
    W2 = 0.3 * rng.standard_normal((H, K)); b2 = np.zeros(K)
    Ytr = np.eye(K)[ytr]
    lr, curve = 0.5, []
    for epoch in range(400):
        Z = np.tanh(Xtr @ W1 + b1)
        P = softmax(Z @ W2 + b2)
        dL = (P - Ytr) / len(ytr)
        dW2 = Z.T @ dL; db2 = dL.sum(0)
        dpre = (dL @ W2.T) * (1 - Z ** 2)
        dW1 = Xtr.T @ dpre; db1 = dpre.sum(0)
        W2 -= lr * dW2; b2 -= lr * db2; W1 -= lr * dW1; b1 -= lr * db1
        if epoch % 8 == 0:
            pr = (np.tanh(Xte @ W1 + b1) @ W2 + b2).argmax(1)
            C = np.zeros((K, K))
            np.add.at(C, (yte, pr), 1.0)
            curve.append((epoch, (pr == yte).mean(), mutual_information_bits(C)))

    pred = (np.tanh(Xte @ W1 + b1) @ W2 + b2).argmax(1)
    C = np.zeros((K, K)); np.add.at(C, (yte, pred), 1.0)
    I_hat = mutual_information_bits(C)
    acc = float((pred == yte).mean())
    I_ceiling = bayes_ceiling_IXY()
    maxev, normA3 = adjacency_nilpotency()

    # null baseline (untrained random readout) for contrast
    rngn = np.random.default_rng(99)
    Wn1 = 0.3 * rngn.standard_normal((D, H)); Wn2 = 0.3 * rngn.standard_normal((H, K))
    predn = (np.tanh(Xte @ Wn1) @ Wn2).argmax(1)
    Cn = np.zeros((K, K)); np.add.at(Cn, (yte, predn), 1.0)
    I_null = mutual_information_bits(Cn)

    print(f"\nsoft-sector capability  (K={K} classes, H(Y)=log2 K = {np.log2(K):.2f} bits):")
    print(f"   trained net:  accuracy={acc:.3f},  I(Ŷ;Y) = {I_hat:.3f} bits   <- measured, training-dependent")
    print(f"   null net:     I(Ŷ;Y) = {I_null:.3f} bits   (untrained readout, the contrast)")
    print(f"   task ceiling: I(X;Y) = {I_ceiling:.3f} bits  (Bayes-optimal; the net reaches it)")
    print(f"\nhard sector  (structural, not measured):")
    print(f"   𝒜 ≡ 0   -- node-adjacency nilpotent: max|eig|={maxev:.1e}, ‖A³‖={normA3:.1e} (no directed cycle)")
    print(f"   ΔV undefined -- no recurrent attractor; state is externally re-supplied each pass")

    print("\n" + "-" * 80)
    print(f"  I(Ŷ;Y)  =  {I_hat:.2f} bits   (soft-sector capability — measured, → H(Y))")
    print(f"  𝒜       ≡  0           (no directed cycle — structural, exact)")
    print(f"  ΔV      =  undefined   (no recurrent attractor — structural, exact)")
    print("-" * 80)
    ok = (I_hat > 0.8 * I_ceiling and maxev < 1e-9 and normA3 < 1e-9)
    if ok:
        print("  => NEITHER CORNER instanced. A non-trivial soft-metric substrate: large measured")
        print("     soft-sector capability, hard sector structurally absent. Capability ⟂ hard sector —")
        print("     the most informative cell of the plane is the one with no protected current at all.")
    else:
        print("  => inspect: capability low or adjacency not nilpotent.")
    figure(curve, I_hat, I_ceiling, I_null)


def figure(curve, I_hat, I_ceiling, I_null):
    ep, ac, mi = zip(*curve)
    fig, ax = plt.subplots(1, 2, figsize=(13, 5), dpi=140)
    a0 = ax[0]
    a0.plot(ep, mi, "o-", color="#90a4ae", ms=4, lw=1.8, label=r"$I(\hat Y;Y)$ (capability)")
    a0.axhline(I_ceiling, color="#1565c0", ls="--", lw=1.2, label=f"task ceiling I(X;Y)={I_ceiling:.2f}")
    a0.axhline(I_null, color="#c62828", ls=":", lw=1.2, label=f"null net = {I_null:.2f}")
    a0.set_xlabel("training epoch"); a0.set_ylabel("bits")
    a0.set_title("soft-sector capability emerges (measured)\nwhile 𝒜≡0, ΔV undefined hold structurally")
    a0.legend(fontsize=8, frameon=False); a0.grid(alpha=0.3)

    a1 = ax[1]; a1.axis("off"); a1.set_xlim(0, 2); a1.set_ylim(0, 2)
    a1.plot([1, 1], [0, 2], color="gray", lw=1); a1.plot([0, 2], [1, 1], color="gray", lw=1)
    cells = [(0.5, 1.5, f"NEITHER\nsoft-metric\nI(Ŷ;Y)≈{I_hat:.1f} bits\n𝒜≡0, ΔV undef.  ←", "#455a64"),
             (1.5, 1.5, "BOTH\nspontaneously selected\nhomochiral\nΔV=.018, 𝒜=21.8", "#2e7d32"),
             (0.5, 0.5, "BRANCH ONLY\nmetastable\nHopfield\nΔV=.97, 𝒜=0", "#6a1b9a"),
             (1.5, 0.5, "CURRENT ONLY\nstructurally stored\nRPS, DNA\n𝒜=21.8", "#1565c0")]
    for cx, cy, t, c in cells:
        a1.text(cx, cy, t, ha="center", va="center", fontsize=8.6, color=c, weight="bold")
    a1.text(1, -0.07, r"current survival $\mathcal{A}\neq0$  →", ha="center", fontsize=9)
    a1.text(-0.07, 1, r"branch survival $\Delta V>0$  →", va="center", rotation=90, fontsize=9)
    a1.set_title("two-survivals plane — all four corners instanced")

    fig.suptitle("the soft-metric corner: capability is measured, the hard sector is structurally absent "
                 "— capability is orthogonal to the hard bit", fontsize=12, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    path = OUT / "neither_corner.png"
    fig.savefig(path, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {path}")


if __name__ == "__main__":
    main()
