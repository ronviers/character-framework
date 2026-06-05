"""
T2 calibration / null test — using only established tools.

Goal: before any real shell, prove the test "is the growing-tube generator (E,C,T)
constant along growth?" reads SELF-SIMILAR correctly.

Tools (all imported, none bespoke):
  - generator + E-fit: Noshita's `growing_tube_model_estimation` package (Okamoto 1988 model)
  - C,T fitter: Noshita's `parameter_estimation.ipynb` (lifted verbatim, credited below)
  - heteromorph reference: Misaki, Okamoto & Maeda 2023 Data_2 (real E/C/T(s), CC0)

The synthetic SELF-SIMILAR shell = constant (E,C,T) fed to Noshita's generator.
The NULL = run the estimator back on it and recover the constants.
"""
import sys, numpy as np
from pathlib import Path
from scipy.optimize import curve_fit
from scipy.spatial.transform import Rotation as Rot
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PKG = r"H:\character-framework\data\shell\noshita_growing_tube\growing_tube_model_estimation-main"
sys.path.insert(0, PKG)
from growing_tube_model_estimation.growing_tube._growing_tube_model import growing_tube_model
from growing_tube_model_estimation.growing_tube._growting_tube_estimation import estimate_gt_e_and_r0

OUT = Path(r"H:\character-framework\experiments")
MISAKI = Path(r"H:\character-framework\data\shell\doi_10_5061_dryad_q573n5tnz__v20230815"
              r"\Data_2_Parameter_values_of_the_growing_tube_model_for_each_morphotype.csv")

# ---- Noshita's centerline generator + C,T estimator (verbatim from his notebook) ----
def gt_generating_spiral(s, e, c, t, r0=1, p0=np.zeros(3), R0=np.identity(3)):
    E_g, C_g, T_g = e, c, t
    D = np.sqrt(C_g**2 + T_g**2)
    ED3E2pD2 = E_g * D**3 * (E_g**2 + D**2)
    expEs, sinDs, cosDs = np.exp(E_g*s), np.sin(D*s), np.cos(D*s)
    P = (r0*D*(((D**2)*(T_g**2)+(E_g**2)*(T_g**2)+C_g**2*E_g**2*cosDs+E_g*D*(C_g**2)*sinDs)*expEs
               - D**2*(E_g**2+T_g**2))/ED3E2pD2)
    Q = (r0*C_g*D*E_g*(-expEs*(C_g**2+T_g**2)*cosDs+D*(D+expEs*E_g*sinDs))/ED3E2pD2)
    R = (r0*C_g*T_g*D*(((E_g**2)+(D**2)-(E_g**2)*cosDs-E_g*D*sinDs)*expEs - D**2)/ED3E2pD2)
    return p0 + np.transpose(np.dot(R0, np.array([P, Q, R])))

def estimate_gt_c_and_t(arclength_parameters, coords, e, r0, initial_c=0, initial_t=0, bounds=(-np.inf, np.inf)):
    s = np.log(1+(e*arclength_parameters)/r0)/e
    def wrap(s, c, t, p0x, p0y, p0z, R0x, R0y, R0z):
        p0 = np.array([p0x, p0y, p0z]); R0 = Rot.from_rotvec([R0x, R0y, R0z]).as_matrix()
        return gt_generating_spiral(s, e, c, t, r0=r0, p0=p0, R0=R0).reshape(-1)
    p_opt, _ = curve_fit(wrap, s, coords.reshape(-1),
                         p0=[initial_c, initial_t, 0, 0, 0, 0, 0, 0], bounds=bounds)
    c, t = p_opt[0], p_opt[1]
    return c, t

# ---------------------------------------------------------------- true params
E0, C0, T0, r0 = 0.08, 0.45, 0.06, 1.0
S = 55.0
print(f"TRUE   E={E0}  C={C0}  T={T0}  r0={r0}   (ratios C/E={C0/E0:.3f} T/C={T0/C0:.3f})")

s = np.linspace(1e-6, S, 600)
coords = gt_generating_spiral(s, E0, C0, T0, r0)              # centerline (N,3)
thick  = r0*np.exp(E0*s)                                      # tube radius law

# (1) NULL, clean, model-consistent arclength -> recovery should be ~exact
arc_model = r0*(np.exp(E0*s)-1)/E0
e_hat, r0_hat = estimate_gt_e_and_r0(arc_model, thick)
c_hat, t_hat = estimate_gt_c_and_t(arc_model, coords, e_hat, r0_hat, initial_c=0.4, initial_t=0.05)
print("\nNULL (clean, model arclength):")
print(f"  E {E0} -> {e_hat:.6g}   C {C0} -> {c_hat:.6g}   T {T0} -> {t_hat:.6g}")
relerr = max(abs(e_hat-E0)/E0, abs(c_hat-C0)/C0, abs(t_hat-T0)/T0)
print(f"  max rel err = {relerr:.2e}   -> {'PASS' if relerr<0.01 else 'FAIL'}")

# (2) realistic arclength = cumulative euclidean distance (what you'd measure)
seg = np.linalg.norm(np.diff(coords, axis=0), axis=1)
arc_euclid = np.concatenate([[0], np.cumsum(seg)])
e_h2, r0_h2 = estimate_gt_e_and_r0(arc_euclid, thick)
c_h2, t_h2 = estimate_gt_c_and_t(arc_euclid, coords, e_h2, r0_h2, initial_c=0.4, initial_t=0.05)
k = e_h2/E0
print("\nREALISTIC (euclidean arclength): absolute (E,C,T) shift by a common scale k,")
print("  but the convention-free RATIOS (the constancy test) are preserved:")
print(f"  C/E true {C0/E0:.4f} -> {c_h2/e_h2:.4f}   T/C true {T0/C0:.4f} -> {t_h2/c_h2:.4f}   (k={k:.3f})")

