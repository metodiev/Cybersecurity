# Cybersecurity Master Academy

> **Status: architecture draft (v0.1.0), first foundations batch authored.** SYS-01 (Computer Architecture and Memory) and SYS-02 (Operating Systems Internals) now have modular tutorials, labs, assessments, and instructor solutions. All are `drafted` and `structural`; no lab has been executed on a clean Linux environment in this repository, so no module is `technical` or `published`.

A structured, source-grounded path from systems fundamentals to research-level cybersecurity, designed for an experienced software developer who wants advanced technical depth, the ability to conduct and publish research, and the skill to teach others.

## What this repository is

- A **progressive curriculum** in six levels, from orientation to research-level contribution.
- A **modular library** of lessons, labs, assessments, diagrams, and capstones, each with a stable identifier.
- A **dependency-driven design**: every module declares prerequisites, measurable outcomes, effort, assessment, sources, and safety constraints.
- A **research apprenticeship**: methods, evidence, reproducibility, ethics, disclosure, and teaching run alongside the technical track rather than appearing at the end.
- A **maintained artifact**: a machine-readable manifest, a source ledger, and validation rules keep the material consistent as standards and tools change.

## What it is not

- **Not a degree, certification, license, or professional authorization.** Completing material here does not grant any credential or permission to test systems.
- **Not a collection of exploit recipes.** Offensive material is taught with detection, mitigation, law, ethics, and isolated-lab requirements.
- **Not a claim of completeness.** Most modules are `planned`; SYS-01 and SYS-02 are `drafted` and `structural`, but their Linux lab paths have not been executed on a clean environment in this repository. No module is `published`.
- **Not a substitute for supervised practice.** Mastery requires evidence, feedback, and real-world judgment, not reading alone.

## Who it is for

**Primary audience:** an experienced software developer (roughly 3+ years) targeting advanced cybersecurity expertise, academic research, and teaching.

**Also usable by:** strong beginners willing to complete the foundation level. No prior security experience is assumed. Prior programming and command-line experience is assumed.

See [`ASSUMPTIONS_AND_GAPS.md`](./ASSUMPTIONS_AND_GAPS.md) for the full learner model, diagnostic plan, and known gaps. If those assumptions are wrong, the plan changes; do not skip that file.

## Design at a glance

| Dimension | Design choice |
|---|---|
| Levels | L0 orientation → L1 systems → L2 core security → L3 advanced → L4 expert/leadership → L5 research |
| Modules | 67 (59 modules, 3 electives, 5 capstones) |
| Measurable outcomes | 201, assessed through module-level artifacts and rubrics |
| Effort | ~1,950 hours for the full breadth; 784–1,164 hours for one learning path |
| Paths | Security Engineering, Application/Product Security, Offensive Security Research, Defensive Security Research (Detection/IR/DFIR), Academic Security Research |
| Research | Eight methods tutorials, five research templates, and a P1–P4 project ladder; `RES-01`, `RES-02`, `RES-06`, and `RES-07` drafted |
| Teaching | `TCH-01` plus a teach-back requirement in every module |
| Source grounding | 149 source records with verification status in [`REFERENCES.md`](./REFERENCES.md) |
| Authored tutorials | 17: 9 systems tutorials and 8 research-methods tutorials |
| Machine-readable state | [`manifest/course-manifest.yaml`](./manifest/course-manifest.yaml) |

## Start here

1. Read [`COURSE_MAP.md`](./COURSE_MAP.md) for the full architecture, module-by-module outcomes, assessment strategy, and milestones.
2. Choose a route in [`LEARNING_PATHS.md`](./LEARNING_PATHS.md).
3. Inspect the prerequisite graph in [`diagrams/dependency-graph.md`](./diagrams/dependency-graph.md).
4. Check your starting point against [`ASSUMPTIONS_AND_GAPS.md`](./ASSUMPTIONS_AND_GAPS.md).
5. Review the research and teaching spine in [`RESEARCH_STRAND.md`](./RESEARCH_STRAND.md).
6. Review the schema and governance rules in [`CURRICULUM_MANIFEST.md`](./CURRICULUM_MANIFEST.md).
7. Before approving the architecture, work through [`ARCHITECTURE_REVIEW.md`](./ARCHITECTURE_REVIEW.md).

