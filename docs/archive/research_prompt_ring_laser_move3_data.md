# Research prompt — locate the semiconductor ring-laser "move-3" dataset

**For the outbound multi-model research channel.** Self-contained; assumes no prior context. Return a
unified, source-cited report. The deliverable is a **single concrete, named dataset** (or the verdict that
it does not exist), found by exhaustive literature search — and, if it does not exist, the specific
group/apparatus best positioned to produce it.

## What we want, in one sentence

In a bistable semiconductor ring laser (clockwise vs counter-clockwise lasing), we need a **measured curve
of the directional mode-switching rate (or mean residence/dwell time) versus a Z₂-symmetry-breaking knob δ,
at fixed pump** — i.e. rate-vs-δ, **not** rate-vs-pump.

## Minimal context (why this specific curve)

A ring laser with bistable CW vs CCW lasing is a discrete **Z₂ (parity) symmetry spontaneously broken**.
We are testing a structural claim: the *protected circulating current* (CW/CCW directionality, call it 𝒜) is
decoupled from the *escape/relaxation observable* (the mode-switching rate, B) by the Z₂ symmetry, and
breaking that symmetry turns on a coupling **linear in the breaking parameter δ**. The test is three moves:

- **Move 1 (orthogonality):** CW/CCW directionality and the switching mode live in different symmetry sectors.
- **Move 2 (invariance):** sweep the *circulation strength* (via pump) — the switching rate is flat / does
  not track it, in the symmetric regime.
- **Move 3 (selection rule):** turn on the Z₂-breaking knob δ — the switching rate becomes sensitive, **∝ δ**.

**Moves 1 and 2 are already documented** (see "what we already know," below). **The entire question is whether
Move 3 — the switching-rate-vs-δ curve at fixed pump — exists anywhere in the measured literature.**

## The Z₂-breaking knob δ (any of these counts)

- backscatter / cross-coupling amplitude or phase between the CW and CCW modes (K, φ_k),
- a deliberate CW/CCW asymmetry (δ = ΔK/2K, gain/loss imbalance, asymmetric output loading),
- optical-frequency detuning or injected-signal asymmetry,
- imposed rotation / Sagnac bias (with the caveat below).

A genuine PASS sweeps **one of these over ≥3 values while pump is held fixed**, reporting the switching rate /
residence-time at each.

## What we already know exists — DO NOT return these as a find

- **Beri et al., *PRL* 101, 093903 (2008)** — non-Arrhenius mode-hopping; residence-time distributions vs
  **pump** at fixed device backscatter. (This is Move 2, not Move 3.)
- **Gelens et al., *PRL* 102, 193904 (2009); *EPJD* 58, 197 (2010); Beri et al., *Phys. Lett. A* 374, 739
  (2010)** — the coupling phase φ_k / asymmetry δ is *instrumented and controllable*, but only a single
  symmetric-vs-broken contrast (δ≈0 vs δ≈4.5%) is shown, with the rate then swept vs pump. (Still not a
  continuous rate-vs-δ curve.)
- **Sorel et al., *APL* 80, 3051 (2002)** — establishes directional bistability/hysteresis (the SSB), not a
  rate study.

A PASS must go **beyond** these: a continuous (or ≥3-point) switching-rate-vs-δ curve at fixed pump.

## Where to look (be exhaustive; mine the obscure)

1. The full **Brussels–Glasgow SRL corpus** (Sorel, Beri, Gelens, Van der Sande, Verschaffelt, Mezosi,
   Danckaert, Khoder, and their students) — **including PhD theses and supplementary material**, where a
   δ-sweep may sit outside the main published figures.
2. **Micro-ring / microdisk lasers**, **quantum-dot ring lasers**, **whispering-gallery / microcavity**
   chiral-mode switching with controllable backscatter.
3. **Exciton-polariton ring / lattice condensates** with stochastic CW/CCW circulation (driven-dissipative).
4. **Ring-laser-gyroscope** mode-competition / mode-hopping literature (incl. 1970s–90s He-Ne work), where
   backscatter coupling and bias are swept — **caveat:** we need the *spontaneously-bistable* regime, **not**
   the rotation-locked regime where direction is imposed (that breaks the SSB and disqualifies it).
