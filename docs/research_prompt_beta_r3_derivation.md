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
