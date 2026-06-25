# Outbound-research prompt — substrate for the β-collapse 3rd register

Landscape question for the outbound channel: locate / validate the best substrate for a genuinely
independent **FDR-aging** third register of the memory-exponent collapse. Pairs with
`beta_collapse_3rd_register_design.md` (my candidate is the confined fractional process; this asks the
channel to validate/improve/replace it and to pin the identities). Returned report files alongside and
feeds the de-risking probe. No framework jargon — answerable by a stochastic-processes / glass-physics model.

---

## Locating a substrate for a three-way memory-exponent collapse — with a genuinely independent aging/FDR register

I want to over-determine a single **memory exponent** `β` by measuring it three *independent* ways on one
stochastic model (or one model family at fixed memory), and checking they collapse onto a common value.
Two ways are settled; I need a third that is genuinely independent, and I want help picking the cleanest
substrate.

**Setup.** Fractional Gaussian noise of Hurst exponent `H ∈ (1/2, 1)` has autocovariance `γ(k) ~ k^(2H−2)`.
Define the memory exponent `β = 2 − 2H ∈ (0,1)`. The same `β` already appears two independent ways:

- **(R1) Two-point correlation.** `β_mem` from the log-log slope of `γ(k) ~ k^(−β)`.
- **(R2) Extreme-value / supremum functional.** Feed the fGn as arrivals into a constant-drain server; the
  stationary backlog `Q` (Loynes) has, by Norros (1994), `P(Q > x) ~ exp(−η x^(2−2H))` — a Weibull tail
  whose stretch exponent is `2−2H = β`. The equality of R1's and R2's exponents is a *theorem*, not a
  definition — distinct functionals, same `β`.

**The gap.** The natural third route is an **aging / fluctuation–dissipation-ratio (FDR) exponent** `α_s`,
with the expected identity `α_s = β_mem = β`. But for *free* fractional Brownian motion the two-time linear
response `R(t,t_w)` is a trivial integral of the memory kernel, so any "aging exponent" extracted from `R`
is *definitionally* the correlation exponent — R3 collapses onto R1, no independent content. I need a
substrate where the response is **non-trivial**, so `α_s` is an independent estimate of `β`.

**My candidate (please validate / improve / replace):** a **harmonically-confined fractional process**
(confined fGn-driven OU, or the fractional Langevin equation), same `H` → same `β = 2−2H`. The confinement
adds a relaxation timescale competing with the memory, which should make the two-time response non-trivial
and the aging FDR `α_s` independent of the correlation exponent.

**Questions:**

1. For a harmonically-confined fractional process / fractional Langevin equation, is the **aging-regime FDR
   exponent `α_s` known**, and does it equal `2−2H` (or relate to `H` by a clean, citable identity)? I
   expect a trade-off: confinement is needed for a non-trivial response, but strong confinement equilibrates
   too fast to leave an aging window. **In what `(confinement strength k, waiting time t_w)` regime is the
   aging-FDR cleanly resolvable**, and is `α_s` constant there?
2. What is the cleanest **field-free linear-response estimator** for such (Gaussian, memory-driven)
   processes — Cugliandolo–Kurchan, Malliavin-weight, Lippiello–Corberi–Zannetti, etc. — given that a
   direct-perturbation `R` is noisy?
3. **Is there a better substrate?** I want three *genuinely independent* operations — a two-point
   correlation, an extreme-value/supremum functional (like the queue tail), and an aging-FDR response — all
   yielding the **same** memory exponent by *distinct* theorems. Candidates I'm weighing: confined
   fractional Langevin/GLE; a fractional-OU; a continuous-time random walk (CTRW); a trap model; a
   kinetically-constrained model (East / Fredrickson–Andersen). Which gives the cleanest, most-pinned
   `β`-identity across all three operations?
4. For the **East (or FA) kinetically-constrained model** specifically: do its (i) two-time aging exponent,
   (ii) stretched-exponential `C(τ) ~ exp(−(τ/τ_α)^β_K)` exponent, and (iii) persistence-time tail exponent
   map onto a *single* common memory exponent by known relations? Its memory is the hierarchical kinetic
   constraint rather than fGn, so I'm unsure there's a clean `β = 2−2H`-type identity to collapse onto — is
   there?
