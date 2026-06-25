# Outbound-research prompt (round 2) — derive the R3 aging-FDR exponent for the confined fLE

Round 2 of the β-collapse 3rd-register substrate question. Round 1
(`research_prompt_beta_3rd_register_substrate.md`) converged: `α_s = 2−2H` is **not** a citable theorem;
the confined fractional Langevin equation is the right substrate; CTRW/trap and East/FA are rejected. This
round asks the channels to **attempt the original derivation** (theory-leads-numerics, per the program
owner). Returned attempts file alongside; they then cross-check the planned vary-`k` numerical probe.

---

## Derive the aging-FDR exponent `α_s` for the harmonically-confined fractional Langevin equation

*Round 1 established: `α_s = 2−2H` is not a citable theorem; the confined fLE is the right substrate;
CTRW/trap and East/FA are rejected (CTRW collapses all three routes onto one `ψ(t)`; KCMs have no single
master exponent). The request now is an **attempt at the original derivation**, not another literature
search.*

**Goal.** Derive the aging-regime fluctuation–dissipation-ratio exponent `α_s` for a harmonically-confined
long-memory process driven at Hurst `H ∈ (1/2,1)` (memory exponent `β = 2−2H`), and determine whether
**`α_s = 2−2H`** or some other clean function of `H`. This is the third, independent register of a
memory-exponent over-determination whose other two are settled theorems: R1 the fGn autocovariance slope
`γ(k) ~ k^(−β)`; R2 the Norros fGn-queue Weibull tail `P(Q>x) ~ exp(−η x^(2−2H))`. R3 must be an FDR-aging
exponent from a **non-trivial** two-time response (free fBm's response is the trivial integrated kernel, so
its `α_s ≡ β_mem` by construction — the obstacle).

**The derivation requested:**

1. **Specify the process precisely.** A harmonically-confined fractional process that *genuinely ages*
   (transient relaxation toward the confined stationary state) **and** has a derivable, non-trivial FDR.
   Round 1 flagged two traps: (i) the Kubo-2nd-FDT-consistent FLE is in thermal equilibrium → `X≡1`, no
   aging; (ii) the external-fGn confined OU `dx = −kx dt + dB_H` ages only transiently and its response may
   decouple from the noise history. Pick the cleanest process that escapes both, and state it explicitly
   (friction kernel, noise, FDT status).
2. **Two-time covariance.** Use the known confined `C(t,t_w)` (Kursawe–Schulz–Metzler, PRE 88, 062124
   (2013); Jeon–Metzler, PRE 81, 021103) in the transient-aging window `t_w ≪ τ_conf ≪ t`
   (`k t_w² ≪ 1 ≪ k t²`).
3. **Response via Cugliandolo–Kurchan.** With linear drift `F = −kx`,
   `R(t,s) = (1/2D)[(∂_s − ∂_t)C(t,s) − (⟨F(x_t)x_s⟩ − ⟨F(x_s)x_t⟩)]`; the force terms reduce to the known
   covariance. Compute `R(t,t_w)`.
4. **The FDR exponent.** `X(t,t_w) = T·R/(∂_{t_w}C)`; extract the aging scaling `X ~ (t/t_w)^{α_s}` (or the
   appropriate two-time form). Give `α_s(H)`.

**Questions:**

1. What is `α_s(H)` — does it equal `2−2H`, or a different clean function (`H`, `1−H`, `H−1/2`, …)?
2. **Is `α_s` genuinely independent**, or "another face of the same Gaussian propagator" (since on a
   linear-Gaussian substrate `C` and `R` are both functionals of one propagator)? If the latter, is there a
   *minimal nonlinearity* that makes `α_s` an independent functional while keeping `β = 2−2H` pinned?
3. The precise `(k, t_w, t)` regime where `α_s` is constant and the derivation holds.
4. Where could the derivation break (the equilibrium trap, response-decoupling, discretization)?

If a closed form is out of reach, an **asymptotic scaling argument** for `α_s` in the `t_w ≪ τ_conf ≪ t`
window is the key deliverable.

----

model a:
This is now squarely in "attempt the derivation" territory rather than literature retrieval, so I'll treat it as a theoretical exercise.

My conclusion after working through the scaling structure is:

> The most likely outcome is **not** ( \alpha_s = 2-2H ).
>
> Instead, for any linear Gaussian confined fractional process, the aging FDR exponent appears to collapse to
>
> [
> \alpha_s = 0,
> ]
>
> with the memory exponent ( \beta = 2-2H ) appearing only in the scaling function and crossover amplitudes.
>
> If that argument is right, the proposed R3 register does **not** furnish an independent exponent.

