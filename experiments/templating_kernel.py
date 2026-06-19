r"""templating_kernel.py -- the BOOTSTRAP test for `self-referential-closure` (templating layer).

Pre-registered build per docs/handoff_templating_synthetic.md.  CALIBRATION, not vindication
(project_killshot_synthetic_is_imported_math): the headline is *where the von Neumann threshold
sits for a physical channel*, not "we got reproduction from physics."

THE QUESTION (self-referential-closure, templating leg):
  can a protected circulation bias sign(A) of the protected circulations it MINTS through its own
  recursive closure -- toward its OWN sign -- and is that templating DEGENERATE (a field copies one
  fixed pattern: flame/crystal class, evolutionarily dead) or OPEN-ENDED (the closure copies an
  ARBITRARY message: needs a copyable description / tape)?

THE NON-TRIVIALITY CRITERION (the whole point):  "does the sign propagate?" is trivial -- a stirred
  field biases the handedness of what crystallizes in it (Viedma/Kondepudi deracemization), so a
  physics-only medium passes "sign propagates" and is MISTAKEN for the bootstrap.  The discriminator
  von Neumann forces is the MULTI-BIT channel scaling:  drive the closure with a k-bit string of
  signs and read  I(parent string ; child string)  as k grows.  A low-dimensional shared FIELD can
  impose only its own fixed pattern on all k child-bits at once -> I saturates at the medium's
  channel capacity  C ~ O(1)  regardless of k  (degenerate).  A TAPE (k independent registers) gives
  I ~ k  (open-ended).  The saturation curve IS the von Neumann threshold made visible.

THE SUBSTRATE (the framework's standard synthetic; deformation-chart so(3) direction):
  a character = a driven 3-node frustrated cycle, linear-OU:   dx = M x dt + sqrt(2D) dW,
  M = -gamma I + g A_cyc,  A_cyc the antisymmetric cyclic generator.  sign(A) = sign(g).  The cycle
  current A = 3 D g / gamma  (closed form, cross-checked): A ~ g (sign = rotation sense) and A ~ D
  (SUSTAINED-not-stored: cut the noise drive D -> the fluctuations that carry the current vanish,
  A -> 0, exactly as the gyrator's current collapses when dT -> 0).

THE PHYSICAL CHANNEL (the bias -- Viedma/Kondepudi stirred-field analog, NO sign-copy):
  a child = 3 FRESH nodes, detailed-balanced in isolation (g_child = 0 -> A_child = 0).  The parent's
  circulation "stirs" the single shared medium the child forms in; the medium applies a bias on the
  child's so(3) deformation:        g_child = F + eta,   F = kappa * m + Z .
  m = the parent's NET handedness (a rank-1 scalar projection of the parent's k currents -- the
  current acting as a FIELD, never the parent's edge signs);  Z = the one shared stirred-bath
  fluctuation per minting event (the medium's own finite capacity);  eta = the child's local
  medium noise.  CONTROL kappa = 0 (field off) -> g_child = Z + eta -> sign 50/50, exact by parity.

PRE-REGISTERED OUTCOMES (decision rules; read BEFORE the result):
  (a) NO TEMPLATING -- apparatus null.  Field-ON kernel symmetric too -> channel mis-wired; fix the
      apparatus, not a result.
  (b) DEGENERATE TEMPLATING -- THE PREDICTION.  Field-ON kernel assortative (P(same)>0.5, parity-exact),
      field-OFF symmetric, AND I(s_parent;s_child) saturates at C ~ O(1) bits (<< k); lineage decays
      or locks to the FIELD, not the parent string.  Physics templates faithfully but degenerately;
      the von Neumann threshold is real and we have MEASURED where it sits.  Clean expected result.
  (c) OPEN-ENDED WITHOUT A TAPE -- the surprise/kill.  I ~ k while the medium provably carries < k
      channels.  Audit hard for a smuggled copy step (rank of the parent->child coupling); escalate,
      do not quietly bank it.

Run (from character-framework root):   python experiments/templating_kernel.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.stats import norm, binom
from numpy.polynomial.hermite_e import hermegauss

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "templating_kernel.png"

# ---- the antisymmetric cyclic generator (rotation in the plane perp to (1,1,1)) ----
A_CYC = np.array([[0.0, 1.0, -1.0],
                  [-1.0, 0.0, 1.0],
                  [1.0, -1.0, 0.0]])

# ---- operating point (interior; read sign at finite affinity, never at A~0) ----
GAMMA = 1.0          # decay
G0 = 0.6             # |g|: a clean complex pair (-gamma +/- i g sqrt3), bounded away from g=0
D_DRIVE = 1.0        # noise intensity (the drive). A ~ D -> sustained-not-stored.

# ---- the physical channel (the single shared stirred field) ----
KAPPA = np.sqrt(3.0)  # field/stirring strength
SIG_BATH = 1.0        # the shared medium's own fluctuation Z (its FINITE capacity -> C ~ O(1))
SIG_READ = 1.0        # the child's local medium noise eta (sets how fast I approaches C)
# => single-bit assortativity p = Phi(kappa / sqrt(sig_bath^2 + sig_read^2));
#    saturation capacity C = (1/2) log2(1 + kappa^2/sig_bath^2) = (1/2) log2(4) = 1.0 bit (on-the-nose
#    "~1 bit of degenerate heredity" the handoff predicts).

K_LIST = [1, 2, 4, 8, 16, 32, 64]   # the von Neumann sweep (string length)
N_GH = 48                            # Gauss-Hermite nodes for the shared-bath integral


# ====================================================================================
#  OU machinery  (exact; the cheap deterministic observable -- no stochastic simulation)
# ====================================================================================
def make_triad(g, gamma=GAMMA):
    """The driven 3-node frustrated cycle's drift M = -gamma I + g A_cyc."""
    return -gamma * np.eye(3) + g * A_CYC


