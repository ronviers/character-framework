# Outside-interpretation prompt — when does a rotational current lower a noise-induced escape barrier?

Self-contained dynamical-systems / large-deviations question for the outbound research channel. No
framework jargon by design — any strong applied-math / stochastic-dynamics model should be able to
engage. The returned report gets filed alongside and folded (after review) into
`character_frontier.md` (`current-aids-escape`) + `character_receipts.md` §Branch-survival barrier.

**Background it bears on.** An earlier round of this channel (`review_prompt_competitive_exclusion.md`)
analyzed a symmetric two-group competition model and *predicted*, for the non-gradient (current-carrying)
case, that "the optimal fluctuation path (the instanton) takes a curved trajectory that surfs the
rotational flow of the internal cycle, drastically reducing the action required to cross the saddle"
(i.e. the Freidlin–Wentzell barrier `ΔV` should fall as the internal current rises). We have now **tested
that prediction on two different substrates and gotten opposite answers** — confirmed on one, a clean null
on the other. We want help interpreting the *regime-dependence*, which may be the substantive finding.

---

## The phenomenon: a protected rotational current that lowers the escape barrier on one substrate but not another

I study driven-dissipative systems that are bistable under a spontaneously broken ℤ₂ symmetry: two
symmetry-related attractors (call the order parameter `m ∈ [−1,1]`, attractors at `±m*`) separated by a
symmetric saddle at `m = 0`. Each attractor also carries an **internal rotational current** — a
non-reciprocal cyclic flow (an asymmetric 3-cycle, strength set by an antisymmetry `a ≠ b`) that makes the
drift non-gradient. I can dial the current on/off *without changing the deterministic landscape* (see the
control below), and I measure how the **noise-induced escape barrier** `ΔV` (the L↔R basin crossing, by
Kramers/Freidlin–Wentzell first passage) depends on the current.

**Two substrates, same protocol, opposite results.**

### Substrate H — hard transcritical / competitive exclusion (boundary-supported attractors)

Six variables, two symmetry-related groups of three (`L`, `R`), each an internal asymmetric 3-cycle,
coupled by mutual inhibition through group totals:
```
dLᵢ/dt = Lᵢ ( F − [ Lᵢ + a·Lᵢ₊₁ + b·Lᵢ₋₁ ] − μ·S_R )
dRᵢ/dt = Rᵢ ( F − [ Rᵢ + b·Rᵢ₊₁ + a·Rᵢ₋₁ ] − μ·S_L )
```
`F=1`, `μ=1.6`, `a+b=1.5`. Above `μ_c=(1+a+b)/3` the symmetric state loses stability and the order
parameter jumps essentially to **full exclusion** `m* = ±1` (winner-take-all; the attractors sit on the
boundary of the positive orthant). The internal current is strong.

### Substrate A — soft supercritical pitchfork (interior attractors)

A Kondepudi–Nelson autocatalytic substrate (autocatalysis + finite-resource saturation + mutual
annihilation), again two mirror groups of three with an internal asymmetric 3-cycle of strength `ec`:
```
dLᵢ/dt = k₁ + (g−k_d)·Lᵢ·(1 − P/cap) − k₃·Lᵢ·S_R − ec·Lᵢ·(a·Lᵢ₊₁ + b·Lᵢ₋₁)     (P = S_L+S_R)
dRᵢ/dt = k₁ + (g−k_d)·Rᵢ·(1 − P/cap) − k₃·Rᵢ·S_L − ec·Rᵢ·(b·Rᵢ₊₁ + a·Rᵢ₋₁)     (mirror)
```
`g=0.70, k_d=0.50, k₃=1.0, cap=2.0, ec=0.15, a+b=1.5`. Here the symmetry breaks via a genuine
**supercritical pitchfork** (`m*² ∝ (k₁c−k₁)` linear; barrier `∝ m*⁴` quadratic), and the broken
attractors sit in the **interior** (`m* ≈ ±0.71`). The internal current is weak.

**The control (identical logic on both).** The internal cycle term `ec·(a·next + b·prev)` splits into a
symmetric part `∝ (a+b)` and an antisymmetric part `∝ (a−b)`. The antisymmetric part is the
divergence-free rotational current; the symmetric part contributes to the competition/saturation. Holding
`(a+b)` (and `ec`) fixed and dialing only `a−b` therefore changes **only the current**, leaving the
deterministic landscape fixed. I verify this directly: the racemic saddle's symmetry-breaking eigenvalue
(substrate H) and the full `m*(k₁)` pitchfork curve (substrate A) are **invariant to machine precision**
across the `a−b` sweep. So the only thing changing is the rotational current.

I quantify the current by the **cycle affinity** `𝒜` (nats per cycle) of the winning attractor — a
deterministic, noise-independent property of the drift, read from the winner's Jacobian in the rotation
plane (rotational-OU frame; `𝒜 = 0` when the relevant eigenvalues are real, i.e. no rotation). The escape
barrier `ΔV` is read from the noise-activated mean first-passage time, demographic (√x, birth–death) noise,
via `ln⟨τ⟩ = const + ΔV·(1/σ²)` (slope = `ΔV`); in the rare-flip regime I read the escape **rate by flip
count** rather than MFPT, because the MFPT estimator is contaminated by walkers censored at the simulation
horizon when flips are rare.