That sounds disappointing, but it is actually an informative de-risking result.

---

## Step 1: Which process?

The round-1 diagnosis was correct.

### Thermal FLE

The generalized Langevin equation

[
m\ddot x(t)
===========

-kx(t)
-\int_0^t \Gamma(t-s)\dot x(s),ds
+\eta(t)
]

with

[
\langle \eta(t)\eta(s)\rangle
=============================

k_BT,\Gamma(|t-s|)
]

obeys the second FDT.

At all times

[
X(t,t_w)=1.
]

No aging register exists.

Rejected.

---

### Fractional OU driven by external fGn

Take

[
\dot x=-kx+\xi_H(t),
]

where

[
\langle \xi_H(t)\xi_H(s)\rangle
\sim |t-s|^{-\beta},
\qquad
\beta=2-2H.
]

Start from a nonstationary initial condition.

This ages transiently because:

* memory is long,
* confinement is finite,
* stationarity has not yet formed.

Most importantly:

[
R(t,s)=e^{-k(t-s)}
]

is independent of the noise history.

This is the cleanest place to do the asymptotics.

---

## Step 2: Covariance scaling

Write

[
x(t)
====

\int_0^t e^{-k(t-u)}\xi_H(u),du.
]

Then

[
C(t,s)
======

\int_0^tdu
\int_0^sdv,
e^{-k(t-u)}
e^{-k(s-v)}
|u-v|^{-\beta}.
]

The key scale is

[
\tau_c\sim k^{-1}.
]

You want

[
s=t_w\ll \tau_c \ll t.
]

The older variable (s) remains in the pre-confined regime while (t) already feels confinement.

A matched-asymptotic estimate gives

[
C(t,s)
\sim
e^{-kt}
,s^{,1-\beta}
]

up to (H)-dependent constants.

The crucial point is that all memory dependence enters through powers of (s).

---

## Step 3: Response

Because the dynamics are linear,

[
R(t,s)
======

# \frac{\delta x(t)}{\delta h(s)}

e^{-k(t-s)}.
]

Nothing fractional survives.

In the same asymptotic window,

[
R(t,s)
\sim
e^{-kt}.
]

---

## Step 4: Compute the FDR

Define

[
X(t,s)
======

T
\frac{R(t,s)}
{\partial_s C(t,s)}.
]

Differentiate the covariance estimate:

[
\partial_s C
\sim
(1-\beta)
e^{-kt}
s^{-\beta}.
]

Therefore

[
X(t,s)
\sim
s^{\beta}.
]

Notice what happened.

The exponent appears on the waiting time only:

[
X(t,s)
\propto
s^{\beta}.
]

There is no surviving factor

[
(t/s)^{\alpha_s}.
]

Rewritten as a two-time scaling form,

[
X(t,s)
======

s^\beta
,\Phi(kt).
]

The aging exponent in the usual CK sense is therefore

[
\boxed{\alpha_s=0}.
]

while

[
\beta
=====

2-2H
]

enters only as a prefactor exponent.

---

## Why this keeps happening

There is a structural reason.

In any linear Gaussian model,

[
C(t,s)
======

G,K,G^T,
]

where:

* (G) = propagator,
* (K) = noise kernel.

Meanwhile

[
R(t,s)=G(t,s).
]

Thus both observables are generated by the same Green function.

The covariance contains one extra convolution with (K), but no new dynamical object appears.

Consequently every exponent extracted from (R) or (X) tends to be inherited from the same propagator.

This is exactly the concern you raised in round 1.

I think the derivation confirms it.

---

## What would produce a genuine R3?

You need a response functional that is not reducible to the Gaussian propagator.

The smallest modification is probably:

[
\dot x
======

-kx
-\lambda x^3
+\xi_H.
]

with

[
0<\lambda\ll1.
]

Then:

* R1 remains controlled by long-memory fGn.
* R2 (queue functional) remains controlled by the same memory exponent.
* R3 involves nonlinear response vertices.

Now (R) is no longer a simple Green function.

The FDR contains genuinely new diagrams rather than another contraction of the same propagator.

That is the first place I would expect an independently measurable aging exponent.

---

## Where the derivation could fail

Three places.

### 1. Wrong aging regime

If

[
t_w \sim \tau_c
]

rather than

[
t_w \ll \tau_c,
]

the covariance asymptotics change.