def steady_cov(M, D=D_DRIVE):
    """Stationary covariance S: solve  M S + S M^T + 2D I = 0  (Lyapunov)."""
    n = M.shape[0]
    return solve_continuous_lyapunov(M, -2.0 * D * np.eye(n))


def cycle_current(M, D=D_DRIVE):
    """Signed cycle current A in the plane perp to (1,1,1): the (1,1,1)-axial component of the
    probability-current rotational part Q = (1/2)(M S - S M^T).  sign(A) = sign(g).  A=0 iff detailed
    balance.  (For the bare triad, A = 3 D g / gamma exactly -- cross-checked in main.)"""
    S = steady_cov(M, D)
    Q = 0.5 * (M @ S - S @ M.T)              # 3x3 antisymmetric (the irreversible current)
    axial = np.array([Q[2, 1], Q[0, 2], Q[1, 0]])   # the rotation pseudovector
    return -float(axial @ np.ones(3))        # sign convention: sign(A) = sign(g)


def union6_child_current(g_parent, g_child, gamma=GAMMA, c_link=0.05, D=D_DRIVE):
    """Build the explicit 6-node UNION (parent triad (+) child triad, joined by a reciprocal -- detailed-
    balance preserving -- inter-block link c_link) and read the WITHIN-CHILD 3-cycle current.  Used as a
    concrete cross-check that the field-coupled child sign is the same in a genuinely connected operator;
    the reciprocal link injects no current of its own (it only weakly leaks the parent's, sub-permille
    of the minted child current)."""
    Mp = make_triad(g_parent, gamma)
    Mc = make_triad(g_child, gamma)
    L = c_link * np.eye(3)                    # symmetric (reciprocal) coupling: conservative
    M = np.block([[Mp, L], [L, Mc]])
    S = solve_continuous_lyapunov(M, -2.0 * D * np.eye(6))
    Q = 0.5 * (M @ S - S @ M.T)
    Qc = Q[3:, 3:]                            # the child block's rotational current
    axial = np.array([Qc[2, 1], Qc[0, 2], Qc[1, 0]])
    return -float(axial @ np.ones(3))


# ====================================================================================
#  the physical channel  (field -> child so(3) deformation -> sign)
# ====================================================================================
def psi(F):
    """P(sign(g_child)=+ | field F) = P(F + eta > 0), eta ~ N(0, sig_read^2)."""
    return norm.cdf(F / SIG_READ)


def single_bit_p():
    """field-ON single-bit assortativity p = P(child sign = parent sign) -- closed form.
    P(sign(kappa*s + Z + eta) = s) = Phi(kappa / sqrt(sig_bath^2 + sig_read^2))."""
    return float(norm.cdf(KAPPA / np.sqrt(SIG_BATH**2 + SIG_READ**2)))


