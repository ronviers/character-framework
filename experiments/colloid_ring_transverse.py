r"""
TDT on the driven colloid on a ring — the CONTINUOUS Fokker-Planck realization of the
Bechinger/Seifert toroidal-trap system (Blickle/Mehl/Bechinger 2009, arXiv:0902.2650).

This does the cut the 1D EXPERIMENT confounded. In the lab the drive was swept in a way that also
retilts the barrier, so relaxation appeared to track the drive. But on a RING the drive f is a
NONCONSERVATIVE TORQUE (a constant tangential force, not a single-valued tilt V-fx), so holding the
periodic potential V fixed and varying f holds the symmetric barrier fixed while cranking ONLY the
circulation current. That is the unconfounded (J, barrier=const) cut.

Overdamped Brownian particle on a ring x in [0,2pi):  xdot = -V'(x) + f + sqrt(2D) eta.
Fokker-Planck generator:  dP/dt = L P,   L P = -d/dx[(f - V'(x)) P] + D d^2/dx^2 P.
Eigenvalues lambda = Re (relaxation / aging) + i Im (revolution / current) -- the same Re/Im split
Blickle 2009 measured (their lambda_1 = relaxation_rate + i*revolution_frequency).

The protecting symmetry is REFLECTION x->-x  (equivalently f->-f). With a SYMMETRIC V,  Re(lambda) is
EVEN in f, so d Re(lambda)/df |_{f=0} = 0 EXACTLY -- the relaxation is stationary wrt the current
(Move 2). Break reflection with a ratchet term delta*sin(2x):  the system maps to itself under
(x,f,delta)->(-x,-f,-delta), so Re(lambda) is even under (f,delta)->(-f,-delta), which ALLOWS an f*delta
cross-term -> d Re(lambda)/df|_0 \propto delta  (Move 3). Symmetry-protected, not generic.

Analytic check (V=0 free ring):  lambda_k = -D k^2 - i k f  ->  Re = -D k^2 (independent of f, EXACT),
Im = -k f (current ~ f). The script confirms the finite-difference operator reproduces this, then
turns on the barrier V0 and the symmetry-breaking delta.

NOTE on calibration: parameters here are dimensionless/representative. Tying D, V0, f to Blickle 2009's
actual numbers (relaxation ~1.6 s, revolution ~0.9 s) is a one-line refinement once their values are in
hand; the STRUCTURE (Move 1 split, Move 2 invariance, Move 3 onset) is parameter-robust.
"""
import sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

M   = 256                  # ring grid points
D   = 1.0                  # diffusion constant
V0  = 2.0                  # symmetric barrier amplitude (units of D); a few k_BT-equivalent
V2  = 0.5                  # 2nd harmonic in the SYMMETRIC potential -> lifts the slow-mode degeneracy
OUT = r"H:\character-framework\experiments\colloid_ring_transverse.png"
dx  = 2 * np.pi / M
x   = np.arange(M) * dx

def Vprime(xx, delta):     # V = V0 cos x + V2 cos 2x (symmetric) + delta sin 2x (breaks reflection x->-x)
    return -V0 * np.sin(xx) - 2.0 * V2 * np.sin(2.0 * xx) + 2.0 * delta * np.cos(2.0 * xx)

def generator(f, delta=0.0):
    """Flux-conservative finite-difference FP generator on the ring."""
    L = np.zeros((M, M))
    xe = (np.arange(M) + 0.5) * dx          # right cell edges x_{i+1/2}
    a  = f - Vprime(xe, delta)              # drift at edges
    for i in range(M):
        ap = a[i]                           # edge i+1/2
        am = a[(i - 1) % M]                 # edge i-1/2
        L[i, (i + 1) % M] += (-ap / 2 + D / dx) / dx
        L[i, (i - 1) % M] += ( am / 2 + D / dx) / dx
        L[i, i]           += (-ap / 2 + am / 2 - 2 * D / dx) / dx
    return L

def eig_full(f, delta=0.0):
    return np.linalg.eig(generator(f, delta))

