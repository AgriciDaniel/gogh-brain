---
type: "rule"
title: "Impeccable Rule Set (45 Detectors)"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/rule"]
domain: "impeccable"
confidence: "evidence-based"
related: ["[[Impeccable (Toolchain)]]", "[[Deterministic Design Detection]]", "[[Impeccable Audit and Detect]]", "[[AI Slop]]", "[[AI Tells (Forbidden Patterns)]]", "[[Required Audits]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
The Impeccable rule set is a 45-rule deterministic detector for common AI frontend anti-patterns and quality issues.

## What it is
The captured README says Impeccable includes 45 deterministic detector rules.
The detector runs without an LLM and without API keys.
It is available through `npx impeccable detect`.
It is also distributed through a browser extension, according to the source ledger and repo extract.
The detector is separate from LLM-only critique checks.
The release capture says CLI 3.2.0 added rule 45 on 2026-07-01.
Rule 45 targets Codex grid-line backgrounds, described as a two-axis gradient overlay pattern.
That release happened six days before the 2026-07-07 capture.
The claim pack records a growth path from 27 rules in May 2026 to 44 rules at v3.0.3 and 45 rules after CLI 3.2.0.
The rule count is therefore a dated observation.
Any cached count other than 45 is stale against the 2026-07-07 capture.
The captured README lists named anti-pattern tells including Inter for everything, purple-to-blue gradients, and cards nested in cards.
The captured SKILL.md adds absolute bans such as side-stripe borders, gradient text, default glassmorphism, hero metric templates, identical card grids, repeated eyebrows, numbered section markers, and text overflow.
The repo extract groups rules across AI slop signatures, general design quality, and color issues.
The rule set is the strongest enforcement layer in the Gogh stack because it can run outside a model conversation.

## How it works
Run `npx impeccable detect src/` to scan a directory.
Run `npx impeccable detect index.html` to scan one HTML file.
Run `npx impeccable detect https://example.com` to scan a URL through Puppeteer.
Run `npx impeccable detect --json .` for CI-friendly JSON output.
Run `npx impeccable detect --no-config src/` for a raw scan that ignores project config.
Use `npx impeccable ignores list` to show detector ignores.
Use `npx impeccable ignores add-file "src/legacy/**"` to waive a file pattern.
Use `npx impeccable ignores add-value overused-font Inter --reason "Brand font"` to waive a rule value.
Use an inline comment such as `impeccable-disable overused-font` when the waiver should travel with the file.
The detector respects `.impeccable/config.json` and `.impeccable/config.local.json`.
The shared detector config includes ignored rules, ignored files, ignored values, and design-system awareness.
Hook lifecycle settings affect automatic hooks, not standalone detector config.
Claude Code, GitHub Copilot, and Codex hooks surface findings after direct UI edits.
Cursor uses a pre-write hook that blocks problematic proposed writes.
The release extract says the Chrome extension released version 1.2.1 on 2026-06-19.
The CI behavior captured in the repo extract shows an example with three anti-patterns that exits 1.
The S5c evidence does not state the exact no-finding exit code, so CI policy should verify it in the installed CLI.
Representative AI slop rules target side tabs, side stripes, purple gradients, gradient text, AI color palettes, bounce easing, elastic easing, dark glows, and decorative grid backgrounds.
Representative quality rules target line length, cramped padding, small touch targets, skipped headings, and overused fonts such as Inter and Arial.
Representative color rules target gray text on colored backgrounds and untinted pure black or gray.
Representative structure rules target cards nested in cards.

## Best practice
- State the detector count as 45 only with the 2026-07-07 observation date EVIDENCE-BASED
- Treat the 27 and 44 counts as historical snapshots, not current counts EVIDENCE-BASED
- Use `--json` when detector output feeds CI or a PR comment EVIDENCE-BASED
- Use file ignores for legacy paths that are out of scope for redesign EVIDENCE-BASED
- Use value ignores when a flagged value is a documented brand requirement EVIDENCE-BASED
- Prefer inline disables when the waiver should stay next to the exception EVIDENCE-BASED
- Keep detector waivers narrow so anti-slop coverage stays useful PRACTITIONER
- Re-run detection after changing DESIGN.md or `.impeccable/design.json` because design-system awareness can affect findings PRACTITIONER
- Pair deterministic detection with `/impeccable critique` when hierarchy or emotional resonance needs judgment EVIDENCE-BASED
- Verify exact pass and fail exit behavior in the installed CLI before hard-blocking CI PRACTITIONER

## Pitfalls
Do not flatten the detector and `/impeccable audit` into the same thing.
The detector catches deterministic anti-patterns and quality issues.
The audit command checks broader technical quality such as accessibility, performance, and responsive behavior.
Do not cite "27 rules" or "44 rules" without a historical date.
Do not claim rule 45 existed before CLI 3.2.0 on 2026-07-01.
Do not turn a brand font waiver into a global overused-font waiver unless the brand system really requires it.
Do not rely on prompt-level instructions alone when a detector can run in CI.
Do not ignore hook parser differences across providers.
Codex hook loading was fixed in Skill 3.9.1 after a strict parser issue.
Do not use the Chrome extension as a substitute for CI if the repository needs reviewable build gates.
Do not describe every detector rule by name unless a later capture includes the full canonical list.

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
- [[Impeccable (Toolchain)]] is the skill anchor for the detector.
- [[Deterministic Design Detection]] explains why no LLM checks matter for CI.
- [[Impeccable Audit and Detect]] separates detector output from audit review.
- [[AI Slop]] names the distributional failure the detector targets.
- [[AI Tells (Forbidden Patterns)]] gives the neighboring Taste Skill ban list.
- [[Required Audits]] is the broader audit context in the current vault.
- [[Design Review as Infrastructure]] compares repeatable review layers.
- [[Constraint Beats Coaxing]] explains why detectors supplement prompts.
- [[Impeccable Project Lifecycle]] shows where detect runs in the workflow.
- [[Impeccable Repo and Site]] records release and capture provenance.

## Next actions
- Capture the full detector documentation if a later slice needs every canonical rule name.
- Confirm no-finding and finding exit codes against the installed CLI before writing CI templates.
- Refresh rule count after every CLI release.
- Watch for additional Codex-specific detector rules after rule 45.
