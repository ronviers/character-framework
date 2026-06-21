# Identification/derivation prompt — is the leading second-order nonequilibrium response coefficient a *geometric curvature*?

Self-contained nonequilibrium-statistical-mechanics / differential-geometry question for the outbound research
channel. **No domain jargon by design** — any strong stochastic-thermodynamics, response-theory, geometric-phase,
or singularity-theory model should engage cold. **The goal is identification, then a forced derivation** (or a
clean negative). We have a measured second-order response coefficient and one question: is it *universally* a
**geometric curvature** of some natural manifold, or *merely the leading analytic Taylor coefficient* of the
response with no geometric content? We want the **named established result + the precise manifold the curvature
lives on**, so we can import it — or a clear "it is only analytic," which is equally usable.

The returned report is folded (after review) into `character_frontier.md` · `curvature-as-coupling-bias` +
`character_receipts.md` (§"Local geometry's coupling role, bounded"). It either promotes the geometric reading
or retires it to the safe analytic form.

---

## 0. The setup (plain)

A driven, dissipative stochastic system sits in a nonequilibrium steady state (NESS). A single scalar
**`𝒜 ≥ 0`** measures how far it is driven from equilibrium — the **cycle affinity** (the steady entropy-
production driving parameter): `𝒜 = 0` is equilibrium / detailed balance; `𝒜 > 0` adds a steady **circulating
(solenoidal) probability current**. The drift splits

```
b(x) = −a(x) ∇V(x)  +  𝒜 · l(x) ,     ⟨l, ∇V⟩ = 0   (the current transverse to the gradient)
```

so the relaxational ("metric") part is the gradient `−a∇V` and the circulating ("topological") part is the
transverse field `𝒜·l`. A known, exact fact (the part we already have): the circulation `𝒜` is **barred from
the leading large-deviation observables** of the gradient sector — the Freidlin–Wentzell quasipotential / escape
barrier `ΔV` is *invariant* under `𝒜` (the transverse term cancels in the Hamilton–Jacobi equation; Graham–Haken;
Freidlin–Wentzell §4.3). The circulation reaches those observables **only at the prefactor** (the irreversible
Eyring–Kramers rate; Bouchet–Reygner), and the **leading symmetry-allowed coupling** between the circulation and
a relaxational observable is **second order, `O(𝒜²)`** (the `O(𝒜¹)` term is forbidden by the `𝒜 → −𝒜`
time-reversal/parity of the relevant scalar).

So near `𝒜 = 0`, a relaxational observable `O` (a transition rate, a branch occupancy, a susceptibility)
expands as

```
O(𝒜) = O(0) + κ · 𝒜²  +  O(𝒜⁴) ,
```

and **`κ` is the object in question.** It has been **measured** on a concrete substrate (a colloidal particle in
a driven toroidal optical trap — the Bechinger/Seifert ring; `ẋ = −V'(x) + f + √(2D)·η`, the nonconservative
torque `f` playing the role of `𝒜`); the measurement gives a finite `κ`. What is **not** established is whether
`κ` is a **geometric curvature**.

## 1. The question

**Is `κ` — the leading symmetry-allowed second-order response coefficient — universally (model-independent) a
geometric curvature of a natural manifold, or merely the leading analytic Taylor coefficient of the response?**

By "geometric curvature" we mean `κ` is, *forced and substrate-independent*, one of (or provably equivalent to):
- a **Hessian / sectional curvature of the Freidlin–Wentzell quasipotential** at the relevant saddle (the
  escape-prefactor geometry);
- a **curvature of a thermodynamic / response manifold** — a Ruppeiner/Weinhold-type metric, or its NESS
  generalization (the Mandelstam–Sivak/Crooks friction/response tensor), whose scalar/sectional curvature is `κ`;
- a **geometric-phase / Berry curvature** of the cyclic NESS (the Sinitsyn–Nemenman geometric-pumping curvature;
  the Berry curvature of the slow driven manifold);
- a **curvature of the non-Hermitian spectral sheet** near an exceptional point (the eigenvalue Riemann-surface
  curvature / Petermann-factor geometry), if the relevant degeneracy is an EP;
- a **curvature of the universal-unfolding surface** of the underlying codim-1 bifurcation (singularity theory —
  Thom/Arnold/Golubitsky–Schaeffer): `κ` as the second fundamental form of the unfolding at the seam.

Our working hypothesis is that one of these holds and that they coincide near the seam; we want it **confirmed
and named**, or **refuted**.

## 2. Tasks (be specific; cite)

1. **Name the result, or state there is none.** Is there an established theorem giving the leading second-order
   nonequilibrium response coefficient `κ` as a geometric curvature, *model-independently*? If yes: the theorem,
   its hypotheses, the **explicit manifold and curvature** (which metric, which connection, scalar vs sectional),
   and the canonical reference. If no single result exists, say which of the candidate geometries (§1) `κ`
   *does* equal under stated conditions, and where the universality fails.
2. **Which manifold — state-space or parameter-space?** Distinguish sharply: is the curvature on the **state
   space** (the quasipotential / Fokker–Planck geometry at a fixed operating point) or on the **parameter /
   control space** (a bifurcation/response manifold as couplings are swept)? These are different objects that
   both go critical near a threshold; do **not** conflate them. State which one carries `κ`.
3. **The forced derivation (if it exists).** For the transverse-split drift `b = −a∇V + 𝒜 l` (`⟨l,∇V⟩ = 0`),
   derive `κ = ∂²O/∂𝒜²|₀` for a representative relaxational observable `O` (an irreversible Eyring–Kramers rate,
   or a stationary-distribution susceptibility) and exhibit it **as** the chosen curvature — forced from the
   structure, not fitted. Give `κ` in closed form in terms of `V`, `a`, `l` at the saddle.
4. **Falsifiable check against the colloid.** State the explicit prediction the geometric identification makes
   for the driven-ring colloid (the nonconservative torque `f` as `𝒜`): the value/scaling of `κ` that the
   curvature formula yields, so we can test it against the **measured** `κ`. If the identification is real, the
   curvature formula must reproduce the measurement; if `κ` is only analytic, the formula will not be forced.
5. **The single importable statement — or the negative.** Distil to one citable proposition: either *"the
   leading `O(𝒜²)` response coefficient is the [named] curvature of [named manifold] [Author, Year, Thm N]"*
   (with hypotheses + the colloid check), **or** *"`κ` is the leading analytic response coefficient; no
   universal geometric-curvature identification holds (it is geometric only case-by-case / gauge-dependent)."*
   A clean negative is a fully acceptable, expected outcome — say so plainly if that is the truth.

## 3. Constraints / what makes a report unusable

- **Forced, not fitted.** A curvature obtained by fitting the measured `κ` to *some* curvature is exactly the
  failure we are guarding against — that is "merely analytic, dressed up." The identification must come from a
  named structure and *then* be checked against the measurement.
- **Modulates, not governs.** Whatever `κ` is, it sits at the **prefactor** — it cannot move the leading
  large-deviation barrier `ΔV` (which is `𝒜`-invariant by the transverse theorem). Any claim that local
  curvature *governs* (not merely biases) the rate is wrong and disqualifies the report.
- **State which geometry.** A report that leaves state-space vs parameter-space ambiguous, or silently bridges
  the two, is unusable (Task 2 is load-bearing).
- **Be honest about a negative.** If `κ` is generically just the leading analytic coefficient, say so — that
  retires a frontier conjecture cleanly, which is a result, not a disappointment.

---

<!-- returned model reports get pasted below this line, as model a / model b / model c -->
----