A different scaling function may emerge.

---

### 2. Thermal FLE accidentally used

Then

[
X\equiv1
]

identically.

The register disappears.

---

### 3. Hidden cancellation in the CK force term

The full CK expression contains

[
\langle F(x_t)x_s\rangle
------------------------

\langle F(x_s)x_t\rangle.
]

For linear drift

[
F=-kx
]

those terms collapse onto combinations of (C).

My estimate assumed that reduction.

If a careful evaluation of the transient covariance produces an additional factor

[
(t/s)^\beta,
]

then the conclusion changes.

That is the single place where a surprise

[
\alpha_s=\beta
]

could still emerge.

---

## My current betting line

If I had to assign probabilities before running the vary-(k) numerical probe:

| Outcome                                      | Probability |
| -------------------------------------------- | ----------- |
| (\alpha_s=0) (no independent aging exponent) | ~60%        |
| (\alpha_s=\beta=2-2H)                        | ~25%        |
| (\alpha_s) another simple function of (H)    | ~10%        |
| no clean asymptotic exponent at all          | ~5%         |

The deeper reason is that the confined fGn/fOU substrate still looks too linear and too Gaussian. The memory exponent survives everywhere, but it survives as the exponent of the kernel itself. Extracting a third *independent* theorem from that structure may require the first controlled nonlinearity rather than a more clever observable.

model b:
This is a rigorous and elegant theoretical stress-test. You are right to demand a strict, original derivation to pre-flight the numerical probe. I will execute the derivation exactly as requested to provide the theory-leads-numerics baseline.

However, balancing empathy for this beautifully structured objective with mathematical candor, I must warn you: the derivation below will prove that a linear confined system cannot yield an independent $\alpha_s$. It acts as a mathematical mirror, reflecting the correlation exponent back at you or breaking scale-invariance entirely.

Here is the derivation, followed by the answers to your specific questions, which explicitly locate where the `vary-k` numerical probe will fail.

---

### 1. Specification of the Process

To escape both the equilibrium trap (which prevents aging) and the external-fOU decoupling trap (which renders response trivial), we must use an **overdamped Generalized Langevin Equation (GLE)** satisfying Kubo’s 2nd FDT, but prepared out of equilibrium via a quench to $X(0) = 0$:

$$\int_0^t \gamma(t-s) \dot{X}(s) ds = -k X(t) + \xi(t)$$

where the friction kernel features long memory $\gamma(t) = \gamma_0 t^{-\beta}$ with $\beta = 2-2H$. To satisfy the generalized FDT, the internal noise $\xi(t)$ is fractional Gaussian noise with covariance $\langle \xi(t)\xi(s) \rangle = k_B T \gamma(|t-s|)$. Because $X(0) = 0$, the system undergoes genuine transient aging as it relaxes toward the confined stationary state.

### 2. Two-Time Covariance

For this process, the fundamental Green's function is the relaxation function $S(t)$, which satisfies $k S(t) + \int_0^t \gamma(t-s) \dot{S}(s) ds = 0$ with $S(0)=1$. Given $\gamma(t) \propto t^{-\beta}$, exact Laplace inversion yields the Mittag-Leffler function:


$$S(t) = E_{2-2H}\left( - (t/\tau_k)^{2-2H} \right)$$


where $\tau_k \propto k^{-1/(2-2H)}$ is the confinement timescale.

Following Kursawe, Schulz, and Metzler (2013), the two-time covariance for this quench is explicitly tied to $S(t)$:


$$C(t, t_w) = \frac{k_B T}{k} \left[ S(t-t_w) - S(t)S(t_w) \right]$$

### 3. Response via Cugliandolo-Kurchan (Linear Regime)

In a linear Gaussian framework, the field-free response to a perturbation is exactly the derivative of the relaxation function. The response $R(t, t_w) = \left. \frac{\delta \langle X(t) \rangle}{\delta h(t_w)} \right|_{h=0}$ is:


$$R(t, t_w) = \frac{1}{k} \frac{\partial}{\partial t_w} S(t-t_w)$$

To construct the Cugliandolo-Kurchan FDR, we need the aging derivative of the covariance:


$$\partial_{t_w} C(t, t_w) = \frac{k_B T}{k} \left[ \frac{\partial}{\partial t_w} S(t-t_w) - S(t)\dot{S}(t_w) \right]$$

### 4. Extracting the FDR Exponent

The Fluctuation-Dissipation Ratio is defined as $X(t, t_w) = \frac{k_B T R(t, t_w)}{\partial_{t_w} C(t, t_w)}$. Substituting the terms from Step 3:


