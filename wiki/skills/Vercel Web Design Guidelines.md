---
type: "skill"
title: "Vercel Web Design Guidelines"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/web-design-guidelines", "note/skill"]
domain: "web-design-guidelines"
confidence: "evidence-based"
related: ["[[Vercel Interface Rule Categories]]", "[[Runtime Rule Fetch]]", "[[Vercel Guidelines Audit]]", "[[Agent Skills Format]]", "[[Required Audits]]", "[[Design Review as Infrastructure]]"]
source_urls: ["https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://api.github.com/repos/vercel-labs/agent-skills (retrieved 2026-07-07)", "https://api.github.com/repos/vercel-labs/web-interface-guidelines (retrieved 2026-07-07)", "https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines (retrieved 2026-07-07)"]
sources: ["[[Vercel Web Design Guidelines Sources]]"]
---
Vercel Web Design Guidelines is Gogh's runtime-fetched audit skill for checking existing UI code against Vercel's Web Interface Guidelines.

## What it is
Vercel web-design-guidelines ships in the vercel-labs/agent-skills repository.
The source ledger records vercel-labs/agent-skills as Vercel's official agent-skills collection.
The parent repository was created on 2025-12-08.
The parent repository had 28,766 stars as of 2026-07-07.
GitHub detected no license file on the parent repository as of 2026-07-07.
The captured wrapper SKILL.md declares metadata author `vercel`.
The captured wrapper SKILL.md declares version `1.0.0`.
The captured wrapper SKILL.md declares argument hint `<file-or-pattern>`.
The skill triggers on UI review, accessibility check, design audit, and UX review requests.
Its mechanism category in Gogh is audit with runtime rule fetch.
The wrapper is roughly 400 words in the 2026-07-07 claim pack.
The wrapper contains the audit procedure but not the substantive rule inventory.
The rule inventory lives in vercel-labs/web-interface-guidelines.
The ruleset repository was created on 2025-09-10.
The ruleset repository had 697 stars as of 2026-07-07.
The ruleset repository is MIT licensed by GitHub detection as of 2026-07-07.
The wrapper capture records README-declared MIT for the wrapper and no LICENSE file.
The install command is `npx skills add vercel-labs/agent-skills --skill web-design-guidelines`.
The skills.sh registry reported 443.8K installs for this skill as of 2026-07-07.
The skill is an audit skill, not a generation skill.
The skill produces findings on existing files instead of choosing aesthetic direction.
Reach for it after implementation when a UI needs accessibility, UX, performance, and interaction checks.

## How it works
The wrapper instructs the agent to fetch the rules fresh before each review.
The exact rules URL is `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`.
The wrapper names WebFetch as the retrieval mechanism for the current rules.
After fetching rules, the agent reads the user-specified files or patterns.
After reading files, the agent checks every fetched rule against those files.
If the user provides no files, the wrapper instructs the agent to ask which files to review.
The fetched command document defines both the rule list and the output format.
The command document groups findings by file.
The command document uses `file:line` findings so editors can make locations clickable.
The command document marks compliant files with an explicit pass marker.
The command document asks for terse wording and no preamble.
The command document says explanations are only needed when a fix is non-obvious.
The rule substance covers accessibility, focus, forms, animation, typography, content, images, performance, navigation, touch, safe areas, dark mode, locale, hydration, hover states, copy, and anti-pattern flags.
The runtime fetch means guideline changes in the ruleset repository can affect later audits without reinstalling the wrapper.
The runtime fetch also means a review result depends on the rules available at audit time.
The wrapper scope is the files or patterns named by the user.
The wrapper does not claim to inspect routes, builds, screenshots, or rendered pages by itself.
The wrapper pairs naturally with [[Impeccable (Toolchain)]] because Impeccable contributes deterministic detectors and Vercel contributes guideline review.
The wrapper pairs naturally with [[Taste Skill (Project)]] because Taste Skill provides taste direction before a Vercel audit checks shipped interface details.

