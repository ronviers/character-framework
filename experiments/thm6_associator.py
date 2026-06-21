r"""thm6_associator.py -- VERIFY the deformation-calculus Thm-6 derivation that came back from the
outbound channel (docs/research_prompt_thm6_bulk_series_derivation.md), before anything is folded
into the canon.  The three returned reports agree on a result that CORRECTS the framework's current
statement, so it is verified here by direct, exact computation -- not banked on the reports.

CLAIMS UNDER TEST (pre-registered numerical check from the prompt, §Task 6):
  The composition  X (X) Y = X - Gamma * inv(Y) * Gamma  (one-sided Schur complement of coupled
  driven-rotation OU triads M = -gamma I + g C) has a non-associative defect
        alpha(A,B,C) = (A(X)B)(X)C - A(X)(B(X)C)
  and the reports claim:
   (1) NO O(eps) term: c1 = 0.  The framework's bound ||alpha|| <~ eps*Sum|gamma| is LOOSE.
   (2) leading order is eps^2 (universal/binary coupling) or eps^4 (chain topology, Gamma_AC=0).
   (3) EVEN POWERS ONLY (alpha is even in the coupling kappa).
   (4) the leading coefficient is FORCED (matches the closed Neumann/Schur form, no fitting):
         universal:  alpha -> -Gamma inv(M_C) Gamma          + O(kappa^4)
         chain:      alpha -> Gamma inv(M_B) Gamma inv(M_C) Gamma inv(M_B) Gamma + O(kappa^6)
   (5) CONVERGENT (Kato resolvent analyticity); radius = eliminated-block gap closure
       (Neumann spectral radius rho(inv(M_B) Gamma inv(M_C) Gamma) -> 1), refining the D~kappa proxy.

Run (from character-framework root):  python experiments/thm6_associator.py
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

OUT = Path(__file__).resolve().parent / "thm6_associator.png"

C_CYC = np.array([[0.0, 1.0, -1.0],
                  [-1.0, 0.0, 1.0],
                  [1.0, -1.0, 0.0]])
G_SHAPE = np.array([[0.0, 1.0, 0.0],       # the O(1) coupling shape G~ (a directed cyclic pattern)
                    [0.0, 0.0, 1.0],
                    [1.0, 0.0, 0.0]])
GAMMA = 1.0
# distinct units, so the associator does not vanish by accident:
GA, GB, GC = 1.3, 2.0, 0.7
PHI = np.sqrt(3.0) * GB                      # a reference intra-unit circulation rate (for eps=kappa/Phi*)


def triad(g, gamma=GAMMA):
    return -gamma * np.eye(3) + g * C_CYC


def bind(X, Y, Gam):
    """one composition: Schur-eliminate Y from the X<->Y coupled pair.  EVEN in Gam (two factors)."""
    return X - Gam @ np.linalg.solve(Y, Gam)


def assoc_universal(MA, MB, MC, kappa):
    """(A(X)B)(X)C - A(X)(B(X)C) with the SAME coupling Gamma=kappa*G_SHAPE at each bind (binary op)."""
    Gam = kappa * G_SHAPE
    left = bind(bind(MA, MB, Gam), MC, Gam)          # = MA - Gam inv(MB) Gam - Gam inv(MC) Gam
    right = bind(MA, bind(MB, MC, Gam), Gam)          # = MA - Gam inv(MB - Gam inv(MC) Gam) Gam
    return left - right


def assoc_chain(MA, MB, MC, kappa):
    """chain topology A-B-C (Gamma_AC = 0): the A-end of (A(X)B) does not reach C, so the outer bind
    in the left-association couples to C with ZERO -> (A(X)B)(X)C = A(X)B."""
    Gam = kappa * G_SHAPE
    left = bind(MA, MB, Gam)                          # no coupling to C
    right = bind(MA, bind(MB, MC, Gam), Gam)          # B is modified by C
    return left - right


def lead_universal(MC, kappa):
    """forced leading term (universal): -Gamma inv(MC) Gamma."""
    Gam = kappa * G_SHAPE
    return -Gam @ np.linalg.solve(MC, Gam)


def lead_chain(MB, MC, kappa):
    """forced leading term (chain): Gamma inv(MB) Gamma inv(MC) Gamma inv(MB) Gamma."""
    Gam = kappa * G_SHAPE
    iB = np.linalg.inv(MB)
    iC = np.linalg.inv(MC)
    return Gam @ iB @ Gam @ iC @ Gam @ iB @ Gam


def fro(A):
    return float(np.linalg.norm(A, "fro"))


def slope(eps, y, lo=0.0, hi=np.inf):
    """log-log slope of y(eps), least squares, fitted only on the window lo<=eps<=hi (so we read the
    ASYMPTOTIC small-eps power, clear of higher orders at large eps and of the roundoff floor at tiny eps)."""
    m = (eps >= lo) & (eps <= hi)
    return float(np.polyfit(np.log(eps[m]), np.log(y[m]), 1)[0])


def main():
    MA, MB, MC = triad(GA), triad(GB), triad(GC)
    print("=" * 92)
    print("THM-6 ASSOCIATOR -- direct verification of the returned derivation (forced, not banked)")
    print("=" * 92)
    print(f"units: M = -{GAMMA} I + g C,  g = ({GA},{GB},{GC});  coupling shape G~ cyclic;  Phi*=sqrt3*gB={PHI:.3f}\n")

    kap = np.geomspace(2e-3, 0.25, 50) * PHI         # kappa sweep deep in the bulk
    eps = kap / PHI
    aU = np.array([fro(assoc_universal(MA, MB, MC, k)) for k in kap])
    aC = np.array([fro(assoc_chain(MA, MB, MC, k)) for k in kap])

    # ---- (1)+(2) leading power: c1=0, slope is 2 (universal) / 4 (chain), NOT 1 ----
    # fit the asymptotic small-eps power on a window clear of higher orders (large eps) and of the
    # machine-precision floor at tiny eps (the chain alpha ~ eps^4 hits ~1e-13 there).
    sU = slope(eps, aU, hi=0.03)
    sC = slope(eps, aC, lo=0.012, hi=0.08)
    print("-" * 92)
    print("[1,2] leading power of the associator (the framework bound claims O(eps^1) -- is it?)")
    print("-" * 92)
    print(f"   universal binary coupling:  ||alpha|| ~ eps^{sU:.3f}   -> leading O(eps^2), c1=0 (bound is LOOSE)")
    print(f"   chain topology (Gamma_AC=0): ||alpha|| ~ eps^{sC:.3f}   -> leading O(eps^4), c1=c2=c3=0")
    power_ok = abs(sU - 2.0) < 0.06 and abs(sC - 4.0) < 0.12

    # ---- (3) even powers only: alpha(kappa) = alpha(-kappa) exactly ----
    print("\n" + "-" * 92)
    print("[3] only EVEN powers: bind is even in kappa (two coupling factors) -> alpha(-kappa)=alpha(kappa)")
    print("-" * 92)
    even_res = max(fro(assoc_universal(MA, MB, MC, k) - assoc_universal(MA, MB, MC, -k)) for k in kap)
    print(f"   max||alpha(kappa) - alpha(-kappa)|| over the sweep = {even_res:.2e}  (exact -> even series, no odd terms)")
    even_ok = even_res < 1e-12

    # ---- (4) the leading coefficient is FORCED (matches the closed form, error -> 0 as kappa->0) ----
    print("\n" + "-" * 92)
    print("[4] leading coefficient FORCED, not fitted: ||alpha - alpha_lead_formula|| / ||alpha|| -> 0")
    print("-" * 92)
    relU = np.array([fro(assoc_universal(MA, MB, MC, k) - lead_universal(MC, k)) / fro(assoc_universal(MA, MB, MC, k))
                     for k in kap])
    relC = np.array([fro(assoc_chain(MA, MB, MC, k) - lead_chain(MB, MC, k)) / fro(assoc_chain(MA, MB, MC, k))
                     for k in kap])
    # the residual is the NEXT even order, so it scales as eps^2 relative to the leading term -- read the
    # slope on a window above the roundoff floor (the chain residual is a diff of ~1e-10 matrices at tiny eps).
    sresU = slope(eps, relU, hi=0.05)
    sresC = slope(eps, relC, lo=0.03, hi=0.15)
    print(f"   universal: derived leading = -Gamma inv(M_C) Gamma;  rel. residual ~ eps^{sresU:.3f} "
          f"-> next even order (rel.err at eps=0.05: {relU[np.argmin(abs(eps-0.05))]:.1e})")
    print(f"   chain:     derived leading = Gamma inv(M_B) Gamma inv(M_C) Gamma inv(M_B) Gamma; "
          f"rel. residual ~ eps^{sresC:.3f} (rel.err at eps=0.05: {relC[np.argmin(abs(eps-0.05))]:.1e})")
    # FORCED ⇔ the residual (alpha − derived-leading) is PURELY the next even order: slope≈2 relative,
    # vanishing as eps→0 (no leftover at leading order, no fitted constant).
    forced_ok = abs(sresU - 2) < 0.12 and abs(sresC - 2) < 0.2 and relU.min() < 1e-3

    # ---- (5) convergent; radius = eliminated-block gap closure (Neumann spectral radius -> 1) ----
    print("\n" + "-" * 92)
    print("[5] CONVERGENT (Kato); bulk boundary = eliminated-block gap closure (Neumann radius rho->1)")
    print("-" * 92)
    kap2 = np.geomspace(0.05, 6.0, 60)               # push kappa up toward / past the boundary
    rho = []
    trunc = []                                        # truncation error of the c2-only model, universal
    detB = []                                         # det of the eliminated block B - Gamma inv(MC) Gamma
    for k in kap2:
        Gam = k * G_SHAPE
        Mblk = MB - Gam @ np.linalg.solve(MC, Gam)    # the block that gets inverted in the right-association
        rho.append(float(max(abs(np.linalg.eigvals(np.linalg.solve(MB, Gam) @ np.linalg.solve(MC, Gam))))))
        detB.append(abs(float(np.linalg.det(Mblk))))
        a = assoc_universal(MA, MB, MC, k)
        trunc.append(fro(a - lead_universal(MC, k)) / max(fro(a), 1e-300))
    rho = np.array(rho); trunc = np.array(trunc); detB = np.array(detB)
    istar = int(np.argmin(np.abs(rho - 1.0)))
    kstar = float(kap2[istar])
    print(f"   Neumann spectral radius rho(inv(M_B) Gamma inv(M_C) Gamma) reaches 1 at kappa ~ {kstar:.2f} "
          f"(~ gamma={GAMMA}, eps ~ {kstar/PHI:.2f}) -- this IS the D~kappa threshold, derived not posited")
    print(f"   deep bulk (kappa={kap2[0]:.2f}): c2 truncation rel.err = {trunc[0]:.1e} (series accurate);  "
          f"at rho=1: rel.err = {trunc[istar]:.2f} (diverged), block det -> {detB[istar]:.1e}")
    print(f"   => series convergent for rho<1 (the 'bulk'); breakdown is the eliminated-block gap closure")
    conv_ok = (rho[0] < 1.0 < rho[-1]) and trunc[0] < 0.05 and trunc[istar] > 0.3 and abs(kstar - GAMMA) < 0.5 * GAMMA

    # ---- verdict ----
    print("\n" + "=" * 92)
    print("VERDICT")
    print("=" * 92)
    bar = [("[1,2] no O(eps) term; leading eps^2 (universal) / eps^4 (chain) -- framework bound LOOSE", power_ok),
           ("[3] even powers only (alpha even in kappa, exact)", even_ok),
           ("[4] leading coefficient FORCED (closed Neumann/Schur form, not fitted)", forced_ok),
           ("[5] convergent; bulk boundary = eliminated-block gap closure (rho->1)", conv_ok)]
    for label, ok in bar:
        print(f"   [{'PASS' if ok else 'FAIL'}]  {label}")
    if all(ok for _, ok in bar):
        print("\n  ==> CONFIRMED. The Thm-6 associator IS a genuine, CONVERGENT, FORCED series in eps=kappa/Phi*,")
        print("      CANONICAL reading: (X) is the MONOIDAL product C x C -> C (character.md S.Composition), so")
        print("      alpha is the monoidal-category associator -> UNIVERSAL coupling -> leading eps^2 = 1/D^2.")
        print("      (chain Gamma_AC=0 -> eps^4 is a non-generic fixed-graph special case, not the associator.)")
        print("      It starts at eps^2 (universal) / eps^4 (chain), EVEN POWERS ONLY -- the")
        print("      current O(eps) bound is a loose norm bound, not the true scaling. The 'smooth-merge closures'")
        print("      are the Neumann/Schur resolvent recursion: forced, no free constant (and the gl(3) drift /")
        print("      Sym+ noise type-closure is automatic). Imports: Kato analytic perturbation theory (resolvent")
        print("      analyticity -> convergence) + Gerstenhaber unobstructed deformation (the algebraic reading).")
        print("      => the gate 'the closures derived, not assumed' is MET, with the leading-order correction.")
    else:
        print("\n  ==> NOT confirmed as stated -- inspect before folding into the canon.")

    figure(eps, aU, aC, relU, kap2, rho, trunc, sU, sC)
    return sU, sC


def figure(eps, aU, aC, relU, kap2, rho, trunc, sU, sC):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.8), dpi=150)

    a0 = ax[0]
    a0.loglog(eps, aU, "o-", color="#c2185b", ms=4, lw=1.8, label=f"universal ⊗  (slope {sU:.2f})")
    a0.loglog(eps, aC, "s-", color="#1565c0", ms=4, lw=1.8, label=f"chain ⊗ (Γ_AC=0)  (slope {sC:.2f})")
    ref2 = aU[0] * (eps / eps[0]) ** 2
    ref1 = aU[0] * (eps / eps[0]) ** 1
    a0.loglog(eps, ref2, "k--", lw=1.0, label=r"$\propto\varepsilon^2$")
    a0.loglog(eps, ref1, color="gray", ls=":", lw=1.0, label=r"framework bound $\propto\varepsilon^1$ (loose)")
    a0.set_xlabel(r"$\varepsilon=\kappa/\Phi^*$"); a0.set_ylabel(r"$\|\alpha(A,B,C)\|_F$")
    a0.set_title("the associator starts at $\\varepsilon^2$ (not $\\varepsilon^1$):\n$c_1=0$, the bound is loose")
    a0.legend(fontsize=7.5, frameon=False); a0.grid(alpha=0.3, which="both")

    a1 = ax[1]
    a1.loglog(eps, relU, "o-", color="#6a1b9a", ms=4, lw=1.8)
    r2 = relU[5] * (eps / eps[5]) ** 2
    a1.loglog(eps, r2, "k--", lw=1.0, label=r"$\propto\varepsilon^2$ (next even order)")
    a1.set_xlabel(r"$\varepsilon=\kappa/\Phi^*$")
    a1.set_ylabel(r"$\|\alpha-\alpha_{\rm lead}\|/\|\alpha\|$")
    a1.set_title("leading coeff is FORCED (closed form):\nresidual $\\to0$ as the next even order")
    a1.legend(fontsize=8, frameon=False); a1.grid(alpha=0.3, which="both")

    a2 = ax[2]
    a2.semilogy(kap2, rho, color="#2e7d32", lw=2, label=r"Neumann radius $\rho$")
    a2.axhline(1.0, color="#c62828", ls="--", lw=1.2, label=r"$\rho=1$ (gap closes)")
    a2.semilogy(kap2, np.clip(trunc, 1e-6, None), color="#ef6c00", lw=1.6, label=r"$c_2$ truncation rel.err")
    a2.set_xlabel(r"coupling $\kappa$"); a2.set_ylabel(r"$\rho$  /  rel. error")
    a2.set_title("bulk boundary = eliminated-block\ngap closure ($\\rho\\to1$); series converges for $\\rho<1$")
    a2.set_ylim(1e-4, 1e2)
    a2.legend(fontsize=8, frameon=False); a2.grid(alpha=0.3, which="both")

    fig.suptitle("Thm-6 deformation calculus, verified: the composition associator is a genuine convergent "
                 "FORCED series in $\\varepsilon=\\kappa/\\Phi^*$ — starting at $\\varepsilon^2$ (even powers), "
                 "not $\\varepsilon^1$ (Kato resolvent analyticity; Gerstenhaber unobstructed deformation)",
                 fontsize=10.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
