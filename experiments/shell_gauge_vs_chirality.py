"""
Extrude-along-path (CG sweep) vs growing tube: which bit is gauge, which is protected.

Ron's observation: in a sweep, flipping the PATH or the PROFILE flips the surface NORMAL.
Claim: that normal is a Z2 GAUGE bit (two different relabelings each flip it -> removable,
soft/metric sector). The COILING CHIRALITY (sign of torsion) is the PROTECTED bit:
invariant under path-reverse AND profile-reverse, flipped ONLY by an ambient reflection
(a discrete mirror = "rewiring"). Demonstrate both, in the actual growing-tube generator.
"""
import sys, numpy as np
PKG = r"H:\character-framework\data\shell\noshita_growing_tube\growing_tube_model_estimation-main"
sys.path.insert(0, PKG)
from growing_tube_model_estimation.growing_tube._growing_tube_model import growing_tube_model

E0, C0, T0, r0, S, Ns, Nphi = 0.08, 0.45, 0.06, 1.0, 50.0, 300, 60
s = np.linspace(1e-6, S, Ns); phi = np.linspace(0, 2*np.pi, Nphi, endpoint=False)
U = growing_tube_model(np.repeat(s, Nphi), np.tile(phi, Ns), E0, C0, T0, r0=r0).T.reshape(Ns, Nphi, 3)
cen = U.mean(axis=1)

def torsion_sign(c):
    c1 = np.gradient(c, axis=0); c2 = np.gradient(c1, axis=0); c3 = np.gradient(c2, axis=0)
    tau = np.einsum('ij,ij->i', np.cross(c1, c2), c3)        # numerator of torsion
    return int(np.sign(np.median(tau[5:-5])))

def normal_sign(grid, c, i=Ns//2, j=Nphi//2):
    n = np.cross(grid[i+1, j]-grid[i, j], grid[i, (j+1) % grid.shape[1]]-grid[i, j])
    return int(np.sign(np.dot(n, grid[i, j]-c[i])))         # +1 = outward

base_tau, base_nrm = torsion_sign(cen), normal_sign(U, cen)
print(f"{'operation':22} {'surface normal':>15} {'coiling chirality':>18}")
print(f"{'-'*22} {'-'*15} {'-'*18}")
print(f"{'identity':22} {base_nrm:+15d} {base_tau:+18d}")

# PATH reverse: reverse the s-ordering (traverse aperture->apex)
Up, cp = U[::-1], cen[::-1]
print(f"{'reverse PATH':22} {normal_sign(Up, cp):+15d} {torsion_sign(cp):+18d}")

# PROFILE reverse: reverse the phi-winding of the circle
Uf = U[:, ::-1]
print(f"{'reverse PROFILE':22} {normal_sign(Uf, cen):+15d} {torsion_sign(cen):+18d}")

# reverse BOTH (two gauge flips compose)
Ub, cb = U[::-1, ::-1], cen[::-1]
print(f"{'reverse BOTH':22} {normal_sign(Ub, cb):+15d} {torsion_sign(cb):+18d}")

# AMBIENT REFLECTION (mirror x): the only thing that flips chirality
M = np.array([-1, 1, 1]); Um, cm = U*M, cen*M
print(f"{'mirror (reflect)':22} {normal_sign(Um, cm):+15d} {torsion_sign(cm):+18d}")

print("\nReading: the normal is GAUGE (flipped by path OR profile relabeling, info-free).")
print("Chirality is PROTECTED (survives both relabelings; flips ONLY under reflection = rewiring).")
