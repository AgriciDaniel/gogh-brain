---
type: "flow"
title: "Impeccable Project Lifecycle"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/flow"]
domain: "impeccable"
confidence: "evidence-based"
related: ["[[Impeccable (Toolchain)]]", "[[Impeccable Audit and Detect]]", "[[Impeccable Rule Set (45 Detectors)]]", "[[Deterministic Design Detection]]", "[[AI Slop]]", "[[Required Audits]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
The Impeccable lifecycle turns setup, shaping, critique, refinement, hardening, live iteration, and detector gates into one command vocabulary.

## What it is
The captured README lists 23 commands under `/impeccable`.
The captured SKILL.md groups those commands by build, evaluate, refine, enhance, fix, and iterate categories.
The lifecycle starts with init.
It then supports shape and craft for planning and building.
It supports critique and audit for evaluation.
It supports polish, bolder, quieter, distill, harden, and onboard for refinement.
It supports animate, colorize, typeset, layout, delight, and overdrive for enhancement.
It supports clarify, adapt, and optimize for targeted fixes.
It supports live for browser-based visual variants.
It supports document and extract for design-system capture.
It supports pin, unpin, and hooks as management commands.
The slice brief asks for 23 commands mapped into the lifecycle.
This note maps the 23 primary commands and mentions the three management commands separately.

## How it works
Lifecycle stage 1 is init.
`init` gathers design context, writes PRODUCT.md and DESIGN.md, configures live mode, and recommends next steps.
Lifecycle stage 2 is shape.
`shape` plans UX and UI before writing code.
Lifecycle stage 3 is craft.
`craft` runs a full shape-then-build feature flow with visual iteration.
Lifecycle stage 4 is document.
`document` generates root DESIGN.md from existing project code.
Lifecycle stage 5 is extract.
`extract` pulls reusable components and tokens into the design system.
Lifecycle stage 6 is critique.
`critique` reviews hierarchy, clarity, and emotional resonance.
Lifecycle stage 7 is audit.
`audit` runs technical checks for accessibility, performance, and responsive behavior.
Lifecycle stage 8 is polish.
`polish` performs final design-system alignment and shipping readiness work.
Lifecycle stage 9 is bolder.
`bolder` amplifies safe or bland designs.
Lifecycle stage 10 is quieter.
`quieter` tones down aggressive or overstimulating designs.
Lifecycle stage 11 is distill.
`distill` strips the interface to its essence.
Lifecycle stage 12 is harden.
`harden` adds error handling, i18n coverage, text overflow handling, and edge cases.
Lifecycle stage 13 is onboard.
`onboard` designs first-run flows, empty states, and activation paths.
Lifecycle stage 14 is animate.
`animate` adds purposeful motion.
Lifecycle stage 15 is colorize.
`colorize` introduces strategic color.
Lifecycle stage 16 is typeset.
`typeset` fixes font choices, hierarchy, and sizing.
Lifecycle stage 17 is layout.
`layout` fixes spacing, visual rhythm, and layout quality.
Lifecycle stage 18 is delight.
`delight` adds moments of joy.
Lifecycle stage 19 is overdrive.
`overdrive` adds technically extraordinary effects.
Lifecycle stage 20 is clarify.
`clarify` improves UX copy, labels, and error messages.
Lifecycle stage 21 is adapt.
`adapt` adapts for different devices and screen sizes.
Lifecycle stage 22 is optimize.
`optimize` diagnoses and fixes UI performance.
Lifecycle stage 23 is live.
`live` enables visual variant mode in the browser.
The live capture says users select elements against a running dev server.
The live capture says three variants are generated through framework HMR.
The live capture says chosen diffs are written back to source files.
The management command `pin <command>` creates standalone shortcuts.
The management command `unpin <command>` removes those shortcuts.
The management command `hooks <on|off|status|...>` manages the design detector hook.

## Best practice
- Start new projects with `/impeccable init` EVIDENCE-BASED
- Use `shape` before `craft` when planning needs separation from building EVIDENCE-BASED
- Use `craft` when the task needs shape-then-build in one command EVIDENCE-BASED
- Use `document` when existing code needs a root DESIGN.md EVIDENCE-BASED
- Use `extract` when reusable tokens and components should become system assets EVIDENCE-BASED
- Use `critique` for hierarchy, clarity, and resonance review EVIDENCE-BASED
- Use `audit` for accessibility, performance, and responsive checks EVIDENCE-BASED
- Use `polish` as the final shipping readiness pass EVIDENCE-BASED
- Use `live` only when a dev server can support browser variant iteration EVIDENCE-BASED
- Use `pin` only for commands the team invokes often PRACTITIONER

## Pitfalls
Do not skip init when PRODUCT.md is missing.
Do not use live mode when the project cannot run a dev server.
Do not confuse `critique` with `audit`.
`critique` is UX design review.
`audit` is technical quality review.
Do not run bolder or quieter without preserving an existing design system.
Skill 3.9.0 says bolder respects existing design systems.
Do not treat overdrive as a default command.
The README describes it as technically extraordinary effects.
Do not pin shortcuts without considering provider surfaces.
Pin scripts write to every harness directory present in the project.
Do not treat management commands as part of the 23 primary design commands.

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
- [[Impeccable (Toolchain)]] is the lifecycle's skill anchor.
- [[Impeccable Design Contracts]] explains init, document, and extract context.
- [[Impeccable Audit and Detect]] explains audit and detect checkpoints.
- [[Impeccable Rule Set (45 Detectors)]] explains the detector that can gate the lifecycle.
- [[Deterministic Design Detection]] explains hook and CI enforcement.
- [[Ecosystem and Alternatives]] decides when Impeccable belongs in a project stack.
- [[Taste Skill (Project)]] places Impeccable among the six skills.
- [[Required Audits]] connects audit commands to release gates.
- [[Greenfield Build (Prompt 1)]] is the adjacent Taste Skill greenfield flow.
- [[Audit-First Redesign (Prompt 2)]] is the adjacent Taste Skill redesign flow.

## Next actions
- Capture command reference files in a future adapter pass if command internals are needed.
- Verify live mode behavior in a sample dev server before writing operator runbooks.
- Add lifecycle checkpoints to the unified pre-flight mega-checklist when that deliverable is updated.
- Re-check the command count after each Skill release.