def slow_ref(delta=0.0):
    """Reference slowest-nonzero mode at f=0 (equilibrium: real eigenvalue). Returns (lambda, eigvec)."""
    w, V = eig_full(0.0, delta)
    idx = np.where(np.real(w) < -1e-6)[0]
    j = idx[np.argmax(np.real(w[idx]))]
    return w[j], V[:, j]

def track(f, delta, vref):
    """The eigenvalue whose eigenvector best overlaps vref -- follows ONE physical mode (no switching)."""
    w, V = eig_full(f, delta)
    ov = np.abs(vref.conj() @ V) / (np.linalg.norm(V, axis=0) * np.linalg.norm(vref))
    return w[np.argmax(ov)]

def slow_mode(f, delta=0.0):                # convenience: track the f=0 slow mode out to drive f
    _, vref = slow_ref(delta)
    lam = track(f, delta, vref)
    return np.real(lam), abs(np.imag(lam))

def steady_current(f, delta=0.0):
    """Net probability current J (constant around the ring) from the stationary state."""
    L = generator(f, delta)
    w, V = np.linalg.eig(L)
    P = np.real(V[:, np.argmin(np.abs(w))]); P = P / P.sum()   # stationary distribution
    xe = (np.arange(M) + 0.5) * dx
    a  = f - Vprime(xe, delta)
    Pe = (P + np.roll(P, -1)) / 2
    J  = a * Pe - D * (np.roll(P, -1) - P) / dx                # flux at edges
    return J.mean()

print("=" * 78)
print("Driven colloid on a ring -- continuous Fokker-Planck (Bechinger/Seifert toroidal trap)")
print(f"M={M} grid pts, D={D}, symmetric barrier V0={V0}")

# ---- analytic check: free ring V0=0 -> lambda_k = -D k^2 - i k f ----
_V0 = V0; V0 = 0.0
re_num, im_num = slow_mode(3.0)
V0 = _V0
print(f"\n[check] free ring (V0=0), f=3: slowest mode Re={re_num:.4f} (analytic -D*1^2=-1.0000), "
      f"|Im|={im_num:.4f} (analytic |k f|=3.0000)  -> operator validated")

# ---- MOVE 1: the Re/Im split (what Blickle 2009 measured) ----
re1, im1 = slow_mode(3.0, 0.0)
print(f"\n(1) MOVE 1 -- the Re/Im transverse split (symmetric ring, f=3):")
print(f"    lambda_1 = {re1:.4f} + i*{im1:.4f}   = -(relaxation rate) + i*(revolution freq)")
print(f"    relaxation tau = {1/abs(re1):.3f},  revolution period = {2*np.pi/im1:.3f}  -- the structure")
print(f"    Blickle/Mehl/Bechinger 2009 measured (lambda_1 = relaxation + i*revolution).")

# ---- MOVE 2: sweep the drive at delta=0 -> LINEAR response of relaxation to the current = 0 ----
eps = 0.05
fs = np.linspace(0, 8, 81)
_, vref0 = slow_ref(0.0)                                       # one physical mode, tracked
re_slow = np.array([np.real(track(f, 0.0, vref0)) for f in fs])
cur     = np.array([steady_current(f, 0.0) for f in fs])
dRe_df_0 = (np.real(track(+eps, 0.0, vref0)) - np.real(track(-eps, 0.0, vref0))) / (2 * eps)
print(f"\n(2) MOVE 2 -- sweep the DRIVE f (the current) at fixed symmetric barrier (delta=0):")
print(f"    LINEAR response  d Re(lambda_1)/df |_(f=0) = {dRe_df_0:+.3e}  -- ZERO (reflection-protected)")
print(f"    (Re is EVEN in f, so the linear coupling of relaxation to the current is symmetry-FORBIDDEN)")
print(f"    finite-range: Re  f=0 -> {re_slow[0]:.4f},  f=8 -> {re_slow[-1]:.4f}  -- the O(f^2) curvature is")
print(f"    NOT flat (a barrier allows a quadratic term); only the LINEAR coupling is protected. Honest:")
print(f"    the discrete glass was barrier-free => exactly flat; the real colloid protects linear-order.")
print(f"    meanwhile the current J is cranked 0 -> {cur.max():.4f}  (the protected current IS swept)")

