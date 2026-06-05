# Character — substrate method (how the door to real data was widened)

How a **viable real-data substrate** for the transverse-decomposition test is found and tested.
The real-data search was stymied for a long time — substrate after substrate failed (shell: a
frozen projection; Harary triad: no perturbation protocol; then a sweep of ~8 physical-device
families, all dead). This file is the method that broke that — recorded in enough detail to
re-run. It is a **method, not new physics**: it promotes nothing into canon but an instanced
result (with a receipt) or a named, runnable owed experiment.

Status: v0.1. One worked instance end-to-end (the driven colloid on a ring → `character.md` §The
cross-rule, receipts §Colloid ring transverse) plus the failure roster it was distilled from
(`character_substrate_ledger.md`).

The method has six moves. The first three are *what to look for and what to exclude*; the last
three are *how to actually land it*.

## 1. State the real requirement — affordance, not salience

A substrate carries the test iff it affords **all** of:

- **(i) a sustained protected current `𝒜`** — a circulation / time-odd flux, maintained by a drive
  (a genuine NESS, broken detailed balance), whose *strength can be varied*;
- **(ii) a metric observable `B`** — an escape rate, barrier, or relaxation/aging exponent,
  measured on the *same* system;
- **(iii) a clean separating symmetry** under which `𝒜` is **odd** and `B` is **even** (this is the
  transverse decomposition, `pa:transverse-decomposition`) — discrete (Zₙ) or topological;
- **(iv) a knob `δ`** that breaks that symmetry;

with **(v) the affinity that sets `𝒜` decoupled from the barrier that sets `B`** (two independent
inputs, not one knob doing both).

"The system *advertises* a topological/protected current" is **salience**, not affordance, and is
anti-correlated with testability (`feedback_substrate_affordance_filter`). Run the gate on the
(substrate × data-modality) pair before any hunt.

## 2. The structural law — the three ways real substrates fail

Almost every real candidate dies in one of three ways. Learn to name them on sight and exclude
them up front:

1. **No current.** Static-state memory (MRAM/MTJ, SRAM, single-domain bits) stores a *metric
   coordinate* (magnetization, voltage). Its retention-rate-vs-bias `r(δ)` data is pristine but is
   plain biased Kramers escape — there is no `𝒜`. Fails (i).
2. **Collinear current.** Current-state memory (magnetic vortices, flux qubits, bistable CW/CCW
   ring lasers) stores the bit **as the current's direction**, so the escape *is the reversal of
   `𝒜`* — current and escape are the same degree of freedom, not transverse. Fails (iii).
3. **Co-tuned current.** Single-knob driven oscillators (laser/parametric pump) crank `𝒜` and the
   barrier with one knob. Fails (v).

**The device-inversion proves its own limit.** A device that *needed* to measure `r(δ)` needed it
*because it is a memory*; a memory is bistable storage; bistable storage makes the current the bit
(collinear) or absent. So no spec-sheet `r(δ)` device can carry the decomposition — by construction.

**Corollary — `r(δ) ≠ the test.** Biased escape rate vs a bias field is universal (Kramers) and is
*not* the selection rule. The test is `∂B/∂𝒜` gated by `δ`, which needs the current as an
**independent axis** from the escape.

## 3. The two door-wideners

The search was stymied because the target was set too narrow on two axes. Relax both:

- **(a) Gate (iii) accepts a *discrete* symmetry, not only a topological invariant.** The
  framework's own passing substrates use `Z₃` (triad), CSS X/Z (surface code), `Z_N` (glass).
  Demanding a topological invariant rejects the corpus. The real gate is any clean symmetry making
  `𝒜` odd and `B` even.
- **(b) The target is the linear *selection rule*, not exact invariance.** Exact flatness ("`B`
  unchanged across the whole `𝒜` sweep") is the rare, degenerate/toy special case. The robust,
  generic target is the **forbidden linear channel**: `∂B/∂𝒜|₀ = 0` while the symmetry holds,
  reopening `∝ δ` when it breaks (`character.md` §The cross-rule). This is the move that widened the
  door most — the candidate class goes from "systems with exact invariance" (almost none) to
  "driven NESS with a transverse current and a separating symmetry" (a real class).

The door opened along the **strength** axis (linear rule, not exact flatness), **not** the
transversality axis. Requirement (iii)/(v) — a genuinely transverse current with independent
affinity — remains the binding gate. The three failure modes of §2 still exclude.

## 4. Search discipline — read primaries, exclude by mechanism, reverse the hunt

- **Read primary sources, not snippets.** External prompt-collection channels bloat and
  salience-match — they keep returning bistable-memory `r(δ)`. Agent scouts that *fetch and read the
  actual papers* are what worked (they correctly killed shell / skyrmion / quantum-Hall / vortex by
  reading the figures, and verified the colloid lead). A research prompt should **lead with the
  exclusions** (the three dead classes of §2, stated by mechanism) so the channel cannot re-propose
  them, and demand one concrete named dataset per candidate (no field-level plausibility).
- **Reverse the hunt.** Do not search fields that *advertise* protected currents (salience). Search
  the **driven-NESS class** where a sustained circulation is *geometrically distinct* from a measured
  relaxation, with a symmetry-breaking knob: driven colloids, stochastic pumps, non-Hermitian
  relaxation spectra, reaction networks with a transverse cycle. (Prompt template:
  `docs/research_prompt_driven_ness_transverse.md`.)

## 5. Generate, don't hunt — even on a real substrate

The winning move. When the real substrate **is a system you can simulate**, do not hunt its frozen
data — build its operator and compute the test, *calibrated to the real system's measured
structure*. The driven colloid on a ring **is** the glass-ring Fokker–Planck model: rather than
chase the (non-public) Bechinger trajectories, build the operator, anchor it to what they *did*
publish (the Re/Im relaxation+revolution split, Blickle 2009), and run the three moves. This
isolates the mechanism at the desk and **emits a concrete, falsifiable experiment**. Real-data
vindication still requires that experiment; the calibration is the bridge from synthetic to real
(`feedback_substrate_affordance_filter`: character lands when you *run the equations*, not when you
download a record stripped of the dynamics).

## 6. Numerical protocol for the selection rule (reproducible)

The computation that isolates the rule — `experiments/colloid_ring_transverse.py`:

1. **Operator.** Build the Fokker–Planck generator `L(f,δ)` for `ẋ = −V'(x) + f + √(2D)η` on a
   discretized ring (flux-conservative finite differences). **Validate** against the analytic free
   ring `λ_k = −Dk² − ikf` (Re = −Dk² independent of `f`; Im = −kf the current).
