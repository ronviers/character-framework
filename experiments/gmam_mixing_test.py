r"""gmam_mixing_test.py -- the selection-rule test: does irrep-MIXING let the current reach the barrier?

The transverse-decomposition reading says the protected current is barred from ΔV only while it stays
transverse to the escape mode (different irreps). gmam_symmetry_break_probe.py showed a within-group Z3
break δ rotates the escape mode into the cyclic sector ∝ δ -- i.e. δ MIXES the irreps. So the prediction
(the Maier-Stein dichotomy, realized inside the substrate):
    ΔŜ_H(δ) = Ŝ(a=b) − Ŝ(a≠b)  is ≈0 at δ=0 (transverse, barrier-invariant) and TURNS ON as δ grows
    (the current acquires a ∇V-component, the instanton bows out, the barrier drops).
If ΔŜ stays flat even at large mixing, the protection is stronger than the selection rule -- also informative.

Same gMAM as the rest (validated on Maier-Stein). Saddle by Newton, attractor by settling, on field_broken.
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
from gmam_symmetry_break_probe import field_broken, CYC, V_BRK, MU, F0, AB
from gmam_current_aids import a_inv, gmam_minimize, initial_path, within_group_spread

OUT = Path(__file__).resolve().parent
OFF, ON = (0.75, 0.75), (0.5, 1.0)


def jac(x, a, b, delta, h=1e-6):
    J = np.zeros((6, 6))
    for k in range(6):
        e = np.zeros(6); e[k] = h
        J[:, k] = (field_broken((x + e)[None, :], a, b, delta)[0]
                   - field_broken((x - e)[None, :], a, b, delta)[0]) / (2 * h)
    return J


def saddle_newton(a, b, delta, x0):
    x = x0.copy()
    for _ in range(100):
        Fv = field_broken(x[None, :], a, b, delta)[0]
        dx = np.linalg.solve(jac(x, a, b, delta), -Fv)
        x = x + dx
        if np.linalg.norm(dx) < 1e-12:
            break
    return x


def attractor(a, b, delta, bias=0.05, T=1500.0, dt=0.01):
    X = np.clip(np.array([1 + bias, 1 + bias, 1 + bias, 1 - bias, 1 - bias, 1 - bias]) / 3.0, 1e-12, None)
    for _ in range(int(T / dt)):
        X = np.clip(X + field_broken(X[None, :], a, b, delta)[0] * dt, 1e-12, None)
    return X


def escape_cyclic(delta, xS):
    """how much the escape mode has rotated into the cyclic sector at this δ (the mixing)."""
    w, V = np.linalg.eig(jac(xS, *OFF, delta)); w = w.real; V = V.real
    eu = V[:, int(np.argmax(w))]; eu = eu / np.linalg.norm(eu)
    return float(np.sqrt(sum((eu @ c) ** 2 for c in CYC)))


def gmam_S(a, b, delta, x0):
    xS = saddle_newton(a, b, delta, x0)
    xA = attractor(a, b, delta)
    drift = lambda X: field_broken(X, a, b, delta)                  # noqa: E731
    ainv = lambda X: a_inv(X, "demographic", 1e-4)                  # noqa: E731
    path, S, _ = gmam_minimize(initial_path(xA, xS), drift, ainv, clip_pos=True,
                               n_iter=40000, dtau=5e-4, reparam_every=100, mom=0.95)
    return S, within_group_spread(path), xS


def main():
    m0 = F0 / (1.0 + AB + 3.0 * MU); x0 = np.full(6, m0)
    deltas = [0.0, 0.01, 0.03, 0.1, 0.3]
    print("=" * 90)
    print("mixing test -- does ΔŜ_H turn on as the irrep-break δ mixes the current into the escape mode?")
    print("   prediction (selection rule): ΔŜ≈0 at δ=0 (transverse), grows with δ (Maier-Stein boundary).")
    print("=" * 90)
    print(f"   {'δ':>6} {'e_u·cyc(mix)':>13} {'Ŝ(a=b)':>9} {'Ŝ(a≠b)':>9} {'ΔŜ':>9} {'sp_off':>7} {'sp_on':>7}")
    rows = []
    for d in deltas:
        mix = escape_cyclic(d, saddle_newton(*OFF, d, x0))
        Soff, spoff, _ = gmam_S(*OFF, d, x0)
        Son, spon, _ = gmam_S(*ON, d, x0)
        rows.append(dict(d=d, mix=mix, Soff=Soff, Son=Son, dS=Soff - Son, spoff=spoff, spon=spon))
        print(f"   {d:>6.2f} {mix:>13.3e} {Soff:>9.4f} {Son:>9.4f} {Soff-Son:>+9.4f} "
              f"{spoff:>7.4f} {spon:>7.4f}")

    dS0 = abs(rows[0]["dS"]); dSmax = rows[-1]["dS"]
    floor = 0.005                                                   # the gMAM Tier-1 noise floor at this regime
    turns_on = (dS0 < floor) and (dSmax > 3 * floor)
    print("\n" + "-" * 90)
    print(f"   ΔŜ(δ=0)={rows[0]['dS']:+.4f} (≈0, transverse)   ΔŜ(δ={deltas[-1]})={dSmax:+.4f}")
    print(f"   VERDICT: {'SELECTION RULE CONFIRMED -- mixing the irreps turns ON a barrier effect' if turns_on else 'no clear turn-on -- protection survives mixing (stronger than the selection rule)'}")
    print(f"   (interpretation: in isolation the current is barred from ΔV; the irrep-mix is the cross-rule /")
    print(f"    Maier-Stein boundary where the instanton can bow out and harvest the now-aligned current.)")
    print("-" * 90)

    d = np.array([r["d"] for r in rows]); dS = np.array([r["dS"] for r in rows])
    mix = np.array([r["mix"] for r in rows])
    fig, ax = plt.subplots(figsize=(8, 5.3))
    ax.plot(mix, dS, "-o", color="#d62728", lw=2, label="ΔŜ_H (barrier drop)")
    ax.axhline(0, color="0.6", lw=0.8); ax.axhline(floor, color="0.7", ls=":", lw=1)
    ax.axhline(-floor, color="0.7", ls=":", lw=1, label="±Tier-1 noise floor")
    for r in rows:
        ax.annotate(f"δ={r['d']}", (r["mix"], r["dS"]), textcoords="offset points", xytext=(5, 5), fontsize=8)
    ax.set_xlabel("escape-mode mixing into the cyclic sector  (e_u·cyclic)")
    ax.set_ylabel("ΔŜ_H = Ŝ(a=b) − Ŝ(a≠b)")
    ax.set_title("the current reaches the barrier only when the irreps mix\n"
                 "(transverse at δ=0 → barrier-invariant; mixed → Maier-Stein bow-out)")
    ax.legend(); fig.tight_layout()
    fig.savefig(OUT / "gmam_mixing_test.png", dpi=140); plt.close(fig)
    print(f"\n   figure -> gmam_mixing_test.png")


if __name__ == "__main__":
    main()
