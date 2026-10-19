# Learner Progress Tracker

> **Status:** reusable tracker template. **Last updated:** 2026-10-19.
> This file does not claim that any learner has completed a module. Copy it to a private learning log or LMS; do not commit personal evidence to a public repository.

## 1. Status vocabulary

| Status | Meaning | Required evidence |
|---|---|---|
| `planned` | Not started | None |
| `drafted` | Lesson, lab, and assessment are authored | Repository files exist |
| `reviewed` | Independent technical and editorial review passed | Reviewer, date, findings closed |
| `lab_validated` | The lab path ran on a clean environment and evidence was reproduced | Environment, commands, raw evidence, deviation log |
| `published` | Released with the required safety and assessment checks | Published URL or release identifier |
| `deprecated` | Superseded or withdrawn | Reason and replacement |

`lab_validated` is not the same as `published`. A module can have a working lab and still be missing accessibility, assessment calibration, or independent review.

## 2. Evidence log

Use one row per substantial learning artifact. A quiz score without an explanation is not evidence of mastery.

| Date | Module / tutorial | Activity | Command or artifact | Result | What I can explain without notes | Reviewer / follow-up |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | e.g. SYS-01.2 | Built layout program | `make all`; `evidence/metadata.txt` | Four binaries; page size recorded | Why two virtual addresses can map to different frames | Self-review; revisit TLB section |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## 3. Current authored modules

This is a convenience view, not the source of truth. The authoritative list is [`manifest/course-manifest.yaml`](./manifest/course-manifest.yaml).

| Module | Level | Status | Validation | Required learner evidence |
|---|---|---|---|---|
| `SYS-01` | L1 | `drafted` | `structural` | Four-build metadata, disassembly annotation, ASLR CSV, analysis report |
| `SYS-02` | L1 | `drafted` | `structural` | Real syscall trace, credential snapshot, namespace evidence, boundary analysis |
| `RES-01` | L5 | `drafted` | `structural` | Search protocol, literature matrix, question and threat models |
| `RES-02` | L5 | `drafted` | `structural` | Design, measurement plan, statistical analysis, replication report |
| `RES-06` | L5 | `drafted` | `structural` | Ethics, authorization, disclosure, and data-management plan |
| `RES-07` | L5 | `drafted` | `structural` | Thesis proposal, claim-evidence map, defense record |

The remaining modules are `planned` and `unvalidated` as of the manifest update date. Do not infer completion from a module appearing in a learning path.

## 4. Gate record

| Gate | Requirement | Evidence | Date | Reviewer |
|---|---|---|---|---|
| G0 — Safety | Read and apply [`LAB_SAFETY.md`](./LAB_SAFETY.md); complete the authorization/scope checklist | Signed scope or explicit local-only statement |  |  |
| G1 — Foundations | `ORI-01`, `SYS-01`, `SYS-02`, networking, programming, and cryptography prerequisites | Practical evidence and oral explanation |  |  |
| G2 — Core practice | Design, application, web/API, vulnerability, detection, and risk modules | Lab reports and assessment results |  |  |
| G3 — Advanced | Specialization modules and a threat-modeled project | Project review and rubric |  |  |
| G4 — Expert | Architecture, leadership, or research depth | Architecture review and portfolio |  |  |
| G5 — Research | Research methods, ethics, reproducibility, and defense | Research portfolio and oral defense |  |  |

A challenge exam may replace a foundation module only under the rules in [`LEARNING_PATHS.md`](./LEARNING_PATHS.md#rules). It does not waive the safety gate or capstone requirements.

## 5. Module evidence template

Copy this block for each module:

```text
Module:
Tutorials completed:
Date started / completed:
Environment (OS, kernel, compiler, tool versions):
Commands or lab path:
Raw evidence location:
Expected vs actual observations:
Hypotheses / claims tested:
What I can explain without notes:
What I could not reproduce:
Reviewer:
Next action:
```

## 6. Mastery checks

A module is not complete merely because the reading is finished. The learner should be able to:

- explain the mechanism from first principles without notes;
- trace a real command or binary to the relevant kernel or compiler mechanism;
- state one thing the evidence does **not** prove;
- reproduce the lab on a clean environment or explain the exact limitation;
- answer the assessment at the stated pass threshold;
- teach one concept back to another person and answer a counterexample.

## 7. Research evidence

For research modules and projects, track the additional artifacts required by [`research/README.md`](./research/README.md):

- literature matrix and search log;
- question, hypotheses, and dual threat model;
- experiment plan with baseline, controls, sampling, and analysis;
- raw evidence and analysis script;
- ethics, authorization, and disclosure record;
- replication or deviation report;
- claim-evidence map and artifact restriction statement.

## 8. Review cadence

Review this tracker after each module, not only at the end of a path. A gap found early is a revision; a gap found at the capstone is a failed prerequisite. Record what changed in the evidence log rather than overwriting the earlier entry.