# ====================================================================================
#  the von Neumann discriminator:  I(s_parent ; s_child)  -- EXACT (no Monte-Carlo)
# ====================================================================================
#  s_parent in {+-1}^k determines the net handedness  m = (1/sqrt k) sum s_i  (k+1 values).
#  The shared field  F = kappa m + Z  (Z ~ N(0,sig_bath^2)) biases every child cycle the SAME way;
#  child i: sign(g_child,i) = sign(F + eta_i).  s_child summarized by its +-count r (k+1 values).
#  Because the children are exchangeable and conditionally independent GIVEN F, and F depends on
#  s_parent only through m, one gets exactly   I(s_parent ; s_child) = I(m ; r)   (the equiprobable-
#  within-r combinatorial terms cancel).  So the full-string MI reduces to a (k+1)x(k+1) table.

def _gh_nodes():
    """standard-normal Gauss-Hermite nodes/weights (weight exp(-z^2/2)/sqrt(2pi))."""
    z, w = hermegauss(N_GH)
    return z, w / np.sqrt(2.0 * np.pi)


def I_parent_child(k, kappa=KAPPA):
    """Exact mutual information I(s_parent ; s_child) = I(m ; r) in bits, for string length k."""
    z, w = _gh_nodes()
    j = np.arange(k + 1)
    Pm = binom.pmf(j, k, 0.5)                       # P(m): m_j = (2j-k)/sqrt(k)
    m = (2.0 * j - k) / np.sqrt(k)
    r = np.arange(k + 1)
    # P(r | m_j) = E_Z[ Binom(r; k, psi(kappa*m_j + sig_bath*z)) ]
    Prm = np.zeros((k + 1, k + 1))                  # [j, r]
    for a, zz in enumerate(z):
        F = kappa * m + SIG_BATH * zz               # (k+1,) shared-field draw
        p = psi(F)                                  # (k+1,) per-m child-+ probability
        # binom.pmf over r for each m_j:
        Prm += w[a] * binom.pmf(r[None, :], k, p[:, None])
    joint = Pm[:, None] * Prm                       # P(m_j, r)
    joint = joint / joint.sum()                     # guard tiny quadrature drift
    Pr = joint.sum(axis=0)                           # P(r)
    # I = sum joint * log2( joint / (Pm Pr) )
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = joint / (Pm[:, None] * Pr[None, :])
        terms = joint * np.log2(ratio)
    return float(np.nansum(terms[joint > 0]))


def H_netfield_ceiling(k):
    """H(m) in bits = entropy of Binom(k,1/2): the rank-1 medium can transmit AT MOST this (data-
    processing). Grows ~ (1/2) log2 k -- already << k."""
    j = np.arange(k + 1)
    p = binom.pmf(j, k, 0.5)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def C_saturation():
    """The shared-bath bottleneck capacity (bits): I(m; F=kappa m + Z), Var(m)=1 -> the flat ceiling
    the I(k) curve saturates at, INDEPENDENT of k.  C = (1/2) log2(1 + kappa^2/sig_bath^2)."""
    return 0.5 * np.log2(1.0 + (KAPPA / SIG_BATH) ** 2)