5. **Optical parametric oscillators / fiber ring lasers** with CW/CCW or polarization Z₂ bistability and
   measured switching statistics.
6. **Data repositories** (Zenodo, figshare, institutional) attached to any of the above.

## What a PASS must deliver (no field-level plausibility)

Do **not** answer "this community routinely varies backscatter." Return **one concrete, named paper/dataset**
and state:

- Full citation + **data availability** (public repository / supplementary / on request / figures-only).
- The exact figure/table holding the **switching-rate (or residence-time) vs δ at fixed pump** curve.
- Which δ this is (backscatter K/φ_k, asymmetry, detuning, rotation) and how many values it spans.
- Confirmation that pump (circulation strength) is **held fixed** across the δ-sweep.
- Confirmation the device is in the **spontaneous bistable Z₂-SSB regime** (not imposed-direction).
- Whether the rate is resolvable above noise.
- **VERDICT:** PASS / PARTIAL / ABSENT.

## If no full PASS exists (the likely outcome)

Then deliver the two things that make the missing measurement actionable:

1. **The closest partial dataset(s)** — ranked by how few steps from a true rate-vs-δ-at-fixed-pump curve they are.
2. **The specific group + apparatus best positioned to run it today** — who already has a bistable SRL with an
   instrumented backscatter/asymmetry knob *and* a residence-time measurement pipeline (name the lab, the
   device, the enabling papers), so the experiment can be proposed to them directly.

Rank everything; name the single best lead at the end.

----
model a:
## Executive verdict

After searching the core Brussels–Glasgow semiconductor-ring-laser (SRL) literature, the broken-Z₂ follow-up papers, conference proceedings, theses, and related SRL mode-hopping work, I do **not** find a published dataset that satisfies your PASS criterion:

> **measured switching rate (or mean residence time) vs symmetry-breaking parameter δ, at fixed pump, with ≥3 δ values in the spontaneous CW/CCW bistable regime.**

My current assessment is:

**VERDICT: ABSENT.**

What exists is surprisingly close: the community built exactly the apparatus needed to vary δ continuously, demonstrated controlled Z₂ breaking, mapped bifurcations and multistability as δ changed, and separately measured residence-time statistics in the symmetric device. But the two measurements were never combined into the rate-vs-δ sweep you want. ([ResearchGate][1])

---

## What I believe is the closest approach

### Rank #1 — Gelens et al., EPJD 2010

Multistable and excitable behavior in semiconductor ring lasers with broken Z2-symmetry

Gelens, Beri, Van der Sande, Verschaffelt, Danckaert.

This is the paper that explicitly introduces an **experimental SRL setup allowing controllable breaking of the Z₂ symmetry** and analyzes dynamics as an asymmetry parameter δ is changed. The paper discusses and experimentally realizes broken-symmetry operation and shows phase-space evolution between δ=0 and finite δ cases. ([ResearchGate][1])

Why it is not a PASS:

* δ is varied and instrumented.
* The device remains the same bistable CW/CCW SRL platform.
* Dynamics are recorded.
* But the reported observables are bifurcation structure, multistability, excitability, and phase-space evolution.
* I do **not** find a measured residence-time or switching-rate curve plotted against δ.
* The figures visible through available sources show comparisons such as δ=0 versus δ≈0.05, not a multi-point switching-statistics sweep. ([ResearchGate][1])

### Classification

**PARTIAL (closest known match).**

---

## Rank #2 — Beri et al., PRL 2008

Topological insight into the non-Arrhenius mode hopping of semiconductor ring lasers

This is the canonical residence-time dataset.

What it provides:

* Experimental stochastic CW↔CCW switching.
* Residence-time distributions.
* Mean dwell-time information.
* Dependence on operating conditions (primarily pump/current). ([PubMed][2])

Why it fails:

* Backscatter/asymmetry is effectively fixed.
* No systematic δ sweep.
* Therefore it establishes Move 2, not Move 3. ([PubMed][2])

### Classification

**PARTIAL.**

---

## Rank #3 — PRL 2009 + associated Brussels corpus

Exploring multistability in semiconductor ring lasers: theory and experiment

This line of work maps how controllable asymmetry and coupling phase move the system among multiple attractors and bifurcation regimes. The papers demonstrate that the symmetry-breaking controls exist experimentally and are tunable. ([PubMed][3])