## First foundations batch

The first authored batch covers the architecture and operating-system concepts that security depends on. Read SYS-01 before SYS-02.

| Module | Tutorials | Lab | Assessment |
|---|---|---|---|
| [SYS-01: Computer Architecture and Memory](./tutorials/sys-01-computer-architecture/README.md) | Machine model, memory and stack, binary anatomy, mitigations | [SYS-01 lab](./labs/sys-01-memory-and-binaries/lab.md) | [SYS-01 assessment](./assessments/sys-01/assessment.md) |
| [SYS-02: Operating Systems Internals](./tutorials/sys-02-operating-systems/README.md) | Privilege levels, processes, files and permissions, syscalls, isolation | [SYS-02 lab](./labs/sys-02-syscalls-and-isolation/lab.md) | [SYS-02 assessment](./assessments/sys-02/assessment.md) |

Both modules are `drafted` and `structural`: content, labs, and assessments exist and the structural checks pass. The labs are research-informed: each states a question, hypotheses, measurement plan, evidence requirements, reproducibility notes, limitations, and manual-testing status. Student instructions, separate rubrics, and instructor solutions are distinct files. They are not `technical` or `published` until every lab path runs on a clean environment and the results are reviewed. Instructor solutions and answer keys are in the repository but excluded from the published site; repository access still controls who can read them.

## Academic research track

The research track is now implemented as a modular methods sequence, not only a requirements document. It covers literature search, source evaluation, questions, hypotheses, threat models, design, baselines, controls, sampling, metrics, statistics, reproducibility, disclosure, ethics, limitations, and scientific writing.

| Component | Start here |
|---|---|
| Track overview | [research/README.md](./research/README.md) |
| Methods tutorials | [Literature search](./research/01-literature-search-and-source-evaluation.md) · [Questions and threat models](./research/02-research-questions-hypotheses-and-threat-models.md) · [Experimental design](./research/03-experimental-design-baselines-and-sampling.md) · [Measurement and statistics](./research/04-measurement-statistics-and-uncertainty.md) · [Reproducibility](./research/05-reproducibility-and-replication.md) · [Ethics and disclosure](./research/06-ethics-disclosure-and-open-science.md) · [Scientific writing](./research/07-scientific-writing-and-publication.md) · [Domain designs](./research/08-domain-research-designs.md) |
| Templates | [Paper review](./authoring-templates/research-paper-review.md) · [Literature matrix](./authoring-templates/literature-matrix.md) · [Experiment plan](./authoring-templates/experiment-plan.md) · [Replication report](./authoring-templates/replication-report.md) · [Publication outline](./authoring-templates/publication-outline.md) |
| Projects | [P1 literature review](./research/projects/01-structured-literature-review.md) · [P2 replication](./research/projects/02-replication-study.md) · [P3 controlled experiment](./research/projects/03-controlled-experiment.md) · [P4 thesis and paper](./research/projects/04-thesis-proposal-and-paper.md) |
| Rubrics | [Research project rubrics](./research/projects/rubrics.md) |
| Assessment | [Research portfolio assessment](./assessments/research/assessment.md) |

The track requires explicit research questions, evidence, alternative explanations, limitations, and reproducibility instructions. It distinguishes original results, cited claims, assumptions, and generated examples. No research result is claimed; the project briefs are specifications awaiting execution and review.

## Repository layout

`✅` = present; `⬜` = planned, not yet created.