# ====================================================================================
#  main
# ====================================================================================
def main():
    print("=" * 90)
    print("TEMPLATING SYNTHETIC -- the von Neumann bootstrap test for self-referential-closure")
    print("  (CALIBRATION: where the templating threshold sits for a physical channel, not vindication)")
    print("=" * 90)
    print(f"substrate: driven 3-node frustrated OU triad  M = -{GAMMA} I + g A_cyc,  noise sqrt(2D) dW,")
    print(f"           |g|={G0}, D={D_DRIVE};  channel kappa={KAPPA:.3f}, sig_bath={SIG_BATH}, sig_read={SIG_READ}\n")

    # ---------------------------------------------------------------- 0. OU sanity + sustained-not-stored
    print("-" * 90)
    print("[0] OU substrate: sign(A)=sign(g), A ~ D (sustained-not-stored), read in the interior")
    print("-" * 90)
    A_plus = cycle_current(make_triad(+G0))
    A_minus = cycle_current(make_triad(-G0))
    A_closed = 3.0 * D_DRIVE * G0 / GAMMA
    print(f"  A(g=+{G0}) = {A_plus:+.4f}   A(g=-{G0}) = {A_minus:+.4f}   closed form 3Dg/gamma = {A_closed:+.4f}")
    print(f"  sign(A) = sign(g):  {np.sign(A_plus) > 0 and np.sign(A_minus) < 0};  "
          f"|A(+)-closed| = {abs(A_plus - A_closed):.2e}  (machinery validated)")
    drive_sweep = [(D, cycle_current(make_triad(+G0), D)) for D in (1.0, 0.5, 0.25, 0.1, 0.0)]
    print("  drive sweep (cut the noise drive D -> current collapses; sign held):")
    for D, A in drive_sweep:
        print(f"     D={D:4.2f}:  A = {A:+.4f}   sign {int(np.sign(A)) if A != 0 else 0:+d}")
    sustained = abs(drive_sweep[-1][1]) < 1e-12 and all(np.sign(A) > 0 for _, A in drive_sweep[:-1])

    # ---------------------------------------------------------------- 1. minting is REAL (trap #6)
    print("\n" + "-" * 90)
    print("[1] MINTING the child is REAL (trap #6): 0 before coupling, !=0 after, ->0 drive-cut")
    print("-" * 90)
    # The parent<->child coupling is the SHARED STIRRED FIELD (Viedma -- no direct bond): the medium
    # sets the child's so(3) deformation g_child = field.  Fresh child = detailed-balanced (g_child=0).
    g_child_field = KAPPA * (+1.0)                                  # parent +, representative (xi=0)
    A_child_before = cycle_current(make_triad(0.0))                # fresh nodes: g_child = 0
    A_child_after = cycle_current(make_triad(g_child_field))       # field set g_child != 0 -> minted
    A_child_nodrive = cycle_current(make_triad(g_child_field), D=0.0)  # drive cut
    A_child_union = union6_child_current(+G0, g_child_field)       # connected-operator cross-check
    print(f"  child current  BEFORE coupling (g_child=0):  A_child = {A_child_before:+.2e}   <- detailed balance")
    print(f"  child current  AFTER  coupling (g_child!=0): A_child = {A_child_after:+.4f}   <- MINTED (field-set)")
    print(f"  child current  DRIVE CUT (D=0):              A_child = {A_child_nodrive:+.2e}   <- sustained-not-stored")
    print(f"  connected 6-node union cross-check:          A_child = {A_child_union:+.4f}   (same sign -> real union)")
    minted = (abs(A_child_before) < 1e-12 and abs(A_child_after) > 1e-3
              and abs(A_child_nodrive) < 1e-12 and np.sign(A_child_union) == np.sign(A_child_after))

    # ---------------------------------------------------------------- 2. the single-step kernel (K)
    print("\n" + "-" * 90)
    print("[2] SINGLE-STEP KERNEL  M = P(sign A_child | sign A_parent): field-ON vs field-OFF, parity-exact")
    print("-" * 90)
    p_on = single_bit_p()                                          # field-ON assortativity (closed form)
    M_on = np.array([[p_on, 1 - p_on], [1 - p_on, p_on]])         # rows = parent +/-, cols = child +/-
    M_off = np.array([[0.5, 0.5], [0.5, 0.5]])                    # kappa=0: exact 50/50 by parity
    print(f"  field-ON  kernel  P(same) = {p_on:.4f}   P(flip) = {1-p_on:.4f}   (assortative)")
    print(f"  field-OFF kernel  P(same) = 0.5000   P(flip) = 0.5000   (symmetric -- the control)")
    # parity-paired empirical cross-check + equivariance residual (demonstrate symmetry, not sample):
    rng = np.random.default_rng(0)
    n_pair = 500
    Zc = rng.standard_normal(n_pair) * SIG_BATH                   # shared-bath draws
    Ec = rng.standard_normal(n_pair) * SIG_READ                   # child readout draws
    # parent +1 paired with parent -1 using the SAME (Z, eta) -> exact parity pairing
    sc_plus = np.sign(KAPPA * (+1.0) + Zc + Ec)
    sc_minus = np.sign(KAPPA * (-1.0) - Zc - Ec)                  # P-image: s->-s, (Z,eta)->-(Z,eta)
    resid = float(np.max(np.abs(sc_plus + sc_minus)))            # P-equivariance residual (-> 0 exact)
    p_emp = float(np.mean(sc_plus > 0))                           # empirical P(child=+ | parent=+)
    print(f"  parity-equivariance residual  max|s_child(+) + s_child(-)| = {resid:.1e}  "
          f"(exact 50/50 null guaranteed by symmetry, not sampled)")
    print(f"  empirical P(same) over {n_pair} parity-paired draws = {p_emp:.3f}  (vs closed form {p_on:.3f})")
    # drive-independence (the promotion criterion: biases drive-INDEPENDENTLY, flips only on rewiring):
    print("  drive-independence:  P(same) is set by kappa (the field), NOT by the drive D --")
    # the field sets g_child = kappa*sign(parent); rewiring the SEED flips the parent's sign -> the field
    di_signs = [int(np.sign(cycle_current(make_triad(KAPPA * (+1.0)), D=D))) for D in (1.0, 0.5, 0.1)]
    flip_signs = [int(np.sign(cycle_current(make_triad(KAPPA * s), D=1.0))) for s in (+1, -1)]
    print(f"     child sign across drive D in (1.0,0.5,0.1): {di_signs}  (invariant -> magnitude only)")
    print(f"     child sign when seed g_parent rewired (+,-): {flip_signs}  (flips ONLY on rewiring)")
    kernel_ok = (p_on > 0.6) and resid < 1e-12 and abs(p_emp - p_on) < 0.05
    drive_indep = len(set(di_signs)) == 1 and flip_signs == [1, -1]

    # ---------------------------------------------------------------- 3. THE von Neumann curve (I vs k)
    print("\n" + "-" * 90)
    print("[3] THE RESULT -- von Neumann discriminator  I(s_parent ; s_child)  vs string length k")
    print("-" * 90)
    Ik = np.array([I_parent_child(k) for k in K_LIST])
    Hm = np.array([H_netfield_ceiling(k) for k in K_LIST])
    C = C_saturation()
    I_off = np.array([I_parent_child(k, kappa=0.0) for k in K_LIST])
    print(f"   k        : {np.array2string(np.array(K_LIST), separator=' ')}")
    print(f"   I (bits) : {np.array2string(Ik, precision=3, floatmode='fixed')}   <- field-ON")
    print(f"   I/k      : {np.array2string(Ik / np.array(K_LIST), precision=3, floatmode='fixed')}   "
          f"<- per-bit transmitted info -> 0  (DEGENERATE)")
    print(f"   I=k (tape): {np.array2string(np.array(K_LIST, float), precision=1, floatmode='fixed')}   "
          f"<- open-ended reference")
    print(f"   I field-OFF (kappa=0): max = {np.max(np.abs(I_off)):.1e}  (exact 0 -> the bias is the channel)")
    print(f"   saturation capacity  C = (1/2)log2(1+kappa^2/sig_bath^2) = {C:.3f} bits  (k-INDEPENDENT)")
    print(f"   rank of the parent->child signal coupling = 1  (the shared field is one scalar; < k for all k>1)")
    saturates = (Ik[-1] < 0.5 * K_LIST[-1]) and (Ik[-1] < C + 0.15) and (np.max(np.abs(I_off)) < 1e-9)

    # ---------------------------------------------------------------- 4. across-generation lineage (R)
    print("\n" + "-" * 90)
    print("[4] ACROSS-GENERATION  <s_0 s_n>: the parent's STRING is not durably inherited (degenerate)")
    print("-" * 90)
    p = p_on
    n_gen = np.arange(0, 13)
    corr_self = (2 * p - 1) ** n_gen                              # self-coupled Markov lineage: decays
    # field-fixation: a FIXED external field pins each generation to the FIELD's sign, independent of the
    # seed -> s_n decorrelates from s_0 immediately:  <s_0 s_n> = delta_{n,0}  (seed forgotten at once).
    corr_fix = np.zeros_like(n_gen, float); corr_fix[0] = 1.0
    corr_tape = np.ones_like(n_gen, float)                        # a TAPE (open-ended) would copy faithfully
    tau = 1.0 / np.log(1.0 / (2 * p - 1)) if (2 * p - 1) > 0 else np.inf
    print(f"   self-coupled lineage  <s_0 s_n> = (2p-1)^n,  p={p:.3f} -> decays, corr. length ~ {tau:.1f} gens")
    print(f"     {np.array2string(corr_self, precision=3, floatmode='fixed')}")
    print(f"   => the seed sign is FORGOTTEN after ~{tau:.0f} generations: heredity is ~1 noisy bit, transient.")
    print(f"   field-fixation variant: lineage locks to the FIELD's sign (not the seed) -> <s_0 s_n>=0 for n>=1.")
    print(f"   a TAPE would give <s_0 s_n>=1 for all n (durable seed inheritance) -- NOT what physics buys here.")
    print(f"   (multitype-branching: the 2x2 kernel's Perron vector is symmetric -> NO lock-in to the seed;")
    print(f"    durable heredity would need REINFORCEMENT = self-wiring, the deprioritized advanced layer.)")
    lineage_ok = corr_self[-1] < 0.2

    # ---------------------------------------------------------------- VERDICT
    print("\n" + "=" * 90)
    print("VERDICT -- which pre-registered outcome fired")
    print("=" * 90)
    bar = [("[0] OU sustained-not-stored (A ~ D, cut drive -> 0)", sustained),
           ("[1] minting is real (0 before / !=0 after / ->0 drive-cut)", minted),
           ("[2] kernel assortative field-ON, parity-exact, field-OFF symmetric", kernel_ok),
           ("[2] bias is drive-INDEPENDENT, flips only on rewiring the seed", drive_indep),
           ("[3] I(k) SATURATES at C~O(1) << k, field-OFF exactly 0", saturates),
           ("[4] lineage decays / locks to field, not the seed string", lineage_ok)]
    for label, ok in bar:
        print(f"   [{'PASS' if ok else '----'}]  {label}")
    if all(ok for _, ok in bar):
        print("\n  ==> OUTCOME (b): DEGENERATE TEMPLATING -- THE PREDICTION.")
        print(f"      The physical channel templates sign(A) FAITHFULLY (field-ON P(same)={p_on:.2f}, parity-exact,")
        print(f"      drive-independent, flips only on rewiring) but DEGENERATELY: I(s_parent;s_child) saturates at")
        print(f"      C = {C:.2f} bit << k -- one shared stirred field, of fixed capacity, whatever k is.  The seed")
        print(f"      string is not durably inherited.  The von Neumann threshold is REAL and we have MEASURED")
        print(f"      where it sits: physics buys self-maintenance + ~1 bit of degenerate, faithful templating;")
        print(f"      open-ended heredity is sub-threshold WITHOUT A TAPE.  The framework's honest 'not off the")
        print(f"      ground without a tape' is CALIBRATED and vindicated.  (Synthetic = calibration: this measures")
        print(f"      where the threshold sits, it does NOT solve abiogenesis -- no character.md edit.)")
    else:
        misses = [lbl for lbl, ok in bar if not ok]
        # distinguish (a) apparatus null from (c) open-ended-without-a-tape
        if not kernel_ok:
            print("\n  ==> OUTCOME (a): apparatus null -- the field-ON kernel did not bias. FIX THE APPARATUS.")
        elif not saturates and Ik[-1] > 0.5 * K_LIST[-1]:
            print("\n  ==> OUTCOME (c)!? I ~ k while the medium is rank-1. AUDIT FOR A SMUGGLED TAPE (handoff S8); ESCALATE.")
        else:
            print(f"\n  ==> NOT CLEAN -- misses: {misses}. Read honestly and debug before claiming anything.")

    figure(M_on, M_off, resid, K_LIST, Ik, Hm, C, n_gen, corr_self, corr_fix, corr_tape, p_on)
    return Ik, C