2. **Move 1 (orthogonality).** The slow eigenvalue is `λ₁ = Re (relaxation) + i·Im (revolution)` —
   the transverse Re/Im split, the structure the experiment measures.
3. **Threshold (Move 2).** On a ring, `f` is a *nonconservative torque* (not a single-valued tilt
   `V−fx`), so sweeping `f` at fixed symmetric potential cranks the current at **fixed barrier** —
   the unconfounded cut. Compute `c₁ = ∂Re λ/∂f|₀` by the **symmetric finite difference**
   `[Re λ(+ε) − Re λ(−ε)]/2ε`: it is machine-zero by the even-ness of `Re λ` in `f`, robust to
   degeneracy and conditioning (this is the load-bearing, symmetry-exact number — verify it as
   equivariance to machine-eps, do not sample it noisily; `feedback_demonstrate_symmetry_not_sample`).
4. **Selection rule (Move 3).** Break reflection with a ratchet `δ·sin 2x`; measure `c₁(δ)` by
   **degenerate 2×2 perturbation theory in a fixed bi-orthonormal slow-pair basis** — `c₁` from the
   `2×2` effective generator `diag(λ) + δ·M_W + f·M₁`. **Not** single-mode perturbation theory and
   **not** finite-difference-in-`f`: both leak the `O(1)` circulation coupling when the slow modes
   are near-degenerate (the symptom is a c₁ that plateaus or jumps instead of scaling).
5. **The degeneracy diagnostic (a general tell).** If the result *reshapes* when you remove an
   **accidental degeneracy** — and gets *cleaner* — you have stripped an accident and exposed the
   generic mechanism. Here: a single-harmonic ring `V₀cos x` has exactly-degenerate slow modes, `δ`
   cancels in the `c₁` ratio, and the onset collapses to a **step**; adding a second harmonic
   `V₀cos x + V₂cos 2x` (still reflection-symmetric, so the threshold is untouched) lifts the
   degeneracy and restores `c₁ = kδ + O(δ³)` — slope 1, clean over **seven decades**. A result that
   becomes more lawful under a *more generic* potential is the fingerprint of the real rule; the
   special-case toy (here, exact flatness) over-inherits epistemic weight until you perturb it.

## 7. The widened door — the resulting candidate class

With §3's two wideners + §4's discipline + §5's generate-don't-hunt, the open class is the
driven-NESS-transverse family: **driven colloids** (instanced), **stochastic pumps**,
**non-Hermitian relaxation spectra** (natively transverse — the Re/Im split is built in), and
**reaction networks with a transverse cycle** (the triad class). Each still owes the transversality
check (§1.iii/v). Still excluded by §2: collinear systems (magnetic textures, bistable memory) and
no-current systems. The door is genuinely wider — but it widened on the strength axis, not the
transversality axis.

## 8. What this is and isn't

A method, not new physics. It produces no claim that is not either an instanced result (with a
receipt) or a named, runnable owed experiment. The failure roster it was distilled from — and the
verdict on every substrate touched — lives in
[`character_substrate_ledger.md`](character_substrate_ledger.md); the structural law of §2 and the
selection-rule reframing of §3(b) are recorded there under §Structural finding and in
`character.md` §The cross-rule.
