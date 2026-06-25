# gMAM build plan — the exact instanton for `current-aids-escape` (turnkey, for a fresh session)

> **STATUS: BUILT + ADJUDICATED (2026-06-04) — verdict = KILL the barrier reading.** The minimizer is
> implemented and validated (Maier–Stein gate, gradient action `0.5000` to 0.01%). On the homochiral
> substrate the σ→0 quasipotential is **flat** in the affinity (`ΔŜ_H≈0` over `𝒜:0→21.8`, robust), so the
> committed finite-σ `ΔV` drop is the **irreversible Eyring–Kramers prefactor**, not the FW barrier — the
> protected current is *transverse* to the escape mode (symmetry-protected; exact across a μ-sweep, broken
> ∝δ by a Z₃ break) and **barred from `ΔV`** by the transverse-decomposition theorem (Graham–Haken; FW §4.3;
> Bouchet–Reygner). Selection rule confirmed in-substrate (mixing the irreps turns the barrier effect on —
> Maier–Stein). Landed: `pa:transverse-decomposition`; receipts §Branch-survival barrier; frontier
> §Tombstones `current-aids-escape`; character.md §Two tangent sectors + §The two-survivals plane.
> Experiments: `gmam_current_aids.py`, `gmam_maier_stein.py`, `gmam_saddle_orthogonality.py`,
> `gmam_affinity_scaling.py`, `gmam_orthogonality_sweep.py`, `gmam_symmetry_break_probe.py`,
> `gmam_mixing_test.py` (+ PNGs). **Open (owed):** Tier-2 Hamiltonian sgMAM to confirm invariance at
> extreme exclusion (μ≈3, past the ε-regularized Tier-1 floor). The plan below is the as-built record.

**Read this first; it is self-contained.** It tells a fresh session (no prior context) exactly what to
build, why, the precomputed anchors, the validation ladder, and the decision rules. Companion artifacts
already in the repo: `experiments/current_aids_escape.py` (the homochiral 3σ result), `..._alignment.py`
(the finding that motivates gMAM), `docs/research_prompt_current_aids_escape_interpretation.md` (3 outside
reports). Scaffold to fill in: `experiments/gmam_current_aids.py` (fields/saddle/attractor/action wired,
minimizer stubbed).

---

## 0. The one-paragraph why

We measured (committed, `12d3b0e`) that on the **homochiral** substrate the protected rotational current
**lowers** the noisy branch-escape barrier: `ΔV` (demographic Kramers MFPT) drops `0.328 → 0.272` as the
cycle affinity `𝒜: 0 → 21.8` nats, metric held to machine precision, 3σ. On the **autocat** substrate the
same protocol shows **no effect** (clean null). Three outside reports read this as a *geometric selection
rule* (current lowers the barrier iff it projects onto the escape path). But a deterministic check
(`current_aids_escape_alignment.py`) found the cheap first-order predictor is **null by symmetry**: the
rotational current `J = f(a≠b) − f(a=b)` is **identically zero on the entire escape route** (saddle,
attractor, and the deterministic heteroclinic are all uniform-within-group, even at `a≠b`; `J` lives only
*off* that subspace). So the effect is intrinsically **higher-order**: the optimal escape path (instanton)
must bend *off* the symmetric subspace into the 3-cycle directions to harvest the current. **Only the
actual instanton shows this** — hence gMAM. gMAM is *required*, not optional; there is no cheap shortcut.

## 1. What gMAM must deliver (the scientific question + decision rules)

Compute the **instanton** (minimum-action escape path) and the **quasipotential** `Ŝ` for the
attractor→saddle transition, on each substrate, at current-OFF (`a=b=0.75`) and current-ON (`a=0.5,b=1.0`),
holding `a+b=1.5`.

Three things to read off:

- **(D1) Action drop.** `ΔŜ_H = Ŝ_H(a=b) − Ŝ_H(a≠b)`. Prediction: `> 0`, reproducing the measured
  `0.328 → 0.272` (so `ΔŜ_H ≈ 0.056`, the demographic geometric action equals the Kramers `ΔV` — see §4).
  `ΔŜ_A ≈ 0` (the autocat null).
- **(D2) Instanton bending.** The current-ON instanton on H **leaves the uniform-within-group subspace**
  (within-group spread > 0 along the path) — *visibly* surfing the 3-cycle — while current-OFF stays in it
  (spread = 0). On A the ON-instanton barely bends. This is the *mechanism*, not just a correlation.
- **(D3) Why A is null.** Confirm A's null is the geometry (the bend doesn't pay: weak off-subspace current
  `|J|_off ≈ 5e-4` vs H's `2.5e-3`, plus a short interior path) — `ΔŜ_A ≈ 0` with an instanton that either
  doesn't bend or bends without lowering the action.

