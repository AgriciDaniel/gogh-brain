---
type: "rule"
title: "MIFB Performance Rules"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/rule"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Typography and Numbers Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Review Checklist]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
MIFB Performance Rules capture the skill's transition-property discipline, restrained GPU hints, and minimum interactive hit-area checks.

## What it is

- This rule note covers the MIFB performance reference file.
- The performance reference covers transition specificity and GPU compositing hints.
- The surfaces reference covers the minimum hit area rule.
- The captured SKILL.md includes avoiding `transition: all` as core principle 14.
- The captured SKILL.md includes restrained `will-change` use as core principle 15.
- The captured SKILL.md includes minimum hit area as core principle 16.
- The performance reference says never to use `transition: all`.
- The performance reference says Tailwind's `transition` shorthand maps to `transition-property: all`.
- The performance reference says exact transition properties should be listed.
- The performance reference says `transition-transform` covers transform, translate, scale, and rotate.
- The performance reference says `will-change` can hint pre-promotion to a GPU compositing layer.
- The performance reference says `will-change` can help first-frame stutter.
- The performance reference says modern browsers already optimize many cases.
- The performance reference says each extra compositing layer costs memory.
- The surfaces reference says WCAG uses 44x44px as a hit-area standard.
- The surfaces reference says MIFB requires at least 40x40px in practice.
- The captured SKILL.md says interactive elements need at least 40x40px hit area.
- The captured SKILL.md says pseudo-elements can extend visible controls.
- The captured SKILL.md says extended hit areas must not overlap.

## How it works

- `transition: all` asks the browser to watch every property for changes.
- The performance reference says `transition: all` can animate unintended properties.
- The performance reference says broad transitions can prevent browser optimizations.
- Explicit transition properties restrict work to the properties that actually change.
- Tailwind bracket syntax can express multiple exact transition properties.
- `transition-transform` is appropriate when only transform-related properties change.
- `will-change: transform` is useful for transform animations when first-frame stutter is observed.
- `will-change: transform, opacity` is useful when both properties need compositor preparation.
- The performance reference lists transform as GPU-compositable.
- The performance reference lists opacity as GPU-compositable.
- The performance reference lists filter as GPU-compositable.
- The performance reference lists clip-path as GPU-compositable.
- The performance reference lists top, left, width, and height as not GPU-compositable.
- The performance reference lists background, border, and color as not GPU-compositable.
- A 20x20 checkbox can use a centered pseudo-element to reach a 40x40px hit area.
- The pseudo-element pattern positions the hit target absolutely around the visible control.
- The collision rule shrinks the extension if another interactive element would overlap.
- The collision rule still asks for the largest possible hit area without overlap.

## Best practice

- Specify exact transition properties instead of using `transition: all`. EVIDENCE-BASED
- Avoid Tailwind's generic `transition` shorthand when it maps to all properties. EVIDENCE-BASED
- Use `transition-transform` when only transform, translate, scale, or rotate is changing. EVIDENCE-BASED
- Use bracketed Tailwind transition properties for multiple non-transform properties. EVIDENCE-BASED
- Add `will-change` only after observing first-frame stutter. EVIDENCE-BASED
- Limit `will-change` to compositor-friendly properties such as transform, opacity, filter, and clip-path. EVIDENCE-BASED
- Never use `will-change: all`. EVIDENCE-BASED
- Avoid `will-change` on background, border, color, padding, width, height, top, or left. EVIDENCE-BASED
- Give interactive elements at least a 40x40px hit area, with 44x44px noted as the WCAG standard in the surfaces reference. EVIDENCE-BASED
- Extend small visible controls with pseudo-elements when the visible control is smaller than the hit area. EVIDENCE-BASED
- Prevent overlapping hit areas between adjacent interactive elements. EVIDENCE-BASED
- Keep hit-area expansion as large as possible when collision constraints force a smaller target. EVIDENCE-BASED

## Pitfalls

- Generic transition shorthands can animate padding, colors, or shadows that were not intended to move.
- Broad transitions can make small state changes feel slow or unpredictable.
- Preemptive `will-change` on many elements can increase memory use.
- `will-change: all` is explicitly rejected by the captured performance reference.
- Adding `will-change` to properties the GPU cannot composite does not help the intended performance problem.
- Tiny visible controls can remain hard to use if their hit area is not extended.
- Expanding one hit area over another control can create ambiguous interaction targets.
- Treating the 40x40px MIFB minimum as a replacement for the 44x44px WCAG standard would overstate the source.

## Sources

- Raw GitHub performance reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md, retrieved 2026-07-07.
- Raw GitHub surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.
- Local MIFB claim pack, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: anchors these constraints in the MIFB skill.
- [[MIFB Typography and Numbers Rules]]: connects layout shift prevention to dynamic number rendering.
- [[MIFB Surface and Shadow Rules]]: contains the surfaces reference that defines hit-area expansion.
- [[MIFB Motion and Feedback Rules]]: uses explicit transitions and press-scale feedback.
- [[MIFB Review Checklist]]: checks transition specificity, will-change, and hit areas.
- [[MIFB Performance Rules|Press Feedback and Hit Areas]]: labels the planned S5g concept while this note carries the local evidence.
- [[Optical Alignment]]: complements hit-area work because visible alignment and invisible targets must both feel right.
- [[Jakub Krehel]]: identifies the author of the source article and skill.
- [[MIFB Repo and Skill File]]: stores the performance and surfaces captures.
- [[Required Audits]]: provides the broader vault concept of checks that gate completion.

## Next actions

- Re-check performance.md before changing transition or `will-change` rules.
- Re-check surfaces.md before changing hit-area sizing or collision rules.
- Keep the 40x40px MIFB rule and 44x44px WCAG note distinct.
- Verify Tailwind transition classes in actual code during review.
- Verify pseudo-element hit areas do not overlap adjacent controls.
- Link the future S5g Press Feedback and Hit Areas concept after S5g creates it.
- Keep press feedback values synchronized with [[MIFB Motion and Feedback Rules]].
- Use the MIFB checklist to audit performance constraints after implementation.