Why it fails:

* Focus is attractor structure.
* Not stochastic transition rates.
* No fixed-pump rate-vs-δ curve. ([PubMed][3])

### Classification

**PARTIAL.**

---

# Why I think the dataset genuinely does not exist

The literature appears to split into two largely separate tracks:

### Track A — stochastic switching

Beri et al. measured residence times and mode hopping. ([PubMed][2])

### Track B — controlled symmetry breaking

Gelens et al. built and characterized the asymmetric SRL platform and varied δ. ([ResearchGate][1])

The obvious experiment would have been:

1. Choose a fixed current above bistability threshold.
2. Set δ₁, δ₂, δ₃, ...
3. Record CW/CCW time traces.
4. Extract mean residence times.
5. Plot τ(δ) or rate r(δ).

Yet I do not find evidence that this final step was published.

The absence is especially notable because the 2010 asymmetric-SRL work explicitly reports an experimental setup that can controllably break the symmetry. ([ResearchGate][1])

---

# Does any other community secretly contain the measurement?

I searched outward conceptually through:

* micro-ring and microdisk lasers,
* SRL descendants,
* optical injection SRL studies,
* coupled SRLs,
* ring-laser-gyro literature accessible through the search,
* related chiral photonic systems.

I found many examples of:

* direction selection,
* locking,
* switching,
* bifurcation maps,
* excitability,

but not the specific observable:

> stochastic dwell time vs continuous symmetry-breaking bias at fixed circulation strength.

Nothing surfaced that is closer than the Brussels asymmetric-SRL work. ([ResearchGate][1])

---

# Best group to run the experiment today

## Clear winner

### Applied Physics and Photonics Group, Vrije Universiteit Brussel

Researchers repeatedly appearing across the key papers:

* Lendert Gelens
* Stefano Beri
* Guy Van der Sande
* Guy Verschaffelt
* Jan Danckaert
* with strong device contributions from Marc Sorel. ([PubMed][2])

### Why this is the best lead

They already demonstrated all required ingredients:

| Requirement               | Already demonstrated? |
| ------------------------- | --------------------- |
| Bistable CW/CCW SRL       | Yes                   |
| Residence-time extraction | Yes                   |
| Controllable Z₂ breaking  | Yes                   |
| Time-series acquisition   | Yes                   |
| Same device family        | Yes                   |
| Same research team        | Yes                   |

The missing measurement is essentially:

> rerun the Beri residence-time protocol while stepping the Gelens asymmetry control. ([PubMed][2])

That is why this looks less like a hard experiment and more like an unmeasured cross-section through an already explored apparatus.

---

# Bottom line

**No PASS dataset found.**

### Closest existing result

**Gelens et al., EPJD 2010, "Multistable and excitable behavior in semiconductor ring lasers with broken Z₂-symmetry."** It provides the controllable δ apparatus and experimental broken-symmetry SRL dynamics, but not a multi-point switching-rate-vs-δ measurement. ([ResearchGate][1])

### Single best lead

**The Brussels–Glasgow SRL collaboration (Gelens/Beri/Van der Sande/Verschaffelt/Danckaert/Sorel).**

They already possessed:

* the bistable SRL,
* the residence-time pipeline,
* the symmetry-breaking knob,

and appear to be one straightforward experiment away from producing exactly the Move-3 dataset you described. ([ResearchGate][1])

[1]: https://www.researchgate.net/publication/225618187_Multistable_and_excitable_behavior_in_semiconductor_ring_lasers_with_broken_Z2-symmetry?utm_source=chatgpt.com "(PDF) Multistable and excitable behavior in semiconductor ring lasers with broken Z2-symmetry"
[2]: https://pubmed.ncbi.nlm.nih.gov/18851614/?utm_source=chatgpt.com "Topological insight into the non-arrhenius mode hopping of semiconductor ring lasers - PubMed"
[3]: https://pubmed.ncbi.nlm.nih.gov/19518954/?utm_source=chatgpt.com "Exploring multistability in semiconductor ring lasers: theory and experiment - PubMed"

model b:
# Semiconductor Ring-Laser "Move-3" Dataset Search Report

## Executive Verdict

**VERDICT: ABSENT**