$$X(t, t_w) = \frac{\partial_{t_w} S(t-t_w)}{\partial_{t_w} S(t-t_w) - S(t)\dot{S}(t_w)} = \left( 1 - \frac{S(t)\dot{S}(t_w)}{\partial_{t_w} S(t-t_w)} \right)^{-1}$$

Let $\Lambda(t, t_w) = \frac{S(t)\dot{S}(t_w)}{\partial_{t_w} S(t-t_w)}$. The scaling of $X$ depends entirely on the asymptotic expansion of $S(t)$:

* **Small times ($t \ll \tau_k$):** $S(t) \approx 1 - a t^\beta \implies \dot{S}(t) \approx -a \beta t^{\beta-1}$
* **Large times ($t \gg \tau_k$):** $S(t) \approx b t^{-\beta} \implies \dot{S}(t) \approx -b \beta t^{-\beta-1}$

Let us evaluate the transient-aging window requested: **$t_w \ll \tau_k \ll t$**.
Here, $S(t)$ is in the large-time limit, and $S(t_w)$ is in the small-time limit.

* $S(t) \approx b t^{-\beta}$
* $\dot{S}(t_w) \approx -a \beta t_w^{\beta-1}$
* $\partial_{t_w} S(t-t_w) \approx b \beta (t-t_w)^{-\beta-1} \approx b \beta t^{-\beta-1}$

Substituting these into $\Lambda$:


$$\Lambda \approx \frac{(b t^{-\beta})(-a \beta t_w^{\beta-1})}{b \beta t^{-\beta-1}} = - a t t_w^{\beta-1}$$


Because $\beta = 2-2H \in (0,1)$, the exponent $(\beta-1)$ is negative. Thus, for $t \gg \tau_k$ and $t_w \ll \tau_k$, $|\Lambda| \gg 1$.
The FDR ratio becomes:


$$X(t, t_w) \approx - \Lambda^{-1} \propto \frac{1}{t t_w^{\beta-1}}$$

---

### Answers to Your Questions

**1. What is $\alpha_s(H)$?**
In your target window ($t_w \ll \tau_k \ll t$), **$\alpha_s$ does not exist**. As proven above, $X(t, t_w) \propto t^{-1} t_w^{1-\beta}$. It fails to form a scale-invariant function of $(t/t_w)$, meaning no clean aging exponent can be resolved.

If we shift to the early transient window ($t_w \ll t \ll \tau_k$), we get $\Lambda \approx -(t/t_w)^{1-\beta}$, which yields $X \approx (t/t_w)^{\beta-1} = (t/t_w)^{1-2H}$. Here $\alpha_s = 1-2H$. However, because $t \ll \tau_k$, the system has not yet felt the confinement; this is mathematically identical to free fBM, putting you back at square one.

**2. Is $\alpha_s$ genuinely independent, or "another face of the same Gaussian propagator"?**
It is fundamentally **not independent**. As shown in Step 4, $X(t,t_w)$ reduces entirely to an algebraic ratio of the Mittag-Leffler relaxation function $S(t)$ and its derivatives. Any exponent you extract is functionally hardcoded by the linear map between $R$ and $C$.

**Minimal Nonlinearity:** To decouple the response from the trivial covariance propagator while keeping $\beta=2-2H$ pinned, you must introduce a mode-coupling term. The minimal model is to replace the harmonic confinement with an anharmonic well, $V(x) = \frac{1}{4}g x^4$. This forces the linear response to depend on higher-order non-Gaussian noise correlations (via generalized Novikov/Malliavin theorems) that are strictly invisible to the two-point $C(t, t_w)$.

**3. The precise $(k, t_w, t)$ regime where $\alpha_s$ is constant and the derivation holds.**
There is a catch-22. $\alpha_s$ is only constant in the pre-relaxation regime $t_w \ll t \ll \tau_k$. Once $t$ exceeds $\tau_k$ (the very confinement you introduced to generate non-triviality), the different asymptotic decay rates of $S(t)$ and its derivative destroy the scale-invariance of the FDR.

**4. Where could the derivation break?**
The derivation will break your numerical probe specifically at the assumption that $X(t,t_w)$ will gracefully map onto a single $(t/t_w)$ curve across the $\tau_k$ boundary. Your `vary-k` numerical runs will show standard free-fBM scaling for early times, and then a chaotic, non-collapsing crossover as $t$ crosses $1/k$, ultimately decaying to zero as $1/t$.

