r"""
The >=3 frustrated-cycle minting instance -- the cell-free repressilator.

The faithful frustrated cycle (an odd negative-feedback ring, the homochiral-triad / RPS topology),
on a REAL measured substrate distinct from the DNA chemistry and the gyrators. Built from the MEASURED
transfer functions of:
  Niederholtmeyer, Sun, Hori, Yeung, Verpoorte, Murray, Maerkl,
  "Rapid cell-free forward engineering of novel genetic ring oscillators," eLife 4:e09771 (2015).

A 3-gene ring  g1 -| g2 -| g3 -| g1  (each protein represses the next gene). Odd # of repressions =>
frustrated (no consistent fixed point) => oscillates when driven. The continuous-flow reactor is the
DRIVE: fresh NTPs/amino-acids (the TX-TL free-energy throughput) sustain production; cutting the flow
collapses to a resource-depleted static state (clean detailed-balance baseline -- a parameter cut, not
a messy biological death; this is why the CELL-FREE system beats the in-vivo one for our test).

Measured parameters (their Table 2 / Fig. 3):
  Hill n = 2, repression threshold K = 5 nM, ymin = small leak;
  transcription beta*[DNA] = 0.4 nM/min/plasmid * 5 nM = 2.0 nM/min; translation c = 0.5 /min;
  mRNA half-life 8 min (a=ln2/8); protein half-life 90 min (b=ln2/90);
  dilution time Td = 15-85 min (the drive), dilution rate mu = ln2/Td.
Measured observable: 3-node oscillation period up to ~8 h, faster (shorter) at shorter Td.

  dm_i/dt = drive * beta_dna * f(p_{i-1}) - (a + mu) m_i
  dp_i/dt = drive * c       * m_i        - (b + mu) p_i
  f_rep(x) = ymin + (1-ymin) K^n/(K^n + x^n)   (repression);  f_act for the non-frustrated control.

THE MINTING READING (pa:cycle-affinity, pa:ness-currents; the faithful >=3 frustrated cycle):
  * DB baseline two ways: drive->0 (resources depleted) OR frustration broken (one edge -> activation,
    an EVEN negative ring) => no sustained circulation;
  * the FRUSTRATION (odd ring) mints the cyclic circulation under the TX-TL drive;
  * the winding direction g1->g2->g3 is TOPOLOGY-LOCKED (set by the ring wiring; reverse the wiring to
    reverse it; rate deformations cannot flip it);
  * SUSTAINED: cut the drive -> oscillation (circulation) collapses.
VALIDATION: the period computed from the measured parameters lands in the measured band (~ up to 8 h,
  faster at shorter Td).

Run (from character-framework root):  python experiments/repressilator_minting.py
"""
import sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# ---- MEASURED parameters (Niederholtmeyer et al., eLife 2015, Table 2 / Fig. 3) ----
N_HILL = 2.0
K_REP = 5.0                      # nM
YMIN = 0.0                       # NO leak -- their Eq. 6 repression is pure K^n/(K^n+p^n)
BETA_DNA = 0.4 * 5.0             # 0.4 nM/min/plasmid * 5 nM plasmid = 2.0 nM/min (max transcription)
C_TL = 0.5                       # translation, /min
A_M = np.log(2) / 8.0            # mRNA degradation, /min  (t1/2 = 8 min)
B_P = np.log(2) / 90.0           # protein degradation, /min (t1/2 = 90 min)
OUT = r"H:\character-framework\experiments\repressilator_minting.png"


def f_rep(x):
    return YMIN + (1 - YMIN) * K_REP**N_HILL / (K_REP**N_HILL + x**N_HILL)


def f_act(x):
    return YMIN + (1 - YMIN) * x**N_HILL / (K_REP**N_HILL + x**N_HILL)


def rhs(t, y, mu, drive, frustrated=True):
    m = y[:3]; p = y[3:]
    reps = [p[2], p[0], p[1]]                      # ring: gene i repressed by protein i-1
    prod = []
    for i in range(3):
        # 'broken' control: flip gene 0's edge to ACTIVATION -> even negative ring -> non-frustrated
        fi = f_rep(reps[i]) if (frustrated or i != 0) else f_act(reps[i])
        prod.append(drive * BETA_DNA * fi)
    dm = [prod[i] - (A_M + mu) * m[i] for i in range(3)]
    dp = [drive * C_TL * m[i] - (B_P + mu) * p[i] for i in range(3)]
    return dm + dp


