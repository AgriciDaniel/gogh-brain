---
type: "audit"
title: "MIFB Review Checklist"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/audit"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Typography and Numbers Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/typography.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
MIFB Review Checklist turns the skill's 14 review items, common mistake fixes, and Before and After output format into a repeatable audit note.

## What it is

- This audit note covers the review checklist captured in the MIFB SKILL.md.
- The captured SKILL.md checklist has 14 items.
- The captured SKILL.md common mistakes table has 10 rows.
- The captured SKILL.md review output format requires markdown tables.
- The output table uses Before and After columns.
- The output groups changes by principle using a heading above each table.
- Each row should focus on a single diff.
- Rows should cite the specific file and property when the changed property is not obvious.
- A principle that was reviewed but did not need a change should not get an empty table.
- The checklist spans surfaces, typography, motion, performance, and hit areas.
- The checklist starts with nested rounded elements.
- The checklist includes optical centering.
- The checklist includes shadows instead of borders.
- The checklist includes split and staggered enters.
- The checklist includes subtle exits.
- The checklist includes dynamic numbers.
- The checklist includes font smoothing.
- The checklist includes heading balance.
- The checklist includes image outlines.
- The checklist includes button press scale.
- The checklist includes `AnimatePresence` page-load behavior.
- The checklist includes exact transition properties.
- The checklist includes restrained `will-change`.
- The checklist includes 40x40px hit areas.

## How it works

- The audit reads UI changes through the MIFB principles rather than through a generic bug list.
- The audit reports only the principles where changes were made.
- The audit uses headings such as Concentric border radius, Tabular numbers, or Scale on press.
- The audit table puts the old state in the Before column.
- The audit table puts the corrected state in the After column.
- The audit table can include code snippets when the change is easiest to scan as code.
- The audit should include every change made, not only a sample.
- The audit omits empty principle tables to reduce noise.
- The checklist item for nested rounded elements maps to concentric border radius.
- The checklist item for icons maps to optical alignment.
- The checklist item for shadows maps to the shadow-over-border rule.
- The checklist item for enter animations maps to split and stagger guidance.
- The checklist item for exits maps to subtle exit guidance.
- The checklist item for dynamic numbers maps to `tabular-nums`.
- The checklist item for font smoothing maps to root `antialiased`.
- The checklist item for headings maps to `text-wrap: balance`.
- The checklist item for images maps to pure black or white low-opacity outlines.
- The checklist item for buttons maps to `scale(0.96)`.
- The checklist item for `AnimatePresence` maps to `initial={false}`.
- The checklist item for transitions maps to exact transition properties.
- The checklist item for `will-change` maps to transform, opacity, and filter constraints.
- The checklist item for interactive controls maps to at least 40x40px hit areas.

## Best practice

- Use this checklist after applying or reviewing MIFB changes. EVIDENCE-BASED
- Group review output by principle instead of listing isolated findings. EVIDENCE-BASED
- Use a markdown table with Before and After columns for each changed principle. EVIDENCE-BASED
- Keep each table row focused on one diff. EVIDENCE-BASED
- Cite the file and property when the property change is not clear from the snippet. EVIDENCE-BASED
- Include every MIFB change made during the pass. EVIDENCE-BASED
- Omit a principle table when that principle was reviewed but did not need changes. EVIDENCE-BASED
- Use the common mistakes table as a quick correction map during review. EVIDENCE-BASED
- Verify both visible polish and invisible interaction targets. EVIDENCE-BASED
- Keep the audit scoped to MIFB craft details rather than full product strategy. EVIDENCE-BASED

## Pitfalls

- Listing Before and After as separate lines violates the captured review output format.
- Reporting only a subset of changes violates the captured review output format.
- Empty tables add noise according to the captured SKILL.md.
- A checklist pass can miss accessibility if it checks visible controls but not hit-area collisions.
- A motion pass can miss page-load noise if it skips the `AnimatePresence` item.
- A typography pass can miss layout shift if it checks wrapping but not tabular numbers.
- A surface pass can miss image quality if it checks cards but not image outlines.
- A performance pass can miss broad Tailwind transitions if it only searches for literal `transition: all`.

| Mistake | Fix |
| --- | --- |
| Same border radius on parent and child | Calculate `outerRadius = innerRadius + padding` |
| Icons look off-center | Adjust optically with padding or fix SVG directly |
| Hard borders between sections | Use layered `box-shadow` with transparency |
| Jarring enter/exit animations | Split, stagger, and keep exits subtle |
| Numbers cause layout shift | Apply `tabular-nums` |
| Heavy text on macOS | Apply `antialiased` to root |
| Animation plays on page load | Add `initial={false}` to `AnimatePresence` |
| `transition: all` on elements | Specify exact properties |
| First-frame animation stutter | Add `will-change: transform` sparingly |
| Tiny hit areas on small controls | Extend with pseudo-element to 40x40px |

## Sources

- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Raw GitHub typography reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/typography.md, retrieved 2026-07-07.
- Raw GitHub surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- Raw GitHub animations reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md, retrieved 2026-07-07.
- Raw GitHub performance reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: anchors the checklist in the skill.
- [[MIFB Typography and Numbers Rules]]: supplies the wrapping, smoothing, and number checks.
- [[MIFB Surface and Shadow Rules]]: supplies the radius, shadow, image, and optical checks.
- [[MIFB Motion and Feedback Rules]]: supplies the enter, exit, icon, and press checks.
- [[MIFB Performance Rules]]: supplies the transition, will-change, and hit-area checks.
- [[Optical Alignment]]: expands the icon centering item.
- [[Jakub Krehel]]: identifies the author of the source skill and article.
- [[MIFB Repo and Skill File]]: stores the captured checklist and source dates.
- [[Required Audits]]: provides the broader vault framing for audit gates.
- [[Pre-Flight Check (Section 14)]]: contrasts Taste Skill's blocking gate with MIFB's review checklist.

## Next actions

- Re-check SKILL.md before changing the 14 checklist items.
- Re-check SKILL.md before changing the 10 common-mistakes rows.
- Use this checklist after editing components with MIFB guidance.
- Keep output in Before and After tables when documenting changes.
- Add file and property details when snippets alone are ambiguous.
- Keep MIFB review separate from full-stack product audits.
- Synchronize checklist items with the four MIFB rule notes after refreshes.
- Avoid adding unchecked checklist items without source evidence.
