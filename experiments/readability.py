r"""readability.py -- battery: the READING TRANSITION as an order parameter.

The abiogenesis arc's load-bearing beam (the strong-model read: "define reading
before heredity -- the framework lives or dies there"). Reading splits the way
reproduction splits:

    metric reading : ecology modulates rate / occupancy / throughput.  dM/dE != 0.
                     instantaneous, generic, pre-heredity. (the cross-rule.)
    bit reading    : ecology modulates the protected sign(A).         dA/dE != 0.
                     NOT within a lifetime -- barred by superselection. Only across
                     replacement (selection over a lineage) = proto-heredity.

The superselection structure (transverse-decomposition theorem, pa:transverse-
decomposition) FORBIDS the instantaneous route: an ecological field couples to the
metric (gradient / curl-free) degrees of freedom, and the protected sign lives in
the orthogonal (cyclic / curl) sector. So ecology can speed the loop up, slow it
down, reshape occupancies -- but it cannot continuously deform the sign.

The only channel from the metric sector into the topological sector is SELECTION:

    metric ecology  -->  population replacement  -->  bit retention

acting almost like a projection operator. No instantaneous route exists; only the
population route. The order parameter is therefore evaluated over a LINEAGE, not a
lifetime:

    R_hard  =  d<sign A> / d(ecology)   over replacement.

    below threshold:  R_hard = 0   (ecology modulates metrics only)
    above threshold:  R_hard != 0  (ecological distinctions sort the inherited sign)

The threshold is the symmetry break delta (TDT move 3: the bit channel reopens
~ delta, zero iff symmetric). And R_hard != 0 needs BOTH the replacement channel
(heritable variation) AND the symmetry break -- so hard reading and heredity are
the SAME bridge seen from opposite sides: reader and heredity co-emerge at the bit.

Built on the strata_sort / composition_law machinery (Schnakenberg / Polettini
gauge representation). Forced-not-fitted throughout: the GRAPH rule sign(A) must
equal the directly-solved NESS current sign.

ASCII-only output (Windows console safety).
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import numpy as np

# ---- the protected 3-loop --------------------------------------------------
RING = [(0, 1), (1, 2), (2, 0)]
V = np.array([0.0, 1.0, 2.0])     # fixed background stratification potential (metric)
U = np.array([0.0, 1.0, 0.3])     # ecological-field shape -- a gradient/potential (metric)
OMEGA0 = 2.0                      # built-in cyclic wiring magnitude (the bit's carrier)
STRAT = 0.6                       # fixed background stratification strength


def rates(d, b, base=1.0):
    r"""Per-edge log-ratio  ln(w_ij/w_ji) = STRAT*(V_i-V_j) + d*(U_i-U_j) + b*OMEGA0/3.
    The first two terms are GRADIENTS (telescope to 0 around the cycle); the third is
    the CYCLIC wiring. Hence A = sum = b*OMEGA0 -- the ecological field d, however
    strong, contributes EXACTLY 0 to the affinity (curl-free). b in {+1,-1} = the bit."""
    e = {}
    for (i, j) in RING:
        aff = STRAT * (V[i] - V[j]) + d * (U[i] - U[j]) + b * OMEGA0 / 3.0
        h = 0.5 * aff
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


def current(edges):
    """Signed NESS cycle current (carries the sign of the bit)."""
    p = stationary(generator(3, edges))
    return p[0] * edges[(0, 1)] - p[1] * edges[(1, 0)]


def occupancy(edges):
    return stationary(generator(3, edges))


print("=" * 78)
print("READABILITY BATTERY -- the reading transition as an order parameter")
print("=" * 78)

# =====================================================================
# [1] METRIC READING (within a lifetime): cheap, generic, turns on.
# =====================================================================
print("\n[1] METRIC READING  (single lifetime): sweep the ecological field d")
print("    d        occ(cell0,1,2)              |current|     A=sign-carrier")
ds = [-2.0, -1.0, 0.0, 1.0, 2.0]
occ0, Jmag0 = None, None
for d in ds:
    e = rates(d, +1)
    p = occupancy(e)
    J = current(e)
    print(f"   {d:+4.1f}     [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]        "
          f"{abs(J):8.4f}     {cycle_affinity(e):+.4f}")
# numeric metric readability d(observable)/dd at d=0
eps = 1e-4
dOcc = (occupancy(rates(eps, +1))[0] - occupancy(rates(-eps, +1))[0]) / (2 * eps)
dJ = (abs(current(rates(eps, +1))) - abs(current(rates(-eps, +1)))) / (2 * eps)
metric_on = abs(dOcc) > 1e-6 and abs(dJ) > 1e-6
print(f"    --> metric readability  d(occ0)/dd = {dOcc:+.4f},  d|J|/dd = {dJ:+.4f}")
print(f"        cheap reading turns on GENERICALLY (ecology reshapes the metric): {metric_on}")

# =====================================================================
# [2] BIT READING within a lifetime is FORBIDDEN  (superselection null / KILL-SWITCH)
# =====================================================================
print("\n[2] BIT READING  (single lifetime): is sign(A) readable by ecology d?")
print("    sweep d at fixed wiring -- A must be INVARIANT (gradient is curl-free)")
A_vals, forced = [], True
for d in ds:
    e = rates(d, +1)
    A = cycle_affinity(e)
    J = current(e)
    A_vals.append(A)
    forced &= (np.sign(A) == np.sign(J))
dA = (cycle_affinity(rates(eps, +1)) - cycle_affinity(rates(-eps, +1))) / (2 * eps)
A_spread = max(A_vals) - min(A_vals)
# the affinity is INVARIANT (the d-term telescopes to exactly 0 around the cycle);
# the verdict reads off that invariance directly. The finite-difference d(A)/dd
# divides a machine-eps numerator by 2*eps and so floors at ~eps_mach/eps ~ 1e-12.
superselect = A_spread < 1e-12 and abs(dA) < 1e-9
print(f"    A across the whole d-sweep: spread = {A_spread:.2e}   "
      f"d(A)/dd = {dA:+.2e}  (finite-diff rounding floor; true value 0)")
print(f"    --> bit readability within a lifetime = 0 to machine precision: {superselect}")
print(f"        no instantaneous route to the sign; sign(A)==sign(current) (forced): {forced}")
print(f"    [KILL-SWITCH: if d(A)/dd were != 0 here, superselection is violated -> framework breaks]")

# =====================================================================
# [3] THE POPULATION ROUTE:  R_hard over a lineage
#     selection on metric work-harvest  w(b;d) = exp( delta * J(b;d) * d )
#     -- harvest = overlap of the loop's current with the ecological flux.
#     delta = the geometric overlap / symmetry break (the "rewiring" knob).
# =====================================================================
def equilibrium_b(d, delta, heritable=True, mu=0.02, tol=1e-12, itmax=20000):
    """Selection-replacement fixed point. Returns <b> = 2 x_+ - 1.
    Selection weights survival by metric harvest (reads only the metric sector);
    reproduction either copies the parent's bit (heritable) or draws it fresh
    (degenerate replication -- the pattern persists, the bit does not)."""
    Jp = current(rates(d, +1))
    Jm = current(rates(d, -1))
    fp = np.exp(delta * Jp * d)
    fm = np.exp(delta * Jm * d)
    x = 0.5
    for _ in range(itmax):
        xs = x * fp / (x * fp + (1 - x) * fm)          # selection (survival)
        if heritable:
            xn = (1 - mu) * xs + mu * (1 - xs)         # inherit parent bit + mutate
        else:
            xn = 0.5                                   # offspring bit independent of parent
        if abs(xn - x) < tol:
            x = xn
            break
        x = xn
    return 2 * x - 1


def R_hard(delta, heritable=True, eps=0.05):
    """Order parameter: d<b>/dd at d=0, evaluated over the lineage (selection eq.)."""
    return (equilibrium_b(+eps, delta, heritable)
            - equilibrium_b(-eps, delta, heritable)) / (2 * eps)


print("\n[3] BIT READING over a LINEAGE:  <b> = mean inherited sign vs ecological field d")
print("    (a) delta=0  (current TRANSVERSE to the flux -- symmetric):")
print("        d        <b>(inherited sign)")
flat = []
for d in ds:
    bbar = equilibrium_b(d, delta=0.0)
    flat.append(bbar)
    print(f"       {d:+4.1f}     {bbar:+.4f}")
below = max(abs(np.array(flat))) < 1e-9
print(f"    --> <b> flat in d: ecology modulates the METRIC only, never the sign. "
      f"R_hard=0: {below}")

print("\n    (b) delta=2  (current OVERLAPS the flux -- symmetry broken / rewired):")
print("        d        <b>(inherited sign)")
tracks = []
for d in ds:
    bbar = equilibrium_b(d, delta=2.0)
    tracks.append(bbar)
    print(f"       {d:+4.1f}     {bbar:+.4f}")
above = (tracks[0] < -0.05 and tracks[-1] > 0.05)   # <b> follows the sign of d
print(f"    --> <b> now TRACKS d: ecology sorts the inherited sign through selection. "
      f"R_hard!=0: {above}")
print(f"        the bit became readable -- but ONLY across replacement, never instantly.")

# =====================================================================
# [4] THE ORDER PARAMETER:  R_hard vs the symmetry break delta
# =====================================================================
print("\n[4] ORDER PARAMETER:  R_hard(delta)  (the reading transition)")
print("    delta     R_hard       R_hard/delta")
deltas = [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]
Rs = []
for dl in deltas:
    R = R_hard(dl)
    Rs.append(R)
    ratio = (R / dl) if dl > 0 else float("nan")
    print(f"    {dl:4.2f}     {R:+.4f}      {ratio if dl>0 else 0.0:+.4f}")
turns_on_at_zero = abs(Rs[0]) < 1e-9 and Rs[-1] > 0.0
# near-threshold linearity: R_hard ~ delta as delta -> 0
lin = abs((Rs[1] / deltas[1]) - (Rs[2] / deltas[2])) < 0.25 * abs(Rs[1] / deltas[1])
print(f"    --> R_hard = 0 at delta=0, rises for delta>0 (zero iff symmetric): {turns_on_at_zero}")
print(f"        ~ linear near threshold (R_hard/delta ~ const, TDT move 3): {lin}")

# =====================================================================
# [5] CO-EMERGENCE:  reader and heredity are the same bridge
#     two axes -- (i) replacement channel: does reproduction COPY the bit?
#                 (ii) symmetry break delta: can metric fitness SEE the bit?
# =====================================================================
print("\n[5] CO-EMERGENCE  (R_hard over the four corners)")
print("    replacement      symmetry-break     R_hard")
corners = [
    ("degenerate", "delta=0", False, 0.0),
    ("degenerate", "delta=2", False, 2.0),
    ("heritable ", "delta=0", True, 0.0),
    ("heritable ", "delta=2", True, 2.0),
]
live = {}
for rep, sym, herit, dl in corners:
    R = R_hard(dl, heritable=herit)
    live[(herit, dl)] = R
    print(f"    {rep}       {sym}            {R:+.4f}")
only_both = (abs(live[(False, 0.0)]) < 1e-9 and abs(live[(False, 2.0)]) < 1e-9
             and abs(live[(True, 0.0)]) < 1e-9 and live[(True, 2.0)] > 0.05)
print(f"    --> R_hard != 0 ONLY when BOTH the replacement channel AND the symmetry")
print(f"        break are open -- hard reading and heredity co-emerge at the bit: {only_both}")

# =====================================================================
print("\n" + "=" * 78)
print("OBSERVED:")
print(f"  - metric reading turns on generically within a lifetime (dM/dd != 0)   : {metric_on}")
print(f"  - bit reading within a lifetime = 0 (superselection, gradient curl-free): {superselect}")
print(f"  - sign(A) == sign(NESS current) throughout (forced-not-fitted)          : {forced}")
print(f"  - R_hard = 0 below threshold (delta=0): ecology modulates metric only    : {below}")
print(f"  - R_hard != 0 above threshold: selection sorts the inherited sign        : {above}")
print(f"  - R_hard(delta) turns on at delta=0, ~linear near threshold              : {turns_on_at_zero and lin}")
print(f"  - R_hard != 0 needs BOTH replacement AND symmetry break (co-emergence)   : {only_both}")
print("=" * 78)
print("READING: 'reading' is two things in different superselection sectors. Metric")
print("  reading is everywhere and instantaneous; it is the cross-rule, pre-heredity.")
print("  Bit reading is barred from any within-lifetime route -- it exists ONLY as a")
print("  channel across replacement (selection as a projection operator from the metric")
print("  sector into the topological one). So the first reader of the protected sector")
print("  and the onset of heredity are the SAME transition viewed from opposite sides:")
print("  from ecology, 'a distinction becomes able to affect a protected bit'; from the")
print("  lineage, 'a protected bit becomes able to survive replacement.' The tape stays")
print("  unforced; carbon stays contingent; the reader is the one novel object.")
print("=" * 78)
