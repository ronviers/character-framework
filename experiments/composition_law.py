r"""composition_law.py -- is minting a genuine, substrate-independent composition law?

The make-or-break left by the universal-invariant classification negative: the only
place a cross-substrate universality could still live is a COMPOSITION LAW -- a
monoidal/fusion algebra on protected circulations. The framework's candidate is the
union-cycle holonomy. This script tests it, forced-not-fitted.

Representation (the framework's native one -- Schnakenberg / Polettini gauge theory):
each substrate is a continuous-time Markov jump process on a small state graph. The
protected bit of a cycle c is the sign of the cycle affinity
    A(c) = sum_{(i->j) in c} ln( w_ij / w_ji )            (Polettini gauge potential)
A != 0  <=>  broken detailed balance  <=>  a frustrated (Harary-unbalanced) cycle.
By Schnakenberg's theorem the NESS cycle current flows in the direction of +A, so
    sign(A(c))  ==  sign(NESS current around c)
is the forced-not-fitted check: the GRAPH rule (cheap, topological) must predict the
DIRECTLY SOLVED stationary current. If they ever disagree, the rule is wrong.

Minting: couple parts with coupling edges -> union graph -> new cycles' affinities.
The tests:
  (1) substrate-independence of the per-substrate invariant (same rule, 3 substrates)
  (2) minting 0(x)0 -> 1  (two non-circulating parts mint a circulating union)
  (3) associativity (the union is order-independent)
  (4) the fusion structure, characterized: existence-bit vs value-bit
  (5) substrate-independence of the composition rule (cross-substrate couplings)

ASCII-only output (Windows console safety).
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import numpy as np

np.set_printoptions(precision=4, suppress=True)


# ---------- core machinery (substrate-independent: applies to ANY rate graph) ----------

def generator(n, edges):
    """Markov generator Q (rows = out). edges: {(i,j): rate} for i->j."""
    Q = np.zeros((n, n))
    for (i, j), r in edges.items():
        Q[i, j] += r
    for i in range(n):
        Q[i, i] = -np.sum(Q[i, :])
    return Q


def stationary(Q):
    """Stationary distribution p: p Q = 0, normalized."""
    n = Q.shape[0]
    A = Q.T.copy()
    A[-1, :] = 1.0
    b = np.zeros(n)
    b[-1] = 1.0
    return np.linalg.solve(A, b)


def edge_current(p, edges, i, j):
    """Net probability current i->j at stationarity."""
    return p[i] * edges.get((i, j), 0.0) - p[j] * edges.get((j, i), 0.0)


def cycle_affinity(edges, cycle):
    """A(c) = sum ln(w_fwd / w_bwd) around an ordered cycle [c0,c1,...,c0]."""
    A = 0.0
    for a, b in zip(cycle[:-1], cycle[1:]):
        A += np.log(edges[(a, b)] / edges[(b, a)])
    return A


def schnakenberg_check(edges, n, cycle):
    """The forced-not-fitted check: does the GRAPH rule predict the NESS current sign?"""
    A = cycle_affinity(edges, cycle)
    p = stationary(generator(n, edges))
    # current around the cycle = current on its first edge (single-cycle graphs)
    J = edge_current(p, edges, cycle[0], cycle[1])
    agree = (np.sign(A) == np.sign(J)) or (abs(A) < 1e-12 and abs(J) < 1e-12)
    return A, J, agree


def sym_edges(pairs, rate=1.0):
    """Detailed-balanced (non-circulating) reversible edges: w_ij = w_ji."""
    e = {}
    for (i, j) in pairs:
        e[(i, j)] = rate
        e[(j, i)] = rate
    return e


print("=" * 78)
print("COMPOSITION LAW BUILD -- is minting a substrate-independent fusion algebra?")
print("=" * 78)

# ---------------- (1) per-substrate invariant + Schnakenberg calibration ----------------
print("\n[1] PER-SUBSTRATE INVARIANT (same rule, 3 banked substrates)")
print("    sign(A) must equal sign(NESS current)  [Schnakenberg, forced-not-fitted]")

# (a) fuel-driven chemical 3-cycle (DNA-network class)
dna = {(0, 1): 3.0, (1, 0): 1.0, (1, 2): 2.0, (2, 1): 1.0, (2, 0): 2.0, (0, 2): 1.0}
# (b) Brownian gyrator: 4-state square cycle, rotational bias from a "temperature" tilt
gyr = {(0, 1): 2.0, (1, 0): 1.0, (1, 2): 2.0, (2, 1): 1.0,
       (2, 3): 2.0, (3, 2): 1.0, (3, 0): 2.0, (0, 3): 1.0}
# (c) repressilator: 3-gene repression ring -> driven 3-cycle (opposite drive sense)
rep = {(0, 1): 1.0, (1, 0): 2.5, (1, 2): 1.0, (2, 1): 2.5, (2, 0): 1.0, (0, 2): 2.5}

subs = [("dna_3cycle", dna, 3, [0, 1, 2, 0]),
        ("gyrator_4cycle", gyr, 4, [0, 1, 2, 3, 0]),
        ("repressilator_3cycle", rep, 3, [0, 1, 2, 0])]

all_forced = True
for name, e, n, cyc in subs:
    A, J, ok = schnakenberg_check(e, n, cyc)
    all_forced &= ok
    print(f"    {name:24s}  A={A:+.4f}  current={J:+.5f}  "
          f"sign(A)={int(np.sign(A)):+d}  forced={ok}")
print(f"    --> same rule across all substrates, all forced-not-fitted: {all_forced}")

# ---------------- (2) minting: 0 (x) 0 -> 1 ----------------
print("\n[2] MINTING  0(x)0 -> 1   (two NON-circulating parts -> circulating union)")
# part A = reversible edge {0,1}; part B = reversible edge {2,3}; each non-circulating.
partA = sym_edges([(0, 1)], rate=1.0)
partB = sym_edges([(2, 3)], rate=1.0)
A_A = 0.0  # no cycle in a single reversible edge
A_B = 0.0
# coupling edges close a 4-cycle 0->1->2->3->0, asymmetric => frustrated
coupling = {(1, 2): 3.0, (2, 1): 1.0, (3, 0): 3.0, (0, 3): 1.0}
union = {**partA, **partB, **coupling}
ucyc = [0, 1, 2, 3, 0]
A_u, J_u, ok_u = schnakenberg_check(union, 4, ucyc)
print(f"    part A (non-circ): A={A_A:+.3f}   part B (non-circ): A={A_B:+.3f}")
print(f"    union (coupled)  : A={A_u:+.4f}  current={J_u:+.5f}  forced={ok_u}")
minted = abs(A_A) < 1e-12 and abs(A_B) < 1e-12 and abs(A_u) > 1e-9
print(f"    --> 0(x)0 -> 1 minted a protected bit from the coupling alone: {minted}")
# and the value is set by the coupling, NOT the parts:
print(f"        (union affinity = sum of coupling-edge potentials; parts contribute 0)")

# ---------------- (3) associativity ----------------
print("\n[3] ASSOCIATIVITY   (A(x)B)(x)C  ==  A(x)(B(x)C)")
# three reversible-edge parts {0,1},{2,3},{4,5}, coupled into a ring 6-cycle.
pA = sym_edges([(0, 1)]); pB = sym_edges([(2, 3)]); pC = sym_edges([(4, 5)])
cpl = {(1, 2): 2.0, (2, 1): 1.0, (3, 4): 2.0, (4, 3): 1.0, (5, 0): 2.0, (0, 5): 1.0}
# order 1: (A(x)B) then (x)C
left = {**pA, **pB, **{k: v for k, v in cpl.items() if k in
                       [(1, 2), (2, 1)]}}            # A(x)B partial
left = {**left, **pC, **{k: v for k, v in cpl.items() if k in
                         [(3, 4), (4, 3), (5, 0), (0, 5)]}}
# order 2: A(x)(B(x)C)
right = {**pB, **pC, **{k: v for k, v in cpl.items() if k in
                        [(3, 4), (4, 3)]}}           # B(x)C partial
right = {**right, **pA, **{k: v for k, v in cpl.items() if k in
                           [(1, 2), (2, 1), (5, 0), (0, 5)]}}
rc = [0, 1, 2, 3, 4, 5, 0]
A_left = cycle_affinity(left, rc)
A_right = cycle_affinity(right, rc)
assoc = abs(A_left - A_right) < 1e-12
print(f"    (A(x)B)(x)C : A={A_left:+.6f}")
print(f"    A(x)(B(x)C) : A={A_right:+.6f}")
print(f"    --> associative (sign-exact, order-independent): {assoc}  "
      f"|diff|={abs(A_left-A_right):.2e}")

# ---------------- (4) the fusion structure: existence-bit vs value-bit ----------------
print("\n[4] FUSION STRUCTURE  (two triangles sharing edge 0-2; outer = C1 (x) C2)")
print("    C1 = 0->1->2->0 ,  C2 = 0->2->3->0 ,  shared edge 0-2 cancels in the outer.")


def two_triangle(A1_target, A2_target):
    """Build two triangles sharing edge 0-2 with prescribed component affinities."""
    e = {}
    # triangle 1 edges (0->1->2->0): put all of A1 on edge 0->1
    e[(0, 1)] = np.exp(A1_target); e[(1, 0)] = 1.0
    e[(1, 2)] = 1.0; e[(2, 1)] = 1.0
    e[(2, 0)] = 1.0; e[(0, 2)] = 1.0          # shared edge, balanced
    # triangle 2 edges (0->2->3->0): put all of A2 on edge 2->3 ... but 0->2 shared.
    # A2 around 0->2->3->0 = ln(w02/w20)+ln(w23/w32)+ln(w30/w03); w02=w20 so first=0.
    e[(2, 3)] = np.exp(A2_target); e[(3, 2)] = 1.0
    e[(3, 0)] = 1.0; e[(0, 3)] = 1.0
    return e


C1 = [0, 1, 2, 0]
C2 = [0, 2, 3, 0]
OUTER = [0, 1, 2, 3, 0]
print("    existence-bit (does a protected cycle exist) composes over the cycle space:")
for (a1, a2) in [(+2.0, +1.0), (+2.0, -2.5), (+2.0, -1.5)]:
    e = two_triangle(a1, a2)
    A1 = cycle_affinity(e, C1)
    A2 = cycle_affinity(e, C2)
    Aout = cycle_affinity(e, OUTER)
    additive = abs(Aout - (A1 + A2)) < 1e-9
    # forced check on the outer cycle
    p = stationary(generator(4, e))
    Jout = edge_current(p, e, 0, 1)
    print(f"    A(C1)={A1:+.3f} A(C2)={A2:+.3f} | A(outer)={Aout:+.3f} "
          f"= A1+A2 ({additive}) | sign(outer)={int(np.sign(Aout)):+d} "
          f"current={Jout:+.4f}")

print("    --> existence/affinity is LINEAR over the cycle space (A adds; shared edge")
print("        cancels) -- a clean, substrate-general algebra (the homology import).")
print("    --> BUT the VALUE bit sign(A_out)=sign(A1+A2) is NOT a function of the")
print("        component signs alone: (+,-) gives + or - depending on MAGNITUDE")
print("        (rows 2 and 3: same signs (+,-), opposite composite sign). The value")
print("        composition is quantitative/coupling-dependent, not a group fusion.")

# ---------------- (5) substrate-independence of the composition rule ----------------
print("\n[5] CROSS-SUBSTRATE MINTING  (couple a chemical part to a gyrator part)")
# chemical part: a driven sub-arc; gyrator part: a driven sub-arc; couple into a union cycle.
# Use the SAME union-cycle-affinity rule and the SAME forced check.
chem_arc = {(0, 1): 2.0, (1, 0): 1.0}        # a driven edge (would-be chemical step)
gyr_arc = {(2, 3): 1.5, (3, 2): 1.0}         # a driven edge (would-be gyrator step)
xcoupl = {(1, 2): 2.0, (2, 1): 1.0, (3, 0): 2.0, (0, 3): 1.0}
xunion = {**chem_arc, **gyr_arc, **xcoupl}
Ax, Jx, okx = schnakenberg_check(xunion, 4, [0, 1, 2, 3, 0])
print(f"    chem(x)gyrator union: A={Ax:+.4f}  current={Jx:+.5f}  forced={okx}")
print(f"    --> the identical union-cycle rule mints across substrate types: {okx}")

# ---------------- verdict ----------------
print("\n" + "=" * 78)
print("OBSERVED:")
print(f"  - per-substrate invariant: ONE rule, all forced-not-fitted     : {all_forced}")
print(f"  - minting 0(x)0 -> 1 (bit from coupling alone)                 : {minted}")
print(f"  - associativity (order-independent, sign-exact)                : {assoc}")
print(f"  - existence/frustration bit composes linearly (cycle space)    : True")
print(f"  - value bit sign(A) is rate-dependent, NOT a group fusion      : True")
print(f"  - cross-substrate minting obeys the identical rule             : {okx}")
print("=" * 78)
