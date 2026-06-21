# Handoff — close out the last two derivation-promotable frontier entries

Turnkey for a fresh session. Two entries remain from the "promotable by a forced derivation" set
(`chiral-rotor-triad`, `curvature-as-coupling-bias`). One is essentially **already done elsewhere** and
needs a **sync**; the other needs the **outbound derivation** (prompt:
[`research_prompt_curvature_as_coupling_bias.md`](research_prompt_curvature_as_coupling_bias.md)). Read this,
then do §1 (cheap, no external input) and §2 (uses the returns).

---

## §1 — `chiral-rotor-triad`  → cross to `battery` (a SYNC, not new work)

**The owed `↑`:** the propeller coefficient `C` computed (a Stokes boundary integral — nonzero guaranteed by
Clebsch–Gordan `2⊗3⊃1`) **+** the drive-sweep / chirality-flip run synthetically → `battery`.

**It is already done in the Triskele build (`H:\triskele\`, `github.com/ronviers/character-triskele`).** Do
not recompute from scratch — read it and sync:

- `H:\triskele\results.json` — `C23 = 3.42` (the propeller coefficient, **nonzero**), reciprocity error
  `C_recip_err ≈ 1.6e-13` (the instantaneous Stokes mobility is reciprocal — the non-reciprocity is
  drive-generated, not bare-mobility), a convergence table (BEM `n = 400…2000`), and the **activation sweep**
  `Lz(Δφ)` peaking at the ring orientation `Δφ = 2π/3` (zero at `Δφ = 0`).
- `H:\triskele\HANDOFF.md`, `WRITEUP.md`, `DERIVATION_PROMPT*.md` (three external passes, adjudicated — the
  "Race" reports), `stokes.py` / `stresslet.py` / `ring.py` / `chirality.py` / `self_assembly.py`.

**The three kill-switches (the entry's ✗) all PASS:** `C ≠ 0` (3.42); the sign is **parity-locked, not
drive-locked** (flips under `δ → −δ`, the achiral point `δ = 0, π`; invariant under drive direction); the
shape is **genuinely chiral** (a chiral-symmetry-measure check, not mere inversion-asymmetry).

**The one nuance to record (do not skip it):** the **deterministic** phase-reduced (Kuramoto) triad
**phase-locks** — it does *not* deterministically circulate. The parity-locked protected current is
**noise-activated**: stochastic hopping around the three symmetry-broken configurations
`A-leads → B-leads → C-leads`. The kill-switches pass on that **stochastic** current. State this plainly —
the protection lives in the affinity/graph-flux sign of the hopping current, not in a deterministic limit
cycle (consistent with `pa:cycle-affinity` and the framework's "current = a hopping, not a wheel" readings).

**Job (no outbound input needed):**
1. Skim Triskele (`results.json` + `HANDOFF.md` + `self_assembly.py`); re-run one verification if you want the
   numbers in-hand (the BEM `C` + the `Δφ` activation + the `δ → −δ` flip).
2. Update `character_frontier.md` · `chiral-rotor-triad`: the `↑` has **fired** (C computed nonzero,
   parity-locked, drive-swept, all three ✗ cleared) → **crosses to `battery`** (synthetic = calibration; the
   *physical build* remains the separate downstream gate that feeds `chirality-protection`'s real-substrate
   instance — keep that owed). Record the noise-activated-hopping nuance.
3. Append a receipt to `character_receipts.md` (§Real-substrate instances or §Chirality protection): the
   Triskele BEM `C = 3.42`, reciprocity-exact, `Δφ = 2π/3`-activated, parity-locked-not-drive-locked,
   noise-activated hopping — **calibration** (a buildable mechanical instance), citing `H:\triskele`.
4. **Discipline:** synthetic = calibration, never vindication (`project_killshot_synthetic_is_imported_math`);
   the BEM/Stokeslet result is imported fluid mechanics read through the protected-sign lens, nothing new.
   This crosses to `battery`, **not** across the line — the line still wants the physical build.

---

## §2 — `curvature-as-coupling-bias`  → settle the one open leap (uses the outbound returns)

**The owed `↑`:** a **forced-not-fitted derivation** identifying the surviving `O(𝒜²)` coefficient with a
**geometric curvature universally** (not case-by-case), *or* a second real-substrate instance → `battery`.

**Where it stands (read first):** `character.md` §Motion and proximity ("**Local geometry, bounded**") +
`character_receipts.md` §"Local geometry's coupling role, bounded" + §"Colloid ring transverse". The standing,
*safe* claim (already core): local geometry — the quasipotential-saddle Hessian (escape prefactor), the
spectral-sheet curvature (EP onset), or the **leading symmetry-allowed `O(𝒜²)` response coefficient** —
**modulates** how strongly the metric and topological sectors communicate (branch occupancy, transition rates)
but does **not generate** the protected circulation (existence = global frustrated topology, protection = cycle
affinity). The verb is *modulates*, not *governs* (the rate is barrier-dominated; local curvature reaches only
the Eyring–Kramers prefactor — the `current-aids-escape` tombstone / the transverse-decomposition theorem).

**The open leap (the *only* thing owed):** the driven colloid (Bechinger toroidal trap; receipts §Colloid ring
transverse) **measures** the surviving `O(𝒜²)` coefficient — but does **not certify it geometric**. Is that
coefficient *universally a geometric curvature* (a Hessian / a reduced-manifold or spectral-sheet or
unfolding-surface curvature), or *merely the leading analytic Taylor coefficient* of the response with no
geometric content?

**The route this session opened (the `seam-classification` lens):** read the `O(𝒜²)` coefficient as the
**curvature of the codim-1 unfolding** at the seam (equivalently the quasipotential-saddle Hessian / the
spectral-sheet curvature near the EP). The outbound prompt asks whether an established result *forces* that
identification, universally. **Use the returns the user brings back**, then:

**Decision rules (pre-registered):**
- **(↑ fires)** if the returns establish — *forced, named import, substrate-independent* — that the surviving
  `O(𝒜²)` coefficient **is** a geometric curvature (e.g. a thermodynamic-geometry / Ruppeiner curvature, a
  geometric-phase / Berry curvature of the cyclic NESS, the FW quasipotential Hessian, or the singularity
  unfolding's curvature), **and** it checks numerically against the colloid's measured coefficient → cross to
  `battery`; a tight sharpening of `character.md` §Motion and proximity ("Local geometry, bounded" → "…is a
  geometric curvature [Author], not merely analytic"). Receipt that same session.
- **(✗ fires — also a clean result)** if the returns show the coefficient is **merely the leading analytic
  coefficient** with no universal geometric meaning (geometric only case-by-case / gauge-dependent) → **drop
  "curvature"**: the claim reduces to its already-safe form ("the leading allowed coupling is a second-order
  response coefficient"). Record the negative; retire the frontier entry to the safe core statement. *A clean
  negative is the expected-quality outcome here (`feedback_prepared_for_invalidation`); do not soften it.*

**Discipline tripwires (carry these):**
- **Parameter-space vs state-space (the logged caveat):** the gallery's connectedness-boundary "saddle" is a
  *parameter-space* bifurcation; the quasipotential saddle is *state-space*. Both go critical → high
  susceptibility, but they are **not the same object** — do not let the returns bridge them silently. State
  which manifold the claimed curvature lives on.
- **Forced, not fitted:** a curvature obtained by fitting the colloid's measured coefficient to *a* curvature
  does **not** meet the gate — that is the "merely analytic, dressed up" failure. The identification must come
  from the structure (a named theorem), then be *checked* against the colloid, not derived from it.
- **Modulates, not governs:** whatever the answer, the coefficient still only reaches the **prefactor** — it
  cannot generate or flip the protected sign (that is the transverse theorem + the just-survived kill,
  `experiments/kill_protected_sign.py`). Any return that has local curvature *governing* the rate is wrong.

**Job:** (1) run the prompt below (or use the user's prepared returns); (2) extract the candidate
identification + its named import; (3) **check it numerically** against the colloid's measured `O(𝒜²)`
coefficient (`experiments/colloid_ring_transverse.py`); (4) fire ↑ or ✗ per the rules; (5) fold (frontier +
receipts; a core sharpening only if ↑ and only at the safe altitude).

---

## §3 — Deliverables
- `chiral-rotor-triad`: synced + crossed to `battery` (the noise-activated-hopping nuance recorded); receipt
  citing `H:\triskele`. No new compute beyond an optional verification re-run.
- `curvature-as-coupling-bias`: ↑ (curvature identification, checked vs the colloid) **or** ✗ (drop
  "curvature", reduce to the safe form) — recorded with its proof/negative shard.
- Net: the deformation-promotable set is then **closed** (the seam family already collapsed under
  `seam-classification`; these were the last two outside it).