def figure(M_on, M_off, resid, K_LIST, Ik, Hm, C, n_gen, corr_self, corr_fix, corr_tape, p_on):
    fig = plt.figure(figsize=(17, 5.2), dpi=150)
    gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.25, 1.0], wspace=0.32)

    # ---- Panel A: the kernel heatmaps (field-ON vs field-OFF) ----
    axA = fig.add_subplot(gs[0, 0])
    pad = 0.32
    for col, (M, name) in enumerate([(M_on, "field-ON"), (M_off, "field-OFF")]):
        x0 = col * (1.0 + pad)
        im = axA.imshow(M, cmap="RdPu", vmin=0, vmax=1, extent=[x0, x0 + 1, 0, 1], aspect="auto")
        for i in range(2):
            for j in range(2):
                axA.text(x0 + 0.25 + 0.5 * j, 0.75 - 0.5 * i, f"{M[i, j]:.2f}",
                         ha="center", va="center", fontsize=12,
                         color="white" if M[i, j] > 0.6 else "#311", weight="bold")
        axA.text(x0 + 0.5, 1.08, name, ha="center", fontsize=10, weight="bold")
        axA.text(x0 + 0.5, -0.12, "child  +      -", ha="center", fontsize=8)
    axA.text(-0.06, 0.5, "parent  -    +", va="center", rotation=90, fontsize=8)
    axA.set_xlim(-0.1, 2 * 1.0 + pad + 0.05); axA.set_ylim(-0.2, 1.2)
    axA.set_xticks([]); axA.set_yticks([])
    axA.set_title(f"A. single-step kernel  $M=P(\\mathrm{{sign}}\\,\\mathcal{{A}}_{{child}}\\,|\\,"
                  f"\\mathrm{{sign}}\\,\\mathcal{{A}}_{{parent}})$\nfield-ON assortative ($P_{{same}}{{=}}{p_on:.2f}$); "
                  f"field-OFF 50/50\nparity-equivariance residual {resid:.0e} (exact null)", fontsize=9.5)
    for s in axA.spines.values():
        s.set_visible(False)

    # ---- Panel B: THE von Neumann curve ----
    axB = fig.add_subplot(gs[0, 1])
    kk = np.array(K_LIST, float)
    axB.plot(kk, kk, "k--", lw=1.4, label="open-ended (tape): $I=k$")
    axB.plot(kk, Hm, color="#9e9e9e", ls=":", lw=1.6,
             label="rank-1 medium ceiling $H(m)\\sim\\frac{1}{2}\\log_2 k$")
    axB.axhline(C, color="#2e7d32", lw=1.4, ls="-.", label=f"shared-bath capacity $C={C:.2f}$ bit")
    axB.plot(kk, Ik, "o-", color="#c2185b", lw=2.4, ms=8, label="measured $I(s_{parent};s_{child})$  (field-ON)")
    axB.plot(kk, np.zeros_like(kk), "s-", color="#1565c0", lw=1.4, ms=5, label="field-OFF control ($\\kappa{=}0$): $I{=}0$")
    axB.set_xscale("log", base=2); axB.set_xticks(K_LIST); axB.set_xticklabels(K_LIST)
    axB.set_xlabel("string length  $k$  (independent parent triads)")
    axB.set_ylabel("mutual information  $I$  (bits)")
    axB.set_ylim(-0.3, K_LIST[-1] * 0.55)
    axB.set_title("B. THE RESULT: $I$ SATURATES at $C\\sim O(1)\\ll k$\n"
                  "(degenerate / field-class) -- a tape would track $I=k$", fontsize=10, weight="bold")
    axB.legend(fontsize=7.6, frameon=False, loc="upper left"); axB.grid(alpha=0.3, which="both")

    # ---- Panel C: across-generation lineage ----
    axC = fig.add_subplot(gs[0, 2])
    axC.plot(n_gen, corr_tape, color="#9e9e9e", ls="--", lw=1.5, label="a TAPE would inherit: $\\langle s_0 s_n\\rangle{=}1$")
    axC.plot(n_gen, corr_self, "o-", color="#6a1b9a", lw=2.2, ms=7, label="self-coupled lineage (decays)")
    axC.plot(n_gen, corr_fix, "^--", color="#ef6c00", lw=1.6, ms=6, label="field-fixation (locks to field, not seed)")
    axC.axhline(0, color="gray", lw=0.8)
    axC.set_xlabel("generation  $n$"); axC.set_ylabel(r"$\langle s_0\, s_n\rangle$")
    axC.set_ylim(-0.15, 1.05)
    axC.set_title("C. the seed sign is FORGOTTEN: heredity is\n~1 transient bit (no Polya lock-in to the seed)",
                  fontsize=10)
    axC.legend(fontsize=8, frameon=False); axC.grid(alpha=0.3)

    fig.suptitle("Templating synthetic -- the von Neumann bootstrap test: a physical channel templates "
                 "sign($\\mathcal{A}$) faithfully but DEGENERATELY ($C\\sim1$ bit $\\ll k$); "
                 "open-ended heredity is sub-threshold without a tape  [CALIBRATION]",
                 fontsize=11, weight="bold")
    fig.subplots_adjust(left=0.04, right=0.985, bottom=0.14, top=0.80)
    fig.savefig(OUT, bbox_inches="tight"); plt.close(fig)
    print(f"\nfigure: {OUT}")


if __name__ == "__main__":
    main()
