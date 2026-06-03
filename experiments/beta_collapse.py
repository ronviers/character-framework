"""beta_collapse.py -- the memory-exponent transport-law falsifier.

character.md (S The memory exponent) and character_receipts.md (S Fractional
memory / transport law) make a single falsifiable claim:

    one memory exponent beta governs THREE registers through fixed maps --
        FDR-aging / memory-kernel exponent    alpha_s = beta_mem = beta
        heavy-traffic queue-tail exponent     g(beta) = beta/(2-beta) | 1/beta
    -- numerically coincident ONLY at beta = 1.
    Falsify: two registers fail to collapse onto a common beta.

This script swings that blade on the one substrate where a single parameter
fixes both registers through DIFFERENT functionals: the Norros fractional-
Brownian-motion queue. Fractional Gaussian noise of Hurst exponent H has

    beta = 2 - 2H        (interior H in (1/2, 1) -> beta in (0, 1))

and that same beta appears, by two independent routes, as:

  Register 1 -- MEMORY KERNEL.  fGn autocovariance gamma(k) ~ k^(2H-2),
      i.e. ~ k^(-beta).  A two-point correlation.  -> beta_mem from the
      log-log slope of gamma(k).

  Register 2 -- QUEUE TAIL.  Feed the fGn as arrivals into a constant-drain
      server (Loynes: stationary backlog Q = sup_n S_n over the negative-
      drift partial sums).  Norros (1994): P(Q > x) ~ exp(-eta x^(2-2H)),
      a Weibull tail with stretch exponent 2-2H = beta.  A supremum
      functional -- NOT the same statistic as gamma(k), and the equality of
      the two exponents is a THEOREM, not a definition (so the registers are
      not "tied definitionally", which would make the falsifier malformed).

Collapse test: beta_mem and beta_queue must both equal 2-2H across the
interior. If they track the diagonal -> the transport law survives. If they
are mutually inconsistent -> the central testable claim is falsified.

Pure direct simulation: no fitting to MPA, no inversion pipeline.
"""
from __future__ import annotations

import math
import sys
import time

import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


# --------------------------------------------------------------------------
# fractional Gaussian noise -- Davies-Harte circulant embedding (vectorized
# over realizations). Lifted from mpa-central fbm primitive, batched.
# --------------------------------------------------------------------------
def fgn(H: float, n: int, n_real: int, rng: np.random.Generator) -> np.ndarray:
    """(n_real, n) fractional Gaussian noise, unit variance, Hurst H."""
    k = np.arange(0, n + 1)
    gamma = 0.5 * (np.abs(k - 1) ** (2 * H) - 2 * np.abs(k) ** (2 * H)
                   + np.abs(k + 1) ** (2 * H))
    c = np.concatenate([gamma, gamma[1:n][::-1]])      # circulant first row, len 2n
    m = c.size
    lam = np.maximum(np.fft.fft(c).real, 0.0)          # eigenvalues (>=0 for fGn embedding)
    sqrt_lam = np.sqrt(lam)
    Z = (rng.standard_normal((n_real, m)) + 1j * rng.standard_normal((n_real, m))) / math.sqrt(2.0)
    x = np.fft.fft(sqrt_lam[None, :] * Z, axis=1).real / math.sqrt(m)
    return x[:, :n]


