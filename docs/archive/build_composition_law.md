# Build brief — is minting a monoidal/fusion product? (the composition law)

The import-hunt is closed: three outbound passes returned a clean negative — there is **no established,
model-independent classifying structure** under which `sign(𝒜)` is a universal invariant (receipts
§Universal-invariant classification; returns in `docs/universal_invariant returns.md`). The deformation /
shared-classifying-space framing is obstructed (a 3-state chemical cycle and a colloid ring carry the same
`sign(𝒜)` but live in different state spaces). **What survived** is that the per-substrate invariant is real
and named (Polettini gauge-cohomology + Harary balance). **The residue — the live make-or-break — is a
composition law:** universality, if it exists at all, is not a shared space but a *product on characters*. All
three passes agree the literature has **no** monoidal/fusion/cobordism algebra of protected circulations. This
brief builds and tests the candidate the framework already owns.

This is Phase C of [`roadmap_universal_invariant.md`](roadmap_universal_invariant.md), **re-aimed**: Phase B's
deformation/transfer test is dropped (obstructed); this composition test replaces it. The colloid experiment
(the superselection premise) still runs in parallel.

---

## The candidate

The framework already derived a composition law (core §Composition; `selective-coupling-class`): coupling two
characters `A`, `B` through a coupling field `Γ_AB` mints a union character whose protected bit is the
**union-cycle holonomy**

```
𝒜_union = ∮ (l_A + l_B + Γ_AB) · dx  =  ∮ Γ_AB · dx     (when the parts do not circulate).
```

The signature property: **minting two non-circulating parts yields a circulating union** — `0 ⊗ 0 → 1`. So the
product is **not** a ℤ₂ group sum of the factors' bits; the new generator is the **coupling edge**, supplied by
`Γ_AB`. That non-triviality is exactly what a genuine fusion/monoidal structure would look like, and exactly
what the literature lacks.

The question this brief settles: **is that product a genuine monoidal/fusion structure, and is it the same
structure across substrates?**

---

## What "a genuine structure" requires (the axioms to check)

1. **Well-defined product.** `sign(𝒜_union)` is determined by `(A, B, Γ_AB)` — computable from the parts plus
   the coupling, via the union graph's cycle space (Schnakenberg/`pa:gauge-thermodynamics`), not by fitting the
   measured composite.
2. **Non-trivial unit.** The uncoupled pair (`Γ_AB = 0`) is the unit (it mints nothing); a non-zero coupling
   supplies the new generator (`0 ⊗ 0 → 1`). Verify the unit law and that the product genuinely adds cycle-space
   rank, rather than reducing to a relabeling.
3. **Associativity.** Couple three parts: `(A ⊗ B) ⊗ C` vs `A ⊗ (B ⊗ C)`. The union character must be
   independent of coupling order (on a graph, `H₁` of the union is order-free — so associativity is *expected*;
   the test is whether the physical minting honors it, including sign).
4. **Substrate-independence (the bar).** The **same** composition rule must hold across the banked minting
   instances — the fuel-driven DNA reaction network, the electronic/colloidal Brownian gyrators, the cell-free
   repressilator. If minting composes by one rule in chemistry and a different rule in the gyrator, there is no
   universal structure.

(Optional, if 1–4 hold: symmetry `A ⊗ B = B ⊗ A` → symmetric monoidal; a coalescence/annihilation partner to
minting → a fusion ring.)

---

## The test (runnable; synthetic = calibration)

For each banked instance:

1. Write the part(s) and the coupling as a signed/oriented graph; compute `sign(𝒜)` of each part and of the
   union from the union graph's cycle space (the forced rule), **before** looking at the composite's measured
   sign.
2. Check the rule **predicts** the composite's `sign(𝒜)` (forced-not-fitted).
3. Build a 3-part coupling and check **associativity** (sign-exact, order-independent).
4. Repeat across ≥3 substrates and check the **rule is identical** (the same map from `(parts, coupling)` to
   `sign(𝒜_union)`).

Code lands in `experiments/composition_law_*.py`, one per substrate + a cross-substrate comparator.

---

## Pre-registered decision rules

- **↑ (fires the frontier `universal-invariant-classification`):** the product is well-defined, unital,
  associative, and the **same rule** holds across ≥3 substrates, forced-not-fitted → minting is a genuine
  (symmetric monoidal / fusion) structure → **character is a physical category** (a third independent
  description), crosses the line. Core edit at the safe altitude; receipt as the proof shard.
- **✗ (the metaphor-verdict, earned):** the composition is substrate-specific — minting obeys no consistent
  cross-substrate rule, or fails associativity/unitality → character is a powerful organizing lens, not one
  category. Record the negative; retire the universal claim to the per-substrate invariant (which stands).

---

## Discipline tripwires

- **Forced, not fitted.** The composition rule must come from the union graph's cycle space / Schnakenberg
  network theory, *then* be checked against the measured composite sign. A rule reverse-engineered to reproduce
  the instances is the failure mode.
- **Substrate-independence is the whole point.** A rule that holds only within one substrate family confirms the
  negative.
- **The signed-graph categorical product ≠ physical coupling** (the returns' caution): Zaslavsky's switching
  classes have a categorical product, but it does not obviously correspond to coupling two physical systems. The
  build must *derive* the physical minting (union holonomy) and check whether it matches a known categorical
  structure — not assume it does.
- **ℤ₂, sub-integer.** The bit is a sign; do not smuggle in integer/winding structure (the gauge group is
  `(ℝ⁺,×)`, non-compact).
- **State space, not parameter space.** The classification lives on the state-space graph; do not bridge to
  parameter-space (Berry/bifurcation) structure silently.
- **Synthetic = calibration.** Running the rule on the banked instances calibrates *whether the structure
  holds*; it is not vindication of character. The load-bearing output is the math fact (is the product a
  monoidal/fusion structure), which is substrate-general if it holds.

---

## The import to attempt alongside

If 1–4 hold, the natural named homes (to ask the channel, or to check directly) are: **signed-graph
homomorphisms / categorical product** (Zaslavsky), an **operad / PROP** of couplings, or a **fusion ring**. The
returns found none of these established for protected circulations — so a positive build here would be the
framework's *own* importable structure, not a borrowed one. That is the "becomes mathematics" outcome.
