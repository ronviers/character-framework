# Character — receipts (the derivations behind the claims)

The derivation and falsifier layer behind [`character.md`](character.md). Each entry is a
result, its mechanism, and a kill condition, with an epistemic tag: `proven` (closed by a
standard import or a closed bespoke shard), `composition` (closes by composing standing
imports), `bespoke` (a framework-original shard), `empirical` (rests on a measured or simulated
instance), `open` (a stated residual), `staked` (a planted falsifier, un-instanced by design),
`corrected` (supersedes an earlier non-flowing form). All formulas are in the
operating-point-flowing form the measurement discipline requires; where an earlier form froze a
quantity, the corrected form is given and marked.

Every imported result resolves to [`character_prior_art.md`](character_prior_art.md) by the
bare `pa:` keys collected in the map at the foot; an entry with no key imports nothing — it is
owned reading. Each entry names its **home** in `character.md`; an entry marked *(ahead)*
derives operational content the unified statement has not yet absorbed — it lives here, in the
derivation reservoir, until it does. `staked` entries mirror one-to-one the `[staked]` rung of
[`character_frontier.md`](character_frontier.md). The Corrections log retains each correction's
superseded form, corrected form, and evidence pointer: that provenance is the supersession
record.

---

## Structural

* **Three-regime threshold** `proven` [Threshold regimes]. The above/near/below-threshold
  trichotomy is the cooperativity pattern of a driven open mode: above $\lambda_A\ll-D$, near
  $|\lambda_A|\lesssim D$, below $\lambda_A\gg D$. The linear-stability shadow of the affinity
  threshold.
* **Sever operator / erasure floor** `proven` [Two degrees of freedom; Boolean limit]. Severing a
  maintained mode to bath costs $W_R/\kappa\ge\ln2\cdot H(A\mid\text{rest})$ — recovering the
  one-bit erasure floor at $\kappa=k_BT\,\xi_{\text{sub}}$. The structural projection's operator
  algebra (try-merge / hold-both / distinguish / sever, with Boolean limits $\land,\lor,\oplus,\neg$)
  is *(ahead)*; only the sever-cost floor is carried in `character.md`.
* **Boolean section / ring deformation** `proven` [Boolean limit and the deformation algebra].
  The operator algebra restricted to the Boolean limit is the $\{\oplus,\land,1\}$ ring (ANF over
  GF(2)); finite drive deforms it, with the affinity $a=\ln(G_0/L)$ the deformation coordinate,
  **not** the unit $1$ (the $1\leftrightarrow G_0$ leg is a type error). `pa:anf-ring`.
* **Capacity ceiling** `proven` [Capacity]. $|\Gamma^*|\le\sqrt{2D/(\alpha\,\gamma_{\min}\,d_{\text{avg}})}$
  from interaction-cost budget vs structural ceiling; occupancy $\eta\to0$ at the $\sqrt D$ ceiling.
  `pa:hopfield`, `pa:ksat-threshold`.
* **Compression contraction** `proven` [Coarse-graining]. $\varepsilon=\|\mathcal{C}\|_{op}<1$ is
  **derived**, not axiomatic — the infrared linear-stability eigenvalue of the level-to-level map
  $D\mathcal{A}_{n+1}/D\mathcal{A}_n$ at the Boolean limit. $\mathcal{C}$ is the heat-tax tower flow
  re-presented on slow-manifold generators ($\Pi_{\text{slow}}$). `pa:banach-fixed-point`,
  `pa:functional-rg`, `pa:mz-projection`.
* **Coarse-graining metric** `proven` *(ahead)* [Coarse-graining]. $\rho([A],[B])=\lim_n\varepsilon^{-n}\|\mathcal{C}^n(d_A-d_B)\|$
  is the dominant-eigenmode amplitude of $d_A-d_B$; well-defined iff a spectral gap, undefined at
  the marginal point (gap closes). `pa:krein-rutman`, `pa:power-iteration`, `pa:nonhermitian-ep`.
* **RG closure** `proven` (scope-bounded) [Coarse-graining]. The level-to-level flow *is* a
  running-coupling functional RG: both flow on a generator space with an infrared-attracting fixed
  point (the Boolean limit). Three steps: locality factorization (spectral gap → $\mathcal{O}(\varepsilon^b)$
  cross-window decay); capacity preserved as the heat tax coarse-grains the two-mode kernel into its
  own form; conjugating isometry $\phi=\Pi_{\text{slow}}$. Proven at $\beta=1$; $\beta<1$ via
  fractional RG. Open: the per-class $\beta$-function. `pa:functional-rg`, `pa:mz-projection`,
  `pa:slaving`.
