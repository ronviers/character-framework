# Character — the translation method (how imports are adopted)

Scope: the framework introduces no new mathematics; it adopts established results into the
driven-dissipative, non-equilibrium-steady-state (NESS) setting and tests their alignment. This is
the discipline for doing that — a six-step process, each step guarding one failure mode — with
fluctuation–dissipation relations (FDR) as the worked example (the inaugural and most-developed
application). As in [`character.md`](character.md), imports are named to their sources; the closing
section states what is owned.

## The problem

Established mathematics is built for systems with fixed structure — configurations, parts, conserved
quantities, a rest state. A NESS has none of these: it exists only as a pattern actively maintained
by a throughput of energy. Much established apparatus has the right *deep form* but the wrong *domain
assumptions* — built around an equilibrium baseline it does not need. The opportunity is to identify
which results generalize to the driven setting; the risk is smuggling an equilibrium or inertness
assumption in unnoticed, producing apparatus that looks native but secretly requires a rest state.

## The six steps

Each step is a discipline against one failure mode. FDR is shown in brackets as the worked example.

1. **Deep commonality** — state what the source result *actually formalizes*, abstracted from its
   substrate. *Guards forced analogies* — not every result shares a deep relation. [FDR: a relation
   between a process's spontaneous fluctuations $C(t,t')$ and its response $R(t,t')$.]
2. **Audit hidden assumptions** — list what the equations silently presume: equilibrium baseline,
   fixed bath temperature, a single scalar observable, stationarity, linear response, a passive
   probe, detailed balance. *Guards smuggled assumptions.* [FDR: in a NESS nearly all of these fail.]
3. **Filter each concept** — sort into *direct transfer*, *modified*, *no transfer*. *Guards
   all-or-nothing* — translation is rarely global success or failure. [FDR: $C,R$, the
   fluctuation–dissipation ratio $X$, the FD plot, the aging diagonal and plateau transfer directly;
   $T\to T_{\text{eff}}$ is modified; single-window readout, linear response, the passive probe, and
   the detailed-balance default do not transfer.]
4. **Replace the no-transfer items** — the gaps are where the work is. *Guards hand-waving.* [FDR:
   fixed $T\to$ a substrate-equivalent decay scale; single-window $\to$ a window-dependent
   $X(t,t',\tau)$; passive $\to$ active probe (response feeds back through the maintenance dynamics);
   equilibrium-as-baseline $\to$ NESS-as-baseline, with equilibrium the zero-drive degeneracy.]
5. **Import established machinery for the replacements** — resist local invention; another field has
   usually already built it. *Guards reinvention.* [FDR: Harada–Sasa (the integrated FDR-departure is
   the entropy-production rate, no absolute temperature needed); Cugliandolo–Kurchan (the aging
   apparatus); stochastic thermodynamics (Crooks, Seifert); time–frequency uncertainty (the
   multi-window reading); nonlinear-response theory.]
6. **Verify integration** — concept-by-concept transfer does not guarantee a coherent whole. *Guards
   false closure.* [FDR: the affinity $a=\ln(G_0/L)$ acquires a thermodynamic grounding as the
   per-transition entropy production (Crooks rate-ratio); and pressing Harada–Sasa against the
   force–flux / thermodynamic-uncertainty machinery surfaced the two conjugate frames — see
   [`character_fdr_treatment.md`](character_fdr_treatment.md).]

## When the method works

Translatability is predicted by what the source result is built around:

- **High** — relations between *spontaneous-variation-like* and *response-like* quantities (or
  *state-like* and *change-like*), where the object is a relation between two general categories
  rather than a fixed substrate: FDR, control theory, information theory, stochastic thermodynamics.
- **Medium** — relational structure but with strong rest-state assumptions: equilibrium
  thermodynamics, elasticity. These transfer with significant modification.
- **Low** — built around conservation laws, symmetry principles, or inertness as *fundamental*
  rather than incidental: Hamiltonian mechanics, much of classical field theory. Their deep structure
  assumes the absence of active maintenance, and they resist translation.

## The method is a development tool, not just documentation

Working a translation *changes the framework*. The two-frame structure (external probe vs.
intrinsic self-probe) was not visible until FDR was pressed against the force–flux machinery in
step 5; it fell out of the integration check, not out of a prior design. So translation is part of
the framework's development, not downstream presentation.

FDR was the inaugural application because it is the empirical surface adjacent substrate work
measures. The same six steps were subsequently applied across roughly ten further adoptions —
damping and resonance, attractor classification, synchronization, nonequilibrium thermodynamics,
information theory, self-organized criticality, dissipative structures, control theory, active
matter, and queueing — each landing as a *composition* of established machinery with the framework's
own identification of the relevant regime. That the method composed cleanly across that range is the
evidence it generalizes.

## What is owned

The method itself — the six steps and their failure-mode disciplines — is a stated procedure, not a
result. The substance it produces is imports, each named to its source. What does **not** reduce to
an existing name: the recognition of which established results share the deep relation that licenses
the transfer; the specific replacements the NESS setting forces (the no-transfer items of step 4);
and the framework-internal recognitions the integration check surfaces (the two-frame structure, the
thermodynamic grounding of the affinity). Everything imported is named — consistent with the
framework's posture: it imports and re-expresses; the residual is the bindings and the falsifiers.

*(An outbound twin, `transport_law_steps.md`, runs the process in reverse — getting predictions out
of already-adopted imports rather than bringing new ones in. Not refactored here.)*
