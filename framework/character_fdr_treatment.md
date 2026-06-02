# Character — fluctuation–dissipation and the two-frame structure

Scope: how fluctuation–dissipation relations enter the framework, the two conjugate frames they
split into, and why those frames are the two faces of one dissipation. The central structural
commitment — *a protected steady current requires a frustrated cycle* — is **derived** here as the
falsifiable direction of an iff-chain, not asserted. As in [`character.md`](character.md), the
machinery is imported and named; what is owned is the reading and the falsifiers (closing section).

## The NESS-general relation

For a stochastic process, fluctuation and response are two observables,
$$C(t,t')=\langle x(t)x(t')\rangle,\qquad R(t,t')=\frac{\delta\langle x(t)\rangle}{\delta h(t')}.$$
At equilibrium they are tied by $1/T$. Away from equilibrium the general form (Cugliandolo–Kurchan)
inserts a **fluctuation–dissipation ratio** $X$:
$$R(t,t')=\frac{X(t,t')}{T}\,\frac{\partial C(t,t')}{\partial t'}\,\theta(t-t'),\qquad X\equiv1\ \text{at equilibrium}.$$
On the FD plot ($\chi$ vs $1-C/C(0)$) the local slope is the effective temperature $T_{\text{eff}}=T/X$.
The aging slope $\alpha_s$ and plateau $P_s$ (Cugliandolo–Kurchan) are the load-bearing
cross-substrate observables.

## Dissipation without a temperature (Harada–Sasa)

The departure of fluctuation from response, integrated, **is** the dissipation rate — no absolute
temperature needed (Harada–Sasa):
$$\textstyle\int(\text{FDR departure})=\langle\sigma\rangle.$$
In velocity form, $J_{\text{diss}}=\gamma\big[\langle v\rangle^2+\int\frac{d\omega}{2\pi}(\tilde C(\omega)-2T\tilde R'(\omega))\big]$,
the integrand vanishing at equilibrium. This is the hinge: it lets one dissipation be read two ways.

## Two conjugate frames

One dissipation, two readings (that the FDR-departure and the precision–cost are connected readings
of one dissipation is a concurrent recognition in the field):

- **External frame** — (amplitude × field) $\to$ the ratio $X$. Defined wherever a probe couples;
  **substrate-conditional** (it needs a probe matched to the substrate). Observables $\alpha_s,P_s$.
- **Self-probe frame** — (current × affinity) $\to$ the tightness $\mathcal{T}$, the thermodynamic
  uncertainty relation (Barato–Seifert; Horowitz–Gingrich):
  $$\mathcal{T}=\langle\sigma\rangle\,\frac{\mathrm{Var}(J)}{2\langle J\rangle^{2}}\ge1,\qquad
  \mathrm{SNR}_J=\frac{\langle J\rangle^{2}}{\mathrm{Var}(J)}\le\frac{\langle\sigma\rangle}{2}.$$
  Dimensionless (affinity in nats). **Defined iff a steady current exists.**

**Definedness asymmetry (the load-bearing fact).** The external frame is defined wherever a probe
couples; the self-probe is defined iff a current exists. This is what makes the self-probe
*intrinsic* — no external probe, no substrate-matching — and the frame's very *existence* is a
diagnostic: a substrate carries the self-probe frame iff it carries a protected current. The two
frames are not parallel by construction; they coincide only where the self-probe is defined.

**Bridge** (Harada–Sasa): $V_{\text{ext}}=\langle\sigma\rangle=J\cdot\mathcal{A}$ — the
externally-integrated departure equals current × affinity. Closed to machine precision on the
rotational Ornstein–Uhlenbeck testbed (the full velocity-form integral, by residue calculus).

## The structural commitment, derived

From the definedness asymmetry plus standard machinery,
$$\text{self-probe defined}\ \Longleftrightarrow\ J\ne0\ \Longleftrightarrow\ \mathcal{A}\ne0\ \Longleftrightarrow\ \text{a frustrated cycle in the coupling graph.}$$
- $J\ne0\Leftrightarrow\mathcal{A}\ne0$ by the Markov reversibility criterion (Kolmogorov):
  $\mathcal{A}=0$ is the detailed-balanced, real-spectrum, gauge-balanceable case.
- $\mathcal{A}\ne0$ gauge-irremovable $\Leftrightarrow$ a frustrated cycle: a 2-cycle current is
  gauge-removable, so the minimal protected carrier is a directed, non-reciprocal, imbalanced
  3-cycle (Toulouse / Harary balance; May–Leonard cyclic dynamics).

The commitment — **protected current $\Rightarrow$ frustrated 3-cycle** — is the falsifiable
direction of this chain, not an independent axiom. Falsified by one real substrate sustaining a
protected current ($\mathcal{A}\ne0$, removable only by rewiring) with no such cycle.

## The two faces of one deformation

The two frames are the two independent faces of the Boolean→character deformation, read as
fluctuation–response:

- **Amplitude face** — the affinity $a=\ln(G_0/L)$ drives the threshold regimes; observables
  $\alpha_s,P_s$ $\to$ external frame.
- **Topological face** — balance of the signed coupling graph; order parameter the Schnakenberg
  cycle affinity $\mathcal{A}=\oint v/D=\ln(\prod_+k/\prod_-k)$ (gauge-invariant) $\to$ self-probe
  frame.

The Boolean limit (infinite drive) is the balanced, gaugeable ring — every signed cycle has even
negative parity, the spectrum is real, no protected current; detailed balance is this degeneracy.
The minimal departure is the frustrated 3-cycle, emitting the self-frame pair: $\mathrm{spec}(M)$ has
a complex-conjugate pair $\Leftrightarrow\mathcal{A}\ne0$ for the isotropic-damping triad, but under
strong overdamping the pair goes real while $\mathcal{A}\ne0$ persists — **the complex pair is the
underdamped signature, not the invariant; the invariant is the affinity.**

**Affinity vs magnitude** — the split that makes the self-probe reference *intrinsic*: $\mathcal{A}$
is intensive, drive-independent, topology-forced; the current magnitude $J_{ss}$ is extensive, scales
with the kinetic rates, flows with the drive. The amplitude self-gain is neither — it is
external-frame (a pump/coupling constant), so **continuous-amplitude autonomy is supplied, not
minted**, while the chirality/topology mints with the affinity. Three consequences lock together:
entropy production $\langle\sigma\rangle=\sum_C J_C\mathcal{A}_C$ (Schnakenberg); the affinity grounds
the per-transition entropy production $a=\ln(G_0/L)$ (Crooks rate-ratio); and the independence of the
two faces means their **disagreement** is a falsifier.

## Meters, status, falsifier

**Meters.** $\langle\sigma\rangle$ from the binned probability current
($\langle\sigma\rangle=\int P\,|v_{\text{curr}}|^2/D$, $v_{\text{curr}}=A-D\nabla\ln P$, the
Fokker–Planck steady-state form); the external $X$ from the perturbed $(\Delta C,\chi)$ locus; both
tared on the rotational Ornstein–Uhlenbeck testbed ($\langle\sigma\rangle=2\omega^2/\kappa$).

**Status.** Verdict-agreement — the two frames give the same regime wherever both are computable —
holds on one real substrate (a class-B laser; both frames flag the NESS) and a synthetic positive
control. The exact magnitude identity $V_{\text{ext}}=\langle\sigma\rangle=J\cdot\mathcal{A}$ is
closed to machine precision on the rotational-OU testbed. Open: a real substrate on which the
self-probe recovers a regime verdict the external frame cannot — the intrinsic-reference payoff —
which is substrate-gated.

**Falsifier.** A substrate where both probes are feasible at one operating point but the self-probe
and external frame give *contradictory* regime verdicts. Sharper — the iff-chain break: the frame
machinery works and verdict-agreement holds, yet there is **no** frustrated cycle in the coupling
graph.

## What is owned

In this register the constituents are the standard ones — the Cugliandolo–Kurchan ratio, the
Harada–Sasa identity, the thermodynamic uncertainty relation, the Schnakenberg cycle affinity, the
Kolmogorov reversibility criterion, signed-graph balance. What does **not** reduce to an existing
name: (1) the identification of the two fluctuation–dissipation frames as the two faces of one
deformation, joined by the definedness asymmetry; (2) the derivation of the structural commitment as
that chain's falsifiable direction; (3) the affinity-vs-magnitude split and its consequence that
continuous-amplitude autonomy is supplied, not minted. Everything else is a renaming — consistent
with the framework's posture: it imports and re-expresses; the residual is the bindings and the
falsifiers.
