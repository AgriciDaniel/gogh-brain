---
type: "rule"
title: "Vercel Interface Rule Categories"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/web-design-guidelines", "note/rule"]
domain: "web-design-guidelines"
confidence: "evidence-based"
related: ["[[Vercel Web Design Guidelines]]", "[[Vercel Guidelines Audit]]", "[[Runtime Rule Fetch]]", "[[MIFB Performance Rules]]", "[[Anthropic Frontend Design Rules]]", "[[Impeccable Rule Set (45 Detectors)]]"]
source_urls: ["https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)", "https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07)", "https://api.github.com/repos/vercel-labs/web-interface-guidelines (retrieved 2026-07-07)"]
sources: ["[[Vercel Web Design Guidelines Sources]]"]
---
Vercel Interface Rule Categories is the 17-category map of the command.md rules fetched by the Vercel audit skill.

## What it is
The captured command.md ruleset was retrieved on 2026-07-07.
The captured command.md document contains a Rules section with 17 category headings.
The local research extract summarizes the capture as roughly 85 discrete guidelines.
A literal bullet-row count of the captured command.md yields 93 bullets.
The claim pack records the ruleset as roughly 90-110 rules across 16 or more categories.
Snyk describes the Vercel skills surface with a 100+ rules shorthand in the 2026-07-07 claim pack.
The local extract also says the upstream README markets 100+ rules.
The discrepancy is a dated observation, not a reason to choose one number without context.
The 17 categories cover accessibility, focus, forms, animation, typography, content handling, images, performance, navigation and state, touch and interaction, safe areas and layout, dark mode and theming, locale and i18n, hydration safety, hover and interactive states, content and copy, and anti-pattern flags.
The ruleset is part of the MIT-licensed vercel-labs/web-interface-guidelines repository as of 2026-07-07.
The ruleset is the source fetched by [[Vercel Web Design Guidelines]] at review time.
The rules are code-review checks rather than a rendered visual inspection protocol.
The output section asks the agent to group findings by file.
The output section asks for terse `file:line` findings.
The output section asks for no preamble.

> [!contradiction]
> The 2026-07-07 local extract says roughly 85 rules, the captured bullet rows total 93, and the market shorthand says 100+ rules.

## How it works
Accessibility has 10 captured bullet rows, including icon button labels, form labels, semantic HTML before ARIA, hierarchical headings, and scroll-margin on heading anchors.
Focus States has 4 captured bullet rows, including visible focus, focus replacement for removed outlines, focus-visible, and focus-within.
Forms has 11 captured bullet rows, including autocomplete, input type, paste allowance, clickable labels, spellcheck control, unified checkbox or radio hit targets, request spinners, inline errors, placeholder examples, autocomplete off for non-auth fields, and unsaved-change warnings.
Animation has 6 captured bullet rows, including reduced motion, transform or opacity animation, explicit transition properties, transform origin, SVG transform wrappers, and interruptible animations.
Typography has 6 captured bullet rows, including the ellipsis character, curly quotes, non-breaking spaces, loading-state ellipses, tabular numbers, and balanced or pretty heading wrapping.
Content Handling has 4 captured bullet rows, including truncation, flex `min-w-0`, empty states, and long user-generated content.
Images has 3 captured bullet rows, including explicit dimensions, lazy loading below the fold, and priority loading above the fold.
Performance has 6 captured bullet rows, including virtualization over 50 list items, no layout reads in render, batched DOM reads and writes, cheap controlled inputs, preconnect links, and font preloading with font-display swap.
Navigation and State has 4 captured bullet rows, including URL-reflected state, anchor or Link navigation, deep links for stateful UI, and confirmation or undo for destructive actions.
Touch and Interaction has 5 captured bullet rows, including touch-action, tap highlight color, overscroll containment, drag-state selection controls, and careful autofocus.
Safe Areas and Layout has 3 captured bullet rows, including safe-area environment variables, unwanted scrollbar avoidance, and flex or grid over JavaScript measurement.
Dark Mode and Theming has 3 captured bullet rows, including color-scheme, theme-color, and explicit native select colors.
Locale and i18n has 4 captured bullet rows, including Intl date formatting, Intl number formatting, language detection from browser signals, and no-translate wrappers for brand names or code tokens.
Hydration Safety has 3 captured bullet rows, including value plus onChange, date or time mismatch guards, and restrained suppressHydrationWarning usage.
Hover and Interactive States has 2 captured bullet rows, including hover states and stronger interactive-state contrast.
Content and Copy has 7 captured bullet rows, including active voice, Title Case, numerals for counts, specific button labels, actionable errors, second person, and ampersands where space constrained.
Anti-patterns has 12 captured bullet rows, including disabled zoom, paste blocking, transition all, removed focus outline, inline click navigation, clickable divs or spans, images without dimensions, large map calls without virtualization, unlabeled form inputs, unlabeled icon buttons, hardcoded date or number formats, and unjustified autofocus.
The anti-pattern category repeats several earlier rules as explicit flags.
The repeated anti-pattern flags explain part of the difference between discrete-rule estimates and bullet-row counts.

