---
type: "concept"
title: "Runtime Rule Fetch"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/web-design-guidelines", "note/concept"]
domain: "web-design-guidelines"
confidence: "evidence-based"
related: ["[[Vercel Web Design Guidelines]]", "[[Vercel Interface Rule Categories]]", "[[Vercel Guidelines Audit]]", "[[Agent Skills Format]]", "[[Deterministic Design Detection]]", "[[Taste Skill (Project)]]"]
source_urls: ["https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Vercel Web Design Guidelines Sources]]", "[[Impeccable Repo and Site]]", "[[Canonical Skill File]]"]
---
Runtime Rule Fetch is the pattern where a skill retrieves its operative rules at review time instead of packaging those rules inside the skill wrapper.

## What it is
The captured Vercel wrapper uses runtime rule fetch.
The wrapper tells the agent to fetch the latest rules before each review.
The fetch target is the raw command.md file in vercel-labs/web-interface-guidelines.
The wrapper says the fetched content contains all rules and output format instructions.
The wrapper itself stays small because command.md carries the rule substance.
The 2026-07-07 claim pack describes the wrapper as roughly 400 words.
The 2026-07-07 claim pack describes the skill as a thin fetch-and-audit shim.
The runtime fetch mechanism makes the ruleset repository the single source of truth for reviews.
The pattern gives fresh guidelines without reinstalling the wrapper.
The pattern also creates drift risk because wrapper behavior and fetched rule content can change on different schedules.
The pattern differs from static SKILL.md guidance.
The pattern differs from compiled detector logic.
In Gogh's mechanism map, Vercel is an audit layer with runtime-fetched rules.
In the same mechanism map, [[Impeccable (Toolchain)]] is toolchain enforcement with deterministic detector rules.
In the same mechanism map, [[Taste Skill (Project)]] is taste prompting with a large static SKILL.md rulebook.

## How it works
The user asks for a UI review, accessibility check, design audit, or UX review.
The agent activates the Vercel wrapper through the skill description.
The wrapper directs the agent to WebFetch command.md from the raw GitHub URL.
The fetched command.md supplies the current rules.
The fetched command.md supplies the file:line output contract.
The agent then reads the requested project files.
The agent checks those files against the fetched categories and rules.
The agent reports findings grouped by file.
The agent marks a file as passing when it has no findings.
If upstream command.md changes, the next compliant runtime fetch can use the changed rules.
If the wrapper changes but command.md does not, the audit procedure can change while rule content stays stable.
If command.md changes but the wrapper does not, rule content can change while the wrapper version remains 1.0.0.
That separation is useful for freshness.
That separation is risky for reproducibility.
The local extract records that the guidelines repo last pushed on 2026-04-06.
The local extract records that the wrapper remained at version 1.0.0 in the 2026-07-07 capture.
The local extract describes the observed cadence as multi-month document revisions.
The pattern can fit interactive review because a fresh fetch is acceptable during a human-guided audit.
The pattern needs extra care in CI because network availability and upstream edits can change results.
The pattern can be made more reproducible by recording the retrieval date and fetched content hash in CI logs.
That reproducibility step is an engineering inference from the runtime fetch mechanism.

> [!key-insight]
> Runtime fetch trades local determinism for freshness, so reviews need retrieval dates when findings matter later.

## Best practice
- Fetch command.md at review time when following the Vercel wrapper EVIDENCE-BASED
- Record the exact retrieval date for any cited Vercel rule EVIDENCE-BASED
- Treat wrapper version 1.0.0 as separate from command.md content EVIDENCE-BASED
- Treat a ruleset change as possible even when the wrapper version has not changed EVIDENCE-BASED
- Store a fetched ruleset snapshot or hash when a CI audit must be reproducible PRACTITIONER
- Prefer the live fetch for interactive reviews where freshness matters PRACTITIONER
- Prefer a pinned capture for release gates where repeatability matters PRACTITIONER
- Contrast Vercel findings with [[Deterministic Design Detection]] when explaining detector confidence PRACTITIONER
- Contrast Vercel's live rules with [[Taste Skill (Project)]] when explaining static skill guidance PRACTITIONER
- Do not imply that runtime fetch proves a rendered UI was tested EVIDENCE-BASED

## Pitfalls
Runtime fetch can hide rule drift if the audit report omits the retrieval date.
Runtime fetch can make two audits disagree even when the reviewed code did not change.
Runtime fetch can fail in network-restricted agent environments.
Runtime fetch can complicate CI because the audit depends on a remote document.
Runtime fetch can make old notes stale when command.md adds, removes, or renames categories.
Wrapper version 1.0.0 does not freeze command.md.
A ruleset repository MIT license does not automatically settle the wrapper repository license nuance.
Runtime-fetched guidance is not the same as deterministic detector execution.
Runtime-fetched guidance is not the same as static taste prompting.
Runtime-fetched guidance still requires the agent to read the target files and apply judgment.

## Sources
- Vercel Labs raw wrapper, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Vercel Labs raw ruleset, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- Impeccable repo, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Taste Skill raw SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Local extract, .raw/research/vercel-web-design-guidelines-extract.md, captured 2026-07-07.
- Local Vercel claim pack, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.
- Local ecosystem claim pack, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.

## Related
- [[Vercel Web Design Guidelines]] is the skill that uses runtime fetch.
- [[Vercel Interface Rule Categories]] is the fetched ruleset's category map.
- [[Vercel Guidelines Audit]] explains how runtime fetch becomes a review workflow.
- [[Agent Skills Format]] explains why SKILL.md wrappers can delegate to external files.
- [[Deterministic Design Detection]] is the compiled-detector contrast.
- [[Impeccable (Toolchain)]] is the toolchain enforcement contrast.
- [[Taste Skill (Project)]] is the static taste-rulebook contrast.
- [[Design Review as Infrastructure]] explains why reusable review contracts matter.
- [[Required Audits]] explains where live and pinned audits may be gated.
- [[AI Slop]] is the broader problem these rule surfaces try to reduce.

## Next actions
- Add retrieval-date fields to future Vercel audit reports.
- Consider a pinned command.md capture for release-critical audits.
- Revisit this note after any upstream wrapper version change.
- Revisit this note after any command.md category change.