model c:
Here is the attempted derivation. I will state the result upfront, then build it step by step.

---

## Result

For the **internal fractional Langevin equation with harmonic confinement** (fLE–trap), in the transient-aging window **t_w ≪ τ_conf ≪ t**, the fluctuation–dissipation ratio scales as

$$X(t,t_w) \;\sim\; \left(\frac{t_w}{t}\right)^{1-\beta} \;=\; \left(\frac{t_w}{t}\right)^{2H-1},$$

so the **aging-FDR exponent is**

$$\boxed{\alpha_s \;=\; 1-\beta \;=\; 2H-1 \;\neq\; \beta.}$$

This is **not** the identity α_s = β you were hoping for. The confinement decouples the response from the correlation kernel enough to make α_s independent of β, but the function it produces is the *complement* 1−β, not β itself. The three registers do **not** collapse onto a single number; they satisfy the **sum rule** β + α_s = 1.

Below is the derivation, followed by an analysis of why this happens and what it means for your program.

---

## 1. Process specification: the internal fLE with harmonic trap

I use the **internal** (Kubo-second-FDT-consistent) fractional Langevin equation with a harmonic restoring force:

$$\gamma\, D^\beta x(t) + \omega^2 x(t) = \xi(t), \qquad x(0)=0,$$

where:
- $D^\beta$ is the Riemann–Liouville fractional derivative of order $\beta = 2-2H \in (0,1)$.
- $\xi(t)$ is fractional Gaussian noise with covariance  
  $\langle \xi(t)\xi(s)\rangle = \gamma k_B T\, K(|t-s|)$,  
  $K(\tau) = \tau^{-\beta}/\Gamma(1-\beta)$.
- $\omega^2 = k$ is the trap strength.
- The confinement timescale is $\tau_{\rm conf} \sim \omega^{-2/\beta}$.

**Why this process:** It satisfies the Kubo fluctuation-dissipation theorem at equilibrium (so the *stationary* state has $X\equiv 1$), but starting from $x(0)=0$ it undergoes **transient aging** toward that stationary state. The trap introduces a competing timescale that makes the two-time response non-trivial. The external fOU ($dx = -\omega^2 x\,dt + dB_H$) is rejected because its noise is not thermally consistent with a memory kernel; the internal fLE is the minimal thermally sound substrate.

---

## 2. Two-time covariance in the aging window

The exact solution is a convolution with the Green's function:

$$x(t) = \int_0^t G(t-u)\,\xi(u)\,du,$$

$$G(t) = t^{\beta-1} E_{\beta,\beta}\!\bigl(-\omega^\beta t^\beta\bigr),$$

where $E_{\beta,\beta}$ is the Mittag-Leffler function.

The two-time correlation is:

$$C(t,t_w) = \langle x(t)x(t_w)\rangle = \frac{\gamma k_B T}{\omega^4}\int_0^t\!da\,G(a)\int_0^{t_w}\!db\,G(b)\,K(|t-t_w-a+b|).$$

**Aging asymptotics (t_w ≪ τ_conf ≪ t).** In this window:
- $G(a)$ for $a \sim t \gg \tau_{\rm conf}$ has decayed into its **Mittag-Leffler tail**:  
  $G(t) \sim -\omega^{-2\beta}\,t^{-\beta-1}/\Gamma(-\beta)$.
- $G(b)$ for $b \sim t_w \ll \tau_{\rm conf}$ is still in its **rise phase**:  
  $\int_0^{t_w} G(b)\,db \sim t_w^\beta/\Gamma(1+\beta)$.
- The noise kernel $K(|t-t_w-a+b|) \approx K(t) \sim t^{-\beta}/\Gamma(1-\beta)$ because $a,b \ll t$.

Factorizing the integrals (valid because $G(t-a) \approx G(t)$ when $a \ll t$ and $G$ has decayed):

$$C(t,t_w) \;\sim\; \frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,\left(\frac{t_w}{t}\right)^\beta.$$

This is the Kursawe–Schulz–Metzler transient-aging result: the correlation decays as a **power law in the ratio** $t_w/t$ with exponent $\beta = 2-2H$.

---

## 3. Response via Cugliandolo–Kurchan

For a perturbation $-h(t)x(t)$ added to the Hamiltonian, the linear response is exact because the drift is linear:

$$R(t,t_w) \;=\; \frac{\delta\langle x(t)\rangle}{\delta h(t_w)}\Big|_{h=0} \;=\; G(t-t_w), \qquad t>t_w.$$

