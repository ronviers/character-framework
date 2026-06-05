"""
Refined T2 test (Ron's idea), v2: self-similarity via the allometric slope.

Self-similar (gnomonic) growth => area A ~ L^2, tube volume V ~ L^3, hence
    log A  vs  log V  is a straight line of slope 2/3   (Huxley allometry).
Fixed point  <=>  constant slope 2/3.  Loss of it  <=>  slope drifts / differs.

This reads the slope (immune to the apex additive offset, which only moves the
intercept) instead of the raw A^3/V^2 ratio. Integral observables => noise-robust.

Anchor: Noshita growing-tube generator (Okamoto 1988). Volume = tube integral
(overlap-immune). Vectorized for a fine grid.
"""
import sys, numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

PKG = r"H:\character-framework\data\shell\noshita_growing_tube\growing_tube_model_estimation-main"
sys.path.insert(0, PKG)
from growing_tube_model_estimation.growing_tube._growing_tube_model import growing_tube_model
OUT = Path(r"H:\character-framework\experiments")

E0, C0, T0, r0, S = 0.08, 0.45, 0.06, 1.0, 55.0
Ns, Nphi = 400, 100
s_vals = np.linspace(1e-6, S, Ns)
phi = np.linspace(0, 2*np.pi, Nphi, endpoint=False)
s_arr = np.repeat(s_vals, Nphi); phi_arr = np.tile(phi, Ns)
Vg = growing_tube_model(s_arr, phi_arr, E0, C0, T0, r0=r0).T.reshape(Ns, Nphi, 3)  # (Ns,Nphi,3)

def cum_area_volume(Vg):
    """cumulative wall area A(k) and tube volume V(k), vectorized."""
    p00 = Vg[:-1, :, :]; p10 = Vg[1:, :, :]
    p01 = np.roll(Vg[:-1, :, :], -1, axis=1); p11 = np.roll(Vg[1:, :, :], -1, axis=1)
    a1 = 0.5*np.linalg.norm(np.cross(p10-p00, p11-p00), axis=2)
    a2 = 0.5*np.linalg.norm(np.cross(p11-p00, p01-p00), axis=2)
    band_area = (a1 + a2).sum(axis=1)                       # (Ns-1,)
    ringvec = np.cross(Vg, np.roll(Vg, -1, axis=1)).sum(axis=1)
    Acr = 0.5*np.linalg.norm(ringvec, axis=1)               # (Ns,) cross-section area
    cen = Vg.mean(axis=1)                                    # (Ns,3) centerline
    ds = np.linalg.norm(np.diff(cen, axis=0), axis=1)        # (Ns-1,)
    band_vol = 0.5*(Acr[:-1] + Acr[1:]) * ds                # (Ns-1,)
    return np.cumsum(band_area), np.cumsum(band_vol), np.cumsum(ds)  # A, V, arclength

def _fit(x, y):
    s, b = np.polyfit(x, y, 1); return s, np.std(y - np.polyval([s, b], x))

def allometric_slope(Vg, lo=0.3, hi=1.0):
    """slopes over the upper part of growth (skip apex transient):
       A-vs-V (target 2/3), V-vs-arclength (target 3), A-vs-arclength (target 2)."""
    A, V, L = cum_area_volume(Vg)
    n = len(A); i0, i1 = int(lo*n), int(hi*n)
    lA, lV, lL = np.log(A[i0:i1]), np.log(V[i0:i1]), np.log(L[i0:i1])
    s_AV, r_AV = _fit(lV, lA)        # 2/3
    s_VL, _ = _fit(lL, lV)           # 3   (volume only)
    s_AL, _ = _fit(lL, lA)           # 2   (area only)
    return s_AV, r_AV, s_VL, s_AL, (A, V)

slope0, resid0, sVL0, sAL0, (A0, V0) = allometric_slope(Vg)
print(f"NULL (clean anchor): allometric slope = {slope0:.4f}  (self-similar target 0.6667)")
print(f"  |slope-2/3| = {abs(slope0-2/3):.4f}   log-log residual sd = {resid0:.4f}   "
      f"-> {'PASS' if abs(slope0-2/3)<0.02 and resid0<0.02 else 'check'}")

# noise robustness (levels that killed the C,T fit: >=0.005)
rng = np.random.default_rng(2)
scale = np.median(np.linalg.norm(Vg.reshape(-1, 3), axis=1))
print("\nROBUST under coord noise (C,T fit NaN at sigma>=0.005).")
print("  comparing: VOLUME-only (target 3.0) vs AREA-only (target 2.0) vs A-vs-V (0.667)")
sig_list = [0.0, 0.005, 0.01, 0.02, 0.05]; slopes = []; svol = []; sarea = []
for sg in sig_list:
    Vn = Vg + rng.normal(0, sg*scale, Vg.shape)
    sl, rs, sVL, sAL, _ = allometric_slope(Vn); slopes.append(sl); svol.append(sVL); sarea.append(sAL)
    print(f"  sigma={sg:5.3f}   V-only={sVL:5.3f} (tgt 3.0)   A-only={sAL:5.3f} (tgt 2.0)   "
          f"A-vs-V={sl:5.3f} (tgt 0.667)")
print(f"\n  -> VOLUME drift over full noise range: {abs(svol[-1]-svol[0])/svol[0]*100:4.1f}%")
print(f"  -> AREA   drift over full noise range: {abs(sarea[-1]-sarea[0])/sarea[0]*100:4.1f}%")

# ---- figure ----
fig, ax = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Refined T2 test v2: self-similarity via allometric slope (logA vs logV -> 2/3)",
             fontweight="bold")
ax[0].plot(np.log(V0), np.log(A0), ".", ms=3, color="k", label="anchor stages")
xx = np.array([np.log(V0).min(), np.log(V0).max()])
ax[0].plot(xx, 2/3*xx + (np.log(A0)[-1]-2/3*np.log(V0)[-1]), "r--", lw=1, label="slope 2/3 (self-similar)")
ax[0].set_xlabel("log V (tube volume)"); ax[0].set_ylabel("log A (wall area)")
ax[0].set_title(f"NULL: slope={slope0:.4f}, target 0.6667\nresidual sd={resid0:.4f}")
ax[0].legend(fontsize=8)
rel = lambda arr, tgt: [abs(v-tgt)/tgt*100 for v in arr]
ax[1].plot(sig_list, rel(svol, 3.0),  "o-", color="tab:green",  label="VOLUME-only (robust)")
ax[1].plot(sig_list, rel(sarea, 2.0), "s-", color="tab:red",    label="AREA-only (fragile)")
ax[1].plot(sig_list, rel(slopes, 2/3),"^-", color="tab:orange", label="A-vs-V combined")
ax[1].set_xlabel("coord noise σ (fraction of size)"); ax[1].set_ylabel("slope error vs self-similar target (%)")
ax[1].set_title("ROBUSTNESS split: volume holds, area collapses\n(C,T fit went NaN at σ≥0.005)")
ax[1].legend(fontsize=8)
fig.tight_layout(rect=[0, 0, 1, 0.95])
png = OUT / "shell_t2_volume.png"; fig.savefig(png, dpi=140)
print(f"\nsaved {png}")
