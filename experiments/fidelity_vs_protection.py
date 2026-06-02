"""
Running the L1 fidelity-floor spec on a synthetic unicyclic NESS, and settling
the precision-vs-protection (Model A vs Model B) dispute with numbers.

Object: uniform unicyclic ring, N states, total cycle affinity A, per-step a = A/N.
Rates (attempt scale 1): p = exp(a/2) forward, q = exp(-a/2) backward.
Net winding x(t): forward events ~ Poisson(p T), backward ~ Poisson(q T), independent.
Cycles J = x / N.   <x> = (p-q)T,  Var(x) = (p+q)T.

Exact, derived from first principles:
  Fano of cycles      F = Var(J)/<J> = (p+q)/(N(p-q)) = (1/N) coth(A/2N)   [saturates Barato-Seifert]
  entropy production   sigma = <J> A                                       [Schnakenberg, single cycle]
  current fidelity     Q = <J>^2/Var(J)                                    [SNR^2 of accumulated current]
  reversal LDP rate    I0 = 2(cosh(a/2)-1) = (sqrt p - sqrt q)^2            [protection proxy: P(J_T/T~0) ~ e^{-T I0}]
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
import numpy as np

def coth(x): return 1.0/np.tanh(x)

def uniform_ring(N, A, T=10.0):
    a = A/N
    p, q = np.exp(a/2), np.exp(-a/2)
    Jmean = (p-q)/N*T
    Jvar  = (p+q)/N**2*T
    return dict(a=a, p=p, q=q, Jmean=Jmean, Jvar=Jvar,
                F=Jvar/Jmean, Q=Jmean**2/Jvar, sigma=Jmean*A,
                I0=2*(np.cosh(a/2)-1))

rng = np.random.default_rng(0)

print("="*74)
print("CHECK 1  fidelity bound   sigma_total >= (A/N) coth(A/2N) * Q")
print("         uniform ring should SATURATE it (ratio = 1), and F should equal")
print("         the Barato-Seifert floor (1/N)coth(A/2N), which sits ABOVE the TUR 2/A")
print("-"*74)
print(f"{'N':>3}{'A':>7}{'F(Fano)':>12}{'BS floor':>12}{'TUR=2/A':>10}{'sigma':>11}{'alpha*Q':>11}{'ratio':>8}")
for N in (3, 6):
    for A in (1.0, 5.0, 14.5, 50.0):
        r = uniform_ring(N, A)
        bs    = coth(A/(2*N))/N
        tur   = 2.0/A
        alpha = (A/N)*coth(A/(2*N))
        print(f"{N:>3}{A:>7.1f}{r['F']:>12.6f}{bs:>12.6f}{tur:>10.6f}"
              f"{r['sigma']:>11.4f}{alpha*r['Q']:>11.4f}{r['sigma']/(alpha*r['Q']):>8.4f}")

print("\n" + "="*74)
print("CHECK 2  Monte-Carlo validation of the exact uniform formulas (N=3, A=14.5)")
print("-"*74)
N, A, T, M = 3, 14.5, 5.0, 400000
a = A/N; p, q = np.exp(a/2), np.exp(-a/2)
J = (rng.poisson(p*T, M) - rng.poisson(q*T, M))/N
r = uniform_ring(N, A, T)
print(f"  <J>  exact {r['Jmean']:.5f}   MC {J.mean():.5f}")
print(f"  Var  exact {r['Jvar']:.5f}   MC {J.var():.5f}")
print(f"  F    exact {r['F']:.5f}   MC {J.var()/J.mean():.5f}")

print("\n" + "="*74)
print("CHECK 3  non-uniform ring: bound must hold STRICTLY (uniform is the optimum).")
print("         same total A, one slow edge (heterogeneous attempt rates).")
print("-"*74)
def gillespie_ring(pv, qv, T, M, rng):
    Nn = len(pv); w = np.empty(M)
    for m in range(M):
        s = 0; x = 0; t = 0.0
        while True:
            rp, rq = pv[s], qv[s]; rt = rp+rq
            t += rng.exponential(1.0/rt)
            if t > T: break
            if rng.random() < rp/rt: s = (s+1) % Nn; x += 1
            else:                    s = (s-1) % Nn; x -= 1
        w[m] = x
    Jj = w/Nn
    return Jj.mean(), Jj.var()

N, A = 3, 14.5
a = A/N
scale = np.array([1.0, 1.0, 0.2])           # one slow edge; per-edge affinity a kept uniform
pv = scale*np.exp(a/2); qv = scale*np.exp(-a/2)
# sanity: uniform MC recovers exact F
um, uv = gillespie_ring(np.full(N, np.exp(a/2)), np.full(N, np.exp(-a/2)), 30.0, 4000, rng)
nm, nv = gillespie_ring(pv, qv, 30.0, 4000, rng)
bound = coth(A/(2*N))/N
print(f"  Barato-Seifert floor (1/N)coth(A/2N) = {bound:.5f}")
print(f"  uniform   ring  F(MC) = {uv/um:.5f}   (should match floor; validates Gillespie)")
print(f"  NON-unif. ring  F(MC) = {nv/nm:.5f}   (must be > floor)")
print(f"  -> strict: {nv/nm:.5f} > {bound:.5f}  ==> {nv/nm > bound}")

print("\n" + "="*74)
print("CHECK 4  THE DISPUTE: is Q 'protection'? does complexity make protection cheaper?")
print("         fixed total A = 14.5; vary cycle length N.")
print("-"*74)
A = 14.5
print(f"{'N':>4}{'a=A/N':>9}{'F(Fano)':>10}{'fidelity 1/F':>14}{'sigma_rate':>12}{'I0(protect)':>13}")
for N in (3, 6, 12, 24, 48):
    a = A/N; p, q = np.exp(a/2), np.exp(-a/2)
    print(f"{N:>4}{a:>9.4f}{coth(a/2)/N:>10.5f}{N/coth(a/2):>14.4f}"
          f"{(p-q)/N*A:>12.5f}{2*(np.cosh(a/2)-1):>13.6f}")
print("  -> fidelity (1/F) RISES with N; protection I0 COLLAPSES ~ (A/N)^2.")
print("     'Q' tracks fidelity, not protection: they diverge.")

print("\n  fixed-PROTECTION reading: hold reversal rate I0 fixed (=> fixed per-step a=0.8),")
print("  vary N, ask the dissipation RATE needed to sustain it:")
print(f"{'N':>4}{'A=N*a':>9}{'I0(fixed)':>11}{'sigma_rate':>12}")
af = 0.8; I0f = 2*(np.cosh(af/2)-1); p, q = np.exp(af/2), np.exp(-af/2)
for N in (3, 6, 12, 24):
    print(f"{N:>4}{N*af:>9.3f}{I0f:>11.6f}{(p-q)/N*(N*af):>12.6f}")
print("  -> at fixed protection, dissipation rate is N-INDEPENDENT (= 2 a sinh(a/2)).")
print("     PROTECTION is set by per-step affinity a, NOT cycle length N.")

print("\n" + "="*74)
print("VERDICT")
print("-"*74)
print("  L1 bound correct: uniform ring saturates sigma >= (A/N)coth(A/2N) Q (ratio 1.000),")
print("    F equals the BS floor, strict for non-uniform rings. The floor 1/N sits ABOVE")
print("    the TUR 2/A at large A: topology bounds fidelity below dissipation alone.")
print("  But Q is FIDELITY (a variance/second-moment quantity), not protection.")
print("  PROTECTION is the reversal LDP rate I0 (a tail/large-deviation quantity), set by")
print("    per-step affinity a=A/N alone. At fixed total A, longer cycles BUY FIDELITY and")
print("    LOSE protection; at fixed protection, dissipation is N-independent.")
print("  => Model A's bound is a real FIDELITY receipt (relabel Q); Model A's 'complexity is")
print("     cheaper to protect' is backwards (it's a fidelity statement). Model B is right:")
print("     precision != protection; the protection bound lives in I0 / reversal lifetime.")