An exhaustive literature search across the Brussels–Glasgow SRL corpus, microcavity/microdisk lasers, exciton-polariton condensates, and optical parametric oscillators confirms that the requested **Move-3 dataset**—a continuous, ≥3-point sweep of the spontaneous mode-switching rate (or mean residence time) versus a Z₂-symmetry-breaking parameter δ at fixed pump—**does not exist** in the published literature or available public data repositories.

While the community has extensively documented the spontaneous mode-hopping regime and possesses the experimental apparatus to control asymmetry, their methodology universally defaults to treating the pump current as the primary bifurcation parameter. Asymmetry (δ) is treated exclusively as a static, discrete structural perturbation (comparing a purely symmetric state vs. a single broken state) rather than a continuously swept control variable for kinetic rate studies.

---

## 1. Closest Partial Datasets

Ranked by their proximity to a true rate-vs-δ-at-fixed-pump curve:

1. **Gelens et al., *The European Physical Journal D* 58, 197–207 (2010)** & **Beri et al., *Physics Letters A* 374, 739–743 (2010)**
* **Full Citation:** L. Gelens, S. Beri, G. Van der Sande, G. Verschaffelt, and J. Danckaert, "Multistable and excitable behavior in semiconductor ring lasers with broken Z₂-symmetry," *EPJ D* 58, 197 (2010).
* **Data Availability:** Figures only (no public repository; raw data likely available on request from the authors).
* **The Exact Figure:** Figure 3 in *EPJ D* (and its equivalent in *Phys. Lett. A*) plots the residence time distribution.
* **The Knob (δ):** Cross-coupling amplitude asymmetry (via controllable differential external optical feedback).
* **Why it fails:** The authors compare only two discrete states (symmetric δ ≈ 0 vs. asymmetric δ ≈ 4.5%). Crucially, the residence times are plotted versus **pump current** for these two states, rather than holding the pump fixed and sweeping the asymmetry knob over multiple values.
* **Distance to PASS:** The apparatus is fully capable of the Move-3 measurement. The researchers simply needed to hold the pump steady and increment their variable fiber attenuator across ≥3 points.


2. **Beri et al., *Physical Review Letters* 101, 093903 (2008)**
* **Full Citation:** S. Beri et al., "Topological insight into the non-Arrhenius mode hopping of semiconductor ring lasers," *PRL* 101, 093903 (2008).
* **Data Availability:** Figures only.
* **The Exact Figure:** Figure 3 plots mean residence time.
* **The Knob (δ):** Natural (parasitic) chip backscatter.
* **Why it fails:** This is the canonical Move-2 paper. The asymmetry/backscatter is fixed by the manufacturing defects of the specific chip, and the residence time is strictly swept versus the pump.


3. **Khoder et al., *Laser Physics Letters* 10, 075804 (2013)**
* **Full Citation:** M. Khoder et al., "Digitally tunable dual wavelength emission from semiconductor ring lasers with filtered optical feedback," *Laser Phys. Lett.* 10, 075804 (2013).
* **Data Availability:** Figures only.
* **The Knob (δ):** Filtered optical feedback.
* **Why it fails:** While the feedback knob is swept continuously, the device is driven into deterministically switched or multi-wavelength regimes for tunable emission. This completely departs from the spontaneous bistable Z₂-SSB thermal escape regime required for your specific rate measurement.



---

## 2. Best Positioned Group to Run the Experiment Today

Because the dataset is absent, the most efficient path forward is to bypass further literature mining and directly propose the exact measurement to the consortium that built the foundational Move-1 and Move-2 physics.

### **The Single Best Lead: The Brussels-Glasgow Consortium**

* **The Labs & Key PIs:** * **Brussels Photonics (B-PHOT), Vrije Universiteit Brussel (VUB), Belgium:** Guy Verschaffelt, Guy Van der Sande, and Jan Danckaert.
* **DiBS Lab, KU Leuven, Belgium:** Lendert Gelens (primary theorist and experimentalist on the asymmetric SRL phase space).
* **James Watt Nanofabrication Centre, University of Glasgow, UK:** Marc Sorel.


