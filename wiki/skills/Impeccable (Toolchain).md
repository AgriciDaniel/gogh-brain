---
type: "skill"
title: "Impeccable (Toolchain)"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/skill"]
domain: "impeccable"
confidence: "evidence-based"
related: ["[[Impeccable Rule Set (45 Detectors)]]", "[[Deterministic Design Detection]]", "[[Impeccable Project Lifecycle]]", "[[Impeccable Audit and Detect]]", "[[Paul Bakaus]]", "[[AI Slop]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
Impeccable is the Gogh stack's toolchain enforcement layer for frontend design agents.

## What it is
Impeccable is an Apache 2.0 design skill and CLI by [[Paul Bakaus]].
The project homepage is impeccable.style.
The repository observation recorded 44.1k stars as of 2026-07-07.
The captured skill version is 3.9.1.
The release capture says Skill 3.9.1 was published on 2026-07-01.
The release capture also says CLI 3.2.0 was published on 2026-07-01.
The captured README describes "1 skill, 23 commands" and 45 deterministic detector rules.
The official site frames the project as "The missing design vocabulary for agents".
Its mechanism category in Gogh is toolchain enforcement.
It also contributes live browser iteration, command vocabulary, design contracts, and no LLM detector checks.
The slice treats its detector findings as upstream Impeccable results, not Gogh-owned findings.
Its install command is `npx impeccable install` from the project root, followed by `/impeccable init` inside the AI coding tool.
The official site also lists `/plugin marketplace add pbakaus/impeccable` for Claude Code and `npx skills add pbakaus/impeccable`.
The capture lists 11 supported providers: Cursor, Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, OpenCode, Pi, Kiro, Trae, Rovo Dev, and Qoder.
Its scope includes websites, landing pages, dashboards, product UI, app shells, components, forms, settings, onboarding, and empty states.
It is not for backend-only or non-UI tasks, according to the captured SKILL.md frontmatter.
Its license is Apache 2.0 in the README and skill frontmatter.
The third-party notices nuance is not expanded in the S5c evidence pack, so this note does not infer bundled dependency licenses.

## How it works
Impeccable starts with `/impeccable init`.
The init flow writes `PRODUCT.md` and offers `DESIGN.md` so later commands share design context.
The design context records audience, brand or product lane, voice, anti-references, colors, type, and components.
The captured SKILL.md requires a context script before design work so the agent reads the project's PRODUCT.md and DESIGN.md when present.
The skill then routes work through `/impeccable <command> <target>`.
The 23 commands cover build, evaluate, refine, enhance, fix, and iterate work.
The detector runs separately through `npx impeccable detect`.
The detector can scan a source directory, an HTML file, or a URL.
The detector can output JSON for CI.
The detector can ignore configured rules, files, or values.
The installer can place provider-native hooks into Claude Code, GitHub Copilot, Cursor, and Codex surfaces.
Claude Code, GitHub Copilot, and Codex surface findings after edits.
Cursor blocks problematic proposed writes before they land.
The live command works against a running dev server.
The official site says live mode swaps three production-quality variants through HMR and writes edits back to source files.
The release capture says rule 45 was added by CLI 3.2.0 on 2026-07-01.
The missing changelog capture says there is no repository CHANGELOG file in the 2026-07-07 tree.
Version information is instead in release pages and skill frontmatter.
When to reach for it in the stack: choose Impeccable when contracts, deterministic detector checks, hooks, or live variant iteration matter.
Do not use Impeccable as the only taste source when the project still needs broad aesthetic direction.
Pair it with Anthropic frontend-design or [[Taste Skill (Project)]] when the project needs taste prompting before enforcement.
Pair it with UI UX Pro Max when the work needs retrieval-backed style or UX databases before command execution.
Pair it with Vercel web design guidelines when the work needs a separate audit surface after implementation.

## Best practice
- Run `/impeccable init` before design commands so PRODUCT.md and DESIGN.md exist as context EVIDENCE-BASED
- Treat the 44.1k star count as a dated observation from 2026-07-07 EVIDENCE-BASED
- Treat Skill 3.9.1 and CLI 3.2.0 as separate version observations from 2026-07-01 EVIDENCE-BASED
- Use `npx impeccable detect --json .` when the result needs to feed CI or a PR gate EVIDENCE-BASED
- Use provider hooks when edit-time feedback matters more than after-the-fact review EVIDENCE-BASED
- Use Cursor hook behavior when pre-write blocking is desired and the project uses Cursor EVIDENCE-BASED
- Keep `.impeccable/design.json` tracked because the README lists it as a shared artifact EVIDENCE-BASED
- Keep screenshots, caches, and live sessions out of git because the README marks them ephemeral EVIDENCE-BASED
- Pair Impeccable with a taste-prompting skill when the project lacks aesthetic direction PRACTITIONER
- Do not treat early v1.x token-cost anecdotes as current v3.9.1 architecture evidence CONTESTED

## Pitfalls
Counts stale quickly in this ecosystem.
Third-party material recorded 27 detector rules in May 2026 and 44 rules at v3.0.3.
The release capture confirms 45 rules on 2026-07-01.
A cached rule count other than 45 is stale for the 2026-07-07 capture.
The skill, CLI, and Chrome extension have separate versions.
The token-cost anecdote in the claim pack describes March 2026 v1.x architecture, not the captured v3.9.1 compiled skill.
The project has a website changelog, but no repository CHANGELOG.md was captured.
The detector is deterministic, but the skill also has LLM-only critique checks.
The exact no-finding exit code is not stated in the S5c capture; the failing example exits 1.
Codex users must approve the project hook through `/hooks` after install or update.
Manual copy commands exist, but the README calls `npx impeccable install` and `npx impeccable update` the normal path.
Opinionated defaults can conflict with existing design systems, according to practitioner reception.

## Sources
- GitHub repo, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Impeccable official site, https://impeccable.style/, retrieved 2026-07-07.
- GitHub releases, https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07.
- computertech.co review, https://computertech.co/impeccable-ai-review/, retrieved 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-impeccable.md, generated 2026-07-07.
- Local raw README capture, .raw/skills/impeccable/README.md, retrieved 2026-07-07.
- Local raw SKILL.md capture, .raw/skills/impeccable/SKILL.md, retrieved 2026-07-07.
- Local missing changelog capture, .raw/skills/impeccable/MISSING-CHANGELOG.md, checked 2026-07-07.

## Related
Rules:
- [[Impeccable Rule Set (45 Detectors)]] records the deterministic detector surface.
- [[AI Tells (Forbidden Patterns)]] gives the adjacent anti-slop vocabulary in Taste Skill.
- [[Anthropic Frontend Design Rules]] is the upstream rule context Impeccable says it started from.
Audits:
- [[Impeccable Audit and Detect]] separates `/impeccable audit` from `npx impeccable detect`.
- [[Required Audits]] explains the broader Gogh audit posture.
Flows:
- [[Impeccable Project Lifecycle]] maps all 23 commands to the lifecycle.
- [[Ecosystem and Alternatives]] helps decide when to add Impeccable to a stack.
Sources:
- [[Impeccable Repo and Site]] is the S5c source provenance note.
- [[Reception Sources]] holds broader ecosystem reception context.
Entities:
- [[Paul Bakaus]] is the author entity.
- [[Coding Agents]] names the agent harness audience.

## Next actions
- Refresh the GitHub repo, official site, and release page after the next Impeccable release.
- Confirm whether the website changelog exposes structured release data that should be captured later.
- Keep token-cost claims linked to [Impeccable Setup Token Cost](../questions/Impeccable%20Setup%20Token%20Cost.md) and [Impeccable Token Cost Measurement](../experiments/Impeccable%20Token%20Cost%20Measurement.md) when S5h lands.
- Re-run the vault linter after other slices create their registry notes.