This is the crucial simplification of the Gaussian substrate: the response is the bare propagator.

In the aging window $t \gg t_w \gg \tau_{\rm conf}$:

$$R(t,t_w) \;=\; G(t-t_w) \;\sim\; G(t) \;\sim\; -\frac{\omega^{-2\beta}}{\Gamma(-\beta)}\,t^{-\beta-1}.$$

Now apply the **Cugliandolo–Kurchan relation**. For Langevin dynamics with linear drift $F=-\omega^2 x$, the force-term difference vanishes by symmetry ($\langle F(x_t)x_s\rangle = \langle F(x_s)x_t\rangle$ for Gaussian variables with zero mean), leaving:

$$R(t,t_w) \;=\; \frac{1}{2k_B T}\Bigl(\partial_{t_w} - \partial_t\Bigr)C(t,t_w).$$

Let us verify consistency. From the correlation scaling:

$$\partial_{t_w} C \;\sim\; \beta\,\frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,t_w^{\beta-1}\,t^{-\beta},$$

$$\partial_t C \;\sim\; -\beta\,\frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,t_w^{\beta}\,t^{-\beta-1}.$$

Since $t \gg t_w$, the $\partial_t C$ term is subdominant by a factor $t_w/t$. Thus:

$$\bigl(\partial_{t_w} - \partial_t\bigr)C \;\sim\; \beta\,\frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,t_w^{\beta-1}\,t^{-\beta}.$$

Inserting into CK:

$$R_{\rm CK}(t,t_w) \;\sim\; \frac{1}{2k_B T}\,\beta\,\frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,t_w^{\beta-1}\,t^{-\beta}.$$

Compare with the exact response $R(t,t_w) \sim t^{-\beta-1}$. These are **not** proportional unless $t_w \sim t$. The CK relation is exact, but the *ratio* of the exact response to the correlation derivative is **not** the equilibrium constant $1/k_B T$; it is a function of $t/t_w$.

---

## 4. The FDR exponent

Define the fluctuation–dissipation ratio as usual:

$$X(t,t_w) \;=\; \frac{k_B T\,R(t,t_w)}{\partial_{t_w}C(t,t_w)}.$$

Using the asymptotic forms:

$$X(t,t_w) \;\sim\; \frac{k_B T \cdot \bigl[\text{const}\times t^{-\beta-1}\bigr]}{\beta\,\frac{k_B T}{\omega^2}\,\frac{\sin(\pi\beta)}{\pi\beta}\,t_w^{\beta-1}\,t^{-\beta}} \;=\; X_0\,\frac{t^{-1}}{t_w^{\beta-1}} \;=\; X_0\left(\frac{t_w}{t}\right)^{1-\beta},$$

where $X_0$ is a constant prefactor of order unity.

Therefore, in the aging regime:

$$\boxed{X(t,t_w) \;\sim\; \left(\frac{t_w}{t}\right)^{2H-1}},$$

and the **FDR exponent is**

$$\boxed{\alpha_s = 1-\beta = 2H-1.}$$

---

## 5. Answers to the four questions

### Q1. What is α_s(H)? Does it equal 2−2H?

**No.** $\alpha_s = 1-\beta = 2H-1$. It equals $\beta = 2-2H$ only at the special point $H=3/4$ ($\beta=1/2$), where the two lines cross by accident. For generic $H \in (1/2,1)$, the FDR register measures a **different** function of $H$.

### Q2. Is α_s genuinely independent? Minimal nonlinearity?

For the **linear Gaussian** substrate, $C$ and $R$ are both functionals of the single propagator $G(t)$. In this sense they are "two faces of the same Gaussian" — the entire process is determined by $G$, and both correlation and response are derived from it. The independence is **structural** (different functionals) but not **deep** (same propagator).

To make $\alpha_s$ an **independent functional** while keeping $\beta = 2-2H$ pinned, one needs a **minimal nonlinearity**. The natural candidate is a weak quartic perturbation to the trap:

$$V(x) = \tfrac{1}{2}\omega^2 x^2 + \tfrac{\lambda}{4}x^4, \qquad \lambda \ll \omega^4.$$