# --------------------------------------------------------------------------
# Register 1 -- memory-kernel exponent from the autocovariance slope.
# --------------------------------------------------------------------------
def beta_from_memory(H, n_real, n_len, rng, k_lo=8, k_hi=None):
    """Memory-kernel exponent two independent ways on the SAME fGn:
      (a) autocovariance tail  gamma(k) ~ k^(2H-2) = k^(-beta)
      (b) low-freq spectrum    S(f) ~ |f|^(1-2H) = |f|^(beta-1)
    fGn is zero-mean by construction -- do NOT subtract the sample mean
    (that strips the low-frequency power carrying the LRD exponent).
    Returns (beta_acov, beta_spec, diagnostics).
    """
    if k_hi is None:
        k_hi = n_len // 8
    x = fgn(H, n_len, n_real, rng)                     # already zero-mean

    # (a) unbiased linear autocovariance via zero-padded FFT, ensemble mean.
    nfft = 1 << (2 * n_len - 1).bit_length()
    F = np.fft.rfft(x, n=nfft, axis=1)
    r = np.fft.irfft(np.abs(F) ** 2, n=nfft, axis=1)[:, :n_len]
    counts = (n_len - np.arange(n_len)).astype(np.float64)   # n-k products at lag k
    g = (r / counts).mean(axis=0)                      # unbiased gamma(k)
    k = np.arange(n_len)
    sel = (k >= k_lo) & (k <= k_hi) & (g > 0)
    slope_a, _ = np.polyfit(np.log(k[sel]), np.log(g[sel]), 1)   # = 2H-2 = -beta
    beta_acov = -slope_a

    # (b) ensemble-averaged periodogram; low-frequency slope = 1-2H = beta-1.
    P = (np.abs(np.fft.rfft(x, axis=1)) ** 2).mean(axis=0) / n_len
    freq = np.fft.rfftfreq(n_len)
    fsel = (freq > 0) & (freq <= 0.05)                 # low-frequency band only
    slope_s, _ = np.polyfit(np.log(freq[fsel]), np.log(P[fsel]), 1)  # = 1-2H
    beta_spec = slope_s + 1.0

    return beta_acov, beta_spec, (k[sel], g[sel])


# --------------------------------------------------------------------------
# Register 2 -- queue-tail Weibull stretch exponent (Loynes / Norros).
# --------------------------------------------------------------------------
def beta_from_queue(H, n_blocks, block_len, drain, rng, batch=2500):
    """Stationary backlog Q = max(0, sup_n S_n), S_n = cumsum(fGn - drain).
    Each block -> one stationary sample (Loynes). Fit P(Q>x) ~ exp(-eta x^beta).
    Blocks are generated in batches to bound memory.
    """
    Qs_all = []
    done = 0
    while done < n_blocks:
        b = min(batch, n_blocks - done)
        x = fgn(H, block_len, b, rng)                  # already zero-mean
        S = np.cumsum(x - drain, axis=1)               # negative-drift partial sums
        q = np.maximum(0.0, S.max(axis=1))             # one stationary sample / block
        Qs_all.append(q)
        done += b
    Q = np.concatenate(Qs_all)
    Q = Q[Q > 0]
    Qs = np.sort(Q)
    # survival P(Q > x) on the body of the tail (avoid bulk + few-sample extreme)
    surv = 1.0 - (np.arange(1, Qs.size + 1) - 0.5) / Qs.size
    lo, hi = np.quantile(Qs, 0.55), np.quantile(Qs, 0.992)
    sel = (Qs >= lo) & (Qs <= hi) & (surv > 0)
    lx = np.log(Qs[sel])
    ly = np.log(-np.log(surv[sel]))                    # log(-log P) ~ beta log x + const
    slope, _ = np.polyfit(lx, ly, 1)                   # slope = stretch exponent = beta
    return slope, (Qs[sel], surv[sel])


# --------------------------------------------------------------------------
def plot_collapse(rows, queue_diag, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:                              # noqa: BLE001
        print(f"  (plot skipped: {e})")
        return
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))

    # Panel 1 -- the collapse: measured beta vs true beta, both registers.
    bt = rows[:, 1]
    ax1.plot([0, 1], [0, 1], "k--", lw=1, alpha=0.6, label="$\\beta_{mem}=\\beta_{queue}$")
    ax1.plot(bt, rows[:, 3], "o-", ms=8, label="memory kernel (spectral)")
    ax1.plot(bt, rows[:, 4], "s-", ms=8, label="queue tail (Norros)")
    ax1.set_xlabel("$\\beta = 2-2H$ (set by Hurst exponent)")
    ax1.set_ylabel("recovered $\\beta$")
    ax1.set_title("Two registers, one $\\beta$")
    ax1.legend(frameon=False, fontsize=9)
    ax1.set_aspect("equal", "box")

    # Panel 2 -- the queue-tail Weibull fits (the independent register).
    for (H, Qs, surv, b) in queue_diag:
        xr = Qs ** b
        ax2.plot(xr, surv, ".", ms=3, alpha=0.5)
        ax2.plot(xr, np.exp(-np.polyfit(xr, -np.log(surv), 1)[0] * xr
                            - np.polyfit(xr, -np.log(surv), 1)[1]),
                 "-", lw=1.2, label=f"H={H:.2f}, $\\beta_q$={b:.2f}")
    ax2.set_yscale("log")
    ax2.set_xlabel("$x^{\\beta_{queue}}$  (Weibull-rectified backlog)")
    ax2.set_ylabel("$P(Q > x)$")
    ax2.set_title("Queue tail $\\sim \\exp(-\\eta\\,x^{\\beta})$")
    ax2.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    print(f"  figure -> {path}")


