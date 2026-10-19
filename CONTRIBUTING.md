# Contributing to Cybersecurity Master Academy

> **Status:** authoring and review contract. **Last updated:** 2026-10-19.

This repository is a source-grounded curriculum, not a collection of notes. A contribution is acceptable when another reviewer can identify its module, reproduce its evidence, verify its sources, and determine what it does **not** establish.

## 1. Before you write

1. Read [`COURSE_MAP.md`](./COURSE_MAP.md), [`LEARNING_PATHS.md`](./LEARNING_PATHS.md), and the relevant manifest entry.
2. Confirm the module has a stable ID and its prerequisites are already declared.
3. For any lab or target interaction, read [`LAB_SAFETY.md`](./LAB_SAFETY.md) before drafting.
4. For research content, read [`RESEARCH_STRAND.md`](./RESEARCH_STRAND.md) and the relevant research tutorial.
5. Check the source ledger in [`REFERENCES.md`](./REFERENCES.md). Do not invent a citation to fill a gap; record the gap.

## 2. Canonical files and the manifest

- Markdown is the canonical format.
- [`manifest/course-manifest.yaml`](./manifest/course-manifest.yaml) is the authoritative machine-readable curriculum state.
- [`COURSE_MAP.md`](./COURSE_MAP.md) and [`diagrams/dependency-graph.md`](./diagrams/dependency-graph.md) are derived views; update them when the manifest changes.
- `mkdocs.yml` controls publication navigation. A page that is not linked from the repository or the navigation must be intentionally private or marked as an authoring artifact.
- Do not edit the `docs/` symlink view; edit the canonical root files.

Run the checks before opening a review:

```bash
make install
make check
make mermaid
```

`make check` runs manifest validation, local links, Markdown lint, and a strict site build. `make mermaid` is optional when `mmdc` is unavailable; record that it was skipped.

## 3. Tutorial contribution checklist

A tutorial must include:

- a stable module and tutorial ID, level, prerequisites, effort, and observable outcomes;
- a first-principles explanation that defines unfamiliar terms before using them;
- at least one meaningful Mermaid diagram with an explanation;
- worked examples with commands or code and labeled outputs;
- a lab reference with scope, setup, expected observations, verification, cleanup, and troubleshooting;
- security implications, failure modes, and a threat model where applicable;
- common misconceptions and progressive exercises;
- knowledge-check questions with answers in a separate instructor key;
- key takeaways, verified further reading, cross-links, and a completion checklist;
- a research artifact or teach-back where the module requires one.

Use [tutorial template](./authoring-templates/tutorial.md) and [lab template](./authoring-templates/lab.md). Remove every `[PLACEHOLDER]` before publishing.

## 4. Source and claim rules

Use primary sources where practical: standards, official project documentation, peer-reviewed papers, and original datasets.

For each source:

- record it in `REFERENCES.md` with a stable ID;
- state the verification level (`V1`–`V5`) and what was actually checked;
- do not mark a source `V1` if the landing page returned an error or you did not inspect it;
- record the version, edition, or date when the claim depends on it;
- mark preprints, drafts, unstable project pages, and blocked publisher pages explicitly.

For each technical claim:

- cite the specific source or show the command output that supports it;
- separate observation from inference;
- label generated examples and hypothetical numbers;
- state version-dependent behavior and the tested environment;
- do not present a template, a remembered result, or a generated output as captured evidence.

If a source cannot be verified, keep the claim out or mark it unresolved. A missing citation is a defect; a fabricated citation is a critical integrity failure.

## 5. Labs and assessments

- Separate learner instructions, instructor solution, and rubric files.
- Never place real credentials, personal data, or production captures in a lab.
- Do not use `--privileged`, host mounts, or production targets without an explicit reviewed exception.
- Every lab path must state what was actually executed and what remains manual.
- An expected observation is not a result. Use language such as "expected, not yet measured" until evidence exists.
- Assessments must map items to outcomes, state a pass rule, and include a separate answer key.
- Do not publish answer keys or solutions in the MkDocs site. Repository access is not a confidentiality control; restrict repository or LMS permissions separately.

## 6. Review roles

| Review | What it checks |
|---|---|
| Technical | Commands, mechanism, terminology, version sensitivity, and whether the evidence supports the explanation |
| Safety | Authorization, isolation, data handling, stop conditions, and blast radius |
| Editorial | Structure, definitions, links, diagrams, accessibility, and consistency |
| Assessment | Outcome alignment, item quality, rubric calibration, and answer-key correctness |
| Research | Question, method, evidence standard, ethics, reproducibility, and claim discipline |

A technical author may not be the only technical or safety reviewer for offensive, forensic, malware, or human-subjects material. Record reviewer names and dates in the manifest when a module moves beyond `drafted`.

## 7. AI assistance

AI assistance is permitted only when it is disclosed and verified. The contributor remains responsible for:

- every citation and quoted claim;
- every command and output;
- the safety and legality of the work;
- the accuracy of the final text.

Do not submit AI-generated citations, experimental results, code output, or source summaries that you have not checked. Mark generated examples explicitly.

## 8. Change workflow

1. Open a focused change with one module or governance area.
2. Update the manifest and derived views together.
3. Run the smallest relevant check, then `make check` before review.
4. For a lab change, record the exact commands and whether the path was executed on a clean environment.
5. For a source change, update the ledger and the affected tutorial references.
6. For a status change, satisfy the lifecycle rules in [`CURRICULUM_MANIFEST.md`](./CURRICULUM_MANIFEST.md) and record the reviewer.
7. Do not mark a module `published` merely because the site builds.

## 9. Definition of done

A contribution is done when:

- the manifest and catalog agree;
- prerequisites are closed and ordered;
- outcomes map to assessment evidence;
- sources resolve and their verification level is honest;
- labs state scope, safety, reproducibility, limitations, and cleanup;
- diagrams render and explain a real mechanism;
- links and anchors resolve;
- Markdown lint passes;
- the strict site build passes;
- a second reviewer has checked the claims that the author cannot independently verify.

## 10. Reporting a problem

For a technical or safety defect, open an issue with the affected file, the command or source used, the observed result, and the expected result. Do not include credentials, personal data, or live target details in a public issue. For a suspected vulnerability in a third-party system, follow [`research/06-ethics-disclosure-and-open-science.md`](./research/06-ethics-disclosure-and-open-science.md) rather than testing further.
