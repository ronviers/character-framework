r"""
CROSS-SUBSTRATE check of the N=2 minting claim -- the colloidal Brownian gyrator.

Locks down generic (N=2) minting across distinct PHYSICAL substrates: from an electronic RC circuit
(gyrator_minting.py) to a FLUIDIC/OPTICAL one. If the SAME operator method recovers a colloid's
measured gyration from raw optical+fluidic parameters, the minting reading is fundamental thermodynamic
structure, not an artifact of one analog setup.

Real measured system: Argun, Soni, Dabelow, Bo, Pesce, Eichhorn, Volpe,
  "Experimental realization of a minimal microscopic heat engine," Phys. Rev. E 96, 052106 (2017);
  arXiv:1708.07197. A colloid in an elliptical optical trap; an electrophoretic-noise field makes the
  x-bath effectively hot -> a genuine NESS gyrator.

Measured parts (their text + Fig. 1-2):
  trap principal stiffnesses kx' = 1.63 pN/um, ky' = 0.86 pN/um (rotated by angle theta vs the bath axes);
  Ty = 292 K (water); Tx = 292 K (equilibrium) or 1750 K (hot); bead 2R = 1.98 um -> Stokes gamma = 6 pi eta R.

Operator (their Eq. 1, overdamped Langevin):  gamma rdot = -K r + xi,  <xi xi> = 2 gamma kB diag(Tx,Ty) delta,
  K = R(theta) diag(kx',ky') R(theta)^T  (lab frame).  => drift A = K/gamma,  diffusion Dd = (kB/gamma) diag(Tx,Ty).
  Stationary Sigma:  K Sigma + Sigma K^T = 2 kB diag(Tx,Ty)   (gamma CANCELS -> Sigma, torque are gamma-free).

THE MINTING READING (same as the electronic gyrator; pa:cycle-affinity, pa:ness-currents):
  * DB baseline two ways: theta=0 (trap aligned with baths -> no off-diagonal coupling) OR Tx=Ty
    (no drive) => zero current;
  * the MISALIGNMENT theta (off-diagonal stiffness K_xy = (kx'-ky')/2 sin2theta) mints the circulation
    under the thermal drive (Tx-Ty); maximal at theta=+-pi/4;
  * sign drive-/coupling-locked by sign(Tx-Ty)*sign(sin2theta); reciprocal (gamma, stiffness-magnitude)
    deformations cannot flip it;
  * SUSTAINED: as Tx->Ty the circulation collapses.

VALIDATION: the operator's torque M = <x dU/dy - y dU/dx> must reproduce Argun's exact closed form
  (their Eq. 7):  M = kB (Tx-Ty) (kx'-ky')/(kx'+ky') sin(2theta),  which they confirmed against measured
  trajectories (their Fig. 2). Two independently-derived results from the SAME measured parts.

Run (from character-framework root):  python experiments/colloidal_gyrator_crosscheck.py
"""
import sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

kB = 1.380649e-23
KXP = 1.63e-6                      # kx' = 1.63 pN/um -> 1.63e-6 N/m
KYP = 0.86e-6                      # ky' = 0.86 pN/um
TY = 292.0                         # water bath (K)
TX_HOT = 1750.0                    # effective hot bath (K)
ETA, RAD = 1.0e-3, 0.99e-6        # water viscosity (Pa s), bead radius (m)
GAMMA = 6 * np.pi * ETA * RAD     # Stokes friction (cancels from Sigma & torque; sets timescale only)
OUT = r"H:\character-framework\experiments\colloidal_gyrator_crosscheck.png"


def Kmat(theta, kx=KXP, ky=KYP):
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return R @ np.diag([kx, ky]) @ R.T


def sigma_of(K, Tx, Ty):
    """K Sigma + Sigma K^T = 2 kB diag(Tx,Ty)  (gamma-free)."""
    Q = 2 * kB * np.diag([Tx, Ty])
    M = np.kron(np.eye(2), K) + np.kron(K, np.eye(2))
    S = np.linalg.solve(M, Q.flatten(order="F")).reshape(2, 2, order="F")
    return 0.5 * (S + S.T)


def torque_operator(theta, Tx, Ty, kx=KXP, ky=KYP):
    """M = <x dU/dy - y dU/dx> = K_xy(Sxx - Syy) + (Kyy - Kxx) Sxy, from the OU stationary covariance."""
    K = Kmat(theta, kx, ky); S = sigma_of(K, Tx, Ty)
    return K[0, 1] * (S[0, 0] - S[1, 1]) + (K[1, 1] - K[0, 0]) * S[0, 1]


def torque_argun(theta, Tx, Ty):
    """Argun et al. Eq. 7 (their exact closed form, confirmed against measured trajectories)."""
    return kB * (Tx - Ty) * (KXP - KYP) / (KXP + KYP) * np.sin(2 * theta)