* **Deformation calculus — Thms 6/7/9** `derived` (Thm 6, Thm 7) / `bespoke` (Thm 9) *(ahead)* [Boolean
  limit]. With $\kappa/\Phi^*=1/D$: Thm 6 (associator) $\|\alpha_C\|\lesssim\tfrac{1}{D}\sum|\gamma|$; Thm 7
  (distributivity defect) $\to0$ likewise; Thm 9 (Boolean deviation) $\Delta_C=1$ iff
  $\gamma_{AB}>0\land D<\gamma_{AB}$ — **not** a series but a singular threshold crossover, the owed object a
  scaling collapse $z=(\gamma-D)/w(D)$ with width exponent $\alpha$ and profile class ($\alpha$ tracks the
  input-noise closure; forcing it needs the noise law from a substrate FDR — `battery:seam-collapse`).
  **Thm 6 — derived, forced-not-fitted (2026-06-21).** The composition $\otimes$ is the one-sided Schur
  complement of coupled driven-OU triads, $A\otimes B=M_A-\Gamma_{AB}M_B^{-1}\Gamma_{BA}$ (= adiabatic
  elimination = Mori–Zwanzig in the gapped regime). Its associator $\alpha_C=(A\otimes B)\otimes
  C-A\otimes(B\otimes C)$ is a **genuine, convergent, forced** power series in $\varepsilon=\kappa/\Phi^*=1/D$,
  **even powers only** ($\otimes$ is even in $\kappa$), starting at $\boldsymbol{\varepsilon^2=1/D^2}$ (generic)
  with **$c_1=0$ — so the $O(1/D)$ bound is loose**, not the true scaling. The
  "smooth-merge closures" are the **Neumann/Schur resolvent recursion** — forced, no free constant; the
  $\mathfrak{gl}(3,\mathbb R)$-drift / $\mathrm{Sym}^+$-noise type-closure is automatic ($\mathfrak{gl}(3)$ is
  all real $3\times3$; the eliminated-block noise correction is PSD by construction). **Convergent** (Kato
  resolvent analyticity), not merely asymptotic, on the open set where the eliminated block stays invertible;
  the radius is the eliminated-block **gap closure** (Neumann $\rho\to1$ at $\kappa\sim\gamma$) — the
  $D\sim\kappa$ threshold *derived not posited*, and exactly the boundary of Thm 9's separate crossover. Thm 7
  follows from the same recursion. Algebraically the associator is the unobstructed obstruction tower of a
  deformation of the $\varepsilon{=}0$ associative Boolean-ring product (Schur is an explicit section).
  **Default (generic) scaling:** $\otimes$ is the monoidal product $\mathfrak{C}\times\mathfrak{C}\to\mathfrak{C}$
  (§Composition under coupling — monoidal/operad/PROP), so $\alpha_C$ is the **monoidal-category associator**,
  leading $-\Gamma M_C^{-1}\Gamma$ (**one** Schur insertion) $\Rightarrow\varepsilon^2=1/D^2$; $\mathfrak{C}$ is
  a *weak monoidal category*, $a_{A,B,C}=\mathrm{id}+O(1/D^2)$, coherent in the Boolean limit. Bookkeeping is
  fixed: $\kappa/\Phi^*=1/D\Rightarrow\varepsilon^n=1/D^n$, leading power $=2\times$(Schur insertions); no
  $\delta=\kappa^2/\Phi^*$ rescaling. A *sparse/local* sub-cascade ($\Gamma_{AC}{=}0$, two insertions →
  $\varepsilon^4=1/D^4$, leading $\Gamma_{AB}M_B^{-1}\Gamma_{BC}M_C^{-1}\Gamma_{CB}M_B^{-1}\Gamma_{BA}$) is the
  special case, more coherent — broken out only when locality is assumed; **the generic $1/D^2$ is the default.**
  Coherence window $N_{\max}\gtrsim D^2$ (vs the bound's loose $D$); the contracting cascade ($\varepsilon_n\to0$)
  makes $\sum\varepsilon_n^2$ converge, aiding the inductive limit (`selective-coupling-class`). Verified
  `experiments/thm6_associator.py` (slopes $2.00/4.03$; even-ness exact;
  leading-coeff residual $\sim\varepsilon^2$, forced; $\rho\to1$ at $\kappa\approx\gamma$). `pa:anf-ring`,
  `pa:kato-perturbation`, `pa:gerstenhaber-deformation`.
* **Hold-both threshold (Thm 7 / $\vee$) — soft** `derived` *(ahead)* [Boolean limit]. The hold-both gate
  $\vee$ keeps two characters coexisting; its threshold is competitive exclusion. Sharp limit ($D\to\infty$):
  a **transcritical** bifurcation, the loser amplitude $\to0$ **linearly** at $c_*$ — the framework's own
  LINEAR competitive-exclusion onset (§Branch-survival barrier), *not* the exactly-symmetric Lotka–Volterra
  (a non-generic degenerate first-order jump). Finite drive $=$ a **maintenance floor**
  $h\sim1/D$ (the open-interior "never extinguished" term), which **unfolds** the transcritical
  (`pa:imperfect-bifurcation`, Golubitsky–Schaeffer): the loser is **pinned** at $x_{\min}\sim h^{1/2}\sim
  D^{-1/2}$ ($p{=}\tfrac12$), the threshold **rounds** over width $w\sim D^{-1/2}$ ($q{=}\tfrac12$), with the
  scaling collapse $x_{\min}/\sqrt h=M((c-c_*)/\sqrt h)$. So the threshold is **$1/D$-soft**, $\vee$ is
  **everywhere-defined (total)**, the apparent obstruction **dissolves** — the open-interval discipline
  vindicated, Thm 9's rounded-crossover precedent matched. **Hard iff** (the residual $\times$) finite drive
  *preserves* the absorbing boundary $x{=}0$ (coefficient renormalization / amplitude-vanishing multiplicative
  noise) **or** the competition is exactly symmetric — both outside the framework's open-interior reading. The
  exponent is normal-form-set ($\tfrac12$ transcritical; an SSB pitchfork unfolds at $p{=}\tfrac13,q{=}\tfrac23$).
  Verified `experiments/thm7_holdboth.py` ($p{=}0.50$, $q{=}0.53$, collapse holds, continuous-vs-jump, $h{=}0$
  hard / $h{>}0$ soft). `pa:imperfect-bifurcation`, `pa:bifurcation-normal-forms`, `pa:lotka-volterra`.
* **Protection as the non-unfoldable stratum (metric→singularity→topology)** `composition` [The two tangent
  sectors]. Composes two standing imports with a standing framework result, adding **no new invariant**:
  *(i)* the protected circulation bit is the gauge-irremovable **discrete graph-flux sign** (Harary balance;
  it flips only on rewiring — §Frustration and the protected current; verified sign $0/200$ graph-fixed
  deformations, `battery:sign-interior`); *(ii)* in a **stratified** operating space (`pa:singularity-
  stratification`) a **topological invariant is constant on each stratum**, changing only across a singular
  seam. $\Rightarrow$ the protected sign is the **non-unfoldable stratum-label** of the coupling space: no
  smooth (stratum-interior) deformation moves it — *re-deriving* "protected" — and **rewiring is precisely
  the seam-crossing** (an edge-sign passage to a different frustration class) at which a topological invariant
  can jump. The metric sector, by contrast, is smooth *within* a stratum (averages, vanishes continuously; a
  lost metric configuration is a generic codim-1 unfolding that **rounds smoothly** at finite drive — the
  hold-both transcritical). The **singularity layer is the middle** fixing which metric quantities vanish
  smoothly (codim-1 seam) vs which change only across a seam (the topological bit) — the
  metric→singularity→topology layering. **Forced** (names the mechanism of an existing protection claim).
  **Falsifier run \+ SURVIVED** (`experiments/kill_protected_sign.py`, 2026-06-21): the kill — *a protected
  sign flips under a smooth stratum-interior deformation* — was attempted adversarially and **failed**. Over
  $19347$ stable $\mathfrak{gl}(3)$ deformations sign($\mathcal{A}$) never flips and never disagrees with
  sign($g$); it **survives the exceptional point** (the complex pair coalesces and dies under shear while the
  affinity's sign lives — *protection is the affinity, not the spectrum*); it flips **only** across the
  $g\to0$ / $\mathcal{A}=0$ seam (rewiring). The current's sign is defined only on the stable operating space
  (an unstable $M$ has no NESS — interior-only / NaN-tripwire); the residual kill — a flip with $M$ **stable**
  and $\mathcal{A}\ne0$ — is none found. `pa:singularity-stratification`,
  `pa:signed-balance`, `pa:bifurcation-normal-forms`.
* **The deformation chart** `proven` (real-instanced) [Boolean limit and the deformation algebra].
  The linear deformation space of $M=-\gamma I+g\,A_{\text{CYC}}$ is $\mathfrak{gl}(3,\mathbb{R})$,
  Cartan-decomposed $\mathbb{R}I\oplus\mathfrak{so}(3)\oplus\mathrm{Sym}_0$ — exhaustive
  ($\dim=9$) and closed (commutator residual $3\!\cdot\!10^{-16}$): damping (scaling) / chirality
  (rotation, axis $(1,1,1)$, sign at the achiral point) / detuning (shear, exceptional point
  $\omega^2=\omega_0^2-(\delta/2)^2$). Extensions close on named structures: noise = diffusion tensor
  (continuous Lyapunov); nonlinearity = pitchfork/Hopf normal forms; drive-periodicity =
  Floquet → Adler circle map; composition = Schur on coupled triads → again $(\mathfrak{gl}(3)$ drift,
  $\mathrm{Sym}^+$ noise$)$, the RG type-identity. The $\sim39°$ sign-reversal node and the
  non-uniform-squeeze tongues are model-specific *landmarks* (falsifiability handles), not
  generators. Falsify: a triad deformation not composable from the generators; a non-model-specific
  response off its canonical form. `pa:nonhermitian-ep`, `pa:adler-locking`, `pa:bifurcation-normal-forms`,
  `pa:nonreciprocal-transition`, `pa:slaving`, `pa:mz-projection`, `pa:sde-lyapunov`.

## The two-mode kernel and its regimes

* **Bridge** `proven` [Threshold regimes; Control parameter]. $\lambda_A\approx L-G_0$ at zero
  amplitude; substituting $-\lambda_A=G_0-L$ into the three regime conditions recovers the affinity
  threshold table — this is what couples the structural and dynamical registers.
* **Affinity** `proven` [Control parameter]. $a=\ln(G_0/L)$ is the per-transition entropy-production
  / log-rate-ratio. Threshold symmetry ($G_0{=}L\Rightarrow0$), additivity across stages, and the
  one-bit floor are three faces of one rate-ratio structure, not independent. `pa:crooks-ft`.
* **Kernel bifurcation** `proven` [The two-mode kernel]. The four pair-types (deep cooperative /
  asymmetric slaving / decoupled / competitive exclusion) are the fixed points of one field equation,
  not an enumeration. `pa:lotka-volterra`, `pa:gain-depletion`.
* **Gain-depletion closed form** `proven` [The two-mode kernel]. $G_{0,A}^{\text{eff}}=G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$;
  the cubic cross-saturation is its small-density leading term; non-Markovian memory via
  $\Gamma_{AB}(\tau)=\Gamma_0e^{-\tau/\tau_c}$, $\tau_c$ set by $\gamma_s$. `pa:gain-depletion`.
* **Dynamic-bath inversion** `proven` [The two-mode kernel]. $\dot B=\gamma_B[1-B\,S(t)]$ with the
  bath history integral projected out; the fast-bath limit recovers gain-depletion.
  `pa:consumer-resource`, `pa:mz-projection`.
* **Fractional memory / transport law** `proven` [The two-mode kernel; The central testable claim].
  $\Gamma_{AB}(\tau)=\Gamma_0E_\beta(-(\tau/\tau_c)^\beta)$, $K(\tau)\sim\tau^{-\beta}/\Gamma(1-\beta)$
  — this *sets* $\beta$. **Transport law (not an identity):** one exponent $\beta$ governs three
  registers through fixed maps, $\alpha_s=\beta_{\text{mem}}=\beta$ and the heavy-traffic exponent
  $g(\beta)=\beta/(2-\beta)$ (Norros) or $1/\beta$ (M/G/1), numerically coincident **only at $\beta=1$**.
  Predictive content is the transport: an exponent in one register fixes the others. Falsify: two
  registers fail to collapse onto a common $\beta$. `pa:caputo-fractional`, `pa:pottier-fdr`,
  `pa:fbm-queueing`, `pa:kingman`.
  **Instanced — survives (2026-06-03).** On the Norros fBm-queue (one Hurst $H$ sets $\beta=2-2H$),
  the kernel/aging register (low-frequency spectral slope) and the heavy-traffic queue-tail register
  (stationary-backlog Weibull stretch) collapse onto a common $\beta$ across the interior
  $\beta\in\{0.8,0.6,0.4\}$ (mean inter-register gap $0.066$); the falsifier did **not** fire. The two
  are not definitionally tied — a 2-point correlation vs a supremum functional, Norros's exponent
  equality a theorem, not a definition. Caveats: on fBm aging $\equiv$ kernel ($\alpha_s=\beta_{\text{mem}}$,
  one exponent), so this is the **2-register** named test (FDR-aging vs queue-tail), not an independent
  third register; and $\beta=0.2$ is finite-block resolution-limited but demonstrably convergent
  (queue estimate $0.455\!\to\!0.344$ as blocks $16\mathrm{k}\!\to\!131\mathrm{k}$). A genuine third,
  independent FDR-aging register awaits an aging-rich substrate (East KCM / fractional-OU).
  `character-framework/experiments/beta_collapse.py`.
* **Relaxation oscillation** `corrected` [The two-mode kernel]. Flowing forms (the audit unfroze a
  smuggled constant): $\gamma_{RO}=(\gamma_s/2)e^{a}$, $\omega_{RO}=\sqrt{2\gamma_sL(e^a-1)-(\gamma_s^2/4)e^{2a}}$,
  $Q=\sqrt{2L(e^a-1)/\gamma_s}\,e^{-a}$. $Q$ is non-monotonic — $\to0$ at both $a\to0^+$ and
  $a\to\infty$, peaking at $a=1$ bit ($G_0/L=2$): underdamped only in a mid-band. The original froze
  $e^a$ at its threshold value. `pa:relaxation-oscillation`, `pa:schawlow-townes`.
* **Attractor classification** `proven` [Threshold regimes; The two-mode kernel]. Below = stable
  origin; near = center manifold ($P_s$ amplitude, $\alpha_s$ slow-eigenvalue residual scaling);
  above = stable focus / pitchfork-broken focus; protected current = Hopf-unstable spiral + attracting
  limit cycle. `pa:bifurcation-normal-forms`, `pa:center-manifold`, `pa:ck-aging`.
* **Codim-2 normal forms** `proven` *(ahead)* [The two-mode kernel]. At the pitchfork–Hopf
  intersection a Bogdanov–Takens normal form is forced; cusp / generalized-Hopf / fold-Hopf follow
  standard catastrophe theory. `pa:codim2-normal-forms`.
* **Occupancy / Erlang** `proven` [Capacity]. $\eta(\Gamma^*)=1-B(c,\rho)$ with the Erlang loss
  formula $B(c,\rho)=\frac{\rho^c/c!}{\sum_{k\le c}\rho^k/k!}$, $c=\lfloor|\Gamma^*|_{\text{crit}}\rfloor$.
  Hard-wall substrates replace $B$ by $\mathbb{1}[|\Gamma^*|\ge c]$. `pa:erlang-b`.
* **Self-organized criticality** `proven` [Threshold regimes; Coarse-graining]. The near-threshold
  state is an attractor in parameter space under feedback-coupled maintenance; branching ratio
  $\mu=e^{a}$, critical at $a=0$ giving mean-field $\tau\approx3/2$. The near-threshold state is the
  *generic* attractor (above over-provisioned, below post-collapse). `pa:soc`, `pa:branching-process`,
  `pa:directed-percolation`.

## The protected current and the two frames

* **Protected current derived** `proven` [Frustration and the protected current]. The $N\ge3$
  obstructive-sign extension of the kernel realises a heteroclinic/circulating attractor — no
  synchronized fixed point, cyclic pumping, drive-independence. A consequence of the kernel + balance
  structure, not a separate axiom. `pa:may-leonard`, `pa:cyclic-attractors`, `pa:signed-balance`,
  `pa:frustration`.
* **Cycle currents** `proven` [Frustration and the protected current]. Affinity lives on the
  master-equation state graph (the raw-mode log-rate-ratio is wrong in non-reciprocal cases). Orbit
  form $\mathcal{A}=\oint v(\theta)/D(\theta)\,d\theta=\ln(\mathcal{P}_+/\mathcal{P}_-)$; topology
  forces $v\not\to0$; drive-independence from the obstructive graph + bath, not amplitude. Tree rows
  $J_C=0$; the frustrated row carries $\sigma_{\text{frust}}=J_{ss}\oint v/D$. `pa:cycle-affinity`,
  `pa:gc-ft`, `pa:may-leonard`.
* **Stochastic thermodynamics** `proven` [Two fluctuation-dissipation readings]. $P(\sigma)/P(-\sigma)=e^\sigma$;
  $\int(\text{FDR departure})=\langle\sigma\rangle$; precision $\mathrm{Var}(J)/\langle J\rangle^2\ge2k_B/\langle\sigma\rangle$;
  the extended bound $\langle\sigma\rangle\ge-\Delta I$ (readout-maintaining states sustain at lower
  $a$ by paying mutual information). `pa:crooks-ft`, `pa:cycle-affinity`, `pa:tur`, `pa:sagawa-ueda`,
  `pa:harada-sasa`.
* **Two-frame construction** `proven` (real-instanced) [Two fluctuation-dissipation readings]. The
  iff-chain — self-probe defined $\Leftrightarrow J\ne0\Leftrightarrow\mathcal{A}\ne0\Leftrightarrow$
  frustrated triad — binds the FDR architecture to the topological commitment in both directions; the
  definedness asymmetry (self-probe defined iff a current exists) makes the frame's *existence* a
  topological diagnostic. Distinguishes the framework from FDR↔TUR unifications that connect the frames
  without committing to triad topology. Full treatment in
  [`character_fdr_treatment.md`](character_fdr_treatment.md). `pa:harada-sasa`, `pa:tur`,
  `pa:cycle-affinity`, `pa:ness-fdr`, `pa:kolmogorov-reversibility`, `pa:signed-balance`, `pa:may-leonard`.
* **Central commitment** `proven` (real-instanced) [Frustration and the protected current]. A
  directed, non-reciprocal, imbalanced 3-cycle ($N=3$ minimal; $N=2$ is gauge/drive-removable) is the
  minimal carrier of gauge-irremovable circulation. $\mathcal{A}=\oint v/D$ gauge-invariant, $\ne0$ iff
  the drift is non-gradient. **Onset of protected circulation requires a triad** (scoped to
  ignition-necessity, not generativity). Falsify: a real substrate with protected circulation and no
  triad. Real instance: a real, non-authored C3-symmetric rock-paper-scissors carries a protected sign
  on a directed 3-cycle, drive-independent, flipping only by rewiring. `pa:signed-balance`, `pa:may-leonard`,
  `pa:cycle-affinity`, `pa:nonreciprocal-transition`, `pa:winding-spitzer`, `pa:skew-product`, `pa:levy-area`,
  `pa:kolmogorov-reversibility`.
* **Two FD frames — two-step near threshold** `staked` [Two fluctuation-dissipation readings].
  Near-threshold FDR is two-step: quasi-equilibrium $X=1$ on short lags, aging $X<1$ on long lags; a
  short-lag $X=1$ alone does not place a substrate below threshold (the long-lag segment is the
  discriminator). Recoverable by the five-vector inversion with a domain-of-validity gate.
  `pa:ck-aging`, `pa:fdr-estimator`, `pa:rfim-avalanche`.
* **Two FD frames — verdict-agreement** `proven` [Two fluctuation-dissipation readings]. External
  ($X$, substrate-conditional) and self-probe ($\mathcal{T}=\langle\sigma\rangle\mathrm{Var}(J)/(2\langle J\rangle^2)\ge1$,
  intrinsic, defined iff a current exists) give the same regime verdict where both are computable.
  Falsify: both probes feasible at one operating point, verdicts disagree. `pa:harada-sasa`, `pa:tur`,
  `pa:cycle-affinity`, `pa:ness-fdr`.
* **Two FD frames — exact magnitude** `proven` [Two fluctuation-dissipation readings]. $V_{\text{ext}}=\langle\sigma\rangle=J\cdot\mathcal{A}$
  holds at exact magnitude on the rotational-OU testbed: the Fokker–Planck rate $2\omega_0^2/\kappa$,
  the cycle×affinity, and the full velocity-form Harada–Sasa integral (both coordinates, all $\omega$,
  by residue calculus) coincide to machine precision; the numeric residual is the analytic $1/\omega^2$
  tail. $\mathcal{T}$ is $\tau$-independent past the transient (the $\tau$'s cancel), so the
  $\tau$-absorbed and $\tau$-explicit forms are one quantity. Falsify: a NESS where the three frames
  give different magnitudes, or $\mathcal{T}$ genuinely $\tau$-dependent. `pa:harada-sasa`, `pa:tur`,
  `pa:cycle-affinity`, `pa:ness-fdr`.
* **Two bits** `corrected` [Two degrees of freedom]. Population bit: the infinite-drive occupancy
  endpoint, erased by the sever operator at the one-bit floor, reversibly flippable. Topological bit:
  the chiral sign of the frustrated triad, gauge-irremovable, observation-window- and
  amplitude-invariant, **free to hold and free to flip** — a sign flip is a reversible bijection (a
  braid: reverse the cycle by rewiring), no erasure, hence no Landauer floor. The cycle-space dimension
  $b_1$ is the count of independent gauge-irremovable signs (topological capacity), not a per-flip cost.
  *Corrected:* the earlier "$\ge1$ bit per protected sign to modify" was a Landauer erasure cost
  wrongly placed on a reversible flip, definable only at the never-attained $\mathcal{A}=0$ boundary
  (a $0/0$). `pa:landauer`, `pa:bennett-reversible`, `pa:topological-memory`, `pa:signed-balance`,
  `pa:cycle-affinity`.
* **Two irreducible sectors (compression)** `composition` [Two degrees of freedom; Object]. The
  protected information of a character is exhausted by two non-interconvertible sectors: the
  continuous **metric** sector (the Cartan tangent directions of $\mathfrak{gl}(n)$ — §The
  deformation chart) and the discrete **topological** sector (the winding of $\mathcal{A}$,
  $\pi_1\ne0$ — §Homotopy obstruction). Other observables factor through them: $\beta$, $X$,
  $\Delta V$, $J$ read the metric sector, $\mathcal{A}$ the topological, $I_{\text{pred}}$ the dual
  of both; the operating point $a$ is the coordinate along which all vary, not a third sector.
  **Cascade consequence:** $\mathcal{C}$ closed under $\otimes$ + the two-sector exhaustion ⇒ the
  tower introduces no new *kind* of protected information (each level is the $\otimes$-composite of
  the one below); minting adds topological organization, the metric sector forced from the parts
  (§The minting claim). Closes by composing the deformation-chart exhaustiveness, the homotopy
  obstruction, and the closure. Falsify: a third irreducible kind — a sustained observable
  reducible to neither sector nor their dual. `pa:cycle-affinity`, `pa:topological-memory`,
  `pa:info-geometry`.
* **Chirality protection** `bespoke` (synthetic) [The minting claim]. The protected carrier of a
  minted circulation is the **gauge-irremovable affinity** (the antisymmetric/non-gradient part of the
  drift), read as $\operatorname{sign}(\mathcal{A})$ — **not** the exceptional pair (suppressible) and
  **not** a conserved integer charge (holonomy sub-integer). A symmetric (reciprocal) deformation cannot
  touch the antisymmetric part but *can* drive the complex pair real, leaving a real-spectrum
  circulation with $\mathcal{A}\ne0$. Tests (linear OU, $N{=}3$): the sign survives 0/200 graph-fixed
  deformations $\gg g$, flipping only on rewiring; the exceptional pair is killed 53/200 by a reciprocal
  gradient; holonomy $\le0.16$. Falsify: a graph-fixed smooth deformation reversing $\operatorname{sign}(\mathcal{A})$
  without rewiring; or a substrate where overdamping the exceptional pair also erases $\mathcal{A}$.
  Owed: a real second instance. `pa:cycle-affinity`, `pa:kolmogorov-reversibility`, `pa:signed-balance`,
  `pa:nonhermitian-ep`, `pa:harada-sasa`, `pa:reversible-spectrum`.
* **Chiral-rotor triad (Triskele) — mechanical calibration instance** `synthetic` [The minting claim]. A
  computed minimal mechanical realization of the protected sign — three identical chiral rotors in a driven
  ring ($\Delta\varphi = 2\pi/3$), the circulating NESS current's sign locked to the shape-chirality
  pseudoscalar $\chi = \varepsilon_2\varepsilon_3\sin\delta$. **All three armed kill-switches pass.** (1) The
  single-body propeller coupling $C \approx 3.4\,\chi$ by a validated regularized-Stokeslet BEM (Cortez 2001),
  isolated by the **parity-odd projection** $D = \tfrac12[R^{TR}(\delta) - R^{TR}(-\delta)]$ (any
  grid-handedness or achiral coupling is $\delta$-even and cancels), **nonzero** by the selection rule
  $2\otimes3\supset1$ at **SNR $\approx 450$** above the numerical floor; the bare $6\times6$ mobility is
  symmetric (reciprocal/Lorentz) to $1.6\times10^{-13}$. (2) The sign is **parity-locked, not drive-locked** —
  set by $\chi$ at fixed drive sense, flipped only by $\delta\to-\delta$ through the achiral point, with **no
  drive-*amplitude* escape** (honestly $J \propto \chi\Omega$ is odd in the drive *arrow* — reversing $\Omega$
  reverses $J$ — but that is time-reversal, not a metric tuning). (3) The shape is **genuinely chiral** — a
  continuous chirality measure $0.75$ vs $7.8\times10^{-16}$ at $\delta=0$. The activation envelope
  $F(\Delta\varphi)$ vanishes at the mirror orientations $0,\pi$ and is nonzero at the ring's $2\pi/3$
  ($F_e \approx 0.87$; the pair mobility is reciprocal there to $5\times10^{-16}$). **The mechanism, corrected
  (carry it — do not re-import the wheel):** the *deterministic* phase-reduced (non-reciprocal Kuramoto) triad
  does **not** circulate — it phase-locks (synchronized/splay); the protected current is **noise-activated
  stochastic hopping** among the three lead-arrangements $\{A,B,C\}$-leads, a May–Leonard cyclic-dominance loop
  with no stable fixed point; the non-reciprocity is **drive-generated** (the even-in-$(\theta_2-\theta_1)$
  phase coupling $\propto C\chi\Omega F(\Delta\varphi)$), not bare-mobility; and the current lives in the
  **collective configuration** (which body leads), not the individual co-rotating bodies. And **frustration is
  minimal** — the harmonic grammar / Clebsch–Gordan was a *sufficient demonstration, not the essential
  requirement* (a hole with a protrusion suffices). **Scope: synthetic = calibration, never vindication** —
  imported fluid mechanics (Stokes BEM) read through the protected-sign lens; the **physical build remains the
  owed real second instance** and this does **not** discharge it. Build: `H:\triskele`
  (`github.com/ronviers/character-triskele`; live builder dashboard `ronviers.github.io/character-triskele`).
  `pa:cycle-affinity`, `pa:ness-currents`.
* **The binding** `composition` [The minting claim]. graph-frustration $\Leftrightarrow\mathcal{A}\Leftarrow$
  spectral, one carrier — closes by composing standing imports, not a bespoke theorem. Two-way carrier:
  the gauge-irremovable frustrated cycle $\Leftrightarrow$ nonzero cycle affinity (`pa:signed-balance`/`pa:frustration`
  $\Leftrightarrow$ `pa:cycle-affinity`/`pa:kolmogorov-reversibility`/`pa:ness-currents`). One-way spectral
  signature: a complex pair $\Rightarrow\mathcal{A}\ne0$ (`pa:reversible-spectrum`), but $\mathcal{A}\ne0\not\Rightarrow$
  complex pair (admits a real overdamped circulation). The owned step is the **weld** — the
  gauge-irremovable nonzero-affinity cycle *is* the Harary-unbalanced signed cycle (same node-relabeling
  gauge; the topological bit = sign parity = gauge-irremovable sign of $\mathcal{A}$). Corrects an
  outside three-way-iff overstatement down to a 2-way carrier + 1-way signature. Falsify: a frustrated
  cycle with $\mathcal{A}=0$ away from balance, or a sustained $\mathcal{A}\ne0$ on a gauge-balanceable
  graph. `pa:reversible-spectrum` + the carrier keys. **Per-substrate, the carrier is named established
  math** (`pa:gauge-thermodynamics`: $\mathcal{A}$ the gauge potential, detailed balance $=$ flat connection,
  $\operatorname{sign}(\mathcal{A})$ the Wilson-loop sign; Harary/Zaslavsky balance) — but that classification
  is *intra-substrate*; there is **no** single cross-substrate classifying structure (the universal-invariant
  question, §Universal-invariant classification below).
* **Universal-invariant classification — bounded (clean negative)** `composed` (2026-06-21) [The minting
  claim]. Three independent outbound passes (`docs/universal_invariant returns.md`) converge: there is **no
  established, model-independent classifying structure under which $\operatorname{sign}(\mathcal{A})$ is a
  universal invariant** with substrate-independent equivalence classes. What exists is **substrate-bound**:
  gauge cohomology / Wilson-loop flatness (`pa:gauge-thermodynamics`, Polettini 2012) on a *fixed* state-space
  graph; Harary/Zaslavsky signed-graph balance (`pa:signed-balance`) — combinatorial, no dynamics;
  large-deviation cycle theory (Andrieux–Gaspard 2007; `pa:cycle-affinity`, `pa:gc-ft`) — a representation
  within one generator. None unify across substrates. **Range:** the bit is $\mathbb{Z}_2$ (a sign),
  **sub-integer** — the thermodynamic gauge group is $(\mathbb{R}^+,\times)$, non-compact, so no integer
  winding (Chern / K-theory is the wrong import; confirmed). **Manifold:** the established classification lives
  on **state space** (the connection on the transition graph), *not* parameter space; conflating them is the
  standard error. **The deformation framing is obstructed** (the minimal counterexample): a discrete 3-state
  chemical cycle and a driven colloid on a ring both carry $\operatorname{sign}(\mathcal{A})=+1$ yet cannot be
  placed in one class — different state spaces (3 points vs $S^1$), bounded vs unbounded generators, a singular
  continuum limit. So "*same character $=$ deformable in one space*" is dead. **But the negative is precise,
  not flat.** (i) The *construction* — gauge-irremovable sign of a cycle holonomy — **is** substrate-independent
  (the same recipe everywhere: Polettini on graphs, de Rham on manifolds), so character is more than a loose
  analogy; (ii) the counterexample over-reads — both systems have first Betti number 1 and the same sign, so it
  kills the single classifying-*space* framing, not a universal *invariant/functor*; what fails is a complete
  classifying space, not the per-substrate invariant. **The residue — the live make-or-break:** universality,
  if it exists, is a **composition law**, not a shared space. The literature has *no* monoidal / fusion /
  cobordism algebra of protected circulations (all three passes; the most original, unbuilt part). The framework
  already derived the candidate: the union-cycle holonomy
  $\mathcal{A}_{\text{union}} = \oint(l_A+l_B+\Gamma_{AB})\,dx = \oint\Gamma_{AB}\,dx$ when the parts do not
  circulate (§Composition; `selective-coupling-class`) — minting two non-circulating parts into a circulating
  union is $0\otimes0\to1$, a *non-trivial* product whose new generator is the coupling edge, not a
  $\mathbb{Z}_2$ sum of the factors. Whether that is a genuine monoidal/fusion structure (associative, unital,
  substrate-independent) is the owed build (`docs/build_composition_law.md`). **Verdict:** the *import* is
  killed; the per-substrate invariant is vindicated and named; the universal claim relocates from a classifying
  space (dead) to a composition law (unbuilt, candidate in hand). Crossed to `character_frontier.md` ·
  `universal-invariant-classification`. `pa:gauge-thermodynamics`, `pa:signed-balance`, `pa:cycle-affinity`.
* **Composition-law build — minting is the cycle-space homology import (calibration)** `synthetic`
  (2026-06-21) [The minting claim]. The runnable half of the universal-invariant make-or-break: is minting a
  genuine monoidal/fusion algebra? Built on the framework's native representation — substrates as Markov-cycle
  graphs, the protected bit \= the sign of the Schnakenberg cycle affinity
  $\mathcal{A}(c)=\sum_{(i\to j)\in c}\ln(w_{ij}/w_{ji})$ (the Polettini gauge holonomy);
  `experiments/composition_law.py`. **All mechanical conditions pass:** (i) one rule across three substrates
  (dna 3-cycle, gyrator 4-cycle, repressilator 3-cycle), **forced-not-fitted** —
  $\operatorname{sign}\mathcal{A}=\operatorname{sign}$(directly-solved NESS current) in every case
  (Schnakenberg's theorem); (ii) minting $0\otimes0\to1$ — two non-circulating ($\mathcal{A}=0$) parts coupled
  into a frustrated union ($\mathcal{A}\approx+2.20$, real current), the bit from the coupling alone; (iii)
  **associativity** sign-exact ($|(A\otimes B)\otimes C-A\otimes(B\otimes C)|=0$); (iv) cross-substrate minting
  (chem$\otimes$gyrator) obeys the identical rule. **The honest structure (the refinement the pre-registered ↑
  missed):** the composition splits. The **existence/frustration bit** composes as a *clean linear algebra over
  the cycle space* — affinities add, shared edges cancel
  ($\mathcal{A}_{\text{outer}}=\mathcal{A}_{C_1}+\mathcal{A}_{C_2}$, exact) — a genuine substrate-general fusion
  structure, **but precisely the signed-graph homology import** (Harary/Zaslavsky/Polettini), not novel
  machinery. The **value bit**
  $\operatorname{sign}\mathcal{A}=\operatorname{sign}(\mathcal{A}_{C_1}+\mathcal{A}_{C_2})$ is **not** a
  function of the component signs — $(+,-)$ composes to $+$ or $-$ by *magnitude* — so the value is
  $\mathbb{R}$-additive and coupling-dependent, **not a group/fusion**. **Verdict (C-middle, made precise):**
  metaphor-collapse **averted** — minting composes by a real, computed, substrate-general, forced law (a second
  cross-substrate structure beside the transverse theorem), not a shared name; physical-category **not won** —
  the algebra is the cycle-space homology *import*, metabolized, and the value-composition is no algebra at all
  (the novel-monoidal-algebra route to a new category is closed). **Synthetic \= calibration, never
  vindication** (`project_killshot_synthetic_is_imported_math`): a graph computation verifying
  Schnakenberg/Harary cannot vindicate a new category — it confirms substrate-general imported structure. The
  one make-or-break piece still open is the colloid superselection premise on real data. Crossed to
  `character_frontier.md` · `universal-invariant-classification`; `character.md` §Composition under coupling.
  `pa:cycle-affinity`, `pa:gauge-thermodynamics`, `pa:signed-balance`.
* **Readability battery — the reading transition as an order parameter (calibration)** `synthetic`
  (2026-06-21) [The reading transition]. The runnable instance of the abiogenesis arc's load-bearing beam
  ("define reading before heredity"). On the same Markov-cycle machinery (`experiments/readability.py`, 3-cell
  protected loop, $\mathcal{A}=b\,\Omega_0$ the bit's carrier), couple the loop to a tunable **ecological
  field** $d$ entered as a **gradient** (a metric potential $d\,(U_i-U_j)$, curl-free by construction) and
  measure two response coefficients. **(1) Metric reading turns on generically** within a lifetime —
  $\partial(\text{occupancy})/\partial d=+0.21$, $\partial|J|/\partial d=-0.019$: the ecology reshapes the
  loop's throughput/occupancy (the cross-rule; cheap, instantaneous, pre-heredity). **(2) Bit reading within a
  lifetime is barred** — $\mathcal{A}$ is **invariant to machine precision** across the whole $d$-sweep (spread
  $6.7\times10^{-16}$; the gradient telescopes to exactly $0$ around the cycle), so
  $\partial(\operatorname{sign}\mathcal{A})/\partial d=0$. This is the **superselection null / kill-switch**: an
  ecological (metric) field *cannot* continuously deform the protected sign — the transverse theorem
  (`pa:transverse-decomposition`) forbidding the instantaneous route. Forced-not-fitted
  ($\operatorname{sign}\mathcal{A}=\operatorname{sign}$ NESS current) holds throughout. **(3) The order
  parameter is over a LINEAGE, not a lifetime.** Define $R_{\text{hard}}=\partial\langle\operatorname{sign}
  \mathcal{A}\rangle/\partial d$ at a selection–replacement fixed point of a population of $\pm$ loops, fitness
  $=$ metric work-harvest $\exp(\delta\,J(b;d)\,d)$ (overlap of the loop's current with the ecological flux;
  $\delta$ $=$ the geometric overlap / **symmetry-break** knob). Result: **$R_{\text{hard}}=0$ below threshold
  ($\delta=0$, current transverse to the flux — $\langle b\rangle$ flat in $d$: ecology modulates the metric
  only); $R_{\text{hard}}\neq0$ above ($\delta>0$ — $\langle b\rangle$ tracks $d$, $\pm0.93$).** The bit becomes
  readable **only across replacement, never instantaneously** — selection is the unique channel from the metric
  sector into the topological one, acting as a projection operator (metric ecology $\to$ population replacement
  $\to$ bit retention). $R_{\text{hard}}(\delta)$ **turns on continuously at $\delta=0$, $\sim$ linear near
  threshold** ($R_{\text{hard}}/\delta\to$ const) — the same zero-iff-symmetric onset as TDT move 3. **(4)
  Co-emergence:** over the four corners (replacement on/off $\times$ symmetry-break on/off), $R_{\text{hard}}\neq
  0$ **only when both** the heritable-replacement channel **and** the symmetry break are open — so hard reading
  and (proto-)heredity are the **same bridge** seen from opposite sides: from ecology, "a distinction becomes
  able to affect a protected bit"; from the lineage, "a protected bit becomes able to survive replacement."
  This mirrors the reproduction split exactly — **degenerate reproduction : pattern :: metric reading : state**,
  and **heritable reproduction : bit :: bit reading : sign**. **Scope: synthetic $=$ calibration, never
  vindication** (`project_killshot_synthetic_is_imported_math`) — a graph computation instancing the metric/bit
  split as a measured order parameter; the reader instanced on a **real** dissipative medium remains owed (the
  `escape-degenerate-replication` bootstrap). Crossed to `character_frontier.md` · `battery:readability`,
  `reading-transition`. `pa:cycle-affinity`, `pa:transverse-decomposition`, `pa:von-neumann-automata`.
* **Amplitude autonomy — supplied, not minted** `proven` [The minting claim]. Continuous-amplitude
  autonomy (a collective amplitude carrying its own self-gain, $\mathrm{Re}\,a_{\text{eff}}>0$ surviving
  drive removal) lives on the external frame, whose reference is always external — so a self-sourced gain
  has no intrinsic referent and can only be pinned to a pump/coupling constant. Over-determined three
  ways: spectral ($\mathrm{Re}\,\lambda_k=\mu+2\kappa\cos\theta_k$, independent of the flowing
  non-reciprocity), dissipation ($\langle\sigma\rangle=J\cdot\mathcal{A}$ carries no amplitude-gain term),
  and affinity grounding ($a$ runs through $J\cdot\mathcal{A}$). So a cascade mints chirality/topology
  (flows with the NESS — legal) but not amplitude autonomy (external-frame — supplied). The
  measurement-discipline "no inert constant" rule recovered as a theorem of the definedness asymmetry.
  Falsify: a substrate where a collective amplitude self-gain flows with a genuine NESS quantity instead
  of a pump/coupling constant. `pa:harada-sasa`, `pa:tur`, `pa:cycle-affinity`, `pa:crooks-ft`,
  `pa:nonreciprocal-transition`.

## Coarse-graining, the tower, the marginal point

* **Heat-tax tower** `proven` [Coarse-graining]. $L_{n+1}=L_{n+1}^{(0)}+\alpha\langle\sigma_n\rangle$:
  level-$n$ entropy production becomes ambient noise to level $n{+}1$. The thermodynamic conjugate of
  the informational tower. `pa:harada-sasa`, `pa:dilution-structure`.
* **Dilution pin** `proven` [Coarse-graining]. $\alpha(\varepsilon)=\alpha_0(1-\varepsilon)$; cumulative
  tax $\propto(1-\varepsilon)\sum\varepsilon^n=1-\varepsilon^N\to1$ for $\varepsilon<1$, diverging at
  $\varepsilon=1$ — the marginal point as a thermodynamic singularity. `pa:dilution-structure`,
  `pa:landauer`.
* **Meta-ledger flow** `proven` [Coarse-graining]. $\mathcal{C}$ is the level-to-level map on
  slow-manifold generators ($\Pi_{\text{slow}}$ + heat-tax substitution into the two-mode kernel);
  continuous inter-level flow integrates the running $\beta$-functions directly. `pa:mz-projection`,
  `pa:slaving`, `pa:functional-rg`.
* **Priority structure** `proven` *(ahead)* [Coarse-graining]. Tower levels are non-preemptive priority
  classes sharing one server; the wait $W_{n+1}=W_0/[(1-\sigma_n)(1-\sigma_{n+1})]$ is the *mechanism* of
  level-to-level load propagation; its divergence at $\sigma\to1^-$ is coincident with $\varepsilon\to1$
  (isomorphism open). `pa:cobham-priority`, `pa:littles-law`, `pa:slaving`.
* **Spatial product-form & critical length** `proven` *(ahead)* [Coarse-graining]. Product-form
  $P(\mathbf Q)=\prod_kP_k(Q_k)$ holds across patches until cross-patch load spikes; the critical length
  $\ell_c(\beta)\to\infty$ as $\sigma_n\to1^-$, and $\to\sqrt{2D_0}$ as $\beta\to0$ at the marginal point
  (a transition from dynamic congestion to frozen-topological domains). `pa:product-form`, `pa:ctrw`.
* **Marginal point = loss of normal hyperbolicity** `corrected` [Coarse-graining]. $\varepsilon\to1$ is
  loss of normal hyperbolicity (`pa:fenichel-nhim`): the transverse gap closes and the reduced plateau
  ceases to persist — necessary, not sufficient, for chaos. Post-marginal chaos is **delay-driven**
  (`pa:delay-hopf`, chaotic at $N{=}1$); the $N\ge3$ 3-torus is robust under weak coupling
  (`pa:dissipative-kam`), so quasiperiodicity (`pa:nrt-chaos`) is a topologically-generic *route*, not a
  forcing. *Superseded:* "$N\ge3$ ascents complete a 3-torus $\Rightarrow$ forced chaos." Diagnostic: the
  CLV minimum angle (`pa:clv`). `pa:fenichel-nhim`, `pa:delay-hopf`, `pa:dissipative-kam`, `pa:nrt-chaos`,
  `pa:clv`.
* **Generic Hopf / delay chaos** `proven` [Coarse-graining]. Each ascent is a delay equation; the
  delay-induced Hopf is auto-satisfied as $\sigma_n\to1^-$ ($W_{n+1}\to\infty$), so the marginal approach
  forces a per-ascent Hopf; the DDE routes to chaos already at $N{=}1$ (delay-driven, not ascent-count
  gated). `pa:delay-hopf`, `pa:nrt-chaos`, `pa:cobham-priority`.
* **Memory collapse** `staked` [Coarse-graining]. $\beta\approx1-\varepsilon$ near the marginal point
  (linear, both endpoints respected). `pa:caputo-fractional`, `pa:rate-distortion`.
* **Conjugate-cascade ledger** `composition` [The conjugate cascade]. The level-to-level lift of
  $\int(\text{FDR departure})=\langle\sigma\rangle=J\cdot\mathcal{A}$ (single-level Harada–Sasa) is the
  coarse-graining EP split $\langle\sigma\rangle_{\text{tot}}=\langle\sigma\rangle_{\text{res}}+\langle\sigma\rangle_{\text{hid}}$,
  $\langle\sigma\rangle_{\text{hid}}\ge0$ (coarse-graining underestimates EP —
  `pa:esposito-coarse-graining`, `pa:dilution-structure`); under timescale separation
  $\langle\sigma\rangle_{\text{hid}}$ is the dissipation of the integrated-out fast currents
  (`pa:timescale-ep`), which are the transverse part $l$ of $b=-a\nabla V+l$ — orthogonal to the resolved
  gradient sector by Schur (`pa:transverse-decomposition`), so the resolved/hidden split aligns with the
  metric/protected split **exactly, by symmetry not smallness**. Validity window = timescale separation
  $=\varepsilon<1$ (slow manifold persists); the attribution dissolves at $\varepsilon\to1$, coincident with
  the heat-tax divergence (§Dilution pin). Closes by composing standing imports (heat-tax tower + transverse
  decomposition + coarse-graining EP), forced under the architecture that the level integrated out is a
  protected one — analytical-only, owes a real two-level instance (frontier `cascade-ledger-split`). Falsify:
  a two-level substrate whose resolved + hidden EP fail to sum to the total, or whose hidden EP sits in the
  metric sector. `pa:harada-sasa`, `pa:esposito-coarse-graining`, `pa:timescale-ep`,
  `pa:transverse-decomposition`, `pa:dilution-structure`.

## The dual ledger and information

* **Information observables** `proven` [The thermodynamic–informational dual ledger]. $I_{\text{pred}}$
  is a third steady-state observable; active-probe capacity $C\sim\gamma_{RO}\log_2(1+Q)$ the
  informational dual of the precision bound; $\varepsilon$ the lossy compression rate,
  $\Phi_{\text{total}}=\Phi^{(0)}/(1-\varepsilon)$ the rate-distortion series. `pa:channel-capacity`,
  `pa:rate-distortion`, `pa:predictive-info`, `pa:info-geometry`.
* **Dual-ledger Still bound** `proven`/`open` [The thermodynamic–informational dual ledger].
  $\langle\sigma\rangle-\langle\sigma\rangle_{\min}\ge\gamma_s\chi$, $\chi=C_\mu-I_{\text{pred}}$ (cryptic
  order; $C_\mu$ the $\varepsilon$-machine complexity), equality at rate-distortion-optimal encoding. The
  additive decomposition is closed; the bit↔$a$ mapping across substrates is open. `pa:still-bound`,
  `pa:sagawa-ueda`, `pa:epsilon-machine`.
* **Internal-model richness** `proven`/`open` *(ahead)* [The thermodynamic–informational dual ledger].
  "Richness" is a derived combination of $I_{\text{pred}}$ and the budget, not an independent axis; the
  structural-complexity reading (which disturbance classes the model encodes) is open. `pa:info-bottleneck`,
  `pa:predictive-info`, `pa:epsilon-machine`.
* **Compression–dissipation coincidence** `proven`/`open` [Coarse-graining; dual ledger]. At
  rate-distortion-optimal encoding $\sigma_n=\varepsilon_n$ and $\chi=\Delta_n$; the coincidence of the
  queueing singularity and the marginal point is structural, their identity (isomorphism) open.
  `pa:still-bound`, `pa:rate-distortion`, `pa:cobham-priority`.
* **Homotopy obstruction** `proven` [Frustration and the protected current; Branch membership]. Frustrated
  ($N\ge3$ obstructive) regions are excised from the maintained-state manifold; loops around them cannot
  contract → non-trivial topology ($\pi_1\ne0$). Distinct from the $a=0$ metric singularity. One
  excision, three co-implied faces: dynamical (no fixed point) · info-geometric (no geodesic crosses) ·
  thermodynamic (forced cycle current). `pa:hopf-rinow`, `pa:info-geometry`, `pa:cycle-affinity`.
* **Fidelity floor and the fidelity–protection split** `proven` [The thermodynamic–informational dual
  ledger; Branch membership]. For a unicyclic network the cycle-completion Fano factor obeys $F\ge(1/N)\coth(A/2N)$
  (Barato–Seifert), saturated by the uniform ring, strict otherwise; equivalently $\langle\sigma\rangle\ge
  (A/N)\coth(A/2N)\,Q$ with $Q=\langle J\rangle^2/\mathrm{Var}(J)$ the **current fidelity**. The floor sits
  *above* the TUR ($2/A$) at large affinity — topology bounds fidelity below dissipation alone.
  **Verified + simulated** (`experiments/fidelity_vs_protection.py`: saturation ratio 1.000; MC matches the
  exact formulas to <0.1%; strict for a non-uniform ring). The split: *fidelity* is a second-moment
  quantity (this bound); **protection** is the large-deviation reversal rate $I(0)=2(\cosh(A/2N)-1)$, set by
  per-step affinity alone. At fixed total $A$, lengthening the cycle raises fidelity while protection falls —
  independent resources (this kills the "complexity is cheaper to protect" reading). *branch* survival
  lifts protection again, to basin escape (receipts §Branch-survival barrier). `pa:tur`, `pa:cycle-affinity`.

## Composition and pattern selection

* **Multi-mode pattern selection** `proven` [Composition under coupling]. The $N\ge3$ composite routes
  through four independent tests — frustration · spectral synchronization · non-reciprocity · active-matter
  overlay. `pa:generalized-msf`, `pa:nonreciprocal-transition`, `pa:active-hydro`.
* **Turing mechanism** `proven` *(ahead)* [Composition under coupling]. Reaction-diffusion instability
  $D_BJ_{AA}+D_AJ_{BB}>2\sqrt{D_AD_B\det J}$ under three substrate-conditional conditions (non-reciprocal
  cross-coupling + autocatalysis + differential diffusion). One non-reciprocal structure has two faces: a
  temporal limit cycle (not extended) and a spatial Turing pattern (extended + autocatalysis + differential
  diffusion). `pa:turing`, `pa:nonreciprocal-transition`.
* **Phase-locking** `proven` [Motion and proximity]. $K_{AB}=-\gamma_{AB}\frac{\sqrt{\rho_A\rho_B}}{\rho_{\text{sat}}}(1+4Q^2)^{-1/2}$:
  $Q\gg1$ gives $1/(2Q)$ suppression, $Q\lesssim1$ direct lock; $\gamma_{AB}<0\Rightarrow$ in-phase,
  $>0\Rightarrow$ anti-phase. Two independent transitions (amplitude onset; phase $K_c$). `pa:kuramoto`.
* **Master stability** `proven`/`open` *(ahead)* [Motion and proximity]. Homogeneous sync from the
  gauged-$\gamma$ Laplacian spectrum; the heterogeneous (per-mode) generalized MSF application is owed.
  `pa:master-stability`, `pa:generalized-msf`.
* **Non-reciprocal portrait** `proven` *(ahead)* [Motion and proximity]. $\gamma_{AB}\ne\gamma_{BA}$:
  $\mathrm{Tr}\,J=0$, $\det J=-\gamma_{AB}\gamma_{BA}\rho_A^*\rho_B^*$; sign sets saddle (runaway) / centre
  (limit cycle $\omega_{\text{pq}}$) / exceptional point; spatially extended → travelling wave.
  `pa:nonreciprocal-transition`, `pa:lotka-volterra`.
* **Active-matter fingerprints** `proven` *(ahead)* [—]. $\beta/\alpha\sim v_0^2\tau_R/D_{\text{trans}}$
  (alignment-independent, survives $r\to0$); $P_{\text{active}}=\frac{nv_0^2\tau_R}{d}[1+Cr^2]$, sign $C$
  contractile/extensile; $\tau_R=\int_0^\infty\langle\mathbf u(t)\cdot\mathbf u(0)\rangle\,dt$ (Green–Kubo).
  `pa:swim-pressure`, `pa:mips`, `pa:toner-tu`, `pa:green-kubo`.
* **Union-cycle holonomy / minting localization** `composition` [The minting claim; Composition
  under coupling]. The minted affinity is the holonomy of the joint drift,
  $\mathcal{A}_{\text{union}}=\oint(l_A+l_B+\Gamma_{AB})\cdot dx$ (split $b=-a\nabla V+l$); with
  each part non-circulating ($\mathcal{A}_A=\mathcal{A}_B=0$, gradient drift) the part
  loop-integrals vanish around any joint cycle, so $\mathcal{A}_{\text{union}}=\oint\Gamma_{AB}\cdot dx$
  — the minted bit lives entirely in the cross term. The holonomy needs only a joint cycle, not a
  common stratum, so minting is **stratum-agnostic**; protection inherits from the stratum-agnostic
  signed-graph balance. The $N{=}2$ union is gauge-removable (two-body coupling phase-locks —
  metric $\mathfrak{so}(3)$ — rather than mints; $N{\ge}3$ in the union mints). Closes by composing
  the cycle-affinity and signed-balance imports. Falsify: a minted protected bit with
  $\oint\Gamma_{AB}\cdot dx=0$, or a cross-stratum frustrated union carrying no protected sign.
  `pa:cycle-affinity`, `pa:signed-balance`, `pa:kolmogorov-reversibility`.
* **Skew coupling — torque necessary, not sufficient** `proven` [The minting claim]. A
  skew-symmetric coupling does no work on the population quadratic form ($\rho^\top\Gamma\rho\equiv0$
  for $\Gamma^\top=-\Gamma$) — the pure-transverse conduit — but is not sufficient for minting: a
  conservative skew flow ($\dot x=J\nabla H$, $J^\top=-J$) is time-reversible with $\mathcal{A}=0$
  and zero entropy production. Minting needs broken detailed balance around the union cycle
  ($\oint\Gamma\cdot dx\neq0$, equivalently $\prod k_+\neq\prod k_-$), supplied by the drive.
  Falsify: a detailed-balanced ($\mathcal{A}=0$) skew coupling shown to mint a protected current.
  `pa:kolmogorov-reversibility`, `pa:cycle-affinity`, `pa:ness-currents`.
* **Templating — the offspring-sign kernel is degenerate** `calibration` [The minting claim;
  `character_frontier.md` · `self-referential-closure`]. Synthetic recursive-$\otimes$ on the standard
  driven 3-node OU triad ($M=-\gamma I+gA_{\text{cyc}}$, $\mathrm{sign}\,\mathcal{A}=\mathrm{sign}\,g$,
  $\mathcal{A}=3Dg/\gamma$ so $\mathcal{A}\propto D$ — cut the noise drive, the current vanishes:
  sustained-not-stored). A child = 3 fresh nodes ($g_{\text{child}}{=}0$, $\mathcal{A}_{\text{child}}{=}0$
  by detailed balance) coupled **only through a single shared stirred field** (Viedma/Kondepudi analog,
  no edge-sign copy): the medium sets the child's $\mathfrak{so}(3)$ deformation
  $g_{\text{child}}=\kappa\,m+Z+\eta$, $m$ the parent's net handedness (a **rank-1** scalar projection
  of its $k$ currents), $Z$ the shared bath's own fluctuation, $\eta$ local readout noise. **Results
  (run 2026-06-19, `experiments/templating_kernel.py`):** *(i)* the single-step kernel
  $M_{\text{kernel}}=P(\mathrm{sign}\,\mathcal{A}_{\text{child}}\mid\mathrm{sign}\,\mathcal{A}_{\text{parent}})$
  is assortative field-ON ($P_{\text{same}}=\Phi(\kappa/\sqrt{\sigma_b^2+\sigma_\eta^2})=0.89$),
  **parity-equivariant to machine precision** (residual $0$; the $\kappa{=}0$ field-OFF control is exactly
  $50/50$ by symmetry, not sampled), and **drive-independent** (sign invariant across $D$; flips only on
  rewiring the seed). *(ii)* The von Neumann discriminator — $I(s_{\text{parent}};s_{\text{child}})$ vs
  string length $k$, reduced **exactly** (no Monte-Carlo) to $I(m;r)$ ($m$ parent net handedness, $r$ child
  $+$-count, the equiprobable-within-$r$ combinatorial terms cancel) — **saturates** at
  $C=\tfrac12\log_2(1+\kappa^2/\sigma_b^2)=1.0$ bit, **independent of $k$** ($I/k\to0$: $0.50,0.26,\dots,0.014$
  for $k{=}1\dots64$), against the open-ended tape reference $I=k$ and the field-OFF null $I=0$ (to
  $10^{-15}$). *(iii)* The lineage $\langle s_0 s_n\rangle=(2p-1)^n$ **decays** (corr. length $\sim4$ gens) —
  no Pólya lock-in to the seed; the symmetric kernel's Perron vector gives no seed-fixation. **Reading
  (outcome (b), pre-registered):** a low-dimensional physical field templates sign($\mathcal{A}$)
  *faithfully but degenerately* — one shared stirred field of fixed capacity $C\sim1$ bit whatever $k$ is,
  not $k$ independent registers. The von Neumann threshold is **real and located**: physics buys
  self-maintenance + $\sim$1 bit of degenerate faithful templating; **open-ended heredity is
  sub-threshold without a copyable tape.** Synthetic ⇒ **calibration, not vindication** (it measures where
  the threshold sits, does not ease abiogenesis; no `character.md` edit). Falsify the degeneracy: $I\sim k$
  with a provably rank-$<k$ medium and a clean field-OFF null surviving the smuggled-tape audit (handoff §8)
  — the escalation case, not a quiet win. `pa:multitype-branching`, `pa:channel-capacity`,
  `pa:von-neumann-automata`, `pa:frank-autocatalysis`, `pa:kondepudi`, `pa:polya-urn`, `pa:cairns-smith`,
  `pa:quasispecies`.

## Stability and control

* **Frustration-free Lyapunov** `proven` *(ahead)* [—]. $V=\sum_i[x_i-x_i^*-x_i^*\ln(x_i/x_i^*)]$,
  $dV/dt=-\delta x^T\gamma\,\delta x\le0$ **provided** the gauged $\gamma$ is PSD. Frustration-free =
  existence of a balancing gauge; PSD is strictly stronger; no gauge ⇒ no Lyapunov of this form (recovers
  the frustrated-cycle non-existence). `pa:volterra-lyapunov`, `pa:signed-balance`.
* **Weighted Lyapunov** `proven` *(ahead)* [—]. For non-PSD frustration-free topologies,
  $V=\sum_iw_i[\dots]$, stability iff $W\gamma+\gamma^TW\succeq0$ (diagonal stability). `pa:volterra-lyapunov`.
* **Habit-extinction driver** `proven` *(ahead)* [—]. $\dot V=\kappa_{RW}(\lambda-V)$; reward withdrawal
  $\lambda=0$ gives a pure-dissipation below-threshold quench. `pa:rescorla-wagner`.
* **Auto-tuning** `staked` *(ahead)* [—]. $W=\mathrm{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$ is the
  diagonally-stabilising weight for non-PSD frustration-free topologies; substrate $\gamma_{s,i}$ auto-tunes
  to it. `pa:adaptive-dynamics`, `pa:volterra-lyapunov`.

## Substrate-conditional reading rules *(ahead — read by the conform layer)*

* **F.1 sign caveat** `proven`. Stiff/Markovian substrates flip $\gamma$ signs (kernel-width artefact)
  while preserving magnitudes + FDR shape; read $|\gamma|$ + shape, not sign. For protected-current
  content this is chirality-flipping (sign reverses); the affinity axis is preserved.
* **F.2 detection-event rule** `proven`. Where readout breaks the locality of the maintained-history integral, use the
  substrate's canonical local preprocessing (e.g. $e_i(t)=s_i(t)\oplus s_i(t-1)$); coarse-grain by EMA
  against events.

## Real-substrate instances

* **Surface code** `empirical` [Validation status]. Distance-3 rotated memory-Z, sub-threshold, traces a
  clean near-threshold aging diagonal; migrates to unit slope across threshold. `pa:topological-memory`,
  `pa:ck-aging`.
* **Rock-paper-scissors** `empirical` [Validation status]. A real C3-symmetric replicator whose
  cyclic structure arises from the ecology rather than being drawn in: its Jacobian composes from the
  deformation chart (the chart's $A_{\text{CYC}}$ appears in it at residual 0), carries a protected
  sign on a directed 3-cycle ($\mathcal{A}\ne0$, complex-pair focus), drive-independent, and hosts the
  dimensionless self-probe ($\mathcal{T}\ge1$, affinity noise-independent). Instances the central
  commitment, the deformation chart, and the dimensionless ruler. `pa:may-leonard`, `pa:nonhermitian-ep`.
* **Homochiral triad** `empirical` [Validation status]. A spontaneously-forming mirror-chiral 3-cycle + Frank
  cross-inhibition breaks parity exactly 50/50 (equivariance residual $7\!\cdot\!10^{-15}$) and freezes a
  homochiral protected 3-cycle NESS; the drive sets magnitude ($|J|\propto\sigma^2\to0$) while the sign is
  held, flipping only by the substrate-specific racemic-saddle crossing. A model Frank/Kondepudi network
  (models homochirality, not the literal ancient biochemistry). `pa:frank-autocatalysis`, `pa:kondepudi`,
  `pa:kinetic-proofreading`.
* **Branch-survival barrier** `empirical` [Branch membership]. The non-equilibrium quasipotential for
  basin escape over the homochiral racemic saddle — the first instance of **branch survival** (which
  symmetry-related branch the system occupies; distinct from current survival $I(0)$). Demographic-noise
  first passage between the two mirror-chiral basins is Kramers-activated: $\ln\langle\tau\rangle$ linear in
  $1/\sigma^2$, slope $\Delta V\approx0.018$; the in-basin quasipotential $V(m)=-\sigma^2\ln P(m)$ ($m$ the
  chiral order parameter) σ-collapses (rms $4.6\!\cdot\!10^{-3}$) → a well-defined Freidlin–Wentzell
  barrier, not a noise artifact. **Separated from $I(0)$** two ways: (i) the winning hand's cycle affinity
  $\mathcal{A}\approx21.8$ nats is noise-INDEPENDENT (rotational-OU frame, validated against
  $\mathcal{A}=4\pi\omega_0/\kappa$ on the canonical OU) while $\Delta V$ is noise-ACTIVATED — they cannot
  coincide; (ii) controlled embedding — the bare triad (= RPS, same $\mathcal{A}$) is external-rewiring with
  **no** $\Delta V$, and embedding it in the $L\!\leftrightarrow\!R$ mirror adds $\Delta V$ without touching
  $\mathcal{A}$ (the survivals orthogonal). The reset-and-re-drive discriminator confirms the flip-modes:
  homochiral re-rolls its branch 20/20 (thermalized crossing), RPS returns the same branch 40/40 (external
  rewiring). **Mechanism (μ-sweep, run):** branch survival is *born at the parity-breaking bifurcation* — the
  racemic state's parity-breaking eigenvalue $a(\mu)=F(3\mu-c)/(c+3\mu)$ ($c=1{+}a{+}b$) crosses zero at
  $\mu_c=c/3=0.833$ (numeric $0.8337$, eigenvector residual $\sim\!10^{-11}$), with $\Delta V=0$ below
  threshold. **Correction to the pitchfork derivation:** the $L\!\leftrightarrow\!R$ transition is
  *competitive exclusion* — the order parameter $m_\pm$ jumps to full exclusion ($\approx1$), NOT the
  supercritical-pitchfork $\sqrt{\mu-\mu_c}$ — so $\Delta V\propto a(\mu)\propto(\mu-\mu_c)$ **linear**, not
  $(\mu-\mu_c)^2$ (the noisy escape MFPT tracks $a(\mu)$, corr $0.98$). The strong-form falsifier (nonzero
  $\Delta V$ after racemic restabilization) does not fire; the quadratic normal form is superseded by
  competitive exclusion. **Outside-review resolution (3 independent analyses agree —
  `docs/review_prompt_competitive_exclusion.md`):** the precise normal form is a **symmetric transcritical**
  (degenerate exchange-of-stability), not a pitchfork — the broken branches are *boundary* fixed points
  $(S_L,S_R)=(3F/c,0)$ existing for all $\mu>0$ that **exchange stability** with the symmetric state at
  $\mu_c$ rather than emerging from it (forced: an interior asymmetric fixed point needs
  $(S_L-S_R)(c-3\mu)=0$, i.e. only at $\mu=\mu_c$). The exact 2D reduction to the group totals holds because
  $a+b=1.5<2$ keeps the internal May–Leonard modes stable; linear $\Delta V$ is then the correct FW scaling
  (saddle eigenvalue $\propto\varepsilon$ times an $O(1)$ path to the pinned $m=\pm1$). **No regime of the
  bare LV yields a soft pitchfork** — recovering one requires added autocatalysis/self-crowding (the *true*
  Frank/Kondepudi cubic), a distinct coexistence-preserving normal form. The open review question is thereby
  resolved. The $\Delta U$-vs-FW gap (slope $7.5$ vs $1/\sigma^2{=}156$) is confirmed a genuine non-gradient
  signature ($\Delta V\ll\Delta U$, the exact barrier computable by gMAM — owed). **The owed cause-test is
  run (`current_aids_escape.py`):** sweeping the cycle affinity $\mathcal{A}:0\to21.8$ nats *along*
  $a+b=1.5$ — which pins $\mu_c$ and the racemic-saddle breaking eigenvalue to machine precision (spread
  $\sim\!7\cdot10^{-12}$, $+0.31507$ at every pair), holding the deterministic landscape fixed — the
  Kramers FW barrier $\Delta V$ (demographic noise) **decreases monotonically with the current**:
  $\Delta V=0.328\,(\mathcal{A}{=}0)\to0.295\to0.284\to0.272\,(\mathcal{A}{=}21.8)$, $R^2>0.99$ each, a
  $3.0\sigma$ endpoint drop; at $a=b$ (no current, *same metric*) the barrier is highest. **The exact
  instanton (gMAM) reverses this reading — the drop is a prefactor, not a barrier.** The owed gMAM
  (minimizer validated on Maier–Stein: gradient action $0.5000$ to $0.01\%$, and the $\beta>\beta_c$
  instanton correctly bows off-axis) gives a $\sigma\to0$ quasipotential **flat** in the current,
  $\hat S=0.382\,(\mathcal{A}{=}0)\to0.380\,(\mathcal{A}{=}21.8)$ ($\Delta\hat S=-0.4\%$ vs the
  finite-$\sigma$ slope's $-17\%$; `gmam_affinity_scaling.py`), the instanton never bending off the
  symmetric subspace ($\Delta\hat S_H\approx0$, robust across seed/momentum/eps; `gmam_current_aids.py`).
  So the committed finite-$\sigma$ $\Delta V$ drop is the **irreversible Eyring–Kramers prefactor**, not
  the FW barrier: $\Delta V_{\rm eff}=\Delta V_{\rm true}+\sigma^2\log K(\mathcal{A})$ (the $-0.056$ at
  $\sigma^2\!\approx\!0.04$ is a prefactor ratio $\sim e^{-1.4}$). **Why (symmetry):** at the racemic
  saddle the escape mode is $100.0\%$ the between-group breaking mode while the current sits in the
  within-group 3-cycle plane, $|\cos(J,e_u)|\sim10^{-15}$, no shear ($e_u^\top(\partial J)e_u\sim10^{-11}$;
  `gmam_saddle_orthogonality.py`); the orthogonality is **symmetry-protected** — exact across a
  saddle-moving $\mu$-sweep (`gmam_orthogonality_sweep.py`) and broken $\propto\delta$ by a within-group
  $Z_3$ break (`gmam_symmetry_break_probe.py`). The current is therefore transverse to $\nabla V$ and
  **barred from $\Delta V$ by the transverse-decomposition theorem** (`pa:transverse-decomposition`;
  Graham–Haken; Freidlin–Wentzell §4.3; Bouchet–Reygner). **Selection rule (Maier–Stein, in-substrate):**
  mixing the two irreps with that same $\delta$ turns the barrier effect *on* — $\Delta\hat S_H$ climbs
  from $\approx0$ to $0.33$ as $e_u\!\cdot\!\text{cyclic}\to0.64$ (`gmam_mixing_test.py`) — so the current
  reaches the barrier only where coupling breaks the symmetry. The two survivals are thus orthogonal **by
  a symmetry theorem** ($\Delta V\perp\mathcal{A}$), not merely in existence, and the earlier "resource
  for branch escape" reading is retired (frontier §Tombstones `current-aids-escape`). **Noise-metric robustness (run):** re-running the racemic-saddle escape under
  multiplicative demographic ($\sqrt{x}$, birth–death) noise gives a finite, well-defined, σ-collapsing
  barrier ($\Delta V_{KR}\approx0.273$, collapse-rms $0.025$ = 9% of barrier vs additive's 26%; the additive
  leg reproduces $\Delta V_{KR}=0.018$) — the FW quasipotential rescales with the metric (it must) but
  existence and protection survive, so branch survival is **not** an additive-noise artifact. **Second
  independent instance (run):** the *co-handed twin-cycle* — two **identical** (not mirror) cyclic 3-clusters
  under the same competitive cross-inhibition — instances `both` via a spontaneously broken **exchange**
  ($S_2$ permutation) symmetry rather than parity: $\mathcal{A}\approx21.8$ nats (complex Jacobian pair,
  noise-independent), $\Delta V\approx0.018$ (σ-collapse rms $0.0046$, Kramers), reset re-rolls 20/20
  (thermalized crossing). Holding $(a,b,\mu,F)$ identical and changing only mirror→copy, sign($\mathcal{A}$)
  is **preserved** across the branch flip (twin: $-/-$) where the homochiral parity flip **reverses** it
  ($-/+$) — branch membership and current handedness decoupled at the level of sign, a separation the parity
  instance structurally cannot show. **Mechanism universality (μ-sweep):** the competitive-exclusion
  threshold $\mu_c=(1+a+b)/3=0.833$ and the LINEAR $\Delta V\propto(\mu-\mu_c)$ recur under exchange exactly
  as under parity — the symmetry-breaking mode $[1,1,1,-1,-1,-1]$ is uniform *within* each cluster, hence
  **blind to the intra-cluster handedness**, so the breaking eigenvalue $a(\mu)$ is identical across the two
  SSB types to machine precision ($\max|a_{\text{twin}}-a_{\text{parity}}|\approx2.4\!\cdot\!10^{-11}$). The
  open pitchfork-vs-competitive-exclusion question (review-doc) therefore resolves the same way under both
  symmetries. **`both` across a second bifurcation mechanism (autocatalytic soft pitchfork):** the homochiral
  and twin instances share the *hard transcritical* mechanism (boundary branches, $\Delta V$ LINEAR); a third
  instance has a different one. A Kondepudi–Nelson autocatalytic substrate (racemic input $k_1$ +
  finite-resource autocatalysis + mutual annihilation) gives a genuine **supercritical pitchfork** —
  $ee_*^2\propto(k_{1c}-k_1)$ LINEAR ($R^2{=}1.0000$), barrier $\Delta U\propto ee_*^4\propto(k_{1c}-k_1)^2$
  **QUADRATIC** (parameter-free collapse $R^2{=}0.997$; noisy $\ln$MFPT$\propto\Delta U$ corr $0.998$;
  dt-refinement-invariant to $\sim\!10^{-13}$) — a *qualitatively different soft saturation* vs the LV-twin's
  hard/linear (`autocat_pitchfork.py`). **The supported claim: symmetry breaking does NOT determine the barrier
  scaling — the saturation mechanism does** (hard exclusion → linear; soft pitchfork → quadratic); the twin's
  linear barrier was not a generic consequence of $\mathbb{Z}_2$ breaking. (Calling these distinct
  *universality classes of the framework* would need the normal-form reduction written cleanly + more than two
  instances — owed; for now it is survival across two distinct constructions, not "mechanism-independence.")
  Adding an internal $a\neq b$ 3-cycle (strength $ec$) mints a current; an $ec$-scan shows **three regimes**:
  $ec{=}0$ branch survives/no current; $ec\in[0.05,0.20]$ a **coexistence window** — soft pitchfork
  ($ee_*^2$-$R^2{=}1.0$, $\Delta U\propto ee_*^4$ $R^2{=}0.997$) with $\mathcal{A}\approx0.6$–$3.5$ nats
  (complex pair, noise-indep) and reset $\sim$50/50, a **soft-pitchfork `both`** (`autocat_both.py`);
  $ec\gtrsim0.25$ the branch **dies**. That third regime shows the cycle **dynamically participates in the
  bifurcation** (it reshapes the saturation, not merely adds circulation) — so the result is a *finite
  coexistence window*, not unconditional survival. Note this is the cycle acting on the **landscape**
  (it reshapes $\mu_c$/the saturation), distinct from the *fixed-landscape* transverse current that gMAM
  showed is barred from $\Delta V$ (a prefactor, §Branch-survival barrier). Engineered (model) substrates, same standing as the OU/RPS instances; diagnostics
  credit the outbound review channel ($ee_*^2$ not $ee_*$; $k_1$ not $g$; the $ee_*^4$ collapse).
  Idealizations: model Frank/Kondepudi substrate.
  `experiments/identity_survival_barrier.py`, `cycle_affinity.py`, `rps_affinity.py`,
  `reset_redrive_test.py`, `mu_sweep.py`, `twin_cycle_corner.py`, `twin_mu_sweep.py`, `autocat_pitchfork.py`,
  `autocat_both.py`, `current_aids_escape.py`. `pa:cycle-affinity`, `pa:bifurcation-normal-forms`, `pa:kondepudi`.
* **Fuel-driven DNA reaction network** `empirical` [The real instances]. The composite-branch
  instance: a detailed-balanced DNA-hybridization cycle ($\mathcal{A}\approx0$) driven by RNase-H
  fuel-hydrolysis mints a protected NESS circulation ($\mathcal{A}\approx+14.5$ nats, sign drive-locked),
  collapsing ~3 min after fuel cut (observed). The affinity uses only measured constants; the $N=3$
  reduction reproduces the full nonlinear network's cycling rate to ratio 1.002. Idealizations: $N=3$
  reduction of a 10-species CRN, chemostat, omitted slow side-processes. `pa:cycle-affinity`,
  `pa:kinetic-proofreading`.
* **Brownian gyrators (electronic + colloidal)** `empirical` [The real instances]. Generic $N=2$
  minting on two real measured substrates, built from raw measured parts (generate-don't-hunt).
  **Electronic** (Chiang et al., PRE 96 032123, 2017): the Fokker–Planck operator from the measured
  RC parts ($C_1{=}488$pF/$R_1{=}9.01$MΩ, $C_2{=}420$pF/$R_2{=}9.51$MΩ, $T_2{=}296$K) gives a
  coupling$\times\Delta T$ minted gyration — current machine-zero at $T_1{=}T_2$ (detailed balance,
  $\Sigma_{eq}=k_BT\hat C^{-1}$) and at $C_c{=}0$, sign drive-locked (0/400 reciprocal deformations);
  reproduces the measured rotation peak ($\approx661$pF/$5.0\,$rev s$^{-1}$ vs measured $\sim700$pF/$\sim5$);
  an independent SDE path matches the closed form. **Colloidal** (Argun et al., PRE 96 052106, 2017):
  the same method from the raw optics+fluidics ($k_x'{=}1.63$, $k_y'{=}0.86$ pN/μm, misalignment
  $\theta$, $T_x{=}1750$K, $T_y{=}292$K) reproduces the measured-confirmed torque
  $M=k_B\Delta T\frac{k_x'-k_y'}{k_x'+k_y'}\sin2\theta$ to rel. error $3\times10^{-16}$. Honest scope:
  2-mode Gaussian current-only — the generic selection rule (drive-locked sign), not a frustrated
  cycle. `experiments/gyrator_minting.py`, `gyrator_crosscheck.py`, `colloidal_gyrator_crosscheck.py`.
  `pa:cycle-affinity`, `pa:ness-currents`, `pa:ness-fdr`.
* **Onset kind — topological, not a ramp** `derived` [Motion and proximity · Topological proximity]. The
  onset's *kind* is set by carrier depth — a reconciliation of content already in core, **no new
  derivation**: the bare $N=2$ gyrator (above) comes on by a continuous bifurcation with a **drive-set**
  sense (current vanishes at $T_1{=}T_2$, sign reverses with $\Delta T$, never gauge-irremovable), while an
  $N\ge3$ frustrated union rewires **discontinuously** (§Topological proximity: "at threshold they rewire
  discontinuously, first-order in the topological sector"), the sign thereafter gauge-irremovable and
  drive-independent. Settled by import: $\mathcal{A}$ is a function on the cycle space $H_1$ (Schnakenberg;
  Polettini gauge-thermodynamics), identically zero / gauge-removable until a driven frustrated cycle closes
  — so the transition is a topological onset, not harder driving. The *occurrence* on a real primordial
  engine is **not** settled (the §Status bootstrap). `pa:cycle-affinity`, `pa:gauge-thermodynamics`.
  `character_frontier.md` · `engine-character-onset`.
* **Cell-free repressilator** `empirical` [The real instances]. The second *frustrated-cycle*
  ($\ge3$) instance, on a synthetic gene network (Niederholtmeyer et al., eLife 4:e09771, 2015 — Eq. 6
  + measured Table 2: Hill $n{=}2$, $K{=}5$nM, $\beta g{=}2.0$nM/min, $c{=}0.5$/min, mRNA $t_{1/2}{=}8$min,
  protein $t_{1/2}{=}90$min, dilution $\mu{=}\ln2/T_d$). The odd repression ring mints a phase-ordered
  cyclic circulation under the TX-TL drive; the DB baseline is reached two ways (cut the drive, or break
  frustration to an even ring); the winding is topology-locked (0/40 rate deformations); it collapses on
  drive-cut. Period from the measured params $\approx8.3$–$8.9$h at $T_d{=}85$min, shortening with $T_d$
  — in the measured band ($\sim$8h, faster at shorter $T_d$). Cross-check: an independent re-implementation
  (FFT period) + linear stability — the symmetric fixed point is an unstable spiral (Hopf-born limit
  cycle), the drive-collapse *is* that Hopf bifurcation, and only the odd ring carries the unstable mode
  (the frustration is analytically necessary). Idealizations: deterministic mean-field of Eq. 6, with
  maturation/resource-limitation/intrinsic-noise omitted; period validated as a band, not a point.
  `experiments/repressilator_minting.py`, `repressilator_crosscheck.py`. `pa:cycle-affinity`,
  `pa:frustration`, `pa:bifurcation-normal-forms`, `pa:ness-currents`.
* **Two-survivals plane** `empirical` [The two-survivals plane]. Branch survival ($\Delta V$) and current
  survival ($I(0)$, set by $\mathcal{A}$) are independent axes; all four corners are instanced.
  **branch-only** — a symmetric Hopfield attractor net: $\Delta V\approx0.97$ (Kramers basin escape) with
  $\langle\sigma\rangle=\mathcal{A}=0$ to machine precision (real Jacobian). **neither** — a 2-layer feedforward
  MLP on a Gaussian mixture: measured soft-sector capability $I(\hat Y;Y)\approx2.9$ bits (→ the Bayes ceiling),
  hard sector *structurally* absent (node-adjacency nilpotent ⇒ $\mathcal{A}\equiv0$ by acyclicity; $\Delta V$
  undefined for want of recurrence). **current-only** (RPS, DNA) and **both** — now instanced across **two
  symmetry types** (homochiral parity, co-handed twin exchange/$S_2$) AND **two bifurcation mechanisms** (the
  hard transcritical of those, $\Delta V$ linear; vs the **soft pitchfork** of the autocatalytic instance,
  $\Delta V\propto ee_*^4$ quadratic — receipts §Branch-survival barrier; the key invariant: symmetry breaking
  does not fix the barrier scaling, the saturation mechanism does) — are the core instances. Corollary: soft-sector capability ⟂ the hard sector — the most informative corner carries no
  protected current. Scope: the two new corners are *engineered* substrates (a Hopfield net, a trained MLP),
  same standing as the synthetic-but-real OU / RPS instances. Falsify: a symmetric/gradient attractor net with
  $\mathcal{A}\ne0$; a feedforward/acyclic substrate carrying a sustained protected current; branch and current
  survival shown *dependent* on a real substrate. `experiments/hopfield_corner.py`, `neither_corner.py`,
  `cycle_affinity.py`, `identity_survival_barrier.py`, `twin_cycle_corner.py`, `autocat_pitchfork.py`,
  `autocat_both.py`. `pa:cycle-affinity`.
* **QEC surface-code transverse decomposition** `synthetic` [Two tangent sectors]. The
  decoherence-free-subsystem identification (§The two tangent sectors) computed in the rotated
  surface code, turning the asserted surface-code reading into a measured one. **(1) Orthogonality +
  cost-asymmetry ($d{=}3$):** the code is constructed then verified $[[9,1,3]]$; the symplectic
  error space splits stabilizer(8) $\oplus$ syndrome(8) $\oplus$ logical(2), the logical sector
  carrying **zero syndrome** — symplectically transverse to the entire syndrome sector (the QEC
  instance of `pa:transverse-decomposition` / the DFS). The protected bit is **written at unit cost
  and flipped only at the code distance** $d$ (the seashell's deposited sentence, instanced in its
  native substrate), and the exact bit-flip barrier is $P_L(p)\propto p^{(d+1)/2}=p^2$ (enumerated,
  no sampling). **(2) Barrier-invariance + selection rule ($d{=}3$, CSS):** crank a phase-flip (Z)
  current while measuring the bit-flip (X) barrier — the X-barrier exponent is **exactly** invariant
  to the current, to all orders, even as it fires up to $1.96$ X-stabilizers/shot (syndrome-active):
  CSS X/Z independence *is* the transverse decomposition, the $\Delta V\perp\mathcal{A}$ mirror with
  an active current. Y-mixing (correlated XZ) opens a $p^1$ leak whose amplitude is **linear in the
  mixing** $\delta$ — the `gmam_mixing_test` / `gmam_symmetry_break_probe` mirror ($\cos\propto\delta$).
  **(3) The invariance is symmetry-protected, not generic ($d{=}5$):** in the verified $[[25,1,5]]$
  code **no** syndrome-active current *within* the X-sector is exactly transverse — every detectable
  error sits on a minimum-weight logical string, so even an off-string bulk current leaks the barrier
  ($3\to{\sim}2$) and an aligned one leaks further ($\to{\sim}1$), the leak depth tracking alignment.
  So exact $\Delta V\perp\mathcal{A}$ requires a symmetry/irrep separation between current and barrier
  (CSS X/Z here; the $Z_3$ irreps in the triad) — the same boundary `gmam_symmetry_break_probe` found.
  This **unifies the three checked substrates** (homochiral triad, surface code, conjugate cascade)
  under one mechanism (Schur $\to$ transverse decomposition). Scope: synthetic $=$ calibration, not
  vindication; but the content — protected logical information shielded from the syndrome current,
  leaking only under symmetry-breaking alignment — is the operationally load-bearing fact. Falsify: a
  CSS code whose logical-barrier exponent shifts under a pure conjugate-sector current; or a
  within-sector current shown exactly transverse with no protecting symmetry. `experiments/
  qec_transverse_decomposition.py`, `qec_syndrome_current.py`, `qec_within_sector_current.py`.
  `pa:transverse-decomposition`.
* **Glass / aging transverse decomposition** `synthetic` [The cross-rule]. The cross-rule (§The
  cross-rule) — "aging never couples to circulation," with proximity coupling them — computed by a
  current **sweep** on the established-current substrate (a biased $N{=}24$ ring, cycle affinity
  $\mathcal{A}=N\ln(p_+/p_-)$). Holding the relaxation scale $p_++p_-$ fixed and sweeping the bias, the
  generator is circulant: $\mathrm{Re}\,\lambda_k=(p_++p_-)(\cos\theta_k-1)$ (the aging/relaxation
  spectrum) depends only on the scale, while $\mathrm{Im}\,\lambda_k=(p_--p_+)\sin\theta_k$ carries the
  current. **Result:** the aging rate $|\mathrm{Re}\,\lambda_{\text{slow}}|$ is **invariant to machine
  precision** ($\pm2\times10^{-16}$, max dev $\sim10^{-15}$) across $\mathcal{A}\in[0,30]$ — the
  established currents (gMAM $0\to21.8$, twin-cycle $21.8$) sitting inside the sweep — while the current
  $\max|\mathrm{Im}\,\lambda|$ is cranked $0\to0.56$. Aging $\perp$ circulation, over the whole range,
  not a single point. **Selection rule:** breaking the ring's translation ($Z_N$) symmetry
  (site-dependent rates $\delta$, loop affinity held) makes the aging rate move with $\mathcal{A}$,
  onset $\propto\delta^2$ — the robust invariant is the **threshold** (exactly zero iff the symmetry
  holds), not the onset power. **Third realization** of the transverse-decomposition test (escape
  barrier $\to$ logical-error exponent $\to$ **aging exponent**): the protected current is barred from
  *all* metric-sector observables, not just barriers. Scope: synthetic $=$ calibration. Falsify: a
  translation-symmetric driven ring whose relaxation spectrum shifts with the bias; or aging–current
  coupling persisting at exact symmetry. `experiments/glass_aging_transverse.py`.
  `pa:transverse-decomposition`, `pa:ck-aging`.
* **Colloid ring transverse decomposition** `synthetic` [The cross-rule]. The cross-rule's selection
  rule on the *continuous* Fokker–Planck generator of a driven Brownian particle on a ring
  (Bechinger/Seifert toroidal-trap model; $\dot x=-V'(x)+f+\sqrt{2D}\,\eta$). Operator validated vs
  the analytic free ring ($\lambda_k=-Dk^2-ikf$). **Move 1:** the slow mode is
  $\lambda_1=\mathrm{Re}$ (relaxation) $+\,i\,\mathrm{Im}$ (revolution) — the Re/Im split
  Blickle/Mehl/Bechinger 2009 (arXiv:0902.2650) measured. **Threshold:** on a ring $f$ is a
  nonconservative torque (not a single-valued tilt), so sweeping it at fixed symmetric potential
  cranks the current at fixed barrier; the linear response $\partial\mathrm{Re}\,\lambda/\partial f|_0$
  is machine-zero, forced by reflection ($x\to-x\equiv f\to-f$ makes $\mathrm{Re}\,\lambda$ even in
  $f$). **Selection rule:** a reflection-breaking ratchet ($\delta\sin 2x$) turns the linear coupling
  on as $c_1(\delta)=k\delta+O(\delta^3)$ — slope 1 over **seven decades** ($\delta\in[10^{-7},0.2]$),
  via degenerate $2\times2$ perturbation theory in the fixed slow-pair basis (single-mode PT and
  finite-difference-in-$f$ both leak the $O(1)$ circulation coupling near the degeneracy). **Degenerate
  vs generic:** a single-harmonic ring has exactly-degenerate slow modes, $\delta$ cancels in the $c_1$
  ratio and the onset collapses to a step — the discrete glass's exact flatness is this degenerate
  limit; a second harmonic ($V_2\cos 2x$, still reflection-symmetric) lifts the degeneracy and restores
  the linear law. Robust invariant: the **threshold** ($c_1=0$ iff symmetric); the onset power is
  parity-dependent, not itself protected. Scope: synthetic = calibration on the real system's measured
  structure (the Re/Im split), **not** a data measurement — real-data vindication is the owed experiment
  (sweep a ring potential through exact reflection symmetry; watch $c_1$ cross zero linearly; software-
  only on the SLM/EOM rig). Falsify: a reflection-symmetric driven ring whose relaxation linear-response
  to the current is nonzero. `experiments/colloid_ring_transverse.py`. `pa:transverse-decomposition`.
* **KaiABC circadian clock** `empirical` [Circulation-held capacity]. The first **capacity-curve anchor** for
  the decomposition *Organization = circulation-held $K(C)$ + archive-held*, with
  $K(C)=K_{\text{topo}}(=b_1)+K_{\text{metric}}$. In-vitro KaiA+KaiB+KaiC+ATP (no DNA / no transcription) read as
  the reduced phosphoform Markov ring U->T->ST->S->U (Rust, Markson, Lenz, Glass, O'Shea, *Science* 318:809,
  2007; reduced model = SOM Eqs. 1-5, Tables S1/S2, read directly from the fetched SOM; rates
  $k_{XY}(S)=k^0_{XY}+k^A_{XY}\,A/(K_{1/2}+A)$, active KaiA $A=\max(0,[\text{KaiA}]-2S)$, $K_{1/2}=0.43\,\mu$M,
  $[\text{KaiA}]=1.3$, $[\text{KaiC}]=3.4\,\mu$M; self-consistent against Table S1's +KaiA column to the digit).
  **Kill #1 (is $K$ philosophy?) -- SURVIVES (structural):** the parameter/state cut is the published model's
  *own* factorization -- the intrinsic constants $k^0,k^A$ (protein structure) are **archive**, the mean-field
  modulation through $A$, a functional of the collective $S$ coordinate, is **circulation** -- so it holds under
  KaiC cooperativity (the coupling is mean-field / scramble-invariant; the cut blurs only in the full
  per-hexamer allosteric ensemble, which is also the memory-bound compute trap). **Kill #2 (is $K=b_1$?) --
  VINDICATED, forced-not-fitted** (`experiments/kaiabc_capacity.py`): the measured constants give a sustained
  limit cycle (period $\approx20.7$ h, amplitude $1.36\,\mu$M); a genuine **forward** cyclic current
  $J_{\text{cyc}}=+0.025\,\mu$M/h equal across all four ring edges (Kirchhoff, single loop) that **collapses to
  0** when the drive is cut ($[\text{KaiA}]=0\Rightarrow$ all KaiC -> U); the winding sign is **structure-locked**
  (0 flips in 26 oscillating rate-deformations); $b_1=1$ ($E-V+1$ of the ring); and the monodromy/Floquet
  multipliers $[1.000,\,0.046,\,6.6\times10^{-5}]$ show **exactly one marginal direction (the phase)** beyond the
  fixed point, so $K_{\text{metric}}=1$. Hence $K(\text{KaiABC})=1+1=2>b_1=1$ -- $K$ is a real observable, not the
  topological count relabeled. **The discriminating finding:** the protected current is **not** a frozen-rate
  bias -- the frozen-operator cycle affinity is *negative* at high KaiA and flips sign with $S$
  ($\operatorname{sign}\mathcal{A}=\operatorname{sign}$ the directly-solved frozen NESS current at every $S$ --
  operator calibration), yet the limit cycle runs forward; the circulation is dynamically generated by the
  collective KaiA-sequestration feedback, living in the collective configuration (cf. the noise-activated
  hopping of `battery:chiral-rotor-triad`). **Scope:** one anchor point; the capacity curve and the
  substrate-generality of the cut are owed (point 2 = a second same-modality oscillator). `pa:ness-currents`,
  `pa:cycle-affinity`.
* **Peroxidase-oxidase reaction** `empirical` [Circulation-held capacity -- point 2]. The capacity curve's
  second anchor and its first **distinct** point ($K\ne2$). Horseradish-peroxidase oxidation of NADH by O2 in
  an open reactor -- a purely chemical, enzyme-catalyzed NESS oscillator, **record-free in the loop** (no DNA /
  transcription; the enzyme turns over but is not synthesized), driven by continuous NADH+O2 feed. Built from
  the BFSO detailed model (Bronnikova, Schaffer, Olsen, *J. Chem. Phys.* 105, 10849 (1996); 10 ODEs, 13
  elementary steps; Tables I/II/III read directly from the fetched PDF; literature constants $k_1$-$k_{13}$,
  $[O_2]_{eq}$ and $[\text{NADH}]_{stock}$ matched to Geest et al.). `experiments/bfso_capacity.py`.
  **$K(\text{PO})=b_1+K_{\text{metric}}=3+1=4>2$**, forced-not-fitted: the measured constants give a sustained
  relaxation oscillation (period $\approx$190 s), the 5 enzyme states are conserved to $10^{-14}$ (validating
  the reconstructed stoichiometry), and the circulation collapses to a fixed point when the NADH/O2 feed is
  cut. **The distinct point is STRUCTURAL:** the peroxidase cycles through 5 oxidation states
  {Per3+, CoI, CoII, CoIII, Per2+} as **two coupled feedback loops** -- the enzyme-state transition graph
  (7 directed edges, 5 nodes) has cycle rank $b_1=E-V+1=3$ (vs KaiABC's single ring, $b_1=1$), reset-stable
  and rate-independent; all 3 independent enzyme-cycle currents are realized nonzero (edge-flux decomposition:
  the Per3+->CoI->CoII loop, the CoIII loop, the Per2+ loop). So $K$ genuinely varies across substrates -- not
  pinned at 2. **Two honest limits.** (1) The literature's *primary-quasiperiodicity* 2-torus (which would give
  $K_{\text{metric}}=2\Rightarrow K=5$) is **not reproduced** here: at the documented $[O_2]_{eq}\approx17.16$
  uM window the model gives a different limit cycle (single fundamental + harmonics), not a torus; reaching it
  would require nudging the *uncertain* $k_8/k_9$ -- i.e. fitting -- so the torus is **not claimed**
  (`project_killshot_synthetic_is_imported_math`). (2) BFSO's steps are written irreversibly, so $K_{\text{topo}}$
  is the protected cycle **count** (the number of independent circulations the NESS carries), each loop's
  direction drive-locked -- a generalization of KaiABC's reversible-cycle affinity sign-bit, not the identical
  object (the open $K_{\text{topo}}$-uniformity item). `pa:ness-currents`, `pa:cycle-affinity`.
* **QEC keep-as-capacity anchor** `derived` [The wall, and the deepest keep]. The §wall claim -- maintenance
  through complete part-turnover *is* error correction, the deepest keep is **topological** ($K_{\text{topo}}=b_1$),
  and a record is forced past the code's capacity -- anchored on the surface/toric code already in canon
  (§QEC transverse decomposition), where every step is an exact code property or an established QEC theorem
  rather than the keep-derivation's one heuristic (the $O(N\log N)$ wiring re-specification;
  `docs/research_prompt_keep_derivation.md`, 3/3 outside models agree, that step flagged). The dictionary is
  literal: physical qubits continuously decohere $=$ parts turn over; the running stabilizer cycle $=$ the
  self-correcting dynamics; $k$ logical qubits $=$ the keep. `experiments/qec_keep_capacity.py`.
  **(1) keep $=b_1=k$, LITERAL.** The number of logical qubits a topological code protects through continuous
  physical-qubit turnover *is* the first Betti number of the code surface: $k=2-\chi$, computed two independent
  ways and shown equal -- $k$ by GF(2) stabilizer rank, $b_1=2-\chi$ by Euler count of the cellulation. Toric
  (closed torus, $\chi=V-E+F=0$): $k=2=b_1$, verified $L=2,3,4$. Planar $[[9,1,3]]$ (disk, relative homology):
  $k=1=b_1$. So the canon's "$b_1$ = topological capacity" (§Two bits) is **not an analogy** -- on a real code
  the protected count *is* the homology, and the keep-derivation's $K_{\text{topo}}=b_1$ term is literal.
  **(2) the distance-vs-keep SPLIT** (the §wall's crystal escape, made exact). Grow the toric lattice $L$: the
  keep $k=b_1=2$ stays **fixed** while the distance $d=L$ **grows** ($d$ exact by min-weight-logical enumeration
  for $L\le3$, $=L$ structurally above). A regular (translationally uniform) code spends extra resource on
  **protection depth** (the metric register), never on **keep** (the topological count); the keep grows only
  with added topology (handles/holes), whose heterogeneous arrangement is exactly the **archived** part. This is
  the §wall's two regimes, exact: crystal $\to$ holds repetition (depth), needs no record; heterogeneous topology
  $\to$ grows keep, forces the record. **(3) the wall $=$ channel capacity, RIGOROUS.** The keep *rate* $k/n$ a
  code holds through turnover obeys the hashing bound $k/n\le 1-H_2(p)$ (Shannon coding theorem), and the error
  **threshold** $p_{\text{th}}\approx0.109$ (Dennis-Kitaev-Landau-Preskill 2002; the random-bond Ising Nishimori
  point) is the maintenance wall: below it the keep is held through *unbounded* turnover (logical error $\to0$ as
  $n$ grows at fixed rate), above it it collapses to 0. The metric/distance register returns only
  **sub-extensively** -- at fixed $k$, extra qubits buy $d\sim\sqrt n$ and logical error $\sim e^{-cd}$, so
  protection deepens but the bit count does not (topological register free/non-decaying below threshold; metric
  register a logarithm -- exactly the derivation's split). **Scope (honest):** an *existence proof + mechanism
  anchor*, not a closure of the wiring-cost item -- it makes $K_{\text{topo}}=b_1$ and the wall's logic exact on
  a real in-canon substrate, but the general biological $O(N\log N)$ step (a *heterogeneous* network vs. QEC's
  *regular* lattice) remains the owed tightening. Falsify: a topological code whose logical-qubit count is not
  its first Betti number; a regular code whose keep (logical count) grows with size at fixed topology; or a
  maintenance-through-turnover channel with unbounded keep at fixed capacity. `pa:topological-memory`,
  `pa:channel-capacity`, `pa:transverse-decomposition`.

* **JCVI-Syn3A archive-term cut** `empirical` [The keep -- the archive-held term, first measurement]. The
  first substrate with archive $\gg 0$ **and** a buildable circulation, so the second term of
  *Organization $=$ circulation-held $K(C)$ $+$ archive-held* can be measured rather than assumed $\approx 0$
  (as it is in the record-free anchors KaiABC/PO). Substrate: the minimal synthetic bacterium JCVI-Syn3A
  (genome CP016816.2, 543,379 bp / 496 genes; metabolism + measured enzyme kinetics + per-gene essentiality
  from Breuer et al. 2019, *eLife* 8:e36842). `experiments/syn3a_archive_term.py`, all data via the verified
  loader `experiments/syn3a_data.py`. **The cut, operationalized.** Archive $\to$ the **essential** genes (the
  irreducible store the circulation cannot route around), $E$; circulation $\to$ the metabolic NESS's gene set,
  $M$. Headline metric $\text{blur}=|E\setminus M|/|E|$ -- a set difference between two *given* datasets
  ($E$ from the essentiality column, $M$ from the kinetics enzyme IDs $P_{xxxx}\!=$ locus
  $\text{JCVISYN3A}\_{xxxx}$ and/or the "Metabolism" annotation), so the framework chooses neither set.
  $\text{blur}\!\approx\!0$ would mean the cut is **well-posed** (the genome is the circulation's parameter
  store); $\text{blur}\!\approx\!1$ means it **blurs** (the irreducible archive is *not* the metabolic
  circulation). **Result: the cut BLURS, robustly.** Reading $M$ at three resolutions -- the built operator
  (95 genes with measured rates), all annotated metabolism (167), metabolism $+$ cellular processes (174,
  most generous) -- the blur runs $0.77\to0.62\to0.61$ ($E=$ essential$+$quasi) and stays a majority even
  most-generously vs essential-only ($0.57$). The metabolic circulation accounts for under half of the
  irreducible archive at every resolution. **Where the blur lives (located, not diffuse):** of the 294
  unaccounted essential$+$quasi genes, the single largest block ($169$, $57\%$) is **Genetic Information
  Processing** -- the transcription/translation/replication apparatus, i.e. the machinery that *reads* the
  archive; the rest is residual metabolism ($63$, lacking kinetics) and "Unclear/generic-essential" ($59$).
  By coding bits the irreducible archive ($8.30\times10^5$ bits) splits $\approx 44\%$ circulation / $41\%$
  **reader** / $14\%$ unclear. **Reading.** The reader is stored (essential, irreducible) yet is itself an
  active maintained process -- neither cleanly term-1 (it is not the metabolic NESS the SBML/kinetics models)
  nor term-2 (it is not passive storage). It is the **self-referential seam**: the archive read by machinery
  the archive specifies. So *Organization $=$ circulation $+$ archive* as a clean **sum** is disfavored at high
  archive -- the two terms **overlap irreducibly at the reader**. **Honest scope (the skeptic).** The framework
  did **not** discover the biology -- that a minimal genome is dominated by expression machinery is a known
  minimal-cell fact (Breuer 2019 states it). What is the framework's is the *prediction of the shape*: the
  self-referential-closure / `reading-transition` threads predicted, before this substrate, that on a
  high-archive substrate the two-term decomposition would fail by an irreducible cross-term that is *both*
  stored and active -- and Syn3A confirms that shape and **locates** it (the reader) and **numbers** it (the
  first archive-term measurement). This is a **sharpening of the object** (the keep needs a third, cross term;
  the "alive loop" north-star is exactly this seam), not a tidy $\uparrow$ -- the make-or-break "is the archive
  term cleanly separable?" came out **no**. **The falsifier that did not trigger:** $\text{blur}$ could have
  been $\approx 0$ (a purely metabolic autocatalytic substrate with no template would give it -- the KaiABC/PO
  regime); it is $\approx0.6$-$0.77$. **Falsify the reading:** a high-archive substrate whose essential archive
  *is* its maintained circulation ($\text{blur}\to0$), or a demonstration that the reader's gene set is fully
  inside the metabolic NESS's flux modes. **Deferral audit (2026-06-25; three independent models, convergent --
  the prior-art credit, in full).** The *concepts* this result touches are owned, by name, by real researchers,
  and the framework imports them: the **archive-held term** (information that must be consulted because the
  dynamics cannot regenerate it) is **Kolchinsky--Wolpert's stored semantic information** (2018); the **reader
  that produces the reader** is **Rosen's closure to efficient causation** / (M,R) systems ($\beta=B$ -- exactly
  core's $\otimes$-fixed-point); the **seam** (symbol becoming dynamics at the expression apparatus) is
  **Pattee's semantic closure / epistemic cut** (the sharpest antecedent); the archive/reader **dual-use** is
  **von Neumann's** tape; the **non-separability** of metabolism and template is **Gánti's chemoton**; and the
  **gene-category split itself** ($\approx$143 metabolic vs $\approx$212 information-processing) is **Breuer
  2019 / Hutchison 2016** -- the number is theirs, not ours. So the *reading* is import-redescription, and the
  framework claims none of the concepts. **The residue, at its true (small) size:** all three models
  independently isolate the same unclaimed piece -- the **quantitative operationalization**: the first
  computation partitioning a real minimal cell's irreducible archive against its metabolic circulation as a set
  difference, the seam *located* (the expression apparatus, $\approx41\%$ of archive bits) and the circulation
  anchored topologically ($K_{\text{topo}}=b_1+K_{\text{metric}}$). That is a **measurement on top of
  fully-credited concepts** -- the framework's settled constraint-language value, instanced; we put a number
  where Pattee/Rosen/Kolchinsky--Wolpert put a concept. Kept, not erased; not inflated.
  `pa:semantic-information`, `pa:rosen-mr-systems`, `pa:pattee-semantic-closure`, `pa:chemoton`,
  `pa:von-neumann-automata`, `pa:channel-capacity`, `pa:transverse-decomposition`.
* **JCVI-Syn3A reader-upkeep -- the energy axis of the seam** `empirical` [frontier `reader-by-overreach`:
  disconfirmer #3, the upkeep side]. Companion to the archive-term cut: that measured the reader on the **bit**
  axis (stored information, $\approx41\%$ of the irreducible archive); this measures it on the **energy/upkeep**
  axis (the running maintenance budget). `experiments/syn3a_reader_upkeep.py`, same loader/data. **The measure**
  (forced, no boundary chosen): reader-upkeep share $=\sum_{\text{GIP}}(\text{copies}\times\text{aa})/
  \sum_{\text{all}}(\text{copies}\times\text{aa})$ -- the reader's (Genetic Information Processing) share of the
  proteome-synthesis budget, from the 4DWCM per-protein copy numbers $\times$ genome CDS lengths; reported beside
  gene count, archive bits, and standing copies so the trend across weightings shows. **Result: reader-upkeep
  $\approx46\%$, co-equal with the metabolic circulation ($43\%$) -- not dominant.** The reader leads on raw
  protein **copies** ($50\%$, half of all molecules) but the lead erodes under length-weighting (r-proteins are
  short, high-copy); the reader/circulation ratio **crosses 1** across axes -- storage favors the circulation
  (bits $0.90$), upkeep favors the reader (copies $1.27$, budget $1.07$). **Cross-check:** on the essential$+$quasi
  subset reader-bits $=40.9\%\approx$ the archive-term's $41\%$ -- the two scripts agree, and the energy axis sits
  beside the bit axis consistently. **The witness (disconfirmer #3).** The audit's sharpest disconfirmer is "the
  crossover dies once the reader's own upkeep is included." On real parameters it does **not**: the cell spends
  $\approx$half its proteome maintenance on the reader **and still reads** (the reader is selected), so
  $\text{re-mint}\ge\text{read}+\text{upkeep}$ -- a large reader-upkeep **witnesses a steep maintenance wall**, not
  a dead crossover. **Honest scope.** This measures the **upkeep side only**; the re-mint counterfactual (the
  $\sim N\log N$ wall) the cell never runs and remains owed (capacity item 5a), so it constrains but does not
  decide the crossover. On the running energy budget the reader and circulation are **co-equal, not
  reader-dominated** -- a deflation of the bit-axis "reader dominates"; dominance returns only once the ribosome's
  rRNA is counted (the standard largest synthesis sink, excluded here -- so $46\%$ is a lower bound). A snapshot
  with $\sim$uniform turnover (upkeep $\sim$ standing amount). **Falsify:** reader-upkeep a *small* fraction (a
  cheap reader -- crossover trivially robust, the seam bit-only), or a high-archive substrate whose reader-upkeep
  dwarfs its re-mint cost. Imports unchanged (crossover $=$ Still/England/Kolchinsky--Wolpert; the wall owed); see
  `docs/research/research_prompt_reader_by_overreach.md`.
* **Archive form: rate-independent symbol; the digital/aperiodic limb deliberately omitted** `derived` [The keep
  and the archive]. Core adds one clause -- the archive is **rate-independent** (a symbol stable against the rates
  it specifies, not swept along by them), crediting **Pattee** (`pa:pattee-semantic-closure`). The *further* claim
  that the archive must be **digital and aperiodic** is **kept out of core**: the reader-by-overreach deferral
  audit (`docs/research/research_prompt_reader_by_overreach.md`, 3 models converge, Q4) finds error-correctable
  discrete encoding is a **bounded selective pressure** as information load grows (**Eigen's error threshold**;
  **von Neumann** reliable computation) -- *not* a necessity -- while the specific aperiodic-polymer form is an
  **n=1 frozen accident** (**Crick**; **Gould** contingency, undecidable at n=1). The modal force is a gradient,
  not a law (`feedback_n1_frozen_accident_not_forced`); only the near-tautological rate-independence crosses.
  `pa:pattee-semantic-closure`.

---

## Falsifier formalizations

Each is a predicted measurement on a named substrate/class; the inline kill conditions above are the same
in context.

* **Surface-code**: unit slope sub-threshold (no aging), or shape unchanged across threshold (no migration).
* **Topological bit**: protected sign requires a per-time maintenance cost scaling with held duration
  (a population bit in disguise), or the sign changes under a continuous deformation without rewiring.
* **Central commitment**: a real substrate sustaining protected circulation with no triad; or a drive sweep
  producing a sign flip. Three fatal nulls: balanced network / 2-component bistable / detailed balance.
* **Capacity**: a soft substrate that snaps, or a hard-wall substrate with soft tails.
* **Open-interval discipline**: any observable attaining exactly $0$ or $1$ at a finite, non-degenerate
  operating point.
* **Precision tightness**: nominally same-class substrates with arbitrary $\mathcal{T}$.
* **Dual ledger**: $I_{\text{pred}}$ scaling departs from its thermodynamic dual.
* **SOC**: a timescale-separated substrate with robust $\tau\ne3/2$; or branching $\ne1$ at the marginal
  point.
* **Heavy-traffic transport**: a substrate's FDR-aging and queue-tail exponents fail to collapse onto a
  common $\beta$ through $g$.
* **Marginal closure-loss**: a substrate at $\varepsilon\to1$ whose reduced description persists (CLV
  minimum angle bounded from 0); or past-marginal chaos requiring $N\ge3$ and absent at $N{=}1$ with the
  delay mechanism present.
* **Memory exponent**: $\beta$ near the marginal point departs from $\approx1-\varepsilon$.
* **Synchronization (chimera)**: only uniform sync/incoherence accessible.
* **Dissipative structures (Turing)**: three-condition failure.
* **Control**: habit-extinction not Caputo $\beta<1$; or auto-tuning $W$ off the inverse-$\gamma_{s,i}$ form.
* **Active matter (MIPS)**: high-Péclet clustering at $\gamma_{AB}\ge0$ without the swim-pressure signature.
* **Two-frame construction**: verdict-disagreement where both frames are computable; the iff-chain break
  (both frames agree, no triad); or definedness-asymmetry collapse (no topological signal in frame existence).

---

## Corrections and promoted refinements

The supersession record — each retains the superseded form, the corrected form, and the evidence.

* **Measurement-discipline audit — two frozen constants** `corrected`. Test: every dynamical quantity
  must flow with the operating point. (1) $\gamma_{RO}$ was frozen at $\gamma_s/2$; the flowing form
  $\gamma_{RO}=(\gamma_s/2)e^{a}$ carries the pump ratio (consequence: $Q$ non-monotonic, peak at $a=1$
  bit). (2) Drive-independence belongs to the affinity $\mathcal{A}$, not the current magnitude $J_{ss}$
  ($J_{ss}$ flows with $a$ — legal); corrected falsifier wording: "$J$ becomes drive-noise-dependent or
  resolves to detailed balance," not "drive-dependent."
* **Transport law (was a three-way identity)** `corrected`. Superseded: the boxed
  $\alpha_s=\beta=$ heavy-traffic exponent as a literal equality. The three legs are *different functions*
  of one $\beta$, coincident only at $\beta=1$; the literal identity auto-falsifies across the
  non-Markovian class. Corrected: one $\beta$ governs three registers through fixed maps; predictive
  content is the transport, falsified by failure to collapse onto a common $\beta$.
* **Topological-drain invariant** `proven` (refined). Superseded: "the invariant is the complex spectrum
  (irreducible rotation)." Corrected: the invariant is the broken-detailed-balance affinity $\mathcal{A}$
  (the non-gradient part of the drift); the complex pair is its underdamped *signature*, suppressible to a
  real overdamped circulation that is still a genuine protected current. The discriminator is
  gradient ($\mathcal{A}=0$) vs non-gradient ($\mathcal{A}\ne0$), not real-vs-complex spectrum.
* **Marginal point — chaos mechanism** `corrected`. Superseded: "$N\ge3$ ascents complete a 3-torus
  $\Rightarrow$ forced chaos." Corrected: the marginal point is loss of normal hyperbolicity (necessary,
  not sufficient); post-marginal chaos is delay-driven (chaotic at $N{=}1$), the 3-torus robust under weak
  coupling. Failure mode: a generic/∃ topological result bound as forced/∀ — the same boundary-overclaim
  pattern as the tombstoned starts. Antidote: the faithful-binding rule (an ∃ result is not bound as ∀;
  boundary behaviour entailed from the interior).
* **Two bits / topological-Landauer** `corrected`. Superseded: "$\ge1$ bit per protected sign to modify"
  + a forced-erasure floor $=b_1$ as a cost. Corrected: a sign flip is a reversible bijection (no erasure,
  no Landauer floor); the $\ge1$ bit was definable only by routing the flip through the never-attained
  $\mathcal{A}=0$ boundary (a $0/0$); $b_1$ is the count of gauge-irremovable signs (capacity), not a
  per-flip cost. Same error family as the chaos-mechanism correction.
* **The binding — discharged by import**. The last floating node of the manifold lift closes by composing
  standing imports + one new one (`pa:reversible-spectrum`), not a bespoke theorem; corrects an outside
  three-way-iff overstatement to a 2-way carrier + 1-way spectral signature.
* **Local geometry's coupling role, bounded** `composed`. Not a new theorem — three standing results
  compose: the transverse-decomposition theorem ($\mathcal{A}$ barred from $\Delta V$, reaching only the
  irreversible Eyring–Kramers prefactor — §Branch-survival barrier, the `current-aids-escape` tombstone),
  the EP-onset-vs-affinity separation (§Topological-drain invariant; `pa:reversible-spectrum`), and the
  cross-rule's surviving $O(\mathcal{A}^2)$ channel (§Colloid ring transverse). They bound to one statement:
  **local geometry — saddle Hessian (prefactor), spectral-sheet curvature (EP onset), or the leading
  symmetry-allowed $O(\mathcal{A}^2)$ coefficient — modulates coupling strength (branch occupancy, transition
  rates) but does not generate the protected circulation** (existence = global frustrated topology, protection
  = cycle affinity). The verb is *modulates*, not *governs*: the rate is barrier-dominated
  ($k\sim A\,e^{-\Delta V/\varepsilon}$) and local curvature reaches only the prefactor $A$, so "governs"
  would re-attribute the rate to local geometry and undo the transverse theorem. **Resolved — clean negative**
  (2026-06-21; retired frontier `curvature-as-coupling-bias`). Three independent outbound derivations converge:
  the surviving $O(\mathcal{A}^2)$ coefficient $\kappa = \tfrac12 \partial_{\mathcal{A}}^2 O|_0$ is the
  **leading analytic response coefficient, not a universal geometric curvature**. Model-independent
  obstructions: (i) $\kappa$ is *observable-dependent* — two observables on one process give different
  $\kappa$, a curvature scalar would not; (ii) the FW quasipotential is $\mathcal{A}$-invariant (the transverse
  theorem), so every curvature built from it is $\mathcal{A}$-invariant while $\kappa \ne 0$ — hence
  $\kappa \ne \mathrm{curv}(W)$, the strongest single obstruction; (iii) each named candidate fails
  structurally — Berry/pumping curvature needs a *cyclic loop* in $\ge 2$ parameters (here one static
  $\mathcal{A}$, vanishing at a point), no exceptional point exists at $\mathcal{A}=0$ (the generator is
  analytic there), $\mathcal{A}=0$ is a regular point not a bifurcation (no unfolding), and the thermodynamic
  (Sivak–Crooks/Ruppeiner) object is a *metric component* $g_{\mathcal{A}\mathcal{A}}$, not its curvature $R$,
  and governs slow-driving dissipation not static response. Closed form (forced, not fitted):
  $\kappa \propto \mathrm{Tr}(H^{-1}LH^{-1}L)$ = the Rayleigh–Schrödinger resolvent sum
  $\sum_{j\ne+}\langle\psi_+^L|\Omega|\psi_j^R\rangle\langle\psi_j^L|\Omega|\psi_+^R\rangle/(\mu_+-\mu_j)$,
  i.e. the equilibrium covariance $\kappa = (1/2D^2)\,\mathrm{Cov}_{\mathrm{eq}}[O,(x-\langle x\rangle)^2]$ on
  the driven ring (Bouchet–Reygner irreversible-EK prefactor; Sivak–Crooks; Sinitsyn–Nemenman). The negative
  **drops "curvature"** and *reinforces* the transverse theorem — the $\mathcal{A}$-invariance of $\Delta V$ is
  exactly what bars the strongest geometric candidate. The state-space-vs-parameter-space caveat held (all
  three kept them distinct; $\kappa$ is a cross-derivative living cleanly in neither as a curvature). Returns:
  `docs/research_prompt_curvature_as_coupling_bias.md`. Crossed to `character.md` §Motion and proximity
  ("Local geometry, bounded").
* **Promotions** `promoted`. The central commitment and two-frame construction crossed to the core on the
  rock-paper-scissors instance; the deformation chart and homochirality on rock-paper-scissors and the
  homochiral triad respectively; composite branch on the DNA reaction network. Each records a real
  instance (synthetic passes are calibration, never vindication), a goalpost that shrinks the falsifiable
  surface, and the doc that absorbed it.

---

## Prior-art map

Each receipt resolves to its `pa:` keys in [`character_prior_art.md`](character_prior_art.md); receipts not
listed import nothing (owned reading). The keys are collected inline per entry above. Generic-toolkit
grounding (overdamped-Langevin response, the adiabatic theorem) is untracked by design.
