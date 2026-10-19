# Architecture Review

> **Status:** architecture approved for implementation. The M0 package is preserved as the design record; M2 adds the first authored foundations batch.
>
> **M1 update (2026-10-19):** the documentation framework is implemented: MkDocs 1.6.1 with Material for MkDocs 9.7.7, five authoring templates, a manifest JSON Schema, local validation scripts, and a CI workflow.
>
> **M2 update (2026-10-19):** SYS-01 and SYS-02 are drafted with nine tutorials, two labs, two assessments, and instructor solutions. Both are `drafted` / `structural`; the Linux lab paths were not executed in this environment.
>
> **M3 update (2026-10-19):** the academic research track is implemented with eight methods tutorials, five templates, a P1–P4 project ladder, objective rubrics, and a portfolio assessment. RES-01, RES-02, RES-06, and RES-07 are `drafted` / `structural`; RES-03–RES-05 remain planned. No research study was executed, so no research result is claimed.

## Table of contents

- [1. What was produced](#1-what-was-produced)
- [2. Architecture summary](#2-architecture-summary)
- [3. Design decisions](#3-design-decisions)
- [4. Trade-offs and risks](#4-trade-offs-and-risks)
- [5. Open questions](#5-open-questions)
- [6. Verification performed](#6-verification-performed)
- [7. Verification not performed](#7-verification-not-performed)
- [8. First milestone acceptance criteria](#8-first-milestone-acceptance-criteria)
- [9. M1 status and next milestone](#9-m1-status-and-next-milestone)
- [10. Approval and next action](#10-approval-and-next-action)
- [11. Architecture review checklist](#11-architecture-review-checklist)

## 1. What was produced

The M0 architecture package produced exactly **ten planning files**: one updated entry point and nine new artifacts. The M1 documentation framework adds the site configuration, templates, schema, scripts, and CI workflow; see the repository layout in `README.md`.

| File | Purpose | Status |
|---|---|---|
| [`README.md`](./index.md) | Orientation, repository map, design summary, safety and source policy | Draft |
| [`COURSE_MAP.md`](./COURSE_MAP.md) | Six-level architecture, 67-module catalog, 201 outcomes, assessment strategy, milestones | Draft |
| [`LEARNING_PATHS.md`](./LEARNING_PATHS.md) | Five paths with sequences, exit competencies, portfolio evidence, and time model | Draft |
| [`diagrams/dependency-graph.md`](./diagrams/dependency-graph.md) | Nine rendered Mermaid views of the prerequisite graph | Draft |
| [`CURRICULUM_MANIFEST.md`](./CURRICULUM_MANIFEST.md) | Manifest schema, field reference, lifecycle, integrity rules, validation procedure | Draft |
| [`manifest/course-manifest.yaml`](./manifest/course-manifest.yaml) | Machine-readable curriculum state: modules, paths, prerequisites, outcomes, effort, sources, safety | Draft |
| [`RESEARCH_STRAND.md`](./RESEARCH_STRAND.md) | Research competencies, lifecycle, artifacts, rigor standards, ethics, teaching | Draft |
| [`ASSUMPTIONS_AND_GAPS.md`](./ASSUMPTIONS_AND_GAPS.md) | Learner model, diagnostic plan, likely gaps, environment constraints, risks | Draft |
| [`REFERENCES.md`](./REFERENCES.md) | 134-entry source ledger with verification codes and known exclusions | Draft |
| [`ARCHITECTURE_REVIEW.md`](./ARCHITECTURE_REVIEW.md) | This review: decisions, trade-offs, checks, open questions, approval checklist | Draft |

The M0 package authored no tutorials, labs, assessments, or capstone briefs. The M2 batch now adds SYS-01 and SYS-02 tutorials, labs, and assessments; no capstone brief has been authored.

## 2. Architecture summary

| Property | Value |
|---|---:|
| Levels | 6 (L0–L5) plus capstones |
| Modules (non-capstone, includes 3 electives) | 62 |
| Electives | 3 |
| Capstones | 5 |
| Total entries | 67 |
| Measurable outcomes | 201 |
| Total learner effort | 1,950 hours |
| Single-path effort | 784–1,164 hours |
| Learning paths | 5 |
| Source records | 134 |
| Mermaid diagrams | 17 across 6 documents (10 in the dependency graph) |
| Modules authored (drafted or later) | 2 |
| Modules validated beyond `unvalidated` | 2 (structural) |

The design separates **breadth** (the full 1,950-hour curriculum) from **depth** (a 784–1,164-hour path). This is intentional: a single path should be completable in 1.3–2.2 years at 10–12 hours per week, while the full curriculum remains a reference for a multi-year apprenticeship.

### Level and path coverage

```text
L0  Orientation            3 modules    30 h
L1  Systems foundations   12 modules   272 h
L2  Core security         12 modules   286 h
L3  Advanced              17 modules   496 h
L4  Expert                11 modules   306 h
L5  Research               7 modules   180 h
    Capstones              5 modules   380 h
```

Paths: Security Engineering (35 modules, 840 h), Application and Product Security (33, 784 h), Offensive Security Research (44, 1,164 h), Defensive Security Research (44, 1,098 h), Academic Security Research (36, 938 h).

## 3. Design decisions

| ID | Decision | Rationale | Alternative considered |
|---|---|---|---|
| D01 | Six levels plus capstones | Separates foundations, core practice, advanced depth, leadership, and research; each has a distinct exit gate | Four levels; rejected because research and leadership would be conflated |
| D02 | Manifest-first, generated catalog and diagrams | Prevents prerequisite drift across prose and diagrams | Prose-first; rejected because it cannot be validated |
| D03 | Separate publication status and validation status | A published page is not necessarily a tested lab; both dimensions matter | Single status; rejected as ambiguous |
| D04 | One catalog file (`COURSE_MAP.md`) | Keeps the full syllabus navigable in one place during architecture review | Per-level catalog files; deferred to Q11 |
| D05 | Research strand begins at L0 | Evidence habits and source discipline must be practiced before the thesis | Research track at the end; rejected because habits form too late |
| D06 | `TCH-01` plus teach-back in every module | Teaching exposes whether the learner can decompose and assess understanding | Optional workshop; rejected because teaching is a mastery test |
| D07 | Path closure is machine-checked | A path that omits a prerequisite is a broken promise | Ad hoc prerequisite checks; rejected |
| D08 | Three electives only | Keeps the full curriculum bounded and the paths coherent | Many electives; rejected for scope control |
| D09 | Diagnostic placement, not a fixed beginner start | The learner is an experienced developer; a fixed start wastes time or skips gaps | Fixed L0 start for everyone; rejected |
| D10 | Source ledger with verification codes | Distinguishes a verified landing page from a full-text review and from an unstable link | Plain bibliography; rejected because verification level matters |
| D11 | Safety flags in the manifest | Safety constraints travel with module data and cannot be lost in a separate document | Safety doc only; rejected |
| D12 | Five capstones, including a thesis | Each path needs a different exit artifact; research needs a thesis | One generic capstone; rejected as too weak |

## 4. Trade-offs and risks

| Trade-off or risk | Why it exists | Mitigation | Residual risk |
|---|---|---|---|
| `COURSE_MAP.md` is long (1,300+ lines) | It holds the complete module catalog and assessment design | TOC and anchors; split into per-level catalogs if navigation suffers (Q11) | Medium |
| Manifest is large (2,900+ lines) | It is the machine-readable source of truth for 67 modules | Generated views; do not hand-edit; validate on change | Low |
| 1,950-hour full breadth may discourage learners | Comprehensive coverage is expensive | Paths reduce scope to 784–1,164 hours; challenge exams | Medium |
| Effort estimates are uncalibrated | No cohort data yet | Revise after the first cohort; record changes >20% | High |
| Sources verified at landing-page level | Full-text review of 134 sources is not feasible in M0 | Module-level verification during authoring | Medium |
| Research path defaults to an application-security anchor | A research path needs technical depth, but interests vary | Alternative binary, cloud, and cryptography anchors are documented | Medium |
| macOS/Apple Silicon assumptions | Some labs need x86 or Windows | Diagnostic, UTM/QEMU, remote x86, sequential labs | Medium |
| No authored labs yet | This milestone is architecture only | M1 templates and safety; M2 pilot before scaling | High |
| CI exists but has not run on GitHub | Local checks pass; GitHub Actions has not executed in this environment | Run the workflow on the remote repository | Medium |
| AI overreliance could weaken mastery | Assistants can generate plausible but unverified work | Evidence requirements, disclosure, oral defense | Medium |
| Offensive content carries dual-use risk | The curriculum teaches real techniques | Isolation, authorization, detection pairing, ethics strand | Medium |
| Vendor/standard drift | ATT&CK, OWASP, cloud APIs, and tools change | Six-month review; version pins; dated claims | Medium |

## 5. Open questions

These require a decision before or during M1. Defaults are proposed; none are silently assumed.

| ID | Question | Why it matters | Proposed default |
|---|---|---|---|
| Q01 | Which virtualization baseline on Apple Silicon? | Determines lab reproducibility and Windows/AD support | UTM/VMware Fusion plus a remote x86 option; decide in M1 |
| Q02 | Which primary cloud provider? | Concrete IAM, network, and logging examples need one provider | One primary provider plus provider-neutral concepts |
| Q03 | How much C/C++ and assembly is required? | Determines pace of `EXP-01`, `REV-01`, `MAL-01` | Require C and one assembly dialect; Rust optional |
| Q04 | Is a statistics bridge required? | `RES-02` assumes probability and inference | Diagnostic P5; add a bridge if below 4/6 |
| Q05 | Should the curriculum map to NICE/DCWF or vendor certifications? | Learners may want a crosswalk | Optional mapping; no equivalence claim |
| Q06 | Should offensive modules be required outside offensive/defensive paths? | Breadth versus time and risk | Required only in offensive/defensive paths; elective elsewhere |
| Q07 | Where do capstones run? | Reproducibility versus privacy and cost | Synthetic/local by default; cloud only with a budget cap |
| Q08 | What license applies to learner submissions? | Affects portfolios and public artifacts | Decide before accepting learner work |
| Q09 | What is the detailed AI-assistant policy? | Assessment integrity and disclosure | Disclosure plus oral defense; refine in M1 |
| Q10 | Cohort or self-paced? | Affects review capacity and teach-back | Self-paced with optional cohort reviews |
| Q11 | Should `COURSE_MAP.md` be split into per-level catalogs? | Navigation and maintenance at scale | Keep one file until it exceeds practical navigation; revisit after M2 |
| Q12 | Should formal math be a bridge module or a prerequisite? | `CRY-01`, `RES-02`, `RES-05` load | Bridge module, not a gate, unless diagnostic shows a large gap |
| Q13 | Should `HW-01` be required in the offensive path? | Hardware access is uneven | Elective; required only for a hardware research focus |
| Q14 | Is the M1 scope (11 files) approved? | Determines the next batch | Approve as listed in section 9 |

## 6. Verification performed

All checks below were run against the repository files on **2026-10-19**, not against an intermediate draft.

| Check | Command or method | Result |
|---|---|---|
| Manifest YAML parse | `PYTHONPATH=/tmp/pylibs python3 -c "import yaml; yaml.safe_load(open('manifest/course-manifest.yaml'))"` | Parsed successfully; 67 modules, 201 outcomes, 1,950 hours |
| Structural validator | Custom Python validator over the manifest | 0 errors, 0 warnings |
| Unique IDs and prereq existence | Validator rules R01–R04 | Pass |
| DAG acyclicity | Depth-first cycle detection | Pass; no cycles or self-dependencies |
| Level monotonicity | Validator rule R04 | Pass; no higher-level prerequisite |
| Outcome and assessment completeness | Validator rules R05–R07 | Pass; every module has ≥2 outcomes, an assessment, and sources |
| Source ledger coverage | Validator rule R08 | Pass; all 134 used source IDs are declared |
| Path closure | Validator rule R09 | Pass for all 5 paths |
| Capstone and orphan checks | Validator rules R10–R11 | Pass; every capstone is in a path; no orphan non-electives |
| Local links and anchors | Custom Markdown link checker | 0 broken links or anchors |
| Markdown structure | One H1 per file; heading-level and fence checks | Pass; no heading jumps or unbalanced fences |
| Markdown lint | `pymarkdown 0.9.41` with `.pymarkdown.json` | 0 issues across 15 files |
| Mermaid rendering | `@mermaid-js/mermaid-cli 12.0.0` with Chrome | 22 of 22 blocks rendered successfully |
| M0 file-count constraint | `git status --short` at M0 | 10 paths: 1 modified, 9 new; M1 adds framework files |
| Source verification | HTTP fetches, Crossref DOI lookups, PDF check | 134 entries recorded with codes V1–V5 |

### Markdown lint configuration

The lint run disables only rules that do not affect rendering or semantics: `MD013` (line length), `MD033` (inline HTML), `MD036` (emphasis used as a heading), `MD059` (link text must be descriptive), `MD060` (compact table separator style), and `MD010` (hard tabs, because captured disassembly contains real tabs). `MD029` allows lists that restart at an extended number after a subsection heading. Structural rules remain enabled.

### Mermaid rendering

Twenty-two Mermaid blocks were rendered at M1 across the architecture pages, the dependency graph, the templates, and the example page. The M2 batch raises the total to 41. Rendering success confirms syntax validity; it does not guarantee readability on every screen size.

### M1 documentation framework checks

| Check | Command | Result |
|---|---|---|
| Full local gate | `make check` | Manifest, links, lint, and strict build all passed |
| MkDocs strict build | `mkdocs build --strict` | Site built successfully in 0.31 seconds (`make build`) |
| Local server | `make serve` plus `curl http://127.0.0.1:8000/` | HTTP 200; example page contained three Mermaid blocks |
| Mermaid render | `scripts/check_mermaid.py --render --require-render` | 22 of 22 blocks rendered |
| Manifest schema | `scripts/validate_manifest.py` | 67 modules, 201 outcomes, 1,950 hours, 5 paths, 134 sources |

### M2 authored foundations checks

| Check | Command | Result |
|---|---|---|
| Content Markdown | `find tutorials labs assessments -type f -name '*.md'` | 23 files: 11 tutorial docs, 8 lab docs, 4 assessment docs |
| Lab support files | `find labs -type f ! -name '*.md'` | 11 files: starter sources, scripts, checksums, Containerfile |
| Manifest schema and structure | `scripts/validate_manifest.py` | Pass; 134 used / 134 declared sources; SYS-01 and SYS-02 `drafted` / `structural` |
| Local links and anchors | `scripts/check_links.py` | Pass; 38 Markdown files, 353 links, 0 missing nav targets |
| Markdown lint | `pymarkdown` with `.pymarkdown.json` | Pass; 0 issues |
| Strict site build | `mkdocs build --strict` | Pass; 19 module and lab pages built; answer keys and solutions excluded |
| Mermaid render | `scripts/check_mermaid.py --render --require-render` | 46 of 46 blocks rendered |
| Search index | built `search/search_index.json` | 34 pages indexed, including all module and lab pages |
| Lab execution | mixed | SYS-01 macOS build and 30-run measurement executed; SYS-02 Linux trace not executed; macOS fallback executed; scripts syntax-checked |

### M3 research track checks

| Check | Command | Result |
|---|---|---|
| Research Markdown | `find research -type f -name '*.md'` | 15 files: 9 track docs and 6 project/rubric docs |
| Templates | `find templates -type f -name '*.md'` | 9 total, including 5 research templates |
| Manifest schema and structure | `scripts/validate_manifest.py` | Pass; 149 used / 149 declared sources; 6 modules `drafted` / `structural` |
| Local links and anchors | `scripts/check_links.py` | Pass; 59 Markdown files, 490 links, 0 missing nav targets |
| Markdown lint | `pymarkdown` with `.pymarkdown.json` | Pass; 0 issues |
| Strict site build | `mkdocs build --strict` | Pass; 15 research pages built; answer keys excluded |
| Mermaid render | `scripts/check_mermaid.py --render --require-render` | 74 of 74 blocks rendered |
| Search index | built `search/search_index.json` | 54 pages indexed, including 15 research pages |
| Research execution | not run | The project briefs are specifications; no data were collected and no results are claimed |

## 7. Verification not performed

The following checks are explicitly **not** complete. Do not describe the curriculum as validated until they are.

| Not performed | Why | When |
|---|---|---|
| Lab execution on a clean environment | No labs are authored yet | M2 onward, per module |
| Classroom or cohort pilot | No learners yet | After M2 |
| Full-text review of standards and papers | M0 verified identity, edition, and landing pages only | During authoring of each module |
| Exhaustive external link crawl | Bot protection and rate limits; sources were sampled and recorded | Before each release |
| Accessibility audit | No rendered site or screen-reader test yet | M1/M2 |
| Manual visual review of every rendered diagram | Render success checked; layout reviewed for the dependency graph only | M1 |
| CI execution | Workflow exists but was not run on GitHub Actions in this environment | On push or pull request |
| Security review of future lab code | No lab code exists yet | Before publishing any lab |
| Legal review of authorization templates | Depends on jurisdiction | M1, with local counsel if needed |
| Assessment calibration | No learner work yet | After first cohort |

## 8. First milestone acceptance criteria

- [x] M0 contained exactly ten planning files, with no tutorials.
- [x] Hierarchical curriculum from orientation to research.
- [x] Measurable learning outcomes for every module.
- [x] Mermaid prerequisite dependency graph, rendered successfully.
- [x] Five learning paths with prerequisites, exit competencies, and capstones.
- [x] Proposed repository tree with status markers.
- [x] Manifest schema with IDs, prerequisites, status, level, effort, and validation.
- [x] Research methodology and teaching strand.
- [x] Assumptions, gaps, diagnostic plan, and risks.
- [x] Source ledger with verification status.
- [x] Architecture review checklist.
- [ ] Learner confirms or corrects the assumptions in `ASSUMPTIONS_AND_GAPS.md`.
- [ ] Decisions on Q01–Q10 and Q14.
- [x] Documentation framework implemented: templates, schema, scripts, CI, example page.
- [ ] CI has run successfully on GitHub Actions.
- [ ] Approval to continue with M1 safety and glossary artifacts.

## 9. M1 status and next milestone

The M1 documentation framework is implemented. It added the following files and did **not** author any technical lesson:

| Artifact | Status |
|---|---|
| `mkdocs.yml` — MkDocs 1.6.1 + Material 9.7.7, search, navigation, Mermaid fence | ✅ |
| `requirements-docs.txt` — pinned documentation toolchain | ✅ |
| `Makefile` — install, serve, build, lint, links, manifest, Mermaid, check | ✅ |
| `manifest/schema.json` — JSON Schema 2020-12 | ✅ |
| `scripts/validate_manifest.py` — schema, DAG, paths, outcomes, sources | ✅ |
| `scripts/check_links.py` — local links, anchors, MkDocs nav targets | ✅ |
| `scripts/check_mermaid.py` — structural checks plus optional `mmdc` rendering | ✅ |
| `templates/tutorial.md` | ✅ |
| `templates/lab.md` | ✅ |
| `templates/assessment.md` | ✅ |
| `templates/research-paper-review.md` | ✅ |
| `templates/architecture-review.md` | ✅ |
| `examples/documentation-example.md` — flowchart, sequence, state | ✅ |
| `.github/workflows/docs.yml` — manifest, links, lint, strict build | ✅ configured, not yet run on GitHub |

Remaining M1 artifacts:

1. `CONTRIBUTING.md` — authoring workflow, review roles, source policy, AI policy.
2. `GLOSSARY.md` — shared terminology, seeded from the module catalog.
3. `LAB_SAFETY.md` — authorization template, isolation checklist, data handling, cleanup, incident reporting.
4. `PROGRESS_TRACKER.md` — learner-facing module status, evidence log, and gate tracking.

The first technical lesson is written in M2 only after `LAB_SAFETY.md` and the templates are reviewed.

## 10. Approval and next action

| Field | Value |
|---|---|
| Architecture owner | Cybersecurity Master Academy curriculum team |
| Reviewer | _To be completed_ |
| Review date | _To be completed_ |
| Decision | ☐ Approve · ☐ Approve with changes · ☐ Reject |
| Conditions | _To be completed_ |
| Next action | Review the framework, then complete the M1 safety/glossary artifacts |

## 11. Architecture review checklist

Use this checklist as the final gate. A checked box requires evidence, not intention.

### A. Scope and audience

- [x] The primary audience is stated and consistent across README, COURSE_MAP, and LEARNING_PATHS.
- [x] The curriculum states what it is not: no degree, certification, license, or authorization.
- [x] Experienced-developer assumptions are explicit and testable.
- [x] Beginner entry is possible through the foundation level without pretending it is fast.
- [ ] The learner has confirmed the assumptions that materially change the plan.

### B. Progression and prerequisites

- [x] Six levels have distinct purposes and exit criteria.
- [x] Every module except ORI-01 has at least one prerequisite.
- [x] The prerequisite graph is acyclic and validated.
- [x] No module depends on a higher-level module.
- [x] Every path is closed under prerequisites.
- [x] No non-elective module is orphaned.
- [ ] The first cohort confirms that the level gates are achievable at the stated pace.

### C. Outcomes and assessment alignment

- [x] Every module has at least two measurable outcomes.
- [x] Every module has at least one assessment that can evidence its outcomes.
- [x] Outcomes use observable verbs and artifacts, not vague familiarity.
- [x] Capstones have a weighted rubric and a panel defense.
- [x] Mastery thresholds and remediation rules are stated.
- [ ] Rubrics have been calibrated against real learner work.

### D. Learning paths

- [x] Five paths cover engineering, application security, offense, defense, and research.
- [x] Each path has a capstone, exit competencies, and portfolio evidence.
- [x] Each path states what it does not cover.
- [x] Time estimates are separated from the full-breadth estimate.
- [x] Acceleration and substitution rules are explicit.
- [ ] The learner has selected a path or a deliberate combination.

### E. Research and teaching

- [x] Research competencies start at L0 and progress to the thesis.
- [x] Every module requires an evidence note or reproduction log.
- [x] Ethics, disclosure, and open science are explicit.
- [x] `TCH-01` and teach-back requirements are defined.
- [x] The thesis has a proposal gate, a rubric, and a defense.
- [ ] The first teaching practicum has been observed and calibrated.

### F. Safety, ethics, and law

- [x] Offensive and malware labs require isolation and authorization.
- [x] The curriculum states that no lab targets a real third-party system.
- [x] Stop conditions, data handling, and cleanup are specified.
- [x] Dual-use and disclosure risks are addressed in the research strand.
- [ ] `LAB_SAFETY.md` and the authorization template exist and are reviewed.
- [ ] Jurisdiction-specific legal review is complete for the learner's context.

### G. Source grounding and accuracy

- [x] Primary sources are preferred over secondary summaries.
- [x] Every used source ID is declared in the ledger.
- [x] Verification levels distinguish landing-page checks from full-text review.
- [x] Draft and unstable sources are labeled.
- [x] No fabricated CVE, benchmark, command output, or citation is presented as fact.
- [ ] Module-level claims have been verified during authoring.

### H. Repository and navigation

- [x] The repository tree is proposed and status-marked.
- [x] The ten milestone files exist at stable paths.
- [x] Relative links and anchors resolve.
- [x] Each long document has a table of contents.
- [x] The manifest is the single source of truth for structure.
- [x] Navigation has been tested in the local MkDocs server.
- [ ] Navigation has been tested on GitHub Pages or another hosted deployment.

### I. Quality assurance and tooling

- [x] Manifest schema, integrity rules, and validation procedure are documented.
- [x] Structural, link, Markdown, and Mermaid checks were run in M0.
- [x] Mermaid charts render with a pinned CLI version.
- [x] Markdown lint passes with a documented configuration.
- [x] The validation scripts are committed.
- [x] The MkDocs site builds strictly.
- [ ] CI has run successfully on GitHub Actions.
- [ ] External link checking runs on a schedule.

### J. Maintainability and versioning

- [x] Schema and curriculum versions are recorded.
- [x] Status and validation lifecycles are defined.
- [x] Change process and semantic-version rules are documented.
- [x] Source refresh cadence is defined.
- [ ] A changelog exists and the first cohort's revisions are recorded.

### K. Learner reality

- [x] Time estimates are explicit and range-based.
- [x] Hardware, network, cloud, and budget constraints are documented.
- [x] Likely gaps and remediation are mapped.
- [x] Burnout and sustainability risks are acknowledged.
- [ ] Accessibility needs have been assessed and accommodated.
- [ ] The learner's actual weekly schedule has been tested for one month.

### L. Teaching readiness

- [x] Lesson, lab, and assessment contracts are specified.
- [x] Teaching outcomes and a rubric are defined.
- [x] The research path requires a teaching practicum.
- [ ] At least one lesson has been taught and revised with feedback.
- [ ] Assessment items have been reviewed for bias, clarity, and alignment.

### M. Final decision

- [ ] The architecture is approved as written.
- [ ] Or: the architecture is approved with the conditions recorded in section 10.
- [ ] Or: the architecture is rejected, with reasons and a revision owner recorded.

**Reviewer signature:** ______________________  **Date:** ______________