```text
.
├── README.md                          ✅  canonical home page; published as docs/index.md
├── index.md -> README.md              ✅  root-relative link alias for the home page
├── authoring-templates -> templates   ✅  root-relative alias for published template links
├── mkdocs.yml                         ✅  MkDocs + Material configuration
├── requirements-docs.txt              ✅  pinned documentation toolchain
├── Makefile                           ✅  install / serve / build / check workflow
├── .pymarkdown.json                   ✅  Markdown lint configuration
├── .github/workflows/docs.yml         ✅  CI: manifest, links, lint, strict build
├── LICENSE                            ✅  GPL-3.0
├── COURSE_MAP.md                      ✅  levels, module catalog, assessment, milestones
├── LEARNING_PATHS.md                  ✅  five routes with sequencing and exit competencies
├── CURRICULUM_MANIFEST.md             ✅  manifest schema, lifecycle, integrity rules
├── RESEARCH_STRAND.md                 ✅  research and teaching spine
├── ASSUMPTIONS_AND_GAPS.md            ✅  learner model, diagnostics, risks
├── REFERENCES.md                      ✅  verified source ledger
├── ARCHITECTURE_REVIEW.md             ✅  decisions, open questions, review checklist
├── manifest/
│   ├── course-manifest.yaml           ✅  machine-readable curriculum state
│   └── schema.json                    ✅  JSON Schema 2020-12
├── diagrams/
│   └── dependency-graph.md            ✅  ten rendered Mermaid views
├── templates/
│   ├── tutorial.md                    ✅  tutorial contract
│   ├── lab.md                         ✅  lab contract
│   ├── assessment.md                  ✅  assessment and rubric contract
│   ├── research-paper-review.md       ✅  paper critique contract
│   ├── literature-matrix.md           ✅  search protocol and evidence matrix
│   ├── experiment-plan.md             ✅  pre-registration-style design
│   ├── replication-report.md           ✅  replication and deviation report
│   ├── publication-outline.md         ✅  claim–evidence map and paper plan
│   └── architecture-review.md         ✅  architecture review contract
├── examples/
│   └── documentation-example.md       ✅  flowchart, sequence, and state diagrams
├── scripts/
│   ├── validate_manifest.py           ✅  schema + DAG + path + source validation
│   ├── check_links.py                 ✅  local links, anchors, nav targets
│   └── check_mermaid.py               ✅  structural and optional render checks
├── docs/                              ✅  MkDocs publication view (symlinks)
│   ├── index.md -> ../README.md
│   ├── COURSE_MAP.md -> ../COURSE_MAP.md
│   ├── diagrams -> ../diagrams
│   ├── manifest -> ../manifest
│   ├── authoring-templates -> ../templates
│   ├── examples -> ../examples
│   ├── tutorials -> ../tutorials
│   ├── labs -> ../labs
│   ├── assessments -> ../assessments
│   ├── research -> ../research
│   └── LICENSE -> ../LICENSE
├── CONTRIBUTING.md                    ⬜  authoring and review workflow
├── GLOSSARY.md                        ⬜  shared terminology
├── LAB_SAFETY.md                      ⬜  authorization, isolation, data handling
├── PROGRESS_TRACKER.md                ⬜  learner-facing progress and evidence log
├── tutorials/                         ✅  SYS-01 and SYS-02 tutorials
├── labs/                              ✅  two research-informed labs with rubrics, reproducibility notes, and instructor solutions
├── assessments/                       ✅  SYS-01, SYS-02, and research portfolio assessments
├── research/                          ✅  methods tutorials, templates links, and P1–P4 project ladder
├── projects/                          ⬜  five capstone briefs and submission packs
```

## Documentation site

The publication site uses **MkDocs 1.6.1** with **Material for MkDocs 9.7.7**. Canonical Markdown remains at the repository root. `docs/` is a publication view built from symlinks, so edit the root files and never edit the symlinks.

Prerequisites: **Python 3.10+** (verified with Python 3.14). Node.js is not required for the normal site build. On Windows, enable symlink support or use WSL, because `docs/` depends on symlinks.

| Command | What it does |
|---|---|
| `make install` | Creates `.venv` and installs the pinned toolchain from `requirements-docs.txt` |
| `make serve` | Serves at `http://127.0.0.1:8000` with live reload |
| `make check` | Runs manifest validation, link/anchor/nav checks, Markdown lint, and a strict MkDocs build |
| `make build` | Builds the static site into `site/` with `--strict` |
| `make mermaid` | Optionally renders every Mermaid block with `mmdc`; reports a skip if `mmdc` is unavailable |
| `make clean` | Removes `site/` |

Mermaid is configured with the documented Material integration: `pymdownx.superfences` with a `mermaid` custom fence. No separate JavaScript bundle is added by this repository; Material initializes the diagram runtime when a page contains a Mermaid block.

MkDocs reserves a `templates/` directory, so the publication view is `docs/authoring-templates/`; the canonical templates remain in `templates/`. The `.venv/` and `site/` directories are intentionally ignored by Git. The CI workflow runs the same checks on every push and pull request.