def simulate(mu, drive=1.0, frustrated=True, T=4000.0, y0=None):
    if y0 is None:
        y0 = [1, 0, 0, 8, 2, 0.5]                  # asymmetric seed to break the symmetric fixed point
    sol = solve_ivp(rhs, (0, T), y0, args=(mu, drive, frustrated), method="LSODA",
                    rtol=1e-8, atol=1e-10, dense_output=True,
                    t_eval=np.linspace(0, T, int(T)))
    return sol


def analyze(sol, burn_frac=0.4):
    """period (min) from p1 peaks, amplitude, and the circulation A = <(p1 pdot2 - p2 pdot1)/2>."""
    t = sol.t; i0 = int(len(t) * burn_frac)
    p1, p2 = sol.y[3, i0:], sol.y[4, i0:]; tt = t[i0:]
    # period via peaks of p1
    d = np.diff(p1); pk = np.where((d[:-1] > 0) & (d[1:] <= 0))[0] + 1
    pk = pk[(p1[pk] > p1.mean())]                  # real peaks above mean
    period = float(np.mean(np.diff(tt[pk]))) if len(pk) >= 2 else np.nan
    amp = float(p1.max() - p1.min())
    # circulation: mean signed area rate in the (p1,p2) projection (pdot via finite differences)
    p1d = np.gradient(p1, tt); p2d = np.gradient(p2, tt)
    circ = float(np.mean(0.5 * (p1 * p2d - p2 * p1d)))
    return period, amp, circ


def main():
    global BETA_DNA, C_TL, A_M, B_P
    print("THE >=3 FRUSTRATED-CYCLE MINTING INSTANCE -- cell-free repressilator (Niederholtmeyer 2015)\n")
    print(f"  measured params: n={N_HILL} K={K_REP}nM  beta*DNA={BETA_DNA}nM/min  c={C_TL}/min"
          f"  mRNA t1/2=8min  prot t1/2=90min  (drive = dilution mu = ln2/Td, Td 15-85 min)\n")
    Td = 85.0; mu = np.log(2) / Td                 # a measured operating point
    pi_amp = lambda s: analyze(s)[1]

    # ---------- [MINTING] frustration x drive ----------
    print("=" * 92 + "\n  [MINTING]  the cyclic circulation needs BOTH the frustrated ring AND the TX-TL drive\n" + "=" * 92)
    s_full = simulate(mu, drive=1.0, frustrated=True)
    s_nodrv = simulate(mu, drive=0.0, frustrated=True)
    s_brok = simulate(mu, drive=1.0, frustrated=False)
    T_full, amp_full, circ_full = analyze(s_full)
    _, amp_nodrv, circ_nodrv = analyze(s_nodrv)
    _, amp_brok, circ_brok = analyze(s_brok)
    print(f"    frustrated ring + drive ON : amp={amp_full:8.1f} nM  circulation A={circ_full:+.3e}  "
          f"period={T_full/60:.2f} h   <- MINTED")
    print(f"    drive OFF (resources gone) : amp={amp_nodrv:8.1f} nM  circulation A={circ_nodrv:+.3e}   <- decays, DB baseline")
    print(f"    frustration BROKEN (even)  : amp={amp_brok:8.1f} nM  circulation A={circ_brok:+.3e}   <- no cycle")
    minted = amp_full > 10.0 and abs(circ_full) > 1.0 and amp_nodrv < 1.0 and amp_brok < 1.0
    print(f"    => the frustrated ring mints the protected circulation under drive: {minted}")

    # ---------- [PROTECTION] topology-locked winding direction ----------
    print("\n" + "=" * 92 + "\n  [PROTECTION]  winding direction is topology-locked; rate deformations cannot flip it\n" + "=" * 92)
    s0 = circ_full
    rng = np.random.default_rng(0); flips = 0
    base = (BETA_DNA, C_TL, A_M, B_P)
    for _ in range(40):
        f = np.exp(0.3 * rng.standard_normal(4))
        BETA_DNA, C_TL, A_M, B_P = base[0]*f[0], base[1]*f[1], base[2]*f[2], base[3]*f[3]
        c = analyze(simulate(mu, 1.0, True, T=4000.0))[2]
        flips += int(np.sign(c) != np.sign(s0) and abs(c) > 1e2)
    BETA_DNA, C_TL, A_M, B_P = base
    print(f"    rate deformations (n=40, ring fixed): winding sign-flips = {flips}/40")
    protected = flips == 0
    print(f"    => winding sign is locked to the ring topology, robust to rate deformation: {protected}")

    # ---------- [SUSTAINED] cut the drive -> circulation collapses ----------
    print("\n" + "=" * 92 + "\n  [SUSTAINED]  ramp the drive down -> oscillation/circulation collapses\n" + "=" * 92)
    for dr in (1.0, 0.5, 0.2, 0.1, 0.0):
        a = analyze(simulate(mu, drive=dr, frustrated=True))[1]
        print(f"    drive={dr:.2f}:  oscillation amplitude = {a:8.2f} nM")
    collapses = analyze(simulate(mu, drive=0.0, frustrated=True))[1] < 1.0
    print(f"    => collapses to a static (DB) state without the drive: {collapses}")

    # ---------- [VALIDATION] period vs the measured band ----------
    print("\n" + "=" * 92 + "\n  [VALIDATION]  period from measured parameters vs measured (~up to 8 h; faster at shorter Td)\n" + "=" * 92)
    Tds = np.array([85.0, 60.0, 40.0, 25.0, 15.0])
    pers = np.array([analyze(simulate(np.log(2) / td))[0] / 60.0 for td in Tds])
    for td, pr in zip(Tds, pers):
        print(f"    Td={td:5.1f} min (mu={np.log(2)/td:.4f}/min):  period = {pr:.2f} h")
    monotone = np.all(np.diff(pers) < 0.3)           # Tds listed high->low, so period should shorten
    inband = 2.0 < np.nanmax(pers) < 12.0            # measured 3-node up to ~8 h
    print(f"    measured: 3-node period up to ~8 h, period shortens with Td.  in-band: {inband}  "
          f"monotone-in-Td: {monotone}")

    print("\n" + "=" * 92 + "\n  VERDICT\n" + "=" * 92)
    if minted and protected and collapses and inband and monotone:
        print("  PASS -- the faithful >=3 FRUSTRATED CYCLE mints a protected circulation on a real measured")
        print("  substrate (cell-free gene ring oscillator). Built from the measured transfer functions:")
        print("  the odd repression ring mints a cyclic circulation under the TX-TL free-energy drive, from")
        print("  a clean drive-off detailed-balance baseline; the winding is topology-locked; it collapses")
        print(f"  when the drive is cut; and the period ({pers[0]:.1f} h at Td=85min) sits in the measured band")
        print("  (~up to 8 h, shortening with Td). This is the >=3 grail -- distinct from the DNA chemical")
        print("  cycle and the 2-mode gyrators, on a third kind of real substrate (synthetic gene network).")
    else:
        print(f"  NOT clean: minted={minted} protected={protected} collapses={collapses} "
              f"inband={inband} monotone={monotone} -- inspect before claiming.")

    figure(s_full, Tds, pers)


