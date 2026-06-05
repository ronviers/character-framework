# Cross-check request — the electronic-gyrator minting instance (before we bank it)

**For the outbound channel / an independent reviewer.** We have a candidate **second real-substrate
instance** of a framework claim and want it *adversarially cross-checked before it is banked*. Please
verify or refute each point below; a clean refutation is as valuable as a confirmation.

## What we did (the claim under test)

We read a real, published, **measured** electronic NESS as an instance of "minting" — a coupling that
creates a protected circulation under a drive, from a detailed-balanced baseline.

- **System:** Chiang, Lee, Lai, Jun, *Phys. Rev. E* **96**, 032123 (2017) (arXiv:1703.10762) — two
  capacitively-coupled RC circuits; R₁ cooled in LN₂ vapor (real Johnson-noise bath T₁), R₂ at room
  temperature T₂ → a genuine NESS gyrator.
- **Measured parts used (their Sec. II):** C₁=488 pF, R₁=9.01 MΩ; C₂=420 pF, R₂=9.51 MΩ; T₂=296 K;
  T₁∈[120,296] K; coupling Cₒ∈[100 pF,10 nF].
- **Operator (their Eq. 1):** `R̂Ĉ V̇ = −V + ξ`, `R̂=diag(R₁,R₂)`, `Ĉ=[[C₁+Cₒ,−Cₒ],[−Cₒ,C₂+Cₒ]]`,
  Johnson noise `⟨ξᵢξⱼ⟩=2k_BTᵢRᵢδᵢⱼδ`. We form `M=(R̂Ĉ)⁻¹`, diffusion `D=½MΞMᵀ` with
  `Ξ=2k_B diag(T₁R₁,T₂R₂)`, solve `MΣ+ΣMᵀ=2D`, and compute the area-rate `Φ=½(MΣ−ΣMᵀ)₁₂` and the
  angular velocity `⟨φ̇⟩=∫(V×ΩV)/|V|² P_ss dV`, `Ω=DΣ⁻¹−M`.
- **Result:** from the measured parts alone the operator reproduces the paper's **measured** rotation
  curve — peak at **Cₒ=661 pF, 5.0 rev/s** (measured ~700 pF, ~5 rev/s); ⟨φ̇⟩∝ΔT, **exactly zero at
  T₁=T₂** (detailed-balance baseline, machine-zero); current is **exactly zero at Cₒ=0** even at large
  ΔT; sign is drive-locked (0/400 reciprocal-deformation flips). An independent SDE simulation (the
  paper's slope-of-φ(t) method) agrees with the closed form.

## What we need checked (be adversarial)

1. **Operator correctness.** Is `M=(R̂Ĉ)⁻¹`, `D=½MΞMᵀ` with `Ξ=2k_B diag(T₁R₁,T₂R₂)` the
   thermodynamically correct operator for this circuit? Is the equilibrium current exactly zero at
   T₁=T₂ for *any* R₁≠R₂ (it should be — verify `Σ_eq=k_B T Ĉ⁻¹` solves the Lyapunov equation)?
2. **Cross-system reproduction (the main ask).** Does the *same* method reproduce a **second,
   independent measured gyrator**? Two targets, please pull their measured parameters and measured
   gyration and check the operator-from-measured-parts reproduces them:
   - **Ciliberto/Imparato electronic gyrator** (two resistors at T₁,T₂ coupled by a capacitor; measured
     angular velocity 𝒲, torque, heat flux). Different lab, same substrate class.
   - **Colloidal Brownian gyrator** (Argun et al., *Exp. realization of a minimal microscopic heat
     engine*; a colloid in an elliptical trap with two bath temperatures; measured gyration/torque).
     **Different physical substrate** — the strongest cross-check.
3. **The hard skeptical question.** Reproducing a gyrator's measured rotation is reproducing standard
   OU gyrator theory, which is well-validated. **Does reading it as "minting" add anything, or is it
   re-labeling a known result?** Our position: the framework brings nothing new — it is a *dissipative
   reading* of an imported, measured structure, and the win is the *instance* (a real cross-substrate
   datum), not a new prediction. Is that defensible, or is the gyrator too trivial a NESS to count as
   a genuine instance of the minting claim (a 2-mode Gaussian current-only NESS, not a ≥3 frustrated
   cycle)?
4. **Any error** in the parameters, the convention (2 vs 4 k_BTR; one- vs two-sided spectra), or the
   reading.

**Return:** a verdict (CONFIRM / REFUTE / CONFIRM-WITH-CAVEATS) on each point, with the second-dataset
reproduction (computed vs measured numbers) if you can run it, and the single most important caveat we
should attach when banking.