5. Literature anchors for: aging and FDR in fractional Langevin / GLE systems; field-free response
   estimators; KCM aging-vs-persistence-vs-relaxation exponent relations; and any worked case where
   correlation, extreme-value, and FDR exponents are shown equal by independent derivations.

-----
model a:
This is a strong prompt already. After looking through the aging/FLE literature, I think the key issue is not "can I find a confined fractional process with aging?"—that part is easy—but rather:

> **Can I find a third register whose exponent is derived from a genuinely different theorem than the correlation exponent?**

That distinction matters because several candidate substrates exhibit aging while still having the response kernel algebraically tied to the same memory kernel that generated R1.

## Executive summary

My reading is:

1. **Confined fGn / fractional OU is probably not the best R3 substrate.**

   * It gives transient aging under confinement.
   * It gives nontrivial response functions.
   * But the response and correlation remain tightly linked through the Gaussian linear structure and generalized FDT machinery. The danger is that your "independent" exponent is ultimately another face of the same kernel. ([PubMed][1])

2. **Fractional Langevin Equation (FLE/GLE) is better than fractional OU.**

   * The memory kernel enters dynamically through friction.
   * Aging and confinement regimes are analytically tractable.
   * There are explicit aging calculations in free and confined cases. ([PubMed][1])

3. **CTRW/trap-model aging gives the cleanest independent aging exponent.**

   * Correlations, persistence, and response arise from renewal statistics rather than Gaussian covariance.
   * Aging exponents and FDR violations are genuinely nontrivial.
   * The downside is that your existing R2 (Norros queue theorem) is fGn-based, so you lose the beautiful common substrate.

4. **East/FA KCMs are probably the weakest candidate for a three-register collapse.**

   * They possess aging, persistence, stretched relaxation, and FDR violations.
   * But there is no known universal identity of the form

   [
   \beta_{\rm aging}
   =================

   # \beta_{\rm corr}

   \beta_{\rm persistence}.
   ]

   The exponents arise from hierarchical facilitation and broad time-scale distributions, not from a single parameter analogous to (H).

---

# Q1. Is an aging/FDR exponent known for confined FLE?

The literature definitely establishes:

* aging in free FLE,
* aging in confined FLE,
* different aging laws in the two cases,
* algebraic relaxation controlled by the fractional memory kernel. ([PubMed][1])

However, I do **not** find evidence that there is a standard, universally cited exponent

[
\alpha_s = 2-2H
]

playing the role you want.

Instead, what appears in the FLE literature are:

* aging corrections to moments,
* waiting-time dependence,
* algebraic relaxation exponents,
* FDR-violation functions.

The dependence is certainly controlled by the same fractional order, but not typically packaged as a standalone theorem:

[
\alpha_s = 2-2H .
]

That identity would need to be derived rather than cited.

So if your goal is a referee-proof "three independent theorems imply the same β," I would currently classify the FLE route as:

| Register       | Status                        |
| -------------- | ----------------------------- |
| R1 correlation | theorem                       |
| R2 queue tail  | theorem                       |
| R3 aging/FDR   | plausible, but not yet pinned |

---

# Q2. What regime resolves aging best?

The confinement tradeoff you identified is real.

Very roughly:

### Too weak confinement

[
k \to 0
]

You recover free fBm/FLE behavior.

Response becomes increasingly kernel-dominated.

Independence from R1 weakens.

### Too strong confinement

[
t_w \gg k^{-1}
]

System approaches stationary confined state.

Aging disappears.

FDR tends toward equilibrium form.

### Sweet spot

You want

[
t_w
\sim
\tau_k
]

where

[
\tau_k
]

is the confinement relaxation scale.

Then:

* confinement is dynamically relevant,
* stationarity has not yet been reached,
* aging corrections remain measurable.

That is exactly the transient-aging window discussed by Kursawe–Schulz–Metzler. ([PubMed][1])

---

# Q3. Field-free response estimators

For numerical work, I would strongly favor the modern fluctuation-response identities over explicit perturb-and-average.

The usual hierarchy is:

### Lippiello–Corberi–Zannetti (LCZ)

Excellent when:

* Markovian dynamics available,
* response can be rewritten as an unperturbed correlation.