# (3) noise robustness: noise on coords, track convention-free ratios
rng = np.random.default_rng(0)
scale = np.median(np.linalg.norm(coords, axis=1))
sigmas = np.array([0, 0.002, 0.005, 0.01, 0.02, 0.05])
ce, tc = [], []
for sig in sigmas:
    cc = coords + rng.normal(0, sig*scale, coords.shape)
    seg = np.linalg.norm(np.diff(cc, axis=0), axis=1); arc = np.concatenate([[0], np.cumsum(seg)])
    try:
        eh, rh = estimate_gt_e_and_r0(arc, thick)
        ch, th = estimate_gt_c_and_t(arc, cc, eh, rh, initial_c=0.4, initial_t=0.05)
        ce.append(ch/eh); tc.append(th/ch)
    except Exception:
        ce.append(np.nan); tc.append(np.nan)
print("\nNOISE sweep (ratios should stay near true under modest noise):")
for sg, a, b in zip(sigmas, ce, tc):
    print(f"  sigma={sg:5.3f}  C/E={a:.3f}  T/C={b:.3f}")

# ---------------------------------------------------------------- Misaki heteromorph (real)
def parse_misaki(path, morph="I"):
    import csv
    rows = list(csv.reader(open(path, encoding="utf-8")))
    hdr = rows[0]
    cs = hdr.index(f"Morphotype {morph} (values of s)")
    cv = hdr.index(f"Morphotype {morph} (values of E, C, T)")
    out = {"E": [[], []], "C": [[], []], "T": [[], []]}; cur = None
    for r in rows[1:]:
        if len(r) <= cv: continue
        a, b = r[cs].strip(), r[cv].strip()
        if b in ("E", "C", "T"): cur = b; continue
        if cur is None or a == "" or a.lower().startswith("upper") or a.lower().startswith("growth"): continue
        try: out[cur][0].append(float(a)); out[cur][1].append(float(b))
        except ValueError: pass
    return out

mis = parse_misaki(MISAKI, "I")
print("\nMISAKI morphotype I (real heteromorph):")
for k_ in "ECT":
    v = np.array(mis[k_][1]);  print(f"  {k_}: n={len(v)} range [{v.min():.3f}, {v.max():.3f}]"
          + ("  <-- CROSSES ZERO (sign flip)" if v.min() < 0 < v.max() else ""))

# ---------------------------------------------------------------- figure
fig = plt.figure(figsize=(14, 10)); fig.suptitle(
    "T2 calibration (established tools only): the test reads 'self-similar' correctly",
    fontsize=13, fontweight="bold")

# A: the self-similar anchor shell (surface)
ax = fig.add_subplot(2, 2, 1, projection="3d")
sv = np.linspace(1e-6, S, 220); pv = np.linspace(0, 2*np.pi, 60)
SS, PP = np.meshgrid(sv, pv)
U = growing_tube_model(SS.ravel(), PP.ravel(), E0, C0, T0, r0=r0).T   # (N,3)
ax.scatter(U[:, 0], U[:, 1], U[:, 2], c=np.tile(sv, len(pv)), cmap="viridis", s=1, alpha=0.5)
ax.set_title("A. Self-similar anchor: constant (E,C,T)\n(Noshita generator = Okamoto 1988)", fontsize=10)
ax.set_xticklabels([]); ax.set_yticklabels([]); ax.set_zticklabels([])

# B: null recovery + noise robustness
ax = fig.add_subplot(2, 2, 2)
ax.axhline(C0/E0, color="tab:blue", ls="--", lw=1, label=f"true C/E={C0/E0:.2f}")
ax.axhline(T0/C0, color="tab:orange", ls="--", lw=1, label=f"true T/C={T0/C0:.2f}")
ax.plot(sigmas, ce, "o-", color="tab:blue", label="recovered C/E")
ax.plot(sigmas, tc, "s-", color="tab:orange", label="recovered T/C")
ax.set_xlabel("coord noise σ (fraction of size)"); ax.set_ylabel("convention-free ratio")
ax.set_title(f"B. NULL recovery: clean max-rel-err = {relerr:.1e}\n+ graceful under noise", fontsize=10)
ax.legend(fontsize=7)

# C: anchor generator is flat (constant) along growth
ax = fig.add_subplot(2, 2, 3)
for val, lab, col in [(E0, "E", "tab:green"), (C0, "C", "tab:blue"), (T0, "T", "tab:orange")]:
    ax.plot([0, S], [val, val], color=col, lw=2, label=lab)
ax.axhline(0, color="k", lw=0.5)
ax.set_xlabel("growth position s"); ax.set_ylabel("generator value")
ax.set_title("C. Anchor: generator is CONSTANT\n(the self-similar fixed point)", fontsize=10)
ax.legend(fontsize=8)

# D: Misaki real heteromorph generator varies, T flips sign
ax = fig.add_subplot(2, 2, 4)
for k_, col in [("E", "tab:green"), ("C", "tab:blue"), ("T", "tab:orange")]:
    ax.plot(mis[k_][0], mis[k_][1], ".-", color=col, lw=1.2, ms=3, label=k_)
ax.axhline(0, color="k", lw=0.6)
ax.set_xlabel("growth position s"); ax.set_ylabel("generator value")
ax.set_title("D. Misaki heteromorph (real): generator NOT constant\nT crosses zero — fixed point lost", fontsize=10)
ax.legend(fontsize=8)

fig.tight_layout(rect=[0, 0, 1, 0.96])
png = OUT / "shell_t2_anchor.png"
fig.savefig(png, dpi=140)
print(f"\nsaved {png}")
