r"""strata_sort.py -- battery core: does a driven stratified medium ever MINT, or only SORT?

Ron's observation: "things falling out of strata" is a phenomenon engineers exploit
constantly (centrifugation, fluidized beds, granular segregation, distillation trays,
sedimentation) -- abundant, measured, real data -- but it is all the METRIC sector.
The battery is the discriminator: sweep a driven stratified medium and ask whether
sorting ever crosses into minting a PROTECTED current (gauge-irremovable sign(A),
drive-independent, flips only on rewiring).

Minimal model: 3 cells (size/density classes) on a ring, the minimal frustrated unit.
Two independent axes:
  - s     = stratification strength (the METRIC drive): a gradient potential V on the
            cells. Pure sorting is CURL-FREE -> cycle affinity A = 0 for any s.
  - Omega = cyclic wiring asymmetry (the TOPOLOGICAL wiring): a non-reciprocal cycle.
            A = Omega, set by the wiring, independent of s.

The protected bit = sign of the cycle affinity A = sum ln(w_ij/w_ji) around 0->1->2->0.
Forced check (Schnakenberg): sign(A) == sign(NESS cycle current).

ASCII-only output (Windows console safety).
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import numpy as np

V = np.array([0.0, 1.0, 2.0])          # stratification potential on the 3 cells
RING = [(0, 1), (1, 2), (2, 0)]


def rates(s, Omega, base=1.0):
    """ln(w_ij/w_ji) = s*(V_i - V_j) + Omega/3 on each ring edge.
    -> gradient part sums to 0 around the cycle (curl-free sorting);
       cyclic part sums to Omega (the protected affinity)."""
    e = {}
    for (i, j) in RING:
        h = 0.5 * (s * (V[i] - V[j]) + Omega / 3.0)
        e[(i, j)] = base * np.exp(h)
        e[(j, i)] = base * np.exp(-h)
    return e


def generator(n, edges):
    Q = np.zeros((n, n))
    for (i, j), r in edges.items():
        Q[i, j] += r
    for i in range(n):
        Q[i, i] = -np.sum(Q[i, :])
    return Q


def stationary(Q):
    n = Q.shape[0]
    A = Q.T.copy()
    A[-1, :] = 1.0
    b = np.zeros(n)
    b[-1] = 1.0
    return np.linalg.solve(A, b)


def cycle_affinity(edges):
    return sum(np.log(edges[(i, j)] / edges[(j, i)]) for (i, j) in RING)


def cycle_current(edges):
    p = stationary(generator(3, edges))
    return p[0] * edges[(0, 1)] - p[1] * edges[(1, 0)]


def sortedness(edges):
    """how stratified the occupancy is: max cell occupancy minus the uniform 1/3."""
    p = stationary(generator(3, edges))
    return p.max() - 1.0 / 3.0


print("=" * 76)
print("STRATA-SORT BATTERY -- does a driven stratified medium SORT or MINT?")
print("=" * 76)

# ---- Sweep 1: pure sorting (Omega = 0). Crank the stratification. ----
print("\n[1] PURE SORTING  (Omega=0): sweep stratification strength s")
print("    s        sortedness   cycle-affinity A   protected current")
for s in [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]:
    e = rates(s, 0.0)
    A = cycle_affinity(e)
    J = cycle_current(e)
    print(f"    {s:4.1f}     {sortedness(e):8.4f}     {A:+.2e}        {J:+.2e}")
print("    --> sortedness rises (metric scale-selection), A == 0 to machine zero for")
print("        EVERY s: no amount of sorting/separation mints a protected current.")

# ---- Sweep 2: minting axis (Omega != 0). The protected current vs the metric drive. ----
print("\n[2] MINTING AXIS  (Omega=2 wiring): sweep the SAME metric drive s")
print("    s        sortedness   cycle-affinity A   sign(A)   current")
signs = []
for s in [0.0, 1.0, 2.0, 4.0, 8.0]:
    e = rates(s, 2.0)
    A = cycle_affinity(e)
    J = cycle_current(e)
    signs.append(np.sign(A))
    print(f"    {s:4.1f}     {sortedness(e):8.4f}     {A:+.4f}        {int(np.sign(A)):+d}     {J:+.4f}")
drive_indep = len(set(signs)) == 1
print(f"    --> A is fixed by the wiring (=Omega), INDEPENDENT of the metric drive s;")
print(f"        sign(A) constant across the whole sorting sweep: {drive_indep}")

# ---- Rewire test: flip the wiring sign. ----
print("\n[3] REWIRE  (Omega: +2 -> -2 at fixed strong sorting s=4)")
ep = rates(4.0, +2.0)
em = rates(4.0, -2.0)
print(f"    Omega=+2: A={cycle_affinity(ep):+.4f}  current={cycle_current(ep):+.4f}")
print(f"    Omega=-2: A={cycle_affinity(em):+.4f}  current={cycle_current(em):+.4f}")
flips = np.sign(cycle_affinity(ep)) != np.sign(cycle_affinity(em))
print(f"    --> the protected sign flips ONLY by rewiring the cyclic asymmetry: {flips}")

# ---- forced check across the board ----
forced = all(
    np.sign(cycle_affinity(rates(s, w))) == np.sign(cycle_current(rates(s, w)))
    or abs(cycle_affinity(rates(s, w))) < 1e-12
    for s in [0.0, 2.0, 4.0] for w in [-2.0, 0.0, 2.0]
)

print("\n" + "=" * 76)
print("OBSERVED:")
print("  - sorting (metric) and minting (topological) are INDEPENDENT axes")
print("  - sorting, however strong, mints nothing (A == 0 on the whole s-sweep)")
print("  - a protected current requires FRUSTRATED WIRING, not separation")
print(f"  - once wired, sign(A) is drive/sort-independent (flips only on rewiring): "
      f"{drive_indep and flips}")
print(f"  - forced-not-fitted (sign A == sign current) throughout: {forced}")
print("=" * 76)
print("READING: the engineering separation corpus lives on the SORTING axis (A=0) --")
print("  abundant, real, and confirmed STAGE-not-actor. The battery's scan is for the")
print("  rare exception: a driven stratified/segregating medium whose inter-strata")
print("  transport carries a sort-INDEPENDENT circulation (sign fixed by geometry,")
print("  flipping only on rewiring) -- a protected current minted on a real medium.")
