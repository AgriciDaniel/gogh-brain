---
type: "meta"
title: "Rules Hub"
status: "evergreen"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/meta"]
domain: "ops"
confidence: "evidence-based"
related: ["[[Index]]", "[[Hot]]", "[[Overview]]", "[[Start Here]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]"]
source_urls: []
sources: []
---

# Rules Hub

Rules collects the hard constraints, bans, thresholds, and operating surfaces that guide frontend work.

## Catalog

### gogh/taste-skill

- [[AI Tells (Forbidden Patterns)]] - AI Tells records Taste Skill v2 bans that target common AI-generated frontend signatures.
- [[Architecture and Stack]] - Architecture and Stack records Taste Skill v2's default implementation choices for React or Next.js, Tailwind v4, Motion, fonts, icons, state, and dependencies.
- [[Em-Dash Ban]] - Em-Dash Ban is Taste Skill v2's zero-tolerance visible-text rule for U+2014 and U+2013, with ASCII hyphen used for ranges and separators.
- [[Hero Discipline]] - Hero Discipline is Taste Skill v2's hard rule set for keeping the first viewport coherent, concise, and complete.
- [[Navigation Discipline]] - Navigation Discipline is Taste Skill v2's rule that desktop navigation stays one line and no taller than 80px.
- [[Scope and Context]] - Scope and Context defines where Taste Skill should be used and where another design system or stack layer should take over.
- [[Taste Skill Color Rules]] - Taste Skill Color Rules enforce one accent, restrained saturation, brand-aware purple overrides, and a banned premium-consumer beige-and-brass default.
- [[Taste Skill Dark Mode Protocol]] - Taste Skill Dark Mode Protocol requires a page-level theme strategy, contrast parity, hierarchy parity, and no mid-page light-dark flipping by default.
- [[Taste Skill Layout Rules]] - Taste Skill Layout Rules keep pages from repeating centered heroes, equal card grids, zigzags, empty bento cells, and unplanned mobile collapse.
- [[Taste Skill Motion Rules]] - Taste Skill Motion Rules bind MOTION_INTENSITY to motivated motion, reduced-motion handling, transform-only animation, and canonical scroll patterns.
- [[Taste Skill Reference Card]] - Taste Skill Reference Card is the compact operating map for Taste Skill v2 dials, rules, workflows, audits, and open questions.
- [[Taste Skill Typography Rules]] - Taste Skill Typography Rules define the captured v2 defaults and bans for display scale, body measure, font choice, serif use, and italic descender clearance.
- [[The Three Locks]] - The Three Locks are Taste Skill v2's page-level consistency checks for accent color, radius system, and theme.

### gogh/mifb

- [[MIFB Motion and Feedback Rules]] - MIFB Motion and Feedback Rules capture the skill's exact values for interruptible transitions, enter and exit motion, contextual icon swaps, and press feedback.
- [[MIFB Performance Rules]] - MIFB Performance Rules capture the skill's transition-property discipline, restrained GPU hints, and minimum interactive hit-area checks.
- [[MIFB Surface and Shadow Rules]] - MIFB Surface and Shadow Rules capture the skill's radius math, optical alignment, depth shadows, image outlines, and surface edge guidance.
- [[MIFB Typography and Numbers Rules]] - MIFB Typography and Numbers Rules capture the skill's text wrapping, root font smoothing, and tabular numeral guidance.

### gogh/impeccable

- [[Impeccable Rule Set (45 Detectors)]] - The Impeccable rule set is a 45-rule deterministic detector for common AI frontend anti-patterns and quality issues.

### gogh/frontend-design

- [[Anthropic Frontend Design Rules]] - Anthropic Frontend Design Rules turn the official skill into an operational rule surface: commit to one grounded direction, avoid named template clusters, and critique the plan before code.

### gogh/ui-ux-pro-max

- [[UX Rules Database (99 Rules)]] - UX Rules Database (99 Rules) is the searchable UX guideline layer inside UI UX Pro Max, designed to retrieve relevant checks instead of loading a large rulebook into every prompt.

### gogh/web-design-guidelines

- [[Vercel Interface Rule Categories]] - Vercel Interface Rule Categories is the 17-category map of the command.md rules fetched by the Vercel audit skill.

### gogh/stack

- [[Unified Anti-Slop Rulebook]] - Unified Anti-Slop Rulebook is a merged ban table, not a harmonized doctrine, because several skills intentionally disagree on which defaults are always wrong.

## Related

- [[Index]] returns to the master catalog.
- [[Hot]] shows the current operating state.
- [[Overview]] gives the one-screen product picture.
- [[Start Here]] orients new readers.
- [[CONVENTIONS]] defines note and hub contracts.
- [[Tag Taxonomy]] explains the domain groups used above.