**Decision rules (what each outcome does to the core):**
- **Vindicate + promote** (cross into `character.md` §The two-survivals plane as a *scoped* dynamical-
  coupling caveat): `ΔŜ_H > 0` reproducing ~0.056 **and** the H instanton visibly bends off-subspace
  **and** `ΔŜ_A ≈ 0`. Then the principle is stated precisely: *the protected current is a resource for
  branch escape only via the instanton's excursion into the current-carrying (3-cycle) directions; it does
  so on the boundary-supported hard-transcritical instance and not on the interior soft pitchfork.* This is
  a forced derivation (not a 2nd noisy instance), so per the frontier `staked→promoted` gate (a
  forced-not-fitted derivation) it can cross — **scoped**, with the autocat null stated as the boundary.
- **Scope/hold**: `ΔŜ_H > 0` but the bending is ambiguous, or `ΔŜ_H` doesn't match the measured 0.056 →
  keep `[sharpening]`, record the discrepancy, do AMS as an independent check.
- **Kill the coupling**: gMAM finds `ΔŜ_H ≈ 0` (the measured MFPT drop was a prefactor/finite-σ artifact,
  not a barrier effect) → the homochiral "current-aids-escape" was not a quasipotential effect; demote and
  tombstone. (This is the real falsification risk — take it seriously; the Kramers slope is a finite-σ
  *effective* barrier, gMAM is the σ→0 truth.)

## 2. Precomputed anchors (do not re-derive)

Both substrates: 6 state vars `x = [L₀,L₁,L₂, R₀,R₁,R₂]`, fields already in the repo.

| | substrate H (homochiral) | substrate A (autocat) |
|---|---|---|
| field | `identity_survival_barrier.field_many(X, a, b)`  (F=1, μ=1.6) | `autocat_both.field(X, k1, ec, a, b)`  (k1=0.05, ec=0.15, g=.7,kd=.5,k3=1,cap=2) |
| current OFF | `a=b=0.75` | `a=b=0.75` |
| current ON | `a=0.5, b=1.0` (`𝒜≈21.8`) | `a=0.5, b=1.0` (`𝒜≈2.3`) |
| **saddle** `x_S` (symmetric) | `0.13699 · ones(6)` | `0.14343 · ones(6)` |
| **attractor** `x_A` (L-winning, *same for a=b and a≠b*) | `[0.4, 0.4, 0.4, 0, 0, 0]` (boundary, `ee=+1`) | `[0.3256,0.3256,0.3256, 0.0553,0.0553,0.0553]` (interior, `ee=+0.709`) |
| reference `ΔV` (demographic Kramers, committed) | a=b **0.328**, a≠b **0.272** | null (flip counts identical) |

Saddle/attractor finders are in the scaffold (symmetry-preserving 1D settle for `x_S`; biased settle for
`x_A`). **Note H's `x_A` has the losing hand at exactly 0** — on the orthant boundary (see §5).

## 3. Method — sgMAM (Hamiltonian form), demographic metric

**Diffusion.** Demographic (birth–death) noise: `dxᵢ = bᵢ(x) dt + σ√xᵢ dWᵢ`, so the diffusion matrix is
`a(x) = diag(x)`. (This is the metric the committed `ΔV` was measured in — §4. Additive `a=I` is a poor fit
here because the boundary attractor would admit negative populations; demographic is the physical choice.)

**Freidlin–Wentzell action** for a path `φ`:  `S_T[φ] = ½ ∫₀ᵀ (φ̇−b)ᵀ a(φ)⁻¹ (φ̇−b) dt`.
**Geometric (reparam-invariant) action** (Heymann–Vanden-Eijnden 2008), minimized over the *curve* `γ`:
```
Ŝ(γ) = ∫₀¹ ( |φ'|_{a⁻¹} · |b|_{a⁻¹}  −  ⟨φ', a⁻¹ b⟩ ) ds ,   |v|_{a⁻¹} = √(vᵀ a⁻¹ v),  φ' = dφ/ds
```
`gMAM` minimizes `Ŝ(γ)` over curves from `x_A` to `x_S` with arc-length parameterization. The minimizer is
the instanton; `Ŝ` at the minimum is the quasipotential `ΔV`.

**Use the Hamiltonian / sgMAM form (Grafke–Schäfer–Vanden-Eijnden 2017), not naive Lagrangian gMAM**, because
of the boundary (§5). Hamiltonian `H(x,p) = ⟨b(x),p⟩ + ½ ⟨p, a(x) p⟩ = ⟨b,p⟩ + ½ Σ xᵢ pᵢ²` (demographic).
The instanton is the zero-energy (`H=0`) heteroclinic of Hamilton's equations from `(x_A,0)` to `(x_S,0)`.
sgMAM evolves the discretized curve by preconditioned descent using only first derivatives of `H`; the
momentum `pᵢ` stays **finite** as `xᵢ→0` (the term `xᵢpᵢ² → 0`), so the boundary is handled gracefully —
unlike the Lagrangian form where `a⁻¹ = diag(1/xᵢ)` blows up.

