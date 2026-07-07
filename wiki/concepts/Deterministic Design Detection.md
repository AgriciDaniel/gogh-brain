---
type: "concept"
title: "Deterministic Design Detection"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/impeccable", "note/concept"]
domain: "impeccable"
confidence: "evidence-based"
related: ["[[Impeccable Rule Set (45 Detectors)]]", "[[Impeccable Audit and Detect]]", "[[Impeccable (Toolchain)]]", "[[Constraint Beats Coaxing]]", "[[Design Review as Infrastructure]]", "[[AI Slop]]"]
source_urls: ["https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://impeccable.style/ (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://computertech.co/impeccable-ai-review/ (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]"]
---
Deterministic design detection is Impeccable's no LLM enforcement path for repeatable frontend anti-pattern checks.

## What it is
The captured README says the CLI and browser extension run deterministic rules with no LLM and no API key.
The captured README says there are 45 deterministic detector rules.
The repo extract says the detector can emit JSON output and build-readable exit codes.
The repo extract documents a failing site example that exits 1.
The detector is different from LLM-only critique checks.
That split makes deterministic detection the part of Impeccable most suitable for CI.
This CI suitability is an inference from no LLM execution, JSON output, and exit-code behavior in the capture.
Prompt-level enforcement depends on a model reading and following instructions.
Deterministic detection depends on a rule implementation scanning files, HTML, or rendered URLs.
The detector can run as a standalone CLI without an AI harness.
The detector can also run inside provider hooks.
The provider hook path makes detection available at edit time.
The standalone CLI path makes detection available in CI and local scripts.
The Chrome extension path makes detection available in a browser review surface.
Together, those surfaces form Impeccable's enforcement grammar.

## How it works
The grammar starts with a target surface.
The target can be a source directory.
The target can be one HTML file.
The target can be a URL rendered through Puppeteer.
The target can be a direct UI file edit observed by a provider hook.
The scanner applies deterministic rules.
The rules produce findings for AI slop signatures and quality issues.
The output can be plain text for local use.
The output can be JSON for CI.
The failing example in the repo extract exits 1.
The config layer can ignore rules.
The config layer can ignore files.
The config layer can ignore values.
The inline layer can disable a rule for a file, line, or next line.
The design-system layer can make detection aware of documented palettes.
The hook layer routes the findings back into the agent.
Claude Code uses `.claude/settings.local.json` and a hook script.
GitHub Copilot uses `.github/hooks/impeccable.json` and a hook script.
Cursor uses `.cursor/hooks.json` and a before-edit hook script.
Codex uses `.codex/hooks.json` and an `.agents/skills/impeccable` hook script.
Claude Code, GitHub Copilot, and Codex surface findings after edits.
Cursor blocks problematic writes before they land.
Skill 3.9.1 fixed Codex plugin hook loading by removing a top-level description field that Codex's strict parser rejected.

## Best practice
- Use deterministic detection for CI because it runs without an LLM or API key EVIDENCE-BASED
- Use JSON output when a machine needs to consume findings EVIDENCE-BASED
- Use provider hooks when findings need to appear during agent edits EVIDENCE-BASED
- Use Cursor hooks when the workflow needs proposed writes blocked before landing EVIDENCE-BASED
- Use post-edit hooks in Claude Code, GitHub Copilot, and Codex when the workflow can accept feedback after edits EVIDENCE-BASED
- Keep prompt rules and detector rules separate in documentation EVIDENCE-BASED
- Treat the CI advantage over prompt-only enforcement as an inference from deterministic execution PRACTITIONER
- Verify exact local exit codes before making a repository-wide required check PRACTITIONER
- Keep waivers explicit and reasoned so deterministic checks do not become noise PRACTITIONER
- Refresh hooks after Impeccable updates because hook manifests can change EVIDENCE-BASED

## Pitfalls
Do not claim deterministic detection can judge every design issue.
The captured README still names LLM-only critique checks.
Do not claim the detector replaces `/impeccable critique`.
Do not assume the no-finding exit code from the S5c evidence.
The S5c capture documents exit 1 for a failing example only.
Do not treat Cursor hook behavior as identical to Claude Code or Codex hook behavior.
Cursor blocks before write, while Claude Code and Codex surface after edit.
Do not skip Codex hook approval after install or update.
The README says Codex requires `/hooks` approval.
Do not commit malformed hook manifests and expect install to merge them.
The README says install or update aborts on malformed hook manifests unless `--force` is used.
Do not treat deterministic detection as market-ready proof for the whole Gogh brain.
Gogh still requires its own vault and release audits.

## Sources
- GitHub repo, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Impeccable official site, https://impeccable.style/, retrieved 2026-07-07.
- GitHub releases, https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07.
- computertech.co review, https://computertech.co/impeccable-ai-review/, retrieved 2026-07-07.
- Local raw README capture, .raw/skills/impeccable/README.md, retrieved 2026-07-07.
- Local raw SKILL.md capture, .raw/skills/impeccable/SKILL.md, retrieved 2026-07-07.
- Local repo extract, .raw/research/impeccable-repo-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-impeccable.md, generated 2026-07-07.

## Related
- [[Impeccable Rule Set (45 Detectors)]] lists rule families and detector surfaces.
- [[Impeccable Audit and Detect]] distinguishes deterministic detection from audit.
- [[Impeccable (Toolchain)]] anchors the toolchain enforcement role.
- [[Design Review as Infrastructure]] frames the prompt versus detector distinction.
- [[Required Audits]] compares overlapping gates in the current vault.
- [[Constraint Beats Coaxing]] explains why constraints outperform vague prompts.
- [[AI Slop]] names the failure class the detector targets.
- [[Pre-Flight Check (Section 14)]] is another blocking enforcement surface.
- [[Design Review as Infrastructure]] explains review moved into repeatable systems.
- [[Impeccable Repo and Site]] holds the source trail.

## Next actions
- Verify pass and fail exit codes in a local Impeccable install before publishing CI snippets.
- Capture the detector docs if future work needs every rule identifier.
- Watch Codex hook release notes because 3.9.1 included a Codex hook parser fix.
- Compare detector findings with Vercel Guidelines findings when that comparison is authored.
