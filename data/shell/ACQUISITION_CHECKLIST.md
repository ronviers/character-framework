# Shell data acquisition — checklist

Goal: pull the datasets the **T2 readout** needs (normal vs heteromorph *within-shell growth
trajectories*). Trying to actually download each one surfaces where Ron has to step in — same
method as the DNA data.

Target dir: `H:\character-framework\data\shell\`
Key: ✅ in hand · ⚠️ blocked → Ron · 🟡 partial (meshes, needs extraction) · ⬜ not fetched (parked)

---

## T2 core

| # | Dataset | Role | Source | Status | Notes |
|---|---------|------|--------|--------|-------|
| 1 | **Collins et al. 2021** "Going round the twist" | **normal gastropod** trajectories | Dryad `10.5061/dryad.p5hqbzknw` | ✅ in hand | Ron browser-downloaded (Dryad Anubis wall). `S_Table_3_hangle_output.csv` = **184 shells × 4–21 stages**, aperture = 18-comp shape vector + ID + Species. Real, verified. (+ bonus `sectioned_shells.tps`, imagery.) Report's Zenodo `12159344` was WRONG (a *Littorina* study) — caught by gate-check. |
| 2 | **Misaki, Okamoto & Maeda 2023** | **heteromorph ammonite** growing-tube E/C/T | Dryad `10.5061/dryad.q573n5tnz` | ✅ in hand | `Data_2` = E/C/T vs growth-position *s* for 8 morphotypes; **T flips sign mid-growth** (non-convergent, verified). `Data_1` = 153 specimens→morphotypes + coiling direction. CC0. |
| 3 | **Liew & Schilthuizen 2016** *Plectostoma/Opisthostoma* | **heteromorph gastropod** aperture-ontogeny | Figshare `10.6084/m9.figshare.877061` | 🟡 in hand | 8 PLY meshes + the aperture-ontogeny Python script (`File_3`) + R script downloaded. Meshes need processing (File_3 / Noshita #4) to yield trajectories. Skipped 230 MB video + 99 MB Blender. |
| 4 | **Noshita** `growing_tube_model_estimation` | the E/C/T extractor (Python) | GitHub `noshita/...` | ✅ in hand | `_growing_tube_model.py`, `_growting_tube_estimation.py`, io/`_mv3d.py`, 2 notebooks. Turns meshes → E/C/T. |
| 5 | **Filin 2026** "Lead and slant" | centerline-isometric vs aperture-allometric (sharpens "self-similar fixed point" for the T2 stress-test) | Zenodo paper `19919684`/`20073984`, **data `19763621`** | ✅ in hand | `noshita-etal-merged.csv` (harmonized morphospace: W, Δ, Γ, **expansion, T.centerline, tan.lead, cot.spiral**) + Noshita-2012 + Araki-Noshita-2023 + Newkrk-Doyle tables + R scripts + paper PDF. CC0. |

## Parked readouts (data gated; fetch only if T2 stalls / Ron redirects)

| # | Dataset | Readout | Source | Status |
|---|---------|---------|--------|--------|
| 6 | NOAA conch lip-thickness | the clock (records stop, not approach) | NCEI `0253469` | ⬜ |
| 7 | Davison Lsdia1 / formin | T1 chirality (counts, not trajectory) | Dryad `10.5061/dryad.r4342` | ⬜ (also Dryad wall) |
| 8 | Palmer et al. 2021 | clock-approach via increments | PANGAEA `941373` | ⬜ |

---

## The wall → where Ron came in  ✅ CLEARED (Ron browser-downloaded both Dryad sets 2026-06-04)

**Dryad** gates automated download two ways: the API `/download` endpoints need a bearer token
(HTTP 401), and the public front-end routes sit behind an **Anubis "Validating…" proof-of-work
bot-check** that a real browser clears transparently but `curl` cannot. (I will not try to defeat
the bot-check — that's the legitimate manual step.) Everything on Zenodo / Figshare / GitHub
downloaded fine anonymously; only Dryad is blocked.

### Ron's step (two browser downloads, small files)

Open each page in any browser (Chrome/Edge/Firefox all pass Anubis), download only the files
listed, drop them in the named folder.

**A) Collins → `H:\character-framework\data\shell\collins_dryad\`**
Page: https://datadryad.org/dataset/doi:10.5061/dryad.p5hqbzknw
- `S_Table_3_hangle_output.csv` (403 KB) ← **the per-aperture trajectory** (most important)
- `S_Table_1_Specimens.csv` (20 KB)
- `S_Table_2_metadata.csv` (8 KB)
- `S_File_1_Process_Snails.Rmd` (84 KB) — the analysis (optional but useful)
- **SKIP** `Collins_et_al_data.zip` (521 MB — CT images, not needed)

**B) Misaki → `H:\character-framework\data\shell\misaki_dryad\`**
Page: https://datadryad.org/dataset/doi:10.5061/dryad.q573n5tnz
- `Data_2_Parameter_values_of_the_growing_tube_model_for_each_morphotype.csv` (6 KB) ← **the params**
- `Data_1_Material_information.csv` (41 KB)
- `README.md`

*(Alternative if you'd rather not click: I can drive a connected browser via the Chrome
extension to fetch these — but the two manual downloads are faster.)*

Once those land, the full normal-vs-heteromorph T2 set is complete and runnable.
