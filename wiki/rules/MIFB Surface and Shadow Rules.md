---
type: "rule"
title: "MIFB Surface and Shadow Rules"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/rule"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Typography and Numbers Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
MIFB Surface and Shadow Rules capture the skill's radius math, optical alignment, depth shadows, image outlines, and surface edge guidance.

## What it is

- This rule note covers the MIFB surfaces reference file.
- The surfaces reference covers border radius, optical alignment, shadows, and image outlines.
- The captured SKILL.md maps surfaces to border radius, optical alignment, shadows, image outlines, and hit areas.
- Concentric border radius is the first core principle in the captured SKILL.md.
- The formula is `outerRadius = innerRadius + padding`.
- The surfaces reference says the rule is most useful when nested surfaces are close together.
- The surfaces reference says padding larger than 24px should be treated as separate surfaces.
- The SKILL.md says mismatched nested radii are a common reason interfaces feel off.
- The Krehel article extract gives a worked example where outer 20px equals inner 12px plus padding 8px.
- Optical alignment is part of the surfaces reference and is expanded in [[Optical Alignment]].
- Shadows over borders is the third core principle in the captured SKILL.md.
- Image outlines are the eleventh core principle in the captured SKILL.md.
- The surfaces reference says image outlines use pure black in light mode.
- The surfaces reference says image outlines use pure white in dark mode.
- The surfaces reference says the outline is inset with `outline-offset: -1px`.
- The surfaces reference says tinted palette outlines can read as dirt on the image edge.
- Hit areas are documented in the surfaces reference and reviewed in [[MIFB Performance Rules]].

## How it works

- Nested rounded surfaces look aligned when the outer radius includes the inner radius and the padding between layers.
- A card with 8px padding and a 12px inner radius uses a 20px outer radius in the captured example.
- A Tailwind outer `rounded-2xl p-2` surface can pair with an inner `rounded-lg` surface in the reference example.
- Using the same radius on parent and child can make the nested curve look visually mismatched.
- Optical alignment adjusts visual balance when geometric centering looks wrong.
- The surfaces reference gives icon-side padding as text-side padding minus 2px for icon-and-text buttons.
- The surfaces reference gives a 2px right shift for play-button triangles.
- The surfaces reference prefers fixing asymmetric icons in the SVG path or viewBox when possible.
- Shadow-as-border uses transparency so surface separation adapts across varied backgrounds.
- The light-mode shadow recipe has three layers.
- The first light-mode shadow layer acts like a 1px ring.
- The second light-mode shadow layer adds subtle lift.
- The third light-mode shadow layer adds ambient depth.
- The dark-mode recipe simplifies to a single white ring.
- The surfaces reference keeps true borders for dividers, table cells, input outlines, and dense separators.
- The image outline uses `outline` rather than `border` so layout size does not change.
- The image outline uses `outline-offset: -1px` so the line is inset.

## Best practice

- Calculate nested radii with `outerRadius = innerRadius + padding` when surfaces sit close together. EVIDENCE-BASED
- Treat gaps larger than 24px as separate surfaces instead of forcing strict radius math. EVIDENCE-BASED
- Use optical adjustment for text-and-icon buttons, play icons, and asymmetric icons when geometric centering looks wrong. EVIDENCE-BASED
- Prefer fixing asymmetric icon assets directly before adding component-level margin hacks. EVIDENCE-BASED
- Replace depth borders on buttons, cards, and containers with layered transparent shadows where appropriate. EVIDENCE-BASED
- Keep borders for dividers, table cell boundaries, input outlines, and layout separators. EVIDENCE-BASED
- Use the three-layer light-mode shadow recipe from the surfaces reference for shadow-as-border treatment. EVIDENCE-BASED
- Use the single white-ring dark-mode recipe from the surfaces reference on dark backgrounds. EVIDENCE-BASED
- Add image outlines with pure black at 10 percent opacity in light mode and pure white at 10 percent opacity in dark mode. EVIDENCE-BASED
- Use `outline-offset: -1px` so image outlines do not change layout size. EVIDENCE-BASED

## Pitfalls

- Reusing the same radius on parent and child is the first common mistake in the captured MIFB table.
- Applying concentric math across large gaps can make unrelated surfaces look mechanically linked.
- Replacing layout dividers with shadows can remove necessary separation in dense UI.
- Using tinted grays or accent colors for image outlines can make image edges look dirty.
- Using borders on images changes box dimensions unless box sizing and layout are accounted for.
- Treating dark-mode depth shadows like light-mode shadows can create invisible elevation.
- Centering a play triangle geometrically can still make it look left-heavy.
- Applying per-use margins to every asymmetric icon can hide an SVG asset problem.

## Sources

- Raw GitHub surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Jakub Krehel, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.
- Local Krehel article extract, .raw/research/krehel-article-extract.md, captured 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: anchors the surfaces rules in the MIFB skill.
- [[MIFB Typography and Numbers Rules]]: complements surfaces because text often sits inside cards and buttons.
- [[MIFB Motion and Feedback Rules]]: covers motion applied to the same buttons, cards, and icons.
- [[MIFB Performance Rules]]: covers hit areas and transition constraints related to these surfaces.
- [[MIFB Review Checklist]]: reviews radius, shadows, images, and icons as checklist items.
- [[Optical Alignment]]: expands the optical-centering rule from the surfaces reference.
- [[MIFB Surface and Shadow Rules|Concentric Radii]]: labels the planned S5g concept while this note carries the local evidence.
- [[Jakub Krehel]]: identifies the author of the article and skill.
- [[MIFB Repo and Skill File]]: stores the surfaces capture and retrieval date.
- [[Encoded Design Principles]]: frames radius math and shadows as codified design details.

## Next actions

- Re-check surfaces.md before changing the 24px padding cutoff.
- Re-check SKILL.md before changing the status of concentric radius as a core principle.
- Keep image outline values pure black or pure white unless new evidence changes the rule.
- Keep border replacement scoped to depth, not layout separation.
- Link the future S5g Concentric Radii concept after S5g creates it.
- Keep hit-area implementation details synchronized with [[MIFB Performance Rules]].
- Add examples only when traceable to the surfaces reference or article extract.
- Use the review checklist to verify nested radii, shadows, images, and icons together.
