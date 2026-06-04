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
