# character-framework — session discipline

The framework lives in [`framework/`](framework/). Read
[`framework/character.md`](framework/character.md) first; the README is the
walk-through. This file is the only standing instruction beyond them.

- **`framework/` is canonical-only — not a scratchpad.** Everything in
  `framework/` is active, canonical source of truth: `character.md` (the
  framework), plus `character_prior_art.md`, `character_receipts.md`,
  `character_frontier.md`, `character_grounding_method.md`,
  `character_fdr_treatment.md`, `character_translation_method.md`,
  `character_substrate_ledger.md` (the substrate roster + verdicts),
  `character_substrate_method.md` (how a viable real-data substrate is found). Working
  material — handoffs, drafts, research and review prompts, session notes — goes
  in [`docs/`](docs/), never `framework/`. A superseded canonical doc goes to
  `framework/archive/`; don't stage scratch in `framework/`.
- **Receipts in the same session.** When a session proves, derives, or composes a
  result that becomes a claim in `character.md`, append its justification to
  `character_receipts.md` *that same session* — citation, composition, or proof
  shard. A claim whose proof tree is genuinely lost gets an honest `unrecovered`
  marker; never fabricate a reconstruction.
- **The canonical docs are allowed to be dense.** `character.md` and its
  companions are the source of truth — keep them rigorous, not thin. Brevity is
  for working docs in `docs/`.
- **Bring nothing new; the only claim is the reading.** Every piece is imported
  and named to its source (`character_prior_art.md`); no claim is anthropocentric
  or domain-specific. The framework is substrate-general — never steer it with a
  single vivid or human-domain example.
- **No declared virtues in copy.** Show the behavior; don't announce it.

The legacy corpus is frozen in `mpa-atlas` (snapshot `character-v0.1`); all
`mpa-*` repos are legacy and this repo does not depend on them.
