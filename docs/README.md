# docs/ — the working drawer

This is the project's **working area**, not the canonical surface. The canon lives in
[`../framework/`](../framework/) — start with [`character.md`](../framework/character.md). Everything here is
scratch: the handoff, outbound research prompts, source material, and retired one-shots.

## Live (top level)

- **[`handoff_next_session.md`](handoff_next_session.md)** — the single state pointer. Open this first: where
  things are and what's next.
- **`character_credo.md`**, **`character_abiogenesis.md`** — believing-mode generators (local-only, gitignored):
  "as if true" speculation to generate ideas *from*, never public claims.

## Folders

- **`research/`** — the *live* outbound research prompts only (work still wanted). Right now: the archive-term
  hunt plus the two real-data make-or-breaks.
- **`sources/`** — copyrighted source papers/data, gitignored (local): `rust/` (KaiABC), `second_capacity_substrate/`
  (peroxidase-oxidase + Oregonator + embryonic cell-cycle), `misc/` (SRL/laser). Extracted constants live in the
  experiment scripts, not here.
- **`archive/`** — retired one-shots: research/review/crosscheck prompts and plans whose results have already
  landed in canon (receipts/frontier). Kept for provenance; nothing here is live. For *why* something was done,
  read git history and the receipts, not this folder.

## Lifecycle (keep it this way)

A prompt or plan is **live only until its result lands in `framework/`** — then it moves to `archive/`. A thread
earns its own deep doc only while it's hot and unlanded; once canon carries it, it collapses back into the
handoff. If `docs/` ever looks intimidating again, it means spent one-shots have piled up at the top — sweep them
to `archive/`.