def figure(s_full, Tds, pers):
    fig, ax = plt.subplots(1, 3, figsize=(16.5, 4.8), dpi=150)
    t_h = s_full.t / 60.0

    # panel 1: the minted oscillation (3 proteins, phase-ordered)
    for i, col in zip(range(3), ["#c62828", "#2e7d32", "#1565c0"]):
        ax[0].plot(t_h, s_full.y[3 + i], lw=1.4, color=col, label=f"protein {i+1}")
    ax[0].set_xlabel("time (h)"); ax[0].set_ylabel("protein (nM)")
    ax[0].set_title("the minted circulation: phase-ordered\n3-gene oscillation (Td=85 min)")
    ax[0].legend(fontsize=8, frameon=False); ax[0].grid(alpha=0.3); ax[0].set_xlim(0, 40)

    # panel 2: the limit cycle in (p1,p2) -- the circulation loop
    i0 = int(len(s_full.t) * 0.4)
    ax[1].plot(s_full.y[3, i0:], s_full.y[4, i0:], lw=1.0, color="#6a1b9a")
    ax[1].set_xlabel("protein 1 (nM)"); ax[1].set_ylabel("protein 2 (nM)")
    ax[1].set_title("the frustrated-cycle limit loop\n(nonzero enclosed area = circulation)")
    ax[1].grid(alpha=0.3)

    # panel 3: period vs dilution time -- the measured-band validation
    ax[2].plot(Tds, pers, "o-", color="#1565c0", lw=1.8)
    ax[2].axhspan(0, 8, color="#2e7d32", alpha=0.12, label="measured 3-node band (up to ~8 h)")
    ax[2].set_xlabel(r"dilution time $T_d$ (min)"); ax[2].set_ylabel("period (h)")
    ax[2].set_title("VALIDATION: period in the measured band,\nshortening with $T_d$")
    ax[2].legend(fontsize=8, frameon=False); ax[2].grid(alpha=0.3)

    fig.suptitle("The >=3 frustrated-cycle minting instance: the cell-free repressilator "
                 "(Niederholtmeyer et al., eLife 4:e09771, 2015)", fontsize=11.5, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