## Best practice
- Cite rule counts as dated observations from 2026-07-07 EVIDENCE-BASED
- Say 17 categories when describing the captured command.md structure EVIDENCE-BASED
- Say roughly 85 rules only as the local extract's summary, not as an exact count EVIDENCE-BASED
- Say 93 bullet rows only when explaining a literal capture count from command.md EVIDENCE-BASED
- Say 100+ rules only as a marketing or market shorthand from the dated evidence CONTESTED
- Preserve the category names when summarizing findings EVIDENCE-BASED
- Treat anti-pattern flags as review triggers that may duplicate earlier category rules EVIDENCE-BASED
- Use representative rules rather than copying the whole ruleset into a wiki page EVIDENCE-BASED
- Keep accessibility, UX, and performance together because the ruleset spans all three EVIDENCE-BASED
- Refresh command.md before changing any count in this note EVIDENCE-BASED

## Pitfalls
Do not flatten the categories into a single undifferentiated checklist.
Do not claim the captured file contains exactly 100 rules.
Do not claim the local extract's roughly 85 count is a line-level count.
Do not use the 93 bullet-row count as a semantic rule count without explaining repeated anti-pattern flags.
Do not treat a Snyk or README shorthand as more authoritative than the captured command.md.
Do not cite category counts without the 2026-07-07 retrieval date.
Do not copy every rule into downstream deliverables when a representative summary is enough.
Do not remove the output-format rules from the category discussion.
Do not turn the audit into a visual taste score.
Do not treat Vercel's code-review rules as a replacement for [[Pre-Flight Check (Section 14)]].
Do not treat them as a replacement for [[Impeccable Rule Set (45 Detectors)]].

## Sources
- Vercel Labs raw ruleset, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- Vercel Labs raw wrapper, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- GitHub API for web-interface-guidelines, https://api.github.com/repos/vercel-labs/web-interface-guidelines, retrieved 2026-07-07.
- Snyk market snapshot, https://snyk.io/articles/top-claude-skills-ui-ux-engineers/, retrieved 2026-07-07.
- Local extract, .raw/research/vercel-web-design-guidelines-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.

## Related
- [[Vercel Web Design Guidelines]] is the skill that fetches these categories at runtime.
- [[Vercel Guidelines Audit]] explains how the categories become findings.
- [[Runtime Rule Fetch]] explains why the category list can change without reinstalling the wrapper.
- [[MIFB Performance Rules]] overlaps with Vercel's performance and animation checks.
- [[MIFB Motion and Feedback Rules]] overlaps with Vercel's animation and interaction checks.
- [[Anthropic Frontend Design Rules]] is a broader taste-prompting peer.
- [[Impeccable Rule Set (45 Detectors)]] is the deterministic detection peer.
- [[Required Audits]] gives the audit-gate context for these rules.
- [[Design Review as Infrastructure]] explains reusable review rulebooks.
- [[AI Tells (Forbidden Patterns)]] is the adjacent anti-pattern vocabulary.

## Next actions
- Re-count command.md after the next upstream capture.
- Keep the roughly 85, 93 bullet-row, and 100+ figures separated in future summaries.
- Add a delta note if upstream categories are renamed.
- Re-run [[Vercel Guidelines Audit]] examples after any rule-category change.