**Results.**

| substrate | mechanism | attractor `m*` | current `𝒜` range | escape barrier vs current |
|---|---|---|---|---|
| **H** (transcritical) | hard / boundary | `±1.0` (full exclusion) | `0 → 21.8` nats | `ΔV` **falls monotonically**, `0.328 → 0.295 → 0.284 → 0.272` (3.0σ, R²>0.99); barrier highest at `𝒜=0` |
| **A** (pitchfork) | soft / interior | `±0.71` | `0 → 2.3` nats | **no effect**: flip counts identical within Poisson across the whole activated window (2→127 / 1000), `𝒜=0` and `𝒜=2.3` indistinguishable |

So on **H** the rotational current demonstrably **lowers** the FW escape barrier (the predicted
instanton-surfing effect, confirmed at 3σ with the deterministic landscape held fixed). On **A** the same
protocol shows **no detectable effect** — and not merely because `𝒜` is smaller: if H's per-nat
sensitivity (`≈0.0026` in `ΔV` per nat) applied to A's `Δ𝒜 = 2.3`, the predicted barrier drop would give a
**~10× excess escape rate** at the measured noise level, whereas the observed excess is ~0 (≲0.3σ).

**The three confounds (I cannot separate them with these two substrates).** H and A differ simultaneously in
(i) **bifurcation/normal-form type** — hard transcritical vs soft supercritical pitchfork; (ii) **attractor
geometry** — boundary face (`m*=±1`, on the orthant boundary, escape path is long and runs along/near the
boundary) vs interior (`m*=±0.71`, escape path is short and interior); (iii) **current magnitude** —
`𝒜≈21.8` vs `≈2.3` nats.

---

## Questions

1. **Is current-assisted escape expected to be regime-dependent like this?** Is the lowering of the FW
   quasipotential by a solenoidal (divergence-free) drift component a *generic* feature of non-gradient
   bistable escape, or does it require a specific geometric condition — e.g. that the rotational flow be
   **aligned with the unstable direction of the escape (instanton) path**? My intuition is that on H the
   boundary-supported, full-exclusion escape path runs in a direction the 3-cycle current can "push along,"
   whereas on A the short interior path may be nearly orthogonal to the current, so the solenoidal part
   does little. Is there a principled statement of *when* a rotational current aids vs is irrelevant to
   basin escape?

2. **Is there a controlling dimensionless group?** Should the size of the effect scale with the current
   relative to the gradient/relaxation drift (a Péclet-like ratio), so that A's `𝒜≈2.3` is simply below the
   threshold where the instanton meaningfully tilts? If so, what is the right dimensionless combination,
   and roughly where is the crossover? (I want to know whether A's null is "structural" — the geometry
   forbids it — or "sub-threshold" — the current is just too weak.)

3. **How would you disentangle the three confounds cleanly?** Can you suggest a *single* substrate or a
   parameter family in which I can vary one feature at a time — e.g. move the attractors continuously from
   the boundary (`m*→1`) into the interior at fixed current and fixed bifurcation type, or hold geometry
   fixed and sweep the current through the suspected crossover? What is the minimal model that isolates the
   geometric-alignment hypothesis from the current-magnitude hypothesis?

4. **Optimal-path diagnostics.** Short of a full quasipotential solve, is there a cheaper diagnostic that
   predicts the sign/size of the effect from the deterministic data alone — e.g. the angle between the
   rotational drift `J` and the minimum-action (instanton) tangent along the escape path, or the
   antisymmetric part of the drift's Jacobian projected onto the saddle's unstable manifold? I will likely
   compute the instanton via gMAM on H (to get the exact barrier and *see* the path tilt with the flow);
   what should I measure on A to confirm whether the path is simply insensitive to its (weak) current?

5. **Rare-event estimator.** In the rare-flip regime my flip-count readout is robust but low-resolution.
   For pinning a *small* barrier difference between two nearly-identical systems (the A case), what is the
   right tool — adaptive multilevel splitting / forward-flux sampling, transition-path / committor methods,
   or direct gMAM action differences? I want a method whose null ("no barrier difference") is trustworthy,
   not just an underpowered MFPT.

6. **Literature anchors** for: the role of the antisymmetric/solenoidal drift component in the
   Freidlin–Wentzell quasipotential and when it lowers vs raises the barrier (Maier–Stein geometry of the
   optimal escape path; Bouchet/Reygner; Vanden-Eijnden/Heymann gMAM); current-assisted vs current-opposed
   noise-induced transitions in NESS; and any results on escape from boundary-supported (competitive
   -exclusion) attractors vs interior attractors.

---

<!-- returned model reports get pasted below this line, as model a / model b / model c -->