**Why this works:**
- The **short-time / high-frequency** dynamics (which determines the memory kernel and hence $\beta$) is controlled by the fractional derivative and the harmonic curvature at the bottom of the well. For small $\lambda$, the local dynamics near $x\approx 0$ are unchanged, so $\beta$ is pinned.
- The **response** to a field is no longer the bare propagator $G$; it involves the non-Gaussian statistics of the aging distribution. The Cugliandolo–Kurchan relation now has non-vanishing force-term cumulants: $\langle F(x_t)x_s\rangle_c \neq \omega^2 C(t,t_w)$.
- The **FDR ratio** $X(t,t_w)$ acquires $\lambda$-dependent corrections that alter its scaling exponent.

**Perturbative conjecture:** At leading order in $\lambda$, the FDR exponent should shift as

$$\alpha_s(\lambda) = (1-\beta) + c_1\lambda + O(\lambda^2).$$

If $c_1 \neq 0$, one could *tune* $\lambda$ to a critical value $\lambda_*$ where $\alpha_s(\lambda_*) = \beta$, making the three registers collapse. This is a **reverse-engineering** of the nonlinearity to force the collapse. Whether such a $\lambda_*$ exists and is universal (independent of $H$) is an open question requiring a perturbative calculation of $c_1$.

**Alternative minimal nonlinearity:** A **piecewise-linear** potential (e.g., a "V-shaped" harmonic trap with a flat bottom) preserves solvability via Laplace transforms while breaking Gaussianity. The response in the flat region is diffusive, while in the harmonic wings it is confined; the competition might produce a tunable $\alpha_s$.

### Q3. Precise (k, t_w, t) regime

The derivation holds in the **triple-separated regime**:

$$t_{\rm micro} \;\ll\; t_w \;\ll\; \tau_{\rm conf} \;\ll\; t,$$

where:
- $t_{\rm micro} \sim dt$ (the microscopic discretization or inertial time) must be negligible.
- $t_w \ll \tau_{\rm conf} = \omega^{-2/\beta}$ ensures the system has **not yet equilibrated** in the trap at the waiting time.
- $t \gg \tau_{\rm conf}$ ensures the **response** has decayed into the Mittag-Leffler tail (trap-dominated).
- $t \gg t_w$ ensures the **correlation** scaling is dominated by the ratio $(t_w/t)^\beta$.

In terms of the dimensionless variables used by Kursawe et al., this is the regime where the TAMSD scaling function depends on the combination $\omega^2 t^{2-2H} = \omega^2 t^\beta \gg 1$ (trap-dominated at observation time) but $\omega^2 t_w^\beta \ll 1$ (free-like at waiting time).

### Q4. Where the derivation breaks

1. **Equilibrium trap:** If $t_w \gtrsim \tau_{\rm conf}$, the system has equilibrated. The correlation becomes stationary ($C(t,t_w) = C_{\rm eq}(t-t_w)$), the response satisfies the equilibrium FDT ($X=1$), and there is **no power-law aging** to extract an exponent from.
2. **Response decoupling:** If $t \lesssim \tau_{\rm conf}$, the response $G(t-t_w)$ is still in its rise phase ($\sim (t-t_w)^{\beta-1}$), not its tail. The scaling changes and the simple $(t_w/t)^{1-\beta}$ law is lost.
3. **Discretization:** Numerical simulation of the fLE requires Grünwald–Letnikov discretization of the fractional derivative. At finite $\Delta t$, the early-time behavior of $G(t)$ is regularized, corrupting the exponent extraction unless $\Delta t \ll t_w \ll \tau_{\rm conf}$.
4. **Gaussian degeneracy:** As noted in Q2, the linearity means $R$ and $C$ are not statistically independent. Any noise in the numerical estimation of $C$ propagates directly into the CK-estimated $R$, making the "independence" of the third register illusory. This is the fundamental limitation of the linear substrate.

---

## Summary for the de-risking probe

| Register | Exponent | Status |
|----------|----------|--------|
| R1: Two-point correlation | $\beta = 2-2H$ | **Theorem** (Cheridito et al.) |
| R2: Extreme-value / queue tail | $\beta = 2-2H$ | **Theorem** (Norros) |
| R3: Aging FDR (confined fLE) | $\alpha_s = 1-\beta = 2H-1$ | **Derived here** |

The confined fLE **fails** the strict $\beta$-collapse test for generic $H$, but it **succeeds** in providing a non-trivial, confinement-induced third route. The relation $\alpha_s + \beta = 1$ is itself a sharp constraint.

**Recommended next step:** If you insist on a genuine three-way collapse to a *single* $\beta$, you must either:
- **(A)** Add a tunable nonlinearity (quartic or piecewise-linear) and compute perturbatively whether $\alpha_s$ can be shifted to $\beta$; or
- **(B)** Change the definition of the FDR exponent (e.g., extract it from the **velocity** response rather than position, or from the **energy** response), though I see no immediate reason this would restore the identity.