def main():
    print("CROSS-SUBSTRATE N=2 MINTING -- colloidal Brownian gyrator (Argun et al. 2017)\n")
    print(f"  measured parts: kx'={KXP*1e6:.2f} ky'={KYP*1e6:.2f} pN/um  Ty={TY:.0f}K  Tx(hot)={TX_HOT:.0f}K"
          f"  2R=1.98um  gamma={GAMMA:.3e} N s/m\n")
    pi4 = np.pi / 4
    TOL = 1e-30  # torque scale ~1e-21 J; baselines must be machine-zero relative to that

    # ---------- [MINTING] misalignment x drive ----------
    print("=" * 90 + "\n  [MINTING]  the circulation needs BOTH the misalignment (theta) AND the drive (dT)\n" + "=" * 90)
    M_aligned = torque_operator(0.0,  TX_HOT, TY)     # theta=0: trap aligned with baths -> no coupling
    M_noT     = torque_operator(pi4,  TY,     TY)     # Tx=Ty: no drive
    M_both    = torque_operator(pi4,  TX_HOT, TY)     # both on
    print(f"    theta=0   (aligned), Tx=1750K:   M = {M_aligned:+.3e} J   <- no off-diagonal coupling")
    print(f"    theta=pi/4, Tx=Ty=292K:          M = {M_noT:+.3e} J   <- no drive (equilibrium)")
    print(f"    theta=pi/4, Tx=1750K:            M = {M_both:+.3e} J   <- MINTED gyration")
    minted = abs(M_aligned) < TOL and abs(M_noT) < TOL and abs(M_both) > 1e3 * TOL
    print(f"    => misalignment mints the protected circulation under drive: {minted}")

    # ---------- [PROTECTION] drive-/coupling-locked sign ----------
    print("\n" + "=" * 90 + "\n  [PROTECTION]  sign(M) is locked to the three structural signs sign(dT)*sign(sin2theta)*sign(kx'-ky')\n" + "=" * 90)
    s_p = np.sign(torque_operator(+pi4, TX_HOT, TY))
    s_th = np.sign(torque_operator(-pi4, TX_HOT, TY))           # reverse the misalignment theta
    s_dT = np.sign(torque_operator(+pi4, TY, TX_HOT))           # reverse the drive (Tx<Ty)
    s_an = np.sign(torque_operator(+pi4, TX_HOT, TY, KYP, KXP)) # reverse the anisotropy (swap stiff axis)
    print(f"    reverse theta -> {s_th:+.0f}   reverse drive -> {s_dT:+.0f}   reverse anisotropy -> {s_an:+.0f}"
          f"   (each structural-sign reversal flips it: {s_p!=s_th and s_p!=s_dT and s_p!=s_an})")
    # deformation-robustness: scale the MAGNITUDES, hold the three structural signs (stiffer axis = x) fixed.
    rng = np.random.default_rng(0); flips = 0
    for _ in range(400):
        f = np.exp(0.5 * rng.standard_normal(2))
        kx, ky = max(KXP * f[0], KYP * f[1]), min(KXP * f[0], KYP * f[1])   # keep x the stiffer axis
        flips += int(np.sign(torque_operator(pi4, TX_HOT, TY, kx, ky)) != s_p)
    print(f"    magnitude deformations holding the structural signs (n=400): sign-flips = {flips}/400")
    protected = (s_p != s_th) and (s_p != s_dT) and (s_p != s_an) and flips == 0
    print(f"    => sign is locked to the drive x coupling structure, robust to magnitude deformation: {protected}")

    # ---------- [SUSTAINED] collapse as the drive is removed ----------
    print("\n" + "=" * 90 + "\n  [SUSTAINED]  remove the drive (Tx -> Ty) -> circulation collapses\n" + "=" * 90)
    for Tx in (1750.0, 1000.0, 500.0, 300.0, 292.0):
        print(f"    Tx={Tx:7.1f}K (dT={Tx-TY:+7.1f}K):  M = {torque_operator(pi4, Tx, TY):+.3e} J")
    collapses = abs(torque_operator(pi4, 292.001, TY)) < abs(M_both) * 1e-3
    print(f"    => collapses to zero as dT->0: {collapses}")

    # ---------- [VALIDATION] reproduce Argun's exact measured-and-confirmed torque (their Eq. 7) ----------
    print("\n" + "=" * 90 + "\n  [VALIDATION]  operator torque vs Argun et al. Eq. 7 (their measured-confirmed closed form)\n" + "=" * 90)
    th = np.linspace(-np.pi / 2, np.pi / 2, 13)
    M_op = np.array([torque_operator(t, TX_HOT, TY) for t in th])
    M_ar = np.array([torque_argun(t, TX_HOT, TY) for t in th])
    rel = np.max(np.abs(M_op - M_ar)) / np.max(np.abs(M_ar))
    print(f"    max relative error operator-vs-Argun over theta in [-pi/2, pi/2]: {rel:.2e}")
    ipk = int(np.argmax(np.abs(M_op)))
    print(f"    peak |M| at theta = {np.degrees(th[ipk]):+.0f} deg (Argun: +-45 deg);  "
          f"M(pi/4, Tx=1750K) = {M_both:.3e} J = {M_both/1e-18:.4f} pN*um")
    valid = rel < 1e-9 and abs(abs(th[ipk]) - pi4) < 1e-6

    print("\n" + "=" * 90 + "\n  VERDICT\n" + "=" * 90)
    if minted and protected and collapses and valid:
        print("  PASS -- N=2 minting reproduced on a SECOND, distinct physical substrate (fluidic/optical).")
        print("  The same OU operator method, fed the colloid's raw measured optics+fluidics, recovers")
        print(f"  Argun et al.'s exact measured-confirmed torque (Eq. 7) to rel. error {rel:.1e}: misalignment")
        print("  mints a protected gyration under the thermal drive, from a detailed-balanced baseline,")
        print("  sign-locked and collapsing as dT->0. Generic (N=2) minting now holds across an electronic")
        print("  circuit AND a colloidal heat engine -- thermodynamic structure, not one analog setup.")
        print("  Honest scope: still a 2-mode current-only NESS, not a >=3 frustrated cycle.")
    else:
        print(f"  NOT clean: minted={minted} protected={protected} collapses={collapses} valid={valid}")

    figure(th, M_op, M_ar)