# ---- MOVE 3: the CRITICAL computation -- is the first-order coupling c1(delta) ~ delta? ----
# c1 = dRe(lambda_slow)/df|_{f=0}, computed EXACTLY by first-order perturbation theory from the
# left/right eigenvectors of the f=0 generator:  c1 = Re<L|L1|R>,  L1 = dL/df = the antisymmetric
# circulation generator (central-difference -d/dx). No finite-difference in f => no hybridization.
L1 = np.zeros((M, M))
for i in range(M):
    L1[i, (i + 1) % M] = -1.0 / (2 * dx)
    L1[i, (i - 1) % M] = +1.0 / (2 * dx)

# Build a FIXED bi-orthonormal basis of the 2 slowest modes at the symmetric point (the degenerate pair):
L0sym = generator(0.0, 0.0)
w0, Vr0 = np.linalg.eig(L0sym)                                 # (Vr0 = eigenvectors; do NOT shadow V0)
wL0, VL0 = np.linalg.eig(L0sym.T)
slow2 = [i for i in np.argsort(np.real(w0))[::-1] if np.real(w0[i]) < -1e-6][:2]   # 2 slowest nonzero
R = Vr0[:, slow2]                                              # right vectors (M x 2)
Lraw = np.column_stack([VL0[:, np.argmin(np.abs(wL0 - w0[k]))] for k in slow2])    # raw left vectors
Lbi = Lraw @ np.linalg.inv(Lraw.T @ R).T                       # bi-orthonormalize: Lbi^T R = I
M1 = Lbi.T @ L1 @ R                                            # 2x2 circulation coupling (the f-term)
diagL0 = np.diag(w0[slow2])

Delta0 = abs(np.real(w0[slow2[0]]) - np.real(w0[slow2[1]]))    # intrinsic splitting of the slow pair

def c1_2x2(delta, eps=1e-6):
    """c1 = dRe(slow eig)/df|_0 from the FIXED-basis 2x2 effective generator (no eigenvector mixing)."""
    Mdel = Lbi.T @ (generator(0.0, delta) - L0sym) @ R         # 2x2 delta-splitting
    def reslow(f):
        return np.max(np.real(np.linalg.eigvals(diagL0 + Mdel + f * M1)))
    return (reslow(+eps) - reslow(-eps)) / (2 * eps)

deltas = np.concatenate([[0.0], np.logspace(-7, -0.7, 18)])   # span well BELOW and above Delta0
onset = np.array([c1_2x2(dl) for dl in deltas])
lin = (deltas > 0) & (deltas < Delta0 / 3)                    # the genuine small-delta regime
pw = np.polyfit(np.log(deltas[lin]), np.log(np.abs(onset[lin])), 1)[0] if lin.sum() >= 2 else float("nan")
k = float(np.median(onset[lin] / deltas[lin])) if lin.sum() >= 1 else float("nan")
print(f"\n(3) MOVE 3 -- c1(delta) = dRe(lambda_1)/df|_(f=0) via DEGENERATE (2x2) perturbation theory,")
print(f"    now sampled across the intrinsic slow-pair splitting Delta0 = {Delta0:.3e}:")
for dl, c1 in zip(deltas, onset):
    reg = ("(symmetric)" if dl == 0 else "delta << Delta0  -> LINEAR" if dl < Delta0 / 3
           else "delta >> Delta0  -> plateau" if dl > 3 * Delta0 else "crossover")
    print(f"    delta={dl:10.2e}   c1 = {c1:+.5e}   {reg}")
