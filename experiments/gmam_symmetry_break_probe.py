r"""gmam_symmetry_break_probe.py -- the SUFFICIENT test for symmetry-protection of current⊥escape.

gmam_orthogonality_sweep.py showed cos(J,e_u)≈0 survives a symmetry-PRESERVING move (the μ-sweep) -- a
necessary check. This is the converse, sufficient one: turn on a symmetry-BREAKING perturbation δ that
mixes the within-group cyclic sector into the between-group breaking sector, and watch the orthogonality
break. If cos(J,e_u) is machine-zero at δ=0 and grows ∝ δ, the orthogonality is *exactly the symmetry*
(zero iff the symmetry holds) -- not an accident that merely happens to persist.

Perturbation: the within-group self-saturation 1·L_i -> (1+δ·d_i)·L_i with d=[1,-1,0] (traceless, breaks
the within-group Z3/S3 permutation symmetry; applied to both groups). At δ=0 this is exactly the
homochiral field. The saddle is re-found by Newton (it is a fixed point regardless of stability).
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
F0, MU, AB = 1.0, 1.6, 1.5
OFF, ON = (0.75, 0.75), (0.5, 1.0)
D = np.array([1.0, -1.0, 0.0])                          # within-group Z3-breaking direction (traceless)

V_BRK = np.array([1, 1, 1, -1, -1, -1.]) / np.sqrt(6)
CYC = []
for g in (slice(0, 3), slice(3, 6)):
    for raw in (np.array([1., -.5, -.5]), np.array([0., np.sqrt(3) / 2, -np.sqrt(3) / 2])):
        v = np.zeros(6); v[g] = raw; CYC.append(v / np.linalg.norm(v))


def field_broken(X, a, b, delta, mu=MU, F=F0):
    L, R = X[:, :3], X[:, 3:]
    SL = L.sum(1, keepdims=True); SR = R.sum(1, keepdims=True)
    selfL = (1.0 + delta * D) * L
    selfR = (1.0 + delta * D) * R
    dL = L * (F - (selfL + a * np.roll(L, -1, 1) + b * np.roll(L, 1, 1)) - mu * SR)
    dR = R * (F - (selfR + b * np.roll(R, -1, 1) + a * np.roll(R, 1, 1)) - mu * SL)
    return np.concatenate([dL, dR], axis=1)


def b1(x, a, b, delta):
    return field_broken(x[None, :], a, b, delta)[0]


def jac(x, a, b, delta, h=1e-6):
    J = np.zeros((6, 6))
    for k in range(6):
        e = np.zeros(6); e[k] = h
        J[:, k] = (b1(x + e, a, b, delta) - b1(x - e, a, b, delta)) / (2 * h)
    return J


def find_saddle(delta, x0):
    x = x0.copy()
    for _ in range(80):
        F = b1(x, *OFF, delta); J = jac(x, *OFF, delta)
        dx = np.linalg.solve(J, -F)
        x = x + dx
        if np.linalg.norm(dx) < 1e-13:
            break
    return x


def unstable(Jm):
    w, V = np.linalg.eig(Jm); w = w.real; V = V.real
    iu = int(np.argmax(w)); eu = V[:, iu] / np.linalg.norm(V[:, iu])
    return w[iu], (eu if eu[0] >= 0 else -eu)


def probe(delta, x0):
    xS = find_saddle(delta, x0)
    lu, eu = unstable(jac(xS, *OFF, delta))
    cosmax = 0.0
    for amp in (0.02, 0.05):
        for c in CYC:
            Jc = b1(xS + amp * c, *ON, delta) - b1(xS + amp * c, *OFF, delta)
            if np.linalg.norm(Jc) > 1e-12:
                cosmax = max(cosmax, abs(eu @ Jc) / np.linalg.norm(Jc))
    cyc = float(np.sqrt(sum((eu @ c) ** 2 for c in CYC)))
    return dict(delta=delta, xS=xS, lu=lu, cosmax=cosmax, cyc=cyc, brk=abs(eu @ V_BRK))


def main():
    m0 = F0 / (1.0 + AB + 3.0 * MU)
    x0 = np.full(6, m0)
    deltas = np.array([0.0, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1])
    print("=" * 84)
    print("symmetry-break probe -- does current⊥escape vanish EXACTLY with the symmetry?")
    print("   perturbation: within-group self 1·x_i -> (1+δ·[1,-1,0])·x_i  (breaks within-group Z3)")
    print("=" * 84)
    print(f"   {'δ':>8} {'λ_u':>9} {'|cos(J,e_u)|':>13} {'e_u·cyclic':>11} {'e_u·brk':>9}")
    rows = []
    for d in deltas:
        r = probe(d, x0); rows.append(r)
        print(f"   {d:>8.0e} {r['lu']:>9.4f} {r['cosmax']:>13.3e} {r['cyc']:>11.3e} {r['brk']:>9.6f}")

    # slope: cos ~ δ^p ?  fit on the δ>0 points
    dd = np.array([r["delta"] for r in rows[1:]])
    cc = np.array([r["cosmax"] for r in rows[1:]])
    p = np.polyfit(np.log(dd), np.log(np.maximum(cc, 1e-300)), 1)[0]
    print("\n" + "-" * 84)
    print(f"   δ=0: |cos|={rows[0]['cosmax']:.2e} (machine-zero)   δ>0 scaling: |cos(J,e_u)| ~ δ^{p:.2f}")
    verdict = ("SYMMETRY-PROTECTED (orthogonality vanishes exactly with the symmetry; ~linear in the break)"
               if rows[0]["cosmax"] < 1e-10 and 0.7 < p < 1.3 else "ambiguous")
    print(f"   VERDICT: {verdict}")
    print("-" * 84)

    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    ax.loglog(dd, cc, "-o", color="#d62728", label="|cos(J, e_u)|")
    ax.loglog(dd, cc[0] * (dd / dd[0]), "--", color="0.6", label="∝ δ (slope 1)")
    ax.set_xlabel("symmetry-breaking δ"); ax.set_ylabel("|cos(J, e_u)|")
    ax.set_title(f"current⊥escape breaks EXACTLY with the symmetry  (|cos| ~ δ^{p:.2f}; "
                 f"{rows[0]['cosmax']:.0e} at δ=0)")
    ax.legend(); fig.tight_layout()
    fig.savefig(OUT / "gmam_symmetry_break.png", dpi=140); plt.close(fig)
    print(f"\n   figure -> gmam_symmetry_break.png")


if __name__ == "__main__":
    main()