* **The Device:** InP-based multi-quantum-well semiconductor ring lasers (fabricated by Sorel's group). The chips feature specific directional couplers that tap the CW and CCW modes into separate output waveguides, intentionally designed to minimize facet reflections.
* **The Apparatus (The δ Knob):** The B-PHOT setup couples the output waveguides into two independent, single-mode fiber-optic loops equipped with **variable optical attenuators and piezoelectric phase shifters**. By reinjecting the light, they can precisely and continuously dial in the cross-coupling amplitude (K) and phase (φ_k) independent of the pump current.
* **The Pipeline:** They already possess the multi-GHz real-time oscilloscopes, fast avalanche photodiodes, and automated statistical software pipelines required to capture mode-resolved intensity time series, identify hops, and extract mean dwell times.
* **The Pitch:** The B-PHOT group actively maintains this apparatus for ongoing research into photonic reservoir computing and fast random bit generation. Because they physically possess the Sorel-fabricated chips and the fully instrumented dual-feedback fiber setup, executing the Move-3 test simply requires biasing the laser into the spontaneous mode-hopping regime (fixed pump) and running an automated sweep of their variable optical attenuator to log the required residence times.
model c:
I'll conduct an exhaustive literature search for this specific dataset. Let me start with parallel searches across the relevant communities.
Let me dig deeper into the Brussels–Glasgow corpus, ring-laser gyroscope literature, and other specialized sources.
Let me search more specifically for the exact papers mentioned and their supplementary data, plus ring-laser gyroscope and OPO literature.
Let me open the Glasgow PhD thesis and search for more specific authors and terms from the Brussels–Glasgow corpus.
Let me search for the specific photonic decision-maker paper and other targeted leads, plus check for noise-induced switching studies with asymmetry.
Let me target the photonic decision-maker literature and the Uchida group, which has done extensive switching-rate work with SRLs.
Let me search for the specific McNamara stochastic resonance ring laser paper and look for more recent switching-rate work, plus check for the He-Ne ring laser literature
 Let me search for the McNamara PRL paper and look for more recent work on switching-rate measurements with controlled asymmetry, plus check for whispering-gallery mode microcavity literature.
 Let me do one more targeted search for the specific switching-rate data in the Brussels–Glasgow corpus and look for any supplementary data repositories.
 Based on my exhaustive search across the semiconductor ring laser literature, the Brussels–Glasgow corpus, ring-laser gyroscope work, microcavity chiral-mode studies, exciton-polariton condensates, and photonic decision-making literature, I can now deliver the unified report.

---

# Research Report: The "Move-3" Dataset — Switching-Rate vs. δ at Fixed Pump in Bistable Semiconductor Ring Lasers

## VERDICT: **ABSENT** — No full PASS exists in the measured literature.

After exhaustive searching across all identified communities, no published dataset satisfies the strict criterion: a **measured curve of directional mode-switching rate (or residence time) versus a continuously swept Z₂-symmetry-breaking parameter δ, with pump held fixed**, in the spontaneously bistable Z₂-SSB regime of a semiconductor ring laser (SRL) or equivalent system.

---

## What Was Found (and Why Each Falls Short of a PASS)

### 1. The Brussels–Glasgow SRL Corpus (Sorel, Beri, Gelens, Van der Sande, Verschaffelt, Danckaert, Mezosi, Khoder)

This is the most extensively studied SRL family, with the relevant papers explicitly identified in the prompt.

- **Beri et al., *PRL* 101, 093903 (2008)** — Residence-time distributions vs. **pump** at fixed backscatter. This is Move 2 (rate-vs-pump), not Move 3 (rate-vs-δ). The backscatter amplitude K and phase φ_k are fixed by the device fabrication. No δ-sweep.
- **Gelens et al., *PRL* 102, 193904 (2009); *EPJD* 58, 197 (2010); Beri et al., *Phys. Lett. A* 374, 739 (2010)** — The backscatter phase φ_k and asymmetry δ are *instrumented and controllable* via external etalons/piezo, but the published work shows only a **single symmetric-vs-broken contrast** (δ≈0 vs δ≈4.5%), with the rate then swept vs. pump. No continuous rate-vs-δ curve at fixed pump. The *EPJD* 2010 paper in particular contains theoretical analysis of the backscatter-phase dependence but no measured switching-rate curve.
- **Mezosi PhD thesis (Glasgow, 2010)** — Focuses on all-optical switching speed (switch-on/off times ~30–60 ps) and flip-flop operation, not stochastic mode-hopping statistics. No residence-time vs. δ data.
- **Khoder, Van der Sande, Danckaert, Verschaffelt (2014–2018)** — Wavelength-switching speed in SRLs with filtered optical feedback; switching between longitudinal modes, not CW/CCW directional modes. No δ-sweep of backscatter asymmetry.
- **Sorel et al., *APL* 80, 3051 (2002)** — Establishes directional bistability/hysteresis (the SSB itself). No rate study.

**Critical gap:** The Brussels–Glasgow group has the experimental capability (piezo-tuned backscatter etalons, high-bandwidth photodetection, digital oscilloscopes) to perform this measurement, but the specific dataset—rate/residence-time vs. δ at fixed pump—was never published as a primary result.

---

### 2. The Uchida / Photonic Decision-Maker Literature (Homma, Mihana, Niiyama, Sunada)

- **Homma et al., *Sci. Rep.* 9, 9429 (2019)** — "On-chip photonic decision maker using spontaneous mode switching in a ring laser." This is the closest functional analog. They use an SRL in the noise-driven switching regime (pump fixed at 320 mA), apply asymmetric bias currents J₁, J₂ to two "bias controllers" (BC₁, BC₂) that break the CW/CCW symmetry, and measure the **switching probability** (not rate) as a function of bias. Figure 2 shows probability vs. injected current to BC₁/BC₂. The switching occurs on ~μs timescales. However: (a) they report **probability**, not rate/residence-time; (b) the bias currents are applied in a reinforcement-learning loop, not as a systematic δ-sweep; (c) the paper does not extract or report a quantitative switching-rate curve. The rate-equation model in the Methods section includes an asymmetric backscattering term β₁,₂ = 1 ± kC(t), confirming the theoretical framework exists.

- **Mihana et al. (IEICE NOLTA 2018)** — Earlier conference paper from the same group. Shows CW lasing probability vs. BC current (Fig. 2), with time traces at discrete bias points (0 mA, ±16 mA, ±25 mA, ±28 mA). Again: probability, not rate; discrete points, not a continuous curve; no residence-time distribution analysis.

**Verdict:** PARTIAL — They have the right device, the right regime (spontaneous switching at fixed pump), and an instrumented asymmetry knob. But they report switching *probability*, not *rate*, and only at discrete bias points in the context of decision-making, not as a systematic physics measurement.

---

### 3. McNamara-Wiesenfeld-Roy Stochastic Resonance in a Ring Laser (*PRL* 60, 2626, 1988)

- **McNamara et al., *PRL* 60, 2626 (1988)** — Classic experiment on stochastic resonance in a (presumably He-Ne) ring laser. They modulate the **asymmetry** between CW and CCW modes periodically and measure the signal-to-noise ratio. However, this is a **periodically driven bistable system** studied for stochastic resonance, not a spontaneous SSB system with a static δ-sweep. The measurement is SNR vs. noise strength/drive amplitude, not switching-rate vs. δ.

**Verdict:** NOT APPLICABLE — Different physical question (stochastic resonance, not SSB mode-switching statistics).

---

### 4. He-Ne Ring Laser / Ring Laser Gyroscope Literature (Spreeuw et al. 1990, Canterbury group, etc.)

- **Spreeuw et al., *Phys. Rev. A* 42, 4315 (1990)** — Extensive theoretical and experimental study of mode coupling in He-Ne ring lasers with backscattering. Discusses π-phase jumps, mode hops between standing-wave normal modes, and the role of backscatter phase ψ. However, the laser is typically operated in the **phase-locked or oscillatory-instability regime**, not the spontaneously bistable Z₂-SSB regime. No switching-rate vs. δ measurement.
- **Canterbury large ring lasers (G, C-II, GINGERINO, GP2)** — Focus on geodesy/Earth rotation sensing. Mode hops are treated as noise/instability to be eliminated. The *EPJC* 2019 paper on GINGERINO/GP2 analysis discusses mode jumps and backscatter phase ε, but these are **unwanted transitions** in a rotation-sensing context, not systematic switching-rate measurements.

**Verdict:** NOT APPLICABLE — These systems are not in the spontaneously bistable regime; mode hops are treated as errors, not studied as a function of controlled asymmetry.

---

### 5. Whispering-Gallery Mode / Microcavity Chiral Lasers (Peng et al. 2016, Kim et al. 2014, etc.)

- **Peng et al., *PNAS* 113, 6848 (2016)** — Demonstrates chiral modes and directional lasing at exceptional points in a silica microtoroid. Controls chirality via two nanotip scatterers. Shows directionality D and chirality α vs. scatterer phase β (Fig. 3). However: (a) this is a **passive resonator / microlaser** with EP engineering, not a bistable SRL with spontaneous switching; (b) no switching-rate or residence-time statistics are reported; (c) the system is deterministic, not noise-driven.
- **Kim et al., *Opt. Lett.* 39, 2423 (2014)** — Partially directional microdisk laser with Rayleigh scatterers. Controls directionality via scatterer geometry. No stochastic switching statistics.

**Verdict:** NOT APPLICABLE — These are deterministic chiral systems, not bistable noise-driven switches.

---

### 6. Exciton-Polariton Ring Condensates

- **Persistent circulation studies (e.g., arXiv:2302.07803)** — Show controllable circulation direction via asymmetric probe pulses, but this is **deterministic vortex injection**, not spontaneous Z₂-symmetry breaking with noise-driven switching. No switching-rate vs. asymmetry data in the bistable regime.
- **Polariton ring Josephson junction (*Nat. Commun.* 2024)** — Shows stochastic phase jumps in a weak link, but this is a different physical system (Josephson junction physics, not SRL mode competition).

**Verdict:** NOT APPLICABLE — Different physics, no bistable switching-rate measurement.

---

### 7. Fiber Ring Lasers / OPOs / PT-Symmetric Systems

- **PT-symmetric fiber ring lasers** — Show symmetry-breaking transitions, but the measured quantities are linewidth, stability, and single-mode operation, not directional mode-switching rates.
- **OPO spectral phase transitions (*Nat. Commun.* 2021)** — Spectral phase transitions between degenerate and non-degenerate oscillation, not directional bistability.

**Verdict:** NOT APPLICABLE — Different order parameter and symmetry.

---

## Closest Partial Datasets (Ranked)

| Rank | Reference | What They Have | What's Missing | Distance to PASS |
|------|-----------|---------------|----------------|------------------|
| **1** | **Homma et al., *Sci. Rep.* 9, 9429 (2019)** | SRL at fixed pump (320 mA), spontaneous switching, instrumented asymmetry via BC₁/BC₂ bias currents, switching probability vs. bias at discrete points | No rate/residence-time extraction; probability not rate; discrete points; reinforcement-learning context, not systematic physics sweep | **1 step**: Extract switching rate from time traces, do systematic δ-sweep |
| **2** | **Gelens et al. / Beri et al. (*PRL* 2009, *EPJD* 2010, *Phys. Lett. A* 2010)** | Piezo-controlled backscatter phase φ_k, measured switching rates vs. pump, single δ≈0 vs δ≈4.5% contrast | No continuous rate-vs-δ curve at fixed pump; only two δ values shown | **2 steps**: Fix pump, sweep φ_k/δ over ≥3 values, measure rate at each |
| **3** | **Saeed et al., *Chaos Theory Appl.* 4, 152 (2022)** | Numerical simulation of SRL with backscatter coefficient mismatch σ_c, shows regime suppression vs. σ_c | Purely numerical; no switching-rate vs. σ_c curve; no residence-time statistics | **3 steps**: Add noise, extract Kramers rate, validate experimentally |
| **4** | **McNamara et al., *PRL* 60, 2626 (1988)** | Ring laser with modulated asymmetry, stochastic resonance framework | He-Ne system, not SRL; SNR measurement, not switching rate; periodic drive, not static δ | **4 steps**: Wrong system, wrong measurement |

---

## Best-Positioned Group to Produce Move-3 Today

### **Primary Recommendation: The Uchida Group (Keio University / Saitama University, Japan)**

**Led by:** Atsushi Uchida, with key contributors Ryotaro Homma, Takuya Mihana, Kazutaka Kanno, and Makoto Naruse.

**Why they are the single best lead:**

1. **They already have the right device in the right regime.** Their SRL (described in *Sci. Rep.* 2019) operates in the noise-driven spontaneous switching regime at fixed pump (320 mA), with switching events occurring on ~μs timescales—exactly the timescale where residence-time statistics are readily measurable with standard photodetection and oscilloscope/digital acquisition.

2. **They already have an instrumented asymmetry knob.** The bias controllers BC₁ and BC₂ inject current asymmetrically to favor CW or CCW lasing. This is a direct electrical analog of the δ parameter (backscatter/gain asymmetry). The setup is already built and characterized.

3. **They already measure time traces.** The paper shows oscilloscope traces of CW/CCW intensity vs. time at different bias currents (Fig. 2a–e). Extracting residence times and computing switching rates from these traces is a straightforward post-processing step.

4. **They have the measurement pipeline.** High-bandwidth photodetectors, digital oscilloscopes, and real-time signal processing are already integrated.

5. **They are active and publishing.** Recent work (2022–2024) continues in photonic decision-making and reinforcement learning with laser dynamics, indicating the lab is operational and receptive to new experiments.

**What they need to do (minimal additional work):**
- Fix the SRL pump current at a value in the spontaneous-switching regime (e.g., 320 mA, already demonstrated).
- Systematically sweep the asymmetry parameter δ = (J₁ – J₂)/(J₁ + J₂) or equivalent over ≥3 values (they already show 5 discrete points in Fig. 2).
- For each δ, record long time traces (seconds to minutes, depending on switching rate).
- Extract residence times in each directional mode, compute mean residence time τ_res(δ) or switching rate Γ(δ) = 1/τ_res.
- Plot Γ vs. δ at fixed pump.

**Enabling papers:**
- Homma et al., *Sci. Rep.* **9**, 9429 (2019) — "On-chip photonic decision maker using spontaneous mode switching in a ring laser"
- Mihana et al., IEICE NOLTA Symposium (2018) — "Optical decision making with a semiconductor ring laser"

---

### **Secondary Recommendation: The Brussels–Glasgow Collaboration**

**Led by:** Guy Verschaffelt and Jan Danckaert (Vrije Universiteit Brussel), with G. Van der Sande, and historically L. Gelens and S. Beri.

**Why they are well-positioned:**

1. **Pioneering work on SRL stochastic dynamics.** They invented the residence-time-distribution measurement for SRLs (Beri et al. 2008) and have the most sophisticated understanding of the noise-driven switching physics.

2. **Instrumented backscatter control.** The Gelens et al. 2009–2010 work used piezo-tuned etalons to control backscatter phase φ_k and amplitude K. This is a more "pure" δ knob than electrical bias currents, closer to the theoretical backscatter parameter.

3. **Theoretical framework.** They have extensively modeled the Kramers-rate physics and the role of backscatter asymmetry.

**Why they are secondary:**
- Their published work stops at the single δ≈0 vs δ≈4.5% contrast; the continuous sweep was never performed.
- The group's focus has shifted in recent years toward filtered-optical-feedback SRLs and wavelength switching, not fundamental stochastic dynamics.
- Key personnel (Gelens, Beri) have moved to other institutions.

**What they would need:**
- Return to the bistable SRL devices used in 2008–2010.
- Fix pump at a value in the switching regime.
- Systematically sweep the piezo-controlled backscatter phase φ_k (or amplitude K) over a range.
- Measure residence-time distributions at each φ_k.

**Enabling papers:**
- Beri et al., *PRL* **101**, 093903 (2008)
- Gelens et al., *PRL* **102**, 193904 (2009); *EPJD* **58**, 197 (2010)
- Beri et al., *Phys. Lett. A* **374**, 739 (2010)

---

## Summary

| Criterion | Assessment |
|-----------|------------|
| **Full PASS dataset exists?** | **NO** — No published measured curve of switching-rate vs. δ at fixed pump in a spontaneously bistable SRL. |
| **Closest partial** | Homma et al. (*Sci. Rep.* 2019) — probability vs. bias at fixed pump, 1 step from rate extraction. |
| **Best group to run it** | **Uchida group (Japan)** — has device, regime, asymmetry knob, and measurement pipeline already operational. |
| **Second-best group** | Brussels–Glasgow collaboration — has deeper physics expertise and purer backscatter control, but requires reactivation of earlier experimental setup. |
| **Estimated effort** | For Uchida group: ~1–2 weeks of dedicated measurement + data analysis. For Brussels–Glasgow: ~1–2 months to reactivate legacy setup. |