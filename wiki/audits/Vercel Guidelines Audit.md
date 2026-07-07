---
type: "audit"
title: "Vercel Guidelines Audit"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/web-design-guidelines", "note/audit"]
domain: "web-design-guidelines"
confidence: "evidence-based"
related: ["[[Vercel Web Design Guidelines]]", "[[Vercel Interface Rule Categories]]", "[[Runtime Rule Fetch]]", "[[Required Audits]]", "[[Pre-Flight Check (Section 14)]]", "[[Impeccable Audit and Detect]]"]
source_urls: ["https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines (retrieved 2026-07-07)", "https://api.github.com/repos/vercel-labs/web-interface-guidelines (retrieved 2026-07-07)"]
sources: ["[[Vercel Web Design Guidelines Sources]]"]
---
Vercel Guidelines Audit is the practical runbook for applying the runtime-fetched Vercel Web Interface Guidelines to specific UI files.

## What it is
The audit is triggered by UI review, accessibility check, design audit, or UX review tasks.
The captured wrapper expects a file or pattern argument.
The captured wrapper tells the agent to ask for files if no targets are specified.
The audit checks existing files rather than generating a new interface.
The audit uses the rules fetched from vercel-labs/web-interface-guidelines command.md.
The audit covers accessibility through labels, semantic elements, focus, keyboard handling, alt text, live regions, headings, and anchor scroll margins.
The audit covers UX through forms, navigation state, destructive action confirmation, touch behavior, hover states, content handling, and copy specificity.
The audit covers performance through list virtualization, compositor-friendly animation, layout-read avoidance, preconnect, font preload, image dimensions, and lazy or priority image loading.
The audit covers rendering safety through dark mode, safe areas, locale formatting, hydration, and image layout stability.
The audit output is grouped by file.
The audit output uses `file:line` findings.
The audit output marks files as pass when no findings are present.
The audit output omits preamble.
The audit output explains only non-obvious fixes.
The audit sits after implementation in the Gogh pipeline.
The audit complements [[Pre-Flight Check (Section 14)]] because Section 14 is a Taste Skill completion gate.
The audit complements [[Impeccable Audit and Detect]] because Impeccable has deterministic detector and command surfaces.

## How it works
Install the skill with `npx skills add vercel-labs/agent-skills --skill web-design-guidelines`.
Invoke the skill with a concrete UI file or glob pattern.
The wrapper fetches `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`.
The wrapper reads the requested files.
The wrapper applies all fetched rules.
The output section in command.md defines the report shape.
Each file gets its own heading.
Each finding starts with the file path and line number.
Each finding states the issue at that location.
Compliant files receive an explicit pass marker.
The report should be concise but comprehensive.
The report should keep high signal-to-noise.
The report should skip explanation when a fix is obvious.
The report should include explanation only when the fix is non-obvious.
The report should not add a preamble.
For audit pipeline order, use taste direction and implementation before this audit.
For Taste Skill work, run [[Pre-Flight Check (Section 14)]] before claiming completion.
For Impeccable work, run [[Impeccable Audit and Detect]] when deterministic anti-pattern detection is needed.
For Vercel work, run this audit when code-level accessibility, UX, performance, and interaction rules need file:line findings.
For release-sensitive work, record the command.md retrieval date in the audit notes.
For CI-sensitive work, consider pinning or archiving the fetched ruleset before comparing results across runs.

## Best practice
- Provide target files or patterns with the audit request EVIDENCE-BASED
- Fetch command.md before applying rules EVIDENCE-BASED
- Keep findings grouped by file EVIDENCE-BASED
- Use `file:line` findings for editor-clickable triage EVIDENCE-BASED
- Mark clean files as pass EVIDENCE-BASED
- Skip preamble in the audit output EVIDENCE-BASED
- Explain only non-obvious fixes EVIDENCE-BASED
- Run the audit after implementation or redesign changes PRACTITIONER
- Run [[Pre-Flight Check (Section 14)]] for Taste Skill completion gating PRACTITIONER
- Run [[Impeccable Audit and Detect]] when deterministic detector coverage is needed PRACTITIONER

## Pitfalls
Do not run the audit without target files unless the agent first asks for them.
Do not summarize findings without line numbers when the output contract requires file:line.
Do not add a long preamble before findings.
Do not treat a pass marker as proof that rendered screenshots were inspected.
Do not treat the Vercel audit as a substitute for accessibility testing with assistive technologies.
Do not treat the Vercel audit as a substitute for performance profiling.
Do not treat the Vercel audit as a substitute for Impeccable's deterministic detector.
Do not treat the Vercel audit as a substitute for Taste Skill's aesthetic pre-flight.
Do not use stale rule counts in audit reports.
Do not omit the retrieval date when the audit result is used as release evidence.
Do not claim the ruleset covers backend or non-UI work.

## Sources
- Vercel Labs raw wrapper, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Vercel Labs raw ruleset, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- skills.sh registry page, https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines, retrieved 2026-07-07.
- GitHub API for web-interface-guidelines, https://api.github.com/repos/vercel-labs/web-interface-guidelines, retrieved 2026-07-07.
- Local extract, .raw/research/vercel-web-design-guidelines-extract.md, captured 2026-07-07.
- Local Vercel claim pack, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.

## Related
- [[Vercel Web Design Guidelines]] is the skill anchor for this audit.
- [[Vercel Interface Rule Categories]] is the category inventory used by this audit.
- [[Runtime Rule Fetch]] explains why the audit fetches command.md at review time.
- [[Required Audits]] places the audit in the larger Gogh gate set.
- [[Pre-Flight Check (Section 14)]] is the Taste Skill pre-completion peer.
- [[Impeccable Audit and Detect]] is the deterministic detector peer.
- [[MIFB Performance Rules]] overlaps with performance and animation review points.
- [[MIFB Motion and Feedback Rules]] overlaps with animation and interaction review points.
- [[Design Review as Infrastructure]] explains why the audit should be repeatable.
- [[Coding Agents]] names the agent harness audience.

## Next actions
- Add a sample Vercel audit report after the integration wave provides stable target files.
- Re-run the audit after command.md changes upstream.
- Capture the fetched command.md retrieval date in future audit outputs.
- Keep pipeline ordering explicit in stack decision deliverables.