The derivation above is the analytical foundation for either path.

---

## Round 3 — inverse-asymptotics push (relayed in chat, recorded here for completeness)

*A meta-methodological push on one of the models: when a derivation keeps collapsing into circularity,
stop asking "what is the theorem?" and instead ask — what asymptotic form would have to exist for
`α_s = β` to come out? Then work backwards. An inverse-asymptotics attack. Its five tricks all converge
on the same conclusion the round-2 derivations reached, and supply the structural why.*

**Trick 1 — dimensional census.** Write the most general scaling `C(t,t_w) = t_w^a F(t/t_w, kt, kt_w)`,
`R(t,t_w) = t_w^b G(...)`. Then `X = R/∂_{t_w}C ~ t_w^{b−a+1} H(...)`. Ask what `a,b` must be for
`X ~ (t/t_w)^β`; this gives algebraic constraints on the scaling dimensions. Inspect the
Kursawe–Schulz–Metzler covariance: if those dimensions are not present, the theorem is impossible before
any detailed calculation.

**Trick 2 — reverse-engineer the required covariance.** Insist `X ∝ (t/t_w)^β`. Then
`∂_{t_w}C ∝ R·(t_w/t)^β`. For the confined Gaussian process `R ~ e^{−k(t−t_w)}`, so
`∂_{t_w}C ~ e^{−k(t−t_w)}(t_w/t)^β`; integrating, `C ~ ∫ e^{−k(t−u)}(u/t)^β du`. Compare with the actual
covariance — if it cannot be massaged into that structure, `α_s = β` cannot occur. Turns the problem into
pattern matching.

**Trick 3 — Laplace-space exponent bookkeeping (cleanest brute force).** `Γ(t) ~ t^{−β}` ⇒
`Γ̃(s) ~ s^{β−1}` at small `s`. Propagator `G̃(s) = 1/(k + s + Γ̃(s)) ~ 1/(k + s + s^{β−1})`. Count powers
of `s`: covariance carries `G²Γ`, response carries `G`, FDR carries `G/(G²Γ)`. Watch whether a leftover
`s^{β−1}` survives (⇒ a power law in time) or cancels (⇒ `α_s = 0`).

**Trick 4 — RG-style exponent conservation (the conceptual heart).** If there is one relevant IR exponent,
every observable is `O_i ~ ℓ^{y_i β}`. Is the FDR a *primary* scaling observable or a *ratio*? If
`X = O_1/O_2`, the `β`'s often cancel — which would naturally explain `α_s = 0`, and the cancellation
*itself* is the theorem. Exactly as in critical phenomena: correlation functions carry anomalous
dimensions, amplitude ratios do not. The FDR may secretly be an amplitude ratio.

**Trick 5 — the forbidden-exponent test.** If `α_s = β`, where could that exponent physically live? Memory
kernel (already → R1), covariance (already → R1), propagator (appears in `R` and `C`, tends to cancel in
ratios), initial-condition sector (usually amplitudes only), or the nonlinearity. Eliminate the first four
⇒ the only surviving slot is the **nonlinear response sector**. If every place capable of carrying a `β`
cancels inside `X`, the exponent must enter through a sector absent from the linear-Gaussian theory.

**The experiment to run (symbolic, before any numerics).** Assume `C ~ t_w^a f(t/t_w)`, `R ~ t_w^b g(t/t_w)`
with `a,b` unknown; derive the most general exponent of `X = R/∂_{t_w}C ~ t_w^{b−a+1}(t/t_w)^μ`; compare the
template against the exact confined-fLE asymptotics. If no choice of coefficients gives `μ = β`, that proves
the desired collapse is *not hidden in the algebra — it is absent from the linear-Gaussian substrate itself*.
The missing ingredient is a response sector not generated by the same propagator that already controls R1.

*Disposition (this repo): the push hardens the closure rather than reopening it — see
`beta_collapse_3rd_register_design.md` (the FDR is an amplitude ratio ⇒ `β` cancels ⇒ the nonlinear sector
is the only surviving slot; this also unifies the a/b/c residual split). The full symbolic census was NOT
run here: it is confirmatory (the park decision is unchanged), and the careful exponent-matching is exactly
where models a/b/c split, so a quick self-calculation would more likely add a wrong fourth opinion than
settle it.*
