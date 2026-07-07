---
type: "audit"
title: "Impeccable Audit and Detect"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/audit"]
domain: "impeccable"
confidence: "evidence-based"
related: ["[[Impeccable (Toolchain)]]", "[[Impeccable Rule Set (45 Detectors)]]", "[[Deterministic Design Detection]]", "[[Required Audits]]", "[[Pre-Flight Check (Section 14)]]", "[[AI Tells (Forbidden Patterns)]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
Impeccable has two audit surfaces: `/impeccable audit` for technical quality review and `npx impeccable detect` for deterministic detector gating.

## What it is
`/impeccable audit` is one of the 23 Impeccable commands.
The README says it runs technical quality checks.
Those checks include accessibility, performance, and responsive behavior.
`npx impeccable detect` is the standalone detector CLI.
The README says the detector catches 45 deterministic issues.
Those issues cover AI slop and general design quality.
The detector runs without an LLM and without an API key.
The detector can run outside an AI harness.
The detector can be used in CI.
The repo extract says detector JSON output and build-readable exit codes support CI and PR gates.
The repo extract records a failing example with three anti-patterns that exits 1.
The S5c evidence does not state the exact no-finding exit code.
This note therefore treats exit 1 as the documented failing example and recommends local verification for pass behavior.
The two surfaces are complementary.
Audit is broader and command-driven.
Detect is narrower, deterministic, and automation-friendly.

## How it works
Use `/impeccable audit <target>` inside the AI coding tool.
The target can scope the audit to a blog, header, checkout flow, or other interface area.
The audit command belongs to the evaluate category in the captured SKILL.md.
Use `npx impeccable detect src/` to scan a directory.
Use `npx impeccable detect index.html` to scan an HTML file.
Use `npx impeccable detect https://example.com` to scan a rendered URL.
Use `npx impeccable detect --json .` to produce machine-readable output.
Use `npx impeccable detect --no-config src/` to ignore project config.
Use `npx impeccable ignores list` to inspect waivers.
Use `npx impeccable ignores add-file "src/legacy/**"` to exclude legacy paths.
Use `npx impeccable ignores add-value overused-font Inter --reason "Brand font"` to allow a brand-specific value.
Use inline disable comments when the waiver should travel with the file.
The detector reads `.impeccable/config.json` and `.impeccable/config.local.json` detector settings by default.
The hook and detector share detector ignore configuration.
Hook lifecycle settings such as `hook.enabled` only affect automatic hooks.
The audit command can find issues that require model judgment.
The detector can catch fixed patterns that do not require model judgment.
CI should call the detector, not the slash command.
Design review should use both when the project needs deterministic gates and broader UX judgment.

## Best practice
- Use `/impeccable audit` for accessibility, performance, and responsive review EVIDENCE-BASED
- Use `npx impeccable detect` for deterministic anti-pattern checks EVIDENCE-BASED
- Use detector JSON output in CI EVIDENCE-BASED
- Treat the documented failing detector example as exit 1 EVIDENCE-BASED
- Verify the no-finding exit code locally before publishing CI policy PRACTITIONER
- Use narrow ignores with reasons when brand or legacy constraints require exceptions PRACTITIONER
- Keep audit and detect results separate in reports EVIDENCE-BASED
- Run detect before final polish when anti-slop issues should not reach review PRACTITIONER
- Run audit after major responsive or performance changes EVIDENCE-BASED
- Pair Impeccable audit with Vercel Guidelines Audit when a second audit surface is required PRACTITIONER

## Pitfalls
Do not call `/impeccable audit` a no LLM detector.
The no LLM claim belongs to the deterministic detector.
Do not call `npx impeccable detect` a full UX critique.
The detector catches deterministic issues.
Do not hard-code exit behavior beyond the captured failing example without local CLI verification.
Do not let waivers hide broad sections of new work.
Do not use `--no-config` in CI unless the project intentionally wants raw scan behavior.
Do not forget that hook findings and detect findings share detector ignore configuration.
Do not treat a passing detector run as proof that hierarchy, clarity, and resonance are good.
Use `critique` for those judgment categories.
Do not ignore stale detector counts in old third-party articles.
Use 45 rules as of the 2026-07-07 capture.

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
- [[Impeccable (Toolchain)]] is the skill anchor.
- [[Impeccable Rule Set (45 Detectors)]] names the deterministic detector rule set.
- [[Deterministic Design Detection]] explains why the detector fits CI.
- [[Required Audits]] gives the broader Gogh audit posture.
- [[Design Review as Infrastructure]] shows where audit gates sit in the stack.
- [[Em-dash audit]] is an adjacent focused audit in the current vault.
- [[Hero discipline audit]] covers hero review outside Impeccable.
- [[Pre-Flight Check (Section 14)]] is the Taste Skill blocking audit.
- [[Rules and Audits Reference Card]] should eventually consolidate these checks.
- [[Impeccable Repo and Site]] records source provenance.

## Next actions
- Verify installed CLI exit codes for pass and fail cases.
- Capture detector docs if future CI guidance needs full rule identifiers.
- Compare `/impeccable audit` findings with Vercel Guidelines findings on a sample app.
- Record any detector waivers in a project decision note when Gogh gains mutation approvals.