Widely used in aging systems.

### Malliavin-weight methods

Especially attractive for:

* Langevin dynamics,
* continuous stochastic systems,
* noisy response measurements.

Often dramatically lower variance than direct perturbation.

### Direct Cugliandolo–Kurchan FDR

Conceptually clean.

Usually noisier numerically.

If your eventual goal is a precision exponent estimate rather than a conceptual demonstration, I would expect a Malliavin-style estimator to dominate.

---

# Q4. East / FA models

This is where I would be cautious.

The East model exhibits:

* stretched relaxation,
* persistence decay,
* aging,
* FDR violations.

But those exponents generally emerge from:

* hierarchical facilitation,
* defect concentration,
* temperature-dependent scale separation.

There is no analogue of

[
H \longrightarrow \beta
]

that simultaneously governs all observables.

In particular:

[
C(t)
\sim
\exp!\left[-(t/\tau)^{\beta_K}\right]
]

does **not** imply that persistence tails or aging exponents share the same (\beta_K).

The literature tends to treat these as related but distinct scaling quantities.

So for your collapse criterion:

| Model           | Single master exponent? |
| --------------- | ----------------------- |
| fGn/FBM         | yes                     |
| Norros queue    | yes                     |
| FLE aging       | maybe                   |
| CTRW trap model | yes-ish                 |
| East model      | generally no            |

---

# My assessment of the substrate search

The most important thing I noticed in your prompt is that you are asking for:

> three independent operations yielding the same exponent.

The strongest candidate may actually be:

### Same memory source (fGn/FLE)

R1:
[
\gamma(k)\sim k^{-\beta}
]

R2:
Norros queue theorem

[
\Pr(Q>x)
\sim
e^{-\eta x^\beta}
]

R3:
derive an aging/FDR exponent from the **fractional friction kernel**

rather than from the covariance directly.

If that derivation can be made rigorous, you get exactly what you want:

* covariance theorem,
* supremum large-deviation theorem,
* response/aging theorem,

all on one substrate.

The current weakness is that I know of explicit theorem-level results for the first two, whereas for the third I find aging and FDR analyses but not yet a canonical theorem stating

[
\alpha_s = \beta = 2-2H.
]

([PubMed][1])

If I were de-risking this program, the next outbound search I'd run would be much narrower:

> "Find a published derivation connecting the aging/FDR scaling exponent of a confined FLE/GLE directly to the fractional friction order (\alpha=2-2H), and determine whether that exponent is identical to the long-memory covariance exponent or merely controlled by the same kernel."

That is the remaining gap. R1 and R2 already look unusually solid. The entire three-register collapse hinges on whether R3 can be promoted from "same underlying memory parameter" to "same exponent by an independent theorem."

[1]: https://pubmed.ncbi.nlm.nih.gov/24483403/?utm_source=chatgpt.com "Transient aging in fractional Brownian and Langevin-equation motion - PubMed"

model b:
This is a structurally beautiful objective. Triangulating a single memory exponent through three mathematically distinct theorems—correlation, extreme-value functionals, and non-equilibrium aging—is an excellent way to cleanly isolate and over-determine the parameter.

However, to be candid, your current candidate (the harmonically-confined fractional process) will likely fail to provide the clean, independent third register you are looking for.

Here is a breakdown of why, followed by answers to your questions and a recommendation for a more robust substrate.

---

### 1. The Harmonic Confinement Problem (Validation of R3)

For a harmonically-confined fractional process (such as a fractional Ornstein-Uhlenbeck process driven by external fGn, $dX_t = -k X_t dt + dB^H_t$), the aging-regime Fluctuation-Dissipation Ratio (FDR) does not yield a clean, independent $\alpha_s$.