**Two implementation tiers (do the first, upgrade if needed):**
- **Tier 1 (recommended start): direct minimization of `Ŝ(γ)`** by gradient descent on the `N+1` discretized
  points (numerical `∂Ŝ/∂xᵢ`, `N~100`, endpoints fixed) + arc-length reparameterization every few steps.
  Brute but easy to verify. Regularize the boundary with `a⁻¹ = diag(1/max(xᵢ, ε))`, `ε~1e-4`, and **start
  the path just off the boundary** (`x_A` with losing hand at `ε`). Report `Ŝ` vs `ε` to show convergence.
- **Tier 2 (upgrade): sgMAM** (Hamiltonian, Grafke et al.) — faster, cleaner at the boundary, no `ε`.

> **⚠ NaN / degeneracy discipline (carry this — it is the through-line of the whole `current-aids-escape`
> thread).** The rare-flip *MFPT* trap that bit the measurement phase (a censoring-contaminated estimator
> faking "ratio = 1.000") does **not** recur here — gMAM is deterministic. But the *same* discipline
> ([[nan-is-falsification-tripwire]], auto-loaded from memory) reappears in a gMAM-specific, **quieter**
> form:
> - The `ε`-floor in `a⁻¹ = diag(1/max(xᵢ,ε))` at H's boundary attractor (`loser=0`) is a **manufactured
>   excluded zero**. It returns a *finite* action that silently depends on `ε` — the memory's "quiet form:
>   a finite number near an orthogonal zero is not yet a converged number; no NaN ≠ trustworthy." **Run an
>   `ε`-convergence study (`ε, ε/2, ε/4`); `Ŝ` must converge.** If it doesn't, switch to Tier-2 (Hamiltonian,
>   no `ε`) — that is the root-cause fix, not a smaller floor. Autocat is interior, so it has no `ε` issue —
>   another reason to do A first.
> - Any **NaN/Inf in the action or gradient halts and is diagnosed** (boundary blowup, `sqrt` of a tiny
>   negative, a runaway step), never filled or skipped. The scaffold guards `sqrt(max(·,0))`; keep such
>   tripwires explicit.
> - The **stuck-in-subspace `ΔŜ=0`** is a *fake null* of the same family (a "0" that is an apparatus
>   artifact, not physics). Always confirm the converged ON-instanton has within-group spread > 0 before
>   reading any `ΔŜ`; a spread-0 ON-instanton means the seeding failed (§5.2), not that the current is inert.
> - Mirror the measurement-phase lesson if AMS is used as the §6.4 cross-check: in any rare-event sampler,
>   read clean event **counts / committors**, not censoring-contaminated MFPT.

## 4. Normalization — the precise validation target

Demographic `dx = b dt + σ√x dW` ⟹ `a = σ² diag(x)`. Then `S_T = (1/σ²)·Ŝ_geo` with `Ŝ_geo` using
`a=diag(x)`, and MFPT `~ exp(Ŝ_geo/σ²)`. The committed Kramers slope `ΔV = d ln⟨τ⟩ / d(1/σ²) = Ŝ_geo`.
**So the geometric action with `a=diag(x)` should equal the measured `ΔV` directly:**
```
Ŝ_geo,H(a=b)  ≈ 0.328      Ŝ_geo,H(a≠b) ≈ 0.272      ΔŜ_H ≈ 0.056
```
That is the validation **and** the result in one. (Caveat: the Kramers slope is a finite-σ *effective*
barrier over σ∈[0.205,0.25]; gMAM is the σ→0 limit. Expect agreement to ~10–20%, not exact. A clean
reproduction of the ~0.056 *drop* is the headline; matching absolute values to ~15% validates the metric.)

## 5. Critical implementation notes (where this system bites)

