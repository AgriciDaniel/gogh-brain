---
type: "concept"
title: "Optical Alignment"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/concept"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Typography and Numbers Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
Optical Alignment is the MIFB rule that visual balance can override geometric centering when icons, triangles, and asymmetric shapes look off.

## What it is

- Optical alignment is the second core principle in the captured MIFB SKILL.md.
- The captured SKILL.md says to align optically when geometric centering looks off.
- The surfaces reference places optical alignment inside the surfaces category.
- The surfaces reference names buttons with text and icons as a primary case.
- The surfaces reference names play button triangles as a primary case.
- The surfaces reference names asymmetric icons such as stars, arrows, and carets as primary cases.
- The Krehel article extract lists optical alignment as technique 9.
- The article extract says icon-and-text buttons reduce padding on the icon side.
- The article extract says the best fix for asymmetry is often inside the SVG itself.
- The surfaces reference gives a rule of thumb where icon-side padding equals text-side padding minus 2px.
- The surfaces reference gives a play triangle adjustment of `margin-left: 2px`.
- The surfaces reference says SVG viewBox or path adjustments are preferred for asymmetric icons when possible.
- Optical alignment is not a license to move every element by eye without a reason.
- Optical alignment is a correction for cases where geometry and perception diverge.
- The MIFB checklist includes icons being optically centered, not only geometrically centered.

## How it works

- Geometric centering places an element by mathematical center points.
- Optical alignment places an element by perceived visual weight.
- A play triangle has more visual mass on one side than its bounding box implies.
- A right-pointing icon in a text button can look pushed outward when both sides use equal padding.
- Reducing icon-side padding by 2px can make an icon-and-text button feel balanced in the MIFB reference.
- Shifting a play icon right by 2px can compensate for its triangular shape in the MIFB reference.
- Fixing the SVG viewBox can make component code cleaner than adding per-instance spacing.
- Adjusting the SVG path can center the asset where it is reused.
- A fallback margin can be used when the icon asset cannot be changed.
- Optical alignment sits next to radius, shadow, and outline rules because small surface details compound.
- Optical alignment interacts with motion because an off-center icon remains off-center while it animates.
- Optical alignment interacts with hit areas because the visual target and interactive target can differ.
- Optical alignment should be reviewed in context, not only in isolated icon files.
- The review checklist turns this concept into a checkable item.

## Best practice

- Check icons visually after geometric centering when they have asymmetric weight. EVIDENCE-BASED
- Use icon-side padding equal to text-side padding minus 2px for text-and-icon buttons when the MIFB condition applies. EVIDENCE-BASED
- Shift play triangles right by 2px when geometric centering makes them look left-heavy. EVIDENCE-BASED
- Prefer fixing asymmetric icons in the SVG viewBox or path when the asset can be changed. EVIDENCE-BASED
- Use component-level margin as a fallback when the icon asset cannot be edited. EVIDENCE-BASED
- Review optical alignment alongside hover, press, and icon animation states. EVIDENCE-BASED
- Keep optical changes small and tied to a named asymmetry case. EVIDENCE-BASED
- Include optical alignment in MIFB review output only when a visible correction was made. EVIDENCE-BASED
- Avoid claiming a universal optical offset beyond the examples captured in the reference. EVIDENCE-BASED
- Keep optical alignment separate from broad layout alignment rules. EVIDENCE-BASED

## Pitfalls

- Equal padding can look wrong when one side contains an icon and the other side contains text.
- A play icon can look off-center even when its SVG box is geometrically centered.
- Component-level margin can accumulate into inconsistent icon handling across the product.
- Over-adjusting an icon can make the correction more visible than the original problem.
- Treating every icon as asymmetric can introduce unnecessary inconsistency.
- Animating an off-center icon can make the alignment issue more noticeable.
- Expanding hit areas without checking visual alignment can create a control that feels mismatched.
- Calling a layout preference optical alignment can weaken the rule's specific evidence base.

## Sources

- Raw GitHub surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Jakub Krehel, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.
- Local Krehel article extract, .raw/research/krehel-article-extract.md, captured 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: names optical alignment as a core principle.
- [[MIFB Surface and Shadow Rules]]: contains the source rule category for optical alignment.
- [[MIFB Motion and Feedback Rules]]: covers animated icons that depend on correct visual centering.
- [[MIFB Performance Rules]]: connects visual target placement with hit-area review.
- [[MIFB Typography and Numbers Rules]]: complements button text and label polish.
- [[MIFB Review Checklist]]: includes the optical-centering review item.
- [[Jakub Krehel]]: identifies the author of the source article and skill.
- [[MIFB Repo and Skill File]]: stores the surfaces capture and article extract.
- [[Encoded Design Principles]]: frames this correction as a codified design rule.
- [[Design Review as Infrastructure]]: frames optical checks as repeatable review work.

## Next actions

- Re-check surfaces.md before changing the 2px padding or play icon examples.
- Keep SVG-level fixes preferred where the asset can be changed.
- Keep fallback margin framed as a fallback.
- Review optical alignment in hover, active, and icon-swap states.
- Coordinate this concept with the future S5g interaction concept notes.
- Add only examples that appear in the MIFB reference or article extract.
- Keep this concept scoped to perception-vs-geometry cases.
- Use the MIFB review checklist to report optical alignment corrections.