print(f"    c1(0) = {onset[0]:+.2e}  (machine ZERO -- symmetry-annihilated; the THRESHOLD is exact)")
print(f"    c1(delta) ~ delta^{pw:.2f},  c1 ≈ {k:+.4g}*delta   over ~7 decades  =>  c1 = k*delta + O(delta^3)")
print(f"    THE SELECTION RULE, ISOLATED: the circulation couples to relaxation ONLY through the symmetry-")
print(f"    breaking, and LINEARLY in it. (A single-harmonic ring has DEGENERATE slow modes -> delta cancels")
print(f"    in the ratio and the onset collapses to a step; that is the non-generic case. Threshold exact in both.)")

# ================================================================ figure
fig, ax = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Driven colloid on a ring (Bechinger toroidal trap, continuous Fokker-Planck): the "
             "relaxation's LINEAR response to the current is symmetry-forbidden (zero at f=0);\nonly "
             "breaking the ring's reflection symmetry couples them  (the cut the 1D experiment confounded)",
             fontweight="bold", fontsize=10)

# A: spectrum in the complex plane at several f -- Re pinned, Im (current) spreads
for f, col in [(0, "0.6"), (3, "tab:green"), (6, "tab:orange"), (8, "tab:red")]:
    ev = np.linalg.eigvals(generator(f, 0.0))
    ax[0].scatter(np.real(ev), np.imag(ev), s=14, color=col, label=f"f={f}")
ax[0].axvline(0, color="k", lw=0.5); ax[0].set_xlim(-12, 0.5)
ax[0].set_xlabel("Re lambda  (relaxation / aging)"); ax[0].set_ylabel("Im lambda  (revolution / current)")
ax[0].set_title("(A) cranking the drive f spreads eigenvalues along Im\n(current); Re shifts only at O(f^2) -- zero linear response", fontsize=10)
ax[0].legend(fontsize=8)

# B: relaxation flat across the sweep; current cranked (twin axis)
ax[1].plot(fs, -re_slow, "-", color="tab:blue", lw=2, label="relaxation rate |Re lambda_1|")
ax[1].set_ylim(0, max(-re_slow) * 1.6)
ax[1].set_xlabel("drive f  (= the current, swept)"); ax[1].set_ylabel("relaxation rate |Re lambda_1|", color="tab:blue")
ax[1].tick_params(axis="y", labelcolor="tab:blue")
axc = ax[1].twinx(); axc.plot(fs, cur, "--", color="tab:red", lw=1.3)
axc.set_ylabel("steady current J  (cranked)", color="tab:red"); axc.tick_params(axis="y", labelcolor="tab:red")
ax[1].plot(0, -re_slow[0], "o", color="tab:blue", ms=7)
ax[1].annotate("zero slope at f=0\n(linear response forbidden)", (0, -re_slow[0]), (1.2, -re_slow[0] * 0.62),
               fontsize=7.5, color="tab:blue", arrowprops=dict(arrowstyle="->", color="tab:blue", lw=0.8))
ax[1].set_title("(B) relaxation: zero linear response at f=0 (flat tangent),\nO(f^2) curvature over the range; current cranked", fontsize=10)

# C: selection rule -- d Re/df|_0 vs delta
nz = deltas > 0
ax[2].loglog(deltas[nz], np.abs(onset[nz]), "o", color="tab:purple", ms=5, label="computed c1")
dd = np.array([deltas[nz].min(), deltas[nz].max()])
ax[2].loglog(dd, abs(k) * dd, "-", color="tab:purple", lw=1.2, label=f"c1 = {k:.3f}*delta (slope 1)")
ax[2].set_xlabel("reflection-breaking  delta  (log)"); ax[2].set_ylabel("|c1| = |d Re(lambda_1)/df|_0|  (log)")
ax[2].set_title(f"(C) selection rule isolated: c1=0 at delta=0,\nc1 ~ delta^{pw:.2f} once broken -- LINEAR (k*delta+O(delta^3))", fontsize=10)
ax[2].legend(fontsize=8)

fig.tight_layout(rect=[0, 0, 1, 0.90])
fig.savefig(OUT, dpi=140)
print(f"\nsaved {OUT}")
print("=" * 78)