1. **Full 6D — do NOT reduce to the group totals `(S_L,S_R)`.** That reduction is exactly the
   uniform-within-group subspace where `J≡0` and the whole effect vanishes. The instanton's payoff lives in
   the within-group 3-cycle directions. Keep all 6 coordinates (or at minimum the winning group's 3 + the
   losing group's total — 4D — but 6D is safest).
2. **Seed the initial path OFF the symmetric subspace.** Saddle, attractor, and heteroclinic are all
   uniform-within-group, and the dynamics preserve that subspace, so it contains a *symmetric critical
   point* of the action (the current-blind path). If you initialize in-subspace, the minimizer stays stuck
   there and misses the lower-action bent instanton. **Initialize with a small within-group asymmetry**
   (e.g. perturb the straight line `x_A→x_S` by a 3-cycle mode `[1,−0.5,−0.5]` on the winning group, amp
   ~0.05) so descent can roll into the bent instanton. Verify the converged ON-instanton has within-group
   spread > 0; the OFF-instanton should converge back to spread = 0.
3. **Boundary attractor on H (`loser = 0`).** Demographic `a⁻¹` is singular there. Use the Hamiltonian form
   (Tier 2) *or* the `ε`-regularization + off-boundary start (Tier 1), and report `ε`-convergence. A is
   interior (no issue) — **do A first** (§6).
4. **Saddle is a rank-1 saddle** (one unstable direction = the uniform breaking mode, `λ_u`: H +0.315, A
   +0.049). The instanton ends at the saddle along its stable manifold. Standard gMAM endpoint handling.

## 6. Validation ladder (in order — don't skip)

1. **Maier–Stein 2D (additive, published instanton).** Implement gMAM, reproduce the known Maier–Stein
   instanton + action (Heymann–VE 2008 give numbers). Confirms the minimizer + action evaluator are correct
   *before* trusting any homochiral number. (Pure code-correctness gate.)
2. **Autocat A, demographic, interior.** Easier real case (no boundary degeneracy). Expect `ΔŜ_A ≈ 0` and an
   ON-instanton that barely bends — reproducing the measured null. Validates the demographic metric + the
   off-subspace seeding on the *easy* geometry.
3. **Homochiral H, demographic, boundary.** The main event. Expect `Ŝ(a=b) ≈ 0.328`, `Ŝ(a≠b) ≈ 0.272`,
   `ΔŜ_H ≈ 0.056`, and the ON-instanton visibly bending off-subspace. Report `ε`-convergence (Tier 1).
4. **(optional cross-check) AMS** (adaptive multilevel splitting) on H for an independent rate estimate
   seeded by the gMAM instanton — the reports' recommended trustworthy-null tool. Only if Tier-1/2 leave
   doubt.

## 7. Deliverables (what the gMAM session produces)

- A figure per substrate: the ON vs OFF instanton (projected to `(m, within-group-spread)` and to a 3-cycle
  plane), showing the bend; and the action bars `Ŝ(a=b)` vs `Ŝ(a≠b)`.
- The numbers: `Ŝ_H(a=b), Ŝ_H(a≠b), ΔŜ_H` vs the measured `0.328/0.272/0.056`; `ΔŜ_A`.
- Then the **held** doc updates land (per §1 decision): frontier `current-aids-escape` (→ promoted/scoped or
  demoted), receipts §Branch-survival barrier (the mechanism: instanton excursion harvests the current),
  and — if vindicated — the scoped `character.md` §The two-survivals-plane caveat. Update this plan's status
  + the handoff.

## 8. Risks / fallbacks

- **gMAM says `ΔŜ_H ≈ 0`** (the measured drop was a prefactor/finite-σ artifact): a real possibility and a
  clean falsification — the Kramers slope is finite-σ. If so, demote and tombstone honestly. AMS would
  confirm.
- **Boundary `ε`-sensitivity** on H: if Tier-1 `Ŝ` doesn't converge in `ε`, switch to Tier-2 (Hamiltonian)
  which removes `ε`.
- **Minimizer stuck in-subspace**: symptom is `ΔŜ_H = 0` with spread-0 instanton even ON — fix by stronger
  off-subspace seeding / a symmetry-breaking nudge during descent (§5.2).
- **Scope creep**: the goal is the H-vs-A `ΔŜ` + the bend. Resist building a general FW solver; bespoke
  6D-demographic sgMAM for these two operating points is enough.

## 9. Literature anchors (from the reports)

- **Heymann & Vanden-Eijnden (2008)**, *Geometric minimum action method* — gMAM algorithm + Maier–Stein
  validation numbers.
- **Grafke, Schäfer & Vanden-Eijnden (2017)**, simplified gMAM (sgMAM) — first-derivative-only, Hamiltonian
  form (use for the boundary).
- **Maier & Stein (1993/1997)** — non-gradient escape, instanton "bows out" to exploit the solenoidal field
  (the qualitative picture we're confirming).
- **Bouchet & Reygner (2016)** — Eyring–Kramers for irreversible diffusions (prefactor, if we need absolute
  rates).
- **Ping Ao (2004)** — gradient + divergence-free decomposition of the drift (the `b = −∇U + J` split).

## 10. Scaffold

`experiments/gmam_current_aids.py` ships with: both fields, the saddle finder (symmetry-preserving 1D),
the attractor finder, the off-subspace-seeded initial path constructor, and a **Tier-1 geometric-action
evaluator `S_hat(path, metric)`** (un-validated — validate against Maier–Stein first per §6.1). The
**minimizer is stubbed** with the descent+reparam loop spelled out in comments. First task next session:
§6.1 (Maier–Stein), then implement the minimizer, then §6.2 (A), §6.3 (H).