def figure(th, M_op, M_ar):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.8), dpi=150)
    pj = 1e21  # J -> zJ for readable axes

    # panel 1: operator torque on Argun's exact curve vs theta (their Fig 2a structure)
    tt = np.linspace(-np.pi / 2, np.pi / 2, 200)
    ax[0].plot(np.degrees(tt), torque_argun(tt, TX_HOT, TY) * pj, "-", color="k", lw=1.5,
               label="Argun Eq. 7 (measured-confirmed)")
    ax[0].plot(np.degrees(th), M_op * pj, "o", color="#c62828", ms=7, label="our OU operator")
    ax[0].axhline(0, color="gray", lw=0.8); ax[0].axvline(0, color="gray", lw=0.8)
    ax[0].set_xlabel(r"misalignment $\theta$ (deg)"); ax[0].set_ylabel("torque $M$ (zJ)")
    ax[0].set_title("VALIDATION: operator recovers the\nmeasured-confirmed torque (zero at $\\theta{=}0$)")
    ax[0].legend(fontsize=8, frameon=False); ax[0].grid(alpha=0.3)

    # panel 2: minting + collapse -- M vs dT at theta=pi/4
    dT = np.linspace(0, TX_HOT - TY, 12)
    Md = np.array([torque_operator(np.pi / 4, TY + d, TY) for d in dT])
    ax[1].plot(dT, Md * pj, "o-", color="#1565c0", lw=1.8)
    ax[1].axhline(0, color="gray", lw=0.8); ax[1].axvline(0, color="gray", lw=0.8)
    ax[1].set_xlabel(r"$\Delta T = T_x - T_y$ (K)"); ax[1].set_ylabel("torque $M$ (zJ)")
    ax[1].set_title(r"MINTING + collapse: $M \propto \Delta T$,""\n"r"zero at $T_x{=}T_y$ ($\theta{=}\pi/4$)")
    ax[1].grid(alpha=0.3)

    # panel 3: the minted probability current at the measured operating point
    K = Kmat(np.pi / 4); S = sigma_of(K, TX_HOT, TY)
    A = K / GAMMA; Dd = (kB / GAMMA) * np.diag([TX_HOT, TY]); Om = Dd @ np.linalg.inv(S) - A
    sd = np.sqrt(np.diag(S))
    g = np.linspace(-3, 3, 22); X, Y = np.meshgrid(g * sd[0], g * sd[1])
    Ux = Om[0, 0] * X + Om[0, 1] * Y; Uy = Om[1, 0] * X + Om[1, 1] * Y
    ax[2].streamplot(X / sd[0], Y / sd[1], Ux, Uy, color="#6a1b9a", density=1.1, linewidth=0.8)
    thc = np.linspace(0, 2 * np.pi, 100)
    ax[2].plot(np.cos(thc), np.sin(thc), color="k", lw=0.8, alpha=0.5)
    ax[2].set_xlabel(r"$x/\sigma_x$"); ax[2].set_ylabel(r"$y/\sigma_y$")
    ax[2].set_title("the minted circulation\n(probability current, $\\theta{=}\\pi/4$, $T_x{=}1750$ K)")
    ax[2].set_aspect("equal"); ax[2].grid(alpha=0.3)

    fig.suptitle("Cross-substrate N=2 minting: the colloidal Brownian gyrator "
                 "(Argun et al., Phys. Rev. E 96, 052106, 2017)", fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