def run(H_list, *, mem_real, mem_len, q_blocks, q_len, drain, seed=20260603,
        plot_path=None):
    print(f"beta-collapse  |  fBm-queue  |  registers: memory-kernel vs queue-tail")
    print(f"  memory:  {mem_real} reals x {mem_len} len")
    print(f"  queue :  {q_blocks} blocks x {q_len} len, drain={drain}")
    print(f"  {'H':>5} {'beta=2-2H':>10} {'b_acov':>8} {'b_spec':>8}"
          f" {'b_queue':>9}  {'acov err':>8} {'spec err':>8} {'q err':>8}")
    rows = []
    queue_diag = []
    for H in H_list:
        rng = np.random.default_rng(seed + int(round(H * 1000)))
        b_true = 2.0 - 2.0 * H
        b_acov, b_spec, _ = beta_from_memory(H, mem_real, mem_len, rng)
        b_q, (Qs, surv) = beta_from_queue(H, q_blocks, q_len, drain, rng)
        rows.append((H, b_true, b_acov, b_spec, b_q))
        queue_diag.append((H, Qs, surv, b_q))
        print(f"  {H:>5.2f} {b_true:>10.3f} {b_acov:>8.3f} {b_spec:>8.3f}"
              f" {b_q:>9.3f}  {b_acov - b_true:>+8.3f} {b_spec - b_true:>+8.3f}"
              f" {b_q - b_true:>+8.3f}")
    rows = np.array(rows)
    # The collapse test: do the memory register (spectral) and the queue
    # register -- two different functionals -- agree on a common beta?
    inter = np.abs(rows[:, 3] - rows[:, 4])
    print(f"\n  inter-register |beta_spec - beta_queue|: "
          f"max {inter.max():.3f}, mean {inter.mean():.3f}")
    if plot_path:
        plot_collapse(rows, queue_diag, plot_path)
    return rows


if __name__ == "__main__":
    if "--converge" in sys.argv:
        # Demonstrate the queue register is finite-block-limited at deep LRD:
        # beta_queue(H) must descend toward 2-2H as block length grows.
        H = 0.90
        b_true = 2.0 - 2.0 * H
        print(f"queue-register convergence  |  H={H}  beta_true={b_true}\n")
        print(f"  {'block_len':>10} {'n_blocks':>9} {'beta_queue':>11} {'err':>8}")
        for block_len, n_blocks in [(16384, 8000), (32768, 8000),
                                    (65536, 8000), (131072, 6000)]:
            rng = np.random.default_rng(424242 + block_len)
            t0 = time.time()
            b_q, _ = beta_from_queue(H, n_blocks, block_len, 0.25, rng, batch=64)
            print(f"  {block_len:>10} {n_blocks:>9} {b_q:>11.3f} {b_q - b_true:>+8.3f}"
                  f"   ({time.time() - t0:.0f}s)")
        sys.exit(0)

    probe = "--full" not in sys.argv
    plot_path = str(__import__("pathlib").Path(__file__).with_name("beta_collapse.png"))
    if probe:
        cfg = dict(mem_real=96, mem_len=8192, q_blocks=4000, q_len=4096, drain=0.30)
        H_list = [0.6, 0.7, 0.8]
        print("[PROBE] small config; pass --full to scale\n")
    else:
        cfg = dict(mem_real=256, mem_len=16384, q_blocks=30000, q_len=16384, drain=0.25)
        H_list = [0.6, 0.7, 0.8, 0.9]
        print("[FULL]\n")
    t0 = time.time()
    rows = run(H_list, **cfg, plot_path=plot_path)
    print(f"\nelapsed: {time.time() - t0:.1f}s")