> [!contradiction]
> License records differ in emphasis: the raw wrapper capture says README-declared MIT, while THIRD_PARTY_NOTICES treats the missing wrapper LICENSE file as a packaging risk.

## Best practice
- Fetch the rules document fresh before every Vercel guidelines review EVIDENCE-BASED
- Record the retrieval date when citing a Vercel rule count EVIDENCE-BASED
- Use the exact install command from the captured wrapper when installing the skill EVIDENCE-BASED
- Provide explicit file paths or globs so the wrapper does not need to ask for targets EVIDENCE-BASED
- Treat `file:line` findings as the output contract for downstream triage EVIDENCE-BASED
- Place this audit after implementation, not before aesthetic direction PRACTITIONER
- Pair it with [[Pre-Flight Check (Section 14)]] when a Taste Skill build needs a blocking pre-flight and a guideline audit PRACTITIONER
- Pair it with [[Impeccable Audit and Detect]] when deterministic anti-pattern detection is also needed PRACTITIONER
- Treat skills.sh install counts as registry-reported dated observations EVIDENCE-BASED
- Avoid copying wrapper prose into releases until the license nuance is resolved CONTESTED

## Pitfalls
Do not treat the wrapper file as the ruleset.
Do not bake a stale copy of command.md into a note without a retrieval date.
Do not say the wrapper repository has a GitHub-detected MIT license.
Do not ignore the local third-party notice that treats the wrapper as risky because no LICENSE file was detected.
Do not call the skill a generator.
Do not call the skill an automated browser audit.
Do not claim visual rendering coverage beyond the code files actually reviewed.
Do not claim the 443.8K skills.sh installs are independently audited.
Do not compare the install count directly with skills that distribute outside skills.sh.
Do not conflate Vercel's ruleset with unrelated Web Interface Guidelines projects.
Do not remove the output contract from summaries, because file:line findings are central to the skill.

## Sources
- Vercel Labs raw wrapper, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Vercel Labs raw ruleset, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- GitHub API for agent-skills, https://api.github.com/repos/vercel-labs/agent-skills, retrieved 2026-07-07.
- GitHub API for web-interface-guidelines, https://api.github.com/repos/vercel-labs/web-interface-guidelines, retrieved 2026-07-07.
- skills.sh registry page, https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines, retrieved 2026-07-07.
- Local extract, .raw/research/vercel-web-design-guidelines-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.
- Local third-party notice, THIRD_PARTY_NOTICES.md, verified 2026-07-07.

## Related
Rules:
- [[Vercel Interface Rule Categories]] is the captured category inventory for this skill.
- [[Anthropic Frontend Design Rules]] is an adjacent taste-prompting rule surface.
- [[Impeccable Rule Set (45 Detectors)]] is the deterministic detector contrast.
- [[MIFB Performance Rules]] overlaps with Vercel's performance-oriented checks.
Audits:
- [[Vercel Guidelines Audit]] is the runbook for applying this skill.
- [[Required Audits]] places this review in the larger Gogh audit posture.
- [[Pre-Flight Check (Section 14)]] is the Taste Skill blocking pre-flight peer.
- [[Impeccable Audit and Detect]] is the Impeccable audit peer.
Concepts:
- [[Runtime Rule Fetch]] explains the live ruleset mechanism.
- [[Agent Skills Format]] explains the SKILL.md distribution surface.
- [[Design Review as Infrastructure]] explains why reusable review checklists matter.
- [[Deterministic Design Detection]] explains the compiled-detector alternative.
Sources:
- [[Vercel Web Design Guidelines Sources]] is the provenance note for this slice.
- [[Reception Sources]] provides broader ecosystem reception context.
Entities:
- [[Coding Agents]] names the agent harness audience for the skill.

## Next actions
- Refresh the wrapper and command.md captures before any market-ready release.
- Re-check the wrapper repository license state before reproducing wrapper prose.
- Re-check skills.sh installs before using the 443.8K observation in a deliverable.
- Re-run this audit after upstream command.md changes because reviews fetch live rules.