`make install` defaults to `python3.14`; override it with `make install PYTHON=python3.12` if needed. The Markdown lint configuration disables only rules that do not affect structure or rendering: line length, inline HTML, emphasis used as a heading, descriptive-link-text, and hard-tab detection (captured tool output contains real tabs). It also allows numbered lists that restart at an extended value after a subsection heading. The Mermaid render target is optional because it requires `mmdc`; the site build itself does not. Material 9.7.7 also prints an upstream warning about future MkDocs 2.0 changes; this repository pins MkDocs 1.6.1 and Material 9.7.7, and the warning does not fail the strict build.

## How the curriculum is built

### 1. One source of truth

Module IDs, prerequisites, levels, effort, outcomes, sources, and safety flags live in [`manifest/course-manifest.yaml`](./manifest/course-manifest.yaml). The catalog and diagrams are generated from that data. A change to a prerequisite is a data change, not a hunt through prose.

### 2. A module contract

Every authored module must contain the 18 elements listed in [`COURSE_MAP.md`](./COURSE_MAP.md#9-definition-of-done-for-a-module), including measurable outcomes, a tested lab, assessment with answer key, defensive implications, misconceptions, further reading, and a completion checklist.

### 3. Evidence before claims

No command output, benchmark, CVE detail, tool capability, or experimental result may be invented. Labs require captured artifacts. Version-dependent statements carry a date or version. Uncertainty is marked explicitly.

### 4. Research and teaching are not electives

Every technical module produces an evidence note or reproduction log for the research strand. Every module includes a teach-back. The academic path adds `TCH-01` and a thesis.

## Safety and ethics

- Work only in systems you own or have **written authorization** to test.
- Offensive labs use intentionally vulnerable applications, synthetic data, local VMs, or isolated containers.
- No lab in this curriculum targets a real third-party system.
- Stop conditions, data-handling rules, and cleanup are part of every lab.
- `LAB_SAFETY.md` is a required milestone-1 artifact. Until it exists, the safety rules in [`COURSE_MAP.md`](./COURSE_MAP.md#10-safety-gate) apply.

If you are unsure whether an action is authorized, stop and ask. Authorization is a written, scoped, and revocable decision, not an assumption.

## Grounding and source policy

The architecture is grounded in primary sources: NIST, CISA, MITRE, IETF RFCs, OWASP, FIRST, CIS, ISO/IEC, official project documentation, and peer-reviewed research. [`REFERENCES.md`](./REFERENCES.md) records what was checked, when, and how.

**Verification is not endorsement.** Most standards pages were checked at the landing-page/edition/date level on 2026-10-19; they were not read end to end for this milestone. Module-level reading and claim verification happen during authoring.

## Versions and review

| Item | Value |
|---|---|
| Curriculum version | `0.1.0` (architecture draft) |
| Manifest schema | `1.0.0` |
| Source verification date | `2026-10-19` |
| Review cadence | Every 6 months, plus event-driven review after major standard/tool changes |
| Change control | Manifest-first; regenerate catalog/diagrams; run validation; record review |

## Roadmap

| Milestone | Scope | Status |
|---|---|---|
| M0 | Architecture, manifest, paths, research strand, source ledger, review checklist | ✅ this milestone |
| M1 | Documentation framework, templates, validation scripts, CI (done); glossary, lab safety, and progress tracker remain | ◐ in progress |
| M2 | Level 0 tutorials, labs, assessments | ⬜ |
| M3 | Level 1 foundations | ◐ SYS-01 and SYS-02 drafted; SYS-03, SYS-04, and the remaining L1 modules pending |
| M4 | Level 2 core security | ⬜ |
| M5 | Level 3 advanced specialization | ⬜ |
| M6 | Level 4 expert practice and leadership | ⬜ |
| M7 | Level 5 research and capstones | ◐ research methods track drafted; domain modules, thesis, and capstones pending |

## License

The repository is licensed under the GNU General Public License v3.0; see [`LICENSE`](./LICENSE). Third-party standards, quotations, and trademarks remain the property of their respective owners. Do not copy third-party material into this repository without checking its license.