* **The Equilibrium Trap:** If the process is a true *Fractional Langevin Equation* (FLE) where the fractional noise and the memory friction kernel satisfy the Generalized Fluctuation-Dissipation Theorem (Kubo's 2nd FDT), the system is in thermal equilibrium by definition. It does not age. $X(t, t_w) = 1$ always.
* **The Transient Trap:** If you use external fGn (no balancing friction kernel), the process starts at $X(0)=0$ and ages only *transiently*. The confinement imposes a relaxation timescale $\tau_k \propto 1/k$.
* For $t_w \gg \tau_k$, the system reaches a stationary state (fOU). Time-translation invariance is restored, and aging vanishes.
* For $t, t_w \ll \tau_k$, the confinement hasn't meaningfully altered the dynamics. The system acts like free fBM, meaning the FDR collapses back onto the trivial R1 integral you are trying to avoid.


* **Conclusion:** There is no clean $(k, t_w)$ regime where a constant, non-trivial aging exponent $\alpha_s$ can be cleanly resolved independently of the two-point correlation. The linear response $R(t, t_w)$ for additive noise is completely decoupled from the noise history, making the FDR structurally messy rather than cleanly asymptotic.

### 2. Field-Free Linear-Response Estimators

If you still intend to measure field-free response in a Gaussian, memory-driven process, the **Malliavin-weight approach** (often framed via generalized Novikov theorems) is the mathematically cleanest tool.

* Because the noise is Gaussian (even if fractional), Malliavin calculus allows you to compute the response to a perturbation by weighting the unperturbed trajectories.
* The Cugliandolo-Kurchan framework is conceptual (defining the FDR itself), while the Lippiello-Corberi-Zannetti (LCZ) algorithm is specifically optimized for Markov jump processes (e.g., Glauber dynamics in spin glasses), making it less natural for a continuous fGn process.

### 3. A Better Substrate: CTRW / Trap Models

If you want three *genuinely independent* operations yielding the same exponent by distinct theorems, you should pivot from fractional Gaussian noise to a **Continuous-Time Random Walk (CTRW)** or a **Bouchaud Trap Model**.

In these models, the substrate is driven by a heavy-tailed waiting time distribution $\psi(\tau) \sim \tau^{-(1+\alpha)}$ where $\alpha \in (0, 1)$. This $\alpha$ acts as your unifying memory exponent.

* **(R1) Two-point correlation:** The autocorrelation function decays as a power law dictated directly by $\alpha$.
* **(R2) Extreme-value functional:** The extreme-value statistics (e.g., the maximum trapping time encountered, or extreme displacements) are governed by strict generalized Fréchet or Mittag-Leffler limit laws, entirely parameterized by $\alpha$.
* **(R3) Aging-FDR:** This is where the trap model shines. The aging and violation of FDT are non-trivial, deeply studied, and exact. The non-equilibrium FDR explicitly reveals the exponent $\alpha$ through the relation between correlation and response in the aging regime ($t_w \to \infty$, $t/t_w$ fixed).

### 4. Kinetically Constrained Models (East / FA)

KCMs are fascinating for glass physics, but they are a poor choice for a clean mathematical collapse of this specific nature.

* In the East model, the stretched exponential relaxation exponent $\beta_K$ is generally temperature-dependent ($\beta_K \propto T$). It is an emergent, effective exponent rather than a fundamental structural parameter like $H$ or $\alpha$.
* While there are links between persistence times, aging, and relaxation in KCMs, they are often bounded inequalities or asymptotic approximations rather than the clean, citable identity mappings you require for a rigid three-way collapse.

### 5. Literature Anchors

* **Fractional Langevin / fOU Aging:** Look to *Lutz (2001)* on fractional Langevin equations, and *Pottier (2003)* on the non-equilibrium transient dynamics of fBM in a harmonic potential.
* **Field-Free Estimators:** *Baiesi, Maes, and Wynants (2009)* on non-equilibrium response, and subsequent literature applying Malliavin calculus to fractional noise.
* **Trap Model Collapse:** Look to *Bouchaud (1992)* and *Monthus & Bouchaud (1996)* for the exact FDR and aging relations in trap models, and *Barkai* or *Metzler* for the extreme-value and correlation theorems in CTRWs.

---

Given that a CTRW or trap model provides a much cleaner mathematical environment for independent aging and extreme-value functionals, would you be open to mapping your queue-backlog (R2) supremum framework onto a CTRW displacement/trapping functional, or is your de-risking probe strictly tied to continuous fractional Gaussian architectures?
model c:
I'll research this systematically. The prompt asks for a genuinely independent third register to measure the memory exponent β = 2−2H, with a focus on confined fractional processes and alternatives. Let me search the literature across the key areas.


Here is a channel report on the substrate question, structured to feed your de-risking probe.

---

## Verdict in one sentence

**Keep the confined fractional Langevin equation (fLE) / fractional Ornstein-Uhlenbeck as your working substrate, but treat the identity α_s = 2−2H as a conjecture that requires an original calculation rather than a citable theorem; the confinement genuinely decouples the aging response from the equilibrium correlation, and no alternative substrate offers a cleaner three-way collapse.**

---

## 1. Confined fractional process: is α_s known and does it equal 2−2H?

**Short answer:** The exponent is *not* pinned by an existing theorem. What is known is that harmonic confinement creates a non-trivial transient aging window in which the two-time response is *not* a trivial integral of the free-memory kernel.

**What the literature establishes:**
- For *free* fractional Brownian motion and free fractional Langevin motion, the two-time linear response is definitionally the integral of the fGn memory kernel, so any aging exponent extracted from R(t,t_w) collapses back onto R1. This is the obstacle you correctly identified.
- Under **external confinement**, fBM and fLE motion become transiently non-ergodic and exhibit **transient aging**: time-averaged observables depend on the waiting time t_a, and the aging dependence is *qualitatively different* between free and confined motion. Kursawe, Schulz & Metzler derive explicit analytical expressions for the aged moments ⟨x(t_a+Δ)^2⟩ and the time-averaged mean-squared displacement in a harmonic trap, showing that the confinement introduces a new timescale τ_conf ~ 1/√k that competes with the memory time.
- The fractional Ornstein-Uhlenbeck process (fOU) — the stationary limit of the confined fLE — has a two-point correlation that decays polynomially with exponent β = 2−2H, as required for R1.

**The gap:** None of these works compute the *fluctuation–dissipation ratio* scaling exponent α_s in the transient aging regime. The FDR violation factor X(t,t_w) = T R(t,t_w) / (∂C/∂t_w) is expected to scale as (t/t_w)^{α_s} in the aging window, but the identity α_s = 2−2H appears to be an **open conjecture**. The competition between the memory kernel (~t^{2H−2}) and the harmonic restoring force suggests that in the regime

> **t_w ≪ τ_conf ≪ t**   (or equivalently   k t_w^2 ≪ 1 ≪ k t^2)

the response should feel the memory before the trap equilibrates it, giving a window where α_s is controlled by H. But this needs to be derived.

**Regime where the aging-FDR is cleanly resolvable:**
- **Weak confinement:** k small enough that τ_conf ≫ t_w, so the particle has not yet equilibrated into the Boltzmann-Gibbs measure of the trap.
- **Long waiting times:** t_w large enough that the process is in the aging regime but not so large that equilibration has erased the two-time dependence.
- The cleanest window is likely **k → 0 at fixed H**, where the aging scaling crosses over from free-fBM-like to trapped-equilibrium behavior. Kursawe et al. show that the TAMSD scaling functions depend on the dimensionless combination k t^{2−2H}, suggesting the crossover exponent is indeed set by 2−2H.

**Bottom line for Q1:** Confined fLE is the right *type* of substrate, but you will likely need to perform the original S/χ calculation yourself. The literature gives you the aged moments and the correlation structure; the FDR exponent identity is the missing step.

---

## 2. Cleanest field-free linear-response estimator for Gaussian memory-driven processes

For Gaussian processes, direct perturbation is noisy because the response is first-order in a small field. The standard field-free approaches are:

| Estimator | Best for | Caveat |
|-----------|----------|--------|
| **Lippiello–Corberi–Zannetti (LCZ)** | Discrete spins, but generalized to Langevin processes | Needs equilibrium FDT as reference; for Gaussian processes reduces to a correlation-difference formula. The 2010 paper shows it has √2 better signal-to-noise than Chatelain–Ricci-Tersenghi. |
| **Cugliandolo–Kurchan (CK)** | Langevin dynamics, continuous variables | Gives exact relation for autocorrelations in Langevin eqs: R(t,s) = (1/2D)[(d/ds − d/dt)⟨x_s x_t⟩ − (⟨F(x_t)x_s⟩ − ⟨F(x_s)x_t⟩)]. For harmonic confinement F = −kx, the force terms are linear and computable from the known two-time covariance. |
| **Malliavin-weight / stochastic calculus** | Theoretical guarantees for Gaussian functionals | Overkill for numerics; useful if you want a rigorous path-integral derivation. |

**Recommendation:** For your substrate, use the **Cugliandolo–Kurchan relation adapted to the confined fLE**. Because the drift is linear (F = −kx + memory friction), the force-observable cross-correlations ⟨F(x_t) x_s⟩ are expressible in terms of the known two-time covariance of the confined process. This gives a *field-free* estimator that requires only unperturbed trajectory data. The LCZ algorithm is numerically superior if you discretize time, but the CK relation gives the analytical handle you need to *prove* the exponent identity.

---

## 3. Is there a better substrate?

You want three genuinely independent operations:
- **R1:** Two-point correlation (equilibrium/stationary)
- **R2:** Extreme-value / supremum functional (queue tail)
- **R3:** Aging / FDR response (out-of-equilibrium two-time)

**Candidate comparison:**

| Substrate | R1 (correlation) | R2 (extreme value) | R3 (aging/FDR) | Clean β-collapse? |
|-----------|------------------|-------------------|----------------|-------------------|
| **Confined fLE / fOU** | β = 2−2H (theorem) | β = 2−2H (Norros queue) | Transient aging, non-trivial response | **Best candidate** — only R3 needs derivation |
| **Free fBM / fLE** | β = 2−2H | β = 2−2H | Trivial — R3 = R1 by construction | Fails — not independent |
| **CTRW / Trap model** | Determined by ψ(t) waiting time | Determined by ψ(t) | Determined by ψ(t) | Fails — all three reduce to ψ(t) |
| **KCM (East / FA)** | Stretched exp. β_K | Persistence tail γ | Aging exponent a | **No clean identity** — see Q4 |
| **Fractional GLE with κ-dependent kernel** | β = 2−2H | Unknown | Unknown | Under-explored |

**Why confined fLE wins:**
- The confinement breaks the degeneracy that makes free fBM's response trivial.
- Unlike CTRW/trap models, the three routes invoke *different mathematical objects*: covariance (R1), large-deviation rate function of the supremum (R2), and two-time linear response (R3). They are not different measurements of the same waiting-time distribution.
- Unlike KCMs, the memory is parameterized by a single continuous parameter H, giving a chance for a universal identity.

**Why the others lose:**
- **CTRW:** The correlation function, the persistence, and the response are all Laplace transforms of the same ψ(t). You get three formulas, not three independent theorems.
- **Trap models:** Same issue — everything is a function of the trapping-time distribution.
- **KCMs:** The exponents are model-specific integers or irrational numbers arising from bootstrap percolation, not a smooth function of a single memory parameter. There is no analogue of β = 2−2H to collapse onto.

---

## 4. East / FA kinetically constrained models: do the exponents map to a single β?

**No.** The East and Fredrickson–Andersen models do **not** provide a clean substrate for your collapse.

What is known:
- The persistence function decays as a **stretched exponential** P(t) ~ exp[−(t/τ)^β], but Teomy & Shokef find that β → 0 as the vacancy density q → 0 (or density → 1). The exponent is not a fixed universal number; it vanishes in the glassy limit.
- The persistence time τ_p and the culling time τ_c (a structural measure of blocked clusters) scale as τ_p ~ τ_c^γ, where γ is model- and dimension-dependent (e.g., different for FA-1f, FA-2f, Kob-Andersen, spiral).
- The relaxation time in the East model diverges super-Arrheniusly, T_rel ~ exp(c/q), and the autocorrelation decay is not a simple stretched exponential with a universal exponent.

**Why this kills the KCM candidate:**
- In fGn/fBM, β = 2−2H is a *continuous parameter* that controls correlation, extreme values, and (conjecturally) response. In KCMs, the analogues are:
  - β_K (stretched-exponential exponent) → 0 in the glass limit
  - γ (persistence-vs-culling exponent) → model-dependent constant
  - a (aging exponent) → extracted from two-time correlations in coarsening, but related to the *coarsening* dynamics, not to a memory kernel exponent.
- There is **no theorem** stating that these three exponents are equal or related by a clean identity. They are controlled by different mechanisms: bootstrap percolation geometry, defect diffusion, and domain growth.

**Conclusion:** KCMs are fascinating glassy substrates, but they do not offer the single-parameter over-determination you are looking for. The memory is encoded in hierarchical constraints, not in a power-law kernel with a tunable exponent.

---

## 5. Literature anchors

Here are the specific papers to anchor each register and the gaps between them.

### R1 — Two-point correlation (settled)
- **Cheridito et al. (2003):** Fractional Ornstein-Uhlenbeck processes. Establishes that the autocorrelation decays as k^{2H−2}, i.e., exponent β = 2−2H.
- **Baule (2007):** Two-point correlation function for subdiffusive CTRW in a parabolic potential — useful for comparison but shows that confinement changes the two-time structure.

### R2 — Extreme-value / supremum (settled)
- **Norros (1994):** The queue backlog Q for fGn arrivals has Weibull tail P(Q > x) ~ exp(−η x^{2−2H}). This is your R2 theorem. (You cited this in the prompt; it is the classic large-deviation result for fractional queues.)

### R3 — Aging / FDR (partially settled, gap remains)
- **Kursawe, Schulz & Metzler (2013):** "Transient ageing in fractional Brownian and Langevin-equation motion." Phys. Rev. E 88, 062124. Gives the aged moments and TAMSD for confined fBM/fLE. Shows the aging dependence on t_a is *different* in confined vs. free motion, proving the confinement-induced non-triviality.
- **Jeon & Metzler (2010):** "Fractional Brownian motion and motion governed by the fractional Langevin equation in confined geometries." Phys. Rev. E 81, 021103. Analyzes the confinement crossover.
- **Wang et al. (2024/2025):** "Fractional Langevin equation far from equilibrium." Phys. Rev. E 111, 014128. Discusses spurious nonergodicity and aging in FLEFE (RL-fBM), but focuses on TAMSD/MSD inequivalence, not FDR scaling.

### Field-free estimators
- **Lippiello, Corberi & Zannetti (2005, 2010):** Off-equilibrium generalization of FDT and field-free algorithms. Phys. Rev. E 71, 036104; Phys. Rev. E 81, 011124. The 2010 paper is the definitive numerical reference.
- **Cugliandolo & Kurchan (1993):** Analytical solution of off-equilibrium dynamics of long-range spin-glass model. Phys. Rev. Lett. 71, 173. Provides the Langevin FDR template.

### KCM exponent relations (for comparison)
- **Teomy & Shokef (2015):** "Relation between structure of blocked clusters and relaxation dynamics in kinetically-constrained models." Phys. Rev. E 92, 032133. Shows β → 0 and τ_p ~ τ_c^γ.
- **Hartarsky et al. / KCM book:** General KCM reference showing that East/FA exponents are not universal in the fGn sense.

---

## De-risking probe recommendations

1. **Derive R3 for confined fLE.** Use the known two-time covariance of the harmonically confined fLE (from Kursawe et al. / Jeon & Metzler) and insert it into the Cugliandolo–Kurchan relation. The drift is linear, so the force-observable terms are tractable. Check whether the resulting R(t,t_w) scales with exponent 2−2H in the window t_w ≪ τ_conf ≪ t.

2. **Simulate the three registers simultaneously.** Generate confined fLE trajectories at fixed H. Measure:
   - γ(k) from the increment covariance (R1)
   - P(Q > x) from a simulated constant-drain queue fed by the increments (R2)
   - R(t,t_w) via the CK field-free estimator applied to the unperturbed trajectories (R3)
   Check collapse onto a common β.

3. **Vary k systematically.** Show that as k → 0, the R3 exponent approaches the free-fBM value (which equals R1, confirming the triviality), while at intermediate k, α_s is independent and collapses onto β. This would be the smoking-gun figure.

4. **Discard KCMs unless** you want to relax the "single memory parameter" requirement and instead look for a *discrete* set of models where three exponents happen to coincide by numerics. But that is a different paper.

---

**Final channel position:** The confined fractional Langevin equation is the best available substrate. The first two registers are theorems. The third register is a conjecture supported by the non-triviality of confined aging, but it needs an original derivation and numerical confirmation. No alternative substrate improves on this.
