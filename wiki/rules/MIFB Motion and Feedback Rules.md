---
type: "rule"
title: "MIFB Motion and Feedback Rules"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/rule"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Typography and Numbers Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
MIFB Motion and Feedback Rules capture the skill's exact values for interruptible transitions, enter and exit motion, contextual icon swaps, and press feedback.

## What it is

- This rule note covers the MIFB animations reference file.
- The animations reference covers interruptible animations, enter transitions, exit transitions, contextual icon animations, and scale on press.
- The captured SKILL.md maps animations to interruptible animations, enter and exit transitions, icon animations, and scale on press.
- Interruptible animations are the fourth core principle in the captured SKILL.md.
- Split and stagger enter animations are the fifth core principle in the captured SKILL.md.
- Subtle exit animations are the sixth core principle in the captured SKILL.md.
- Contextual icon animations are the seventh core principle in the captured SKILL.md.
- Scale on press is the twelfth core principle in the captured SKILL.md.
- Skipping animation on page load is the thirteenth core principle in the captured SKILL.md.
- The MIFB claim pack records button press feedback as `scale(0.96)`.
- The MIFB claim pack records a floor that should never go below `0.95`.
- The captured SKILL.md says Motion spring settings use duration `0.3` and bounce `0`.
- The captured SKILL.md says CSS fallback icon animation uses `cubic-bezier(0.2, 0, 0, 1)`.
- The captured SKILL.md says icon animation values are scale `0.25` to `1`, opacity `0` to `1`, and blur `4px` to `0px`.
- The Krehel article extract records article demo enter durations around 800ms.
- The MIFB skill extract records derived skill enter values around 300 to 400ms.

## How it works

- CSS transitions interpolate toward the latest state.
- CSS transitions can retarget when the user changes intent mid-interaction.
- CSS keyframe animations run a fixed timeline.
- The animations reference reserves keyframes for staged sequences that run once.
- The animations reference recommends splitting a page header into title, description, and buttons.
- The animations reference recommends about 100ms delay between semantic groups.
- The animations reference recommends about 80ms stagger between individual title words.
- The animations reference combines opacity, blur, and vertical movement for enter effects.
- The CSS-only stagger example starts at opacity `0`, `translateY(12px)`, and blur `4px`.
- The CSS-only stagger example animates to opacity `1`, `translateY(0)`, and blur `0`.
- The animations reference says exits should be softer and less attention-grabbing than enters.
- The subtle exit example uses opacity `0`, y `-12`, blur `4px`, duration `0.15`, and ease `easeIn`.
- The animations reference says exit duration should be shorter than enter duration.
- The Motion icon example uses `AnimatePresence` and a spring transition with duration `0.3` and bounce `0`.
- The CSS icon approach keeps both icons in the DOM and cross-fades them.
- The CSS icon approach uses one absolute icon over a non-absolute icon that defines layout size.
- Press feedback uses a scale transition so release can smoothly return the button to normal.
- The static prop pattern disables press scale when motion would distract.
- `initial={false}` on `AnimatePresence` prevents default-state enter animation on first render.

## Best practice

- Use CSS transitions for interactive state changes because the animations reference defines them as interruptible. EVIDENCE-BASED
- Reserve keyframes for staged sequences that run once. EVIDENCE-BASED
- Split enter animations into semantic chunks instead of animating one large container. EVIDENCE-BASED
- Stagger semantic groups by about 100ms. EVIDENCE-BASED
- Stagger individual title words by about 80ms when word-level title animation is used. EVIDENCE-BASED
- Make exits shorter and subtler than enters. EVIDENCE-BASED
- Use scale `0.25` to `1`, opacity `0` to `1`, and blur `4px` to `0px` for contextual icon animation. EVIDENCE-BASED
- Use Motion spring duration `0.3` and bounce `0` when Motion or Framer Motion is already installed. EVIDENCE-BASED
- Use CSS cross-fade with `cubic-bezier(0.2, 0, 0, 1)` when no Motion dependency exists. EVIDENCE-BASED
- Use `scale(0.96)` for press feedback and never use a press value below `0.95`. EVIDENCE-BASED
- Provide a static option to disable press scale when the motion would distract. EVIDENCE-BASED
- Use `initial={false}` for default-state elements in `AnimatePresence`. EVIDENCE-BASED

## Pitfalls

- A keyframe on an interactive drawer can snap or restart when the user reverses intent.
- Animating one large container can make page entrance feel blunt instead of staged.
- Removing exit animation entirely can make elements vanish without context.
- Using a full-height exit can steal attention from the user's next target.
- Changing the icon scale values to `0.5` or `0.6` violates the captured MIFB rule.
- Adding Motion only for an icon swap conflicts with the captured CSS fallback guidance.
- Using bounce above `0` conflicts with the captured spring rule.
- Scaling a button below `0.95` is called exaggerated by the captured rule.
- Running default-state enter animations on page load can make tabs or toggles feel noisy.

## Sources

- Raw GitHub animations reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Jakub Krehel, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.
- Local Krehel article extract, .raw/research/krehel-article-extract.md, captured 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: anchors the animation values in the skill.
- [[MIFB Typography and Numbers Rules]]: covers text rules that interact with animated titles and counters.
- [[MIFB Surface and Shadow Rules]]: covers surfaces and icons that often receive motion feedback.
- [[MIFB Performance Rules]]: covers transition-property specificity and GPU hints.
- [[MIFB Review Checklist]]: includes split enter motion, subtle exits, press scale, and page-load checks.
- [[MIFB Motion and Feedback Rules|Interruptible Animation]]: labels the planned S5g concept while this note carries the local evidence.
- [[MIFB Performance Rules|Press Feedback and Hit Areas]]: connects press scale with the hit-area review path.
- [[Optical Alignment]]: complements contextual icon motion because icons must start from a balanced position.
- [[Jakub Krehel]]: identifies the author of the article and skill.
- [[MIFB Repo and Skill File]]: stores the animations capture and retrieval date.

## Next actions

- Re-check animations.md before changing scale, blur, opacity, spring, or easing values.
- Re-check the article extract before describing the 800ms article demo values.
- Keep article demo values separate from derived skill values when they differ.
- Keep bounce fixed at `0` unless a refreshed capture changes the rule.
- Link the future S5g Interruptible Animation concept after S5g creates it.
- Keep press scale synchronized with [[MIFB Performance Rules]].
- Use the checklist note to verify motion changes after implementation.
- Avoid adding a Motion dependency solely for icon swaps.
