---
type: "concept"
title: "Impeccable Design Contracts"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/concept"]
domain: "impeccable"
confidence: "practitioner"
related: ["[[Impeccable (Toolchain)]]", "[[Impeccable Project Lifecycle]]", "[[Agent Skills Format]]", "[[Encoded Design Principles]]", "[[The Three Locks]]", "[[Architecture and Stack]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
Design contracts are Impeccable's persistent project context files for keeping agent design work aligned across commands.

## What it is
The captured README says `/impeccable init` writes PRODUCT.md and offers DESIGN.md.
The init command is described as one-time setup.
PRODUCT.md records the product brief and design context.
DESIGN.md records the design system context.
The repo extract says PRODUCT.md captures users, metrics, task context, brand voice, and anti-references.
The repo extract says DESIGN.md is a portable design system spec.
The repo extract reports DESIGN.md in Google Stitch format.
The Google Stitch format detail is practitioner and single-source in the S5c claim pack.
The captured SKILL.md requires the context script to read PRODUCT.md and DESIGN.md when present.
If PRODUCT.md is missing, the captured SKILL.md says setup must stop and follow the init reference.
The README says later commands read the design context before designing.
The README lists `.impeccable/design.json` as a shared design spec that should stay tracked.
The README lists `.impeccable/config.json` and `.impeccable/live/config.json` as shared artifacts.
The README lists screenshots, runtime caches, live sessions, and per-developer config as ephemeral.
The contract pattern is how Impeccable avoids starting each command from a blank design brief.

## How it works
The init interview asks whether the surface is brand or product.
Brand covers marketing, landing pages, and portfolios in the README.
Product covers app UI, dashboards, and tools in the README.
The interview gathers audience.
The interview gathers brand or product lane.
The interview gathers voice.
The interview gathers anti-references.
The interview gathers colors.
The interview gathers type.
The interview gathers components.
The captured SKILL.md routes marketing, landing pages, campaigns, long-form content, and portfolios to a brand register.
The captured SKILL.md routes app UI, admin, dashboards, and tools to a product register.
The captured SKILL.md lets an existing PRODUCT.md `register` field decide when task cues and surface cues do not.
The `document` command can generate root DESIGN.md from existing project code.
The `extract` command can pull reusable components and tokens into the design system.
The live command uses `.impeccable/live/config.json` for framework wiring.
The detector can respect design-system context through `detector.designSystem.enabled`.
The contract files create portability across DESIGN.md-aware tools according to the repo extract.
This portability claim is reported from first-party site context in the repo extract.
This note treats automatic overwrite as unsafe because the S5c captures do not document a rollback path for replacing existing contracts.
That "do not overwrite casually" rule is an operational inference, not a direct upstream quote.

> [!gap]
> The Google Stitch format detail is present in the repo extract and claim pack, but the claim pack marks related directory evidence as single-source where not verified against repo files.

## Best practice
- Run `/impeccable init` before other Impeccable design commands EVIDENCE-BASED
- Preserve PRODUCT.md because the captured SKILL.md treats missing PRODUCT.md as a setup blocker EVIDENCE-BASED
- Preserve DESIGN.md when present because later commands use it as design-system context EVIDENCE-BASED
- Treat `.impeccable/design.json` as a shared tracked artifact EVIDENCE-BASED
- Keep `.impeccable/config.local.json` out of git because the README marks it per-developer EVIDENCE-BASED
- Use `/impeccable document` when an existing project has code but no DESIGN.md EVIDENCE-BASED
- Use `/impeccable extract` when reusable tokens and components should move into the design system EVIDENCE-BASED
- Update contracts deliberately instead of overwriting them wholesale PRACTITIONER
- Mark Google Stitch format claims as practitioner unless a later raw capture verifies the file format directly PRACTITIONER
- Treat brand and product registers as different design contracts, not one generic brief EVIDENCE-BASED

## Pitfalls
Do not run a command flow as if context exists when the context script reports no PRODUCT.md.
Do not mix brand storytelling goals with product task-efficiency goals without naming the register.
Do not commit ephemeral `.impeccable/live/` session state.
Do not ignore `.impeccable/design.json` when detector results seem design-system aware.
Do not cite the Google Stitch format as fully repo-verified from the S5c evidence.
Do not infer that DESIGN.md-aware tools all implement the same schema unless a later source proves it.
Do not treat the contract files as a substitute for inspecting existing CSS, tokens, or components.
The captured SKILL.md still requires reading a project file before design work.
Do not let a generated DESIGN.md silently erase hand-authored brand constraints.
Do not assume live-mode HMR wiring is configured until init or live config confirms it.

## Sources
- GitHub repo, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Impeccable official site, https://impeccable.style/, retrieved 2026-07-07.
- GitHub releases, https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07.
- computertech.co review, https://computertech.co/impeccable-ai-review/, retrieved 2026-07-07.
- Local raw README capture, .raw/skills/impeccable/README.md, retrieved 2026-07-07.
- Local raw SKILL.md capture, .raw/skills/impeccable/SKILL.md, retrieved 2026-07-07.
- Local repo extract, .raw/research/impeccable-repo-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-impeccable.md, generated 2026-07-07.

## Related
- [[Impeccable (Toolchain)]] is the skill that creates and reads the contracts.
- [[Impeccable Project Lifecycle]] shows where init, document, and extract fit.
- [[Deterministic Design Detection]] explains how detector config can use design context.
- Impeccable Design Contracts, the PRODUCT.md and DESIGN.md pair, is this contract concept anchor.
- [[Architecture and Stack]] places contracts inside the broader Gogh stack.
- [[Agent Skills Format]] gives the adjacent SKILL.md portability context.
- [[Encoded Design Principles]] explains why written constraints travel across sessions.
- [[The Three Locks]] is a comparable Taste Skill contract pattern.
- [[Architecture and Stack]] is the adjacent stack context note.
- [[Impeccable Repo and Site]] records source provenance for the contract claims.

## Next actions
- Capture an actual generated PRODUCT.md and DESIGN.md sample if a future slice needs field-level detail.
- Verify the Google Stitch format claim against a raw first-party file before treating it as evidence-based.
- Connect future S5h token-cost notes to whether contract files reduce repeated context load.
- Re-check tracked and ignored `.impeccable/` files after the next README update.
