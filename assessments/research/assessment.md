# Research Track Portfolio Assessment

> **Track:** Academic Cybersecurity Research · **Level:** L5 · **Type:** portfolio plus oral defense
> **Time:** completed across the research modules · **Open book:** yes · **Status:** drafted · **Validation:** structural

## Purpose

This assessment tests whether you can conduct and defend a bounded piece of research, not whether you can recite definitions. It is a portfolio review: you submit artifacts produced during the research tutorials and projects, then defend the decisions orally.

It does not replace project-specific rubrics. It samples the portfolio against the same standards.

## Required portfolio

| # | Artifact | Source tutorial or project | Weight |
|---|---|---|---:|
| 1 | Search protocol and literature matrix with at least 12 sources | Research 1, P1 | 15 |
| 2 | Bounded question, hypotheses, and dual threat model | Research 2 | 15 |
| 3 | Experiment plan with baseline, controls, sampling, and analysis | Research 3–4, P3 | 20 |
| 4 | Replication or measurement report with uncertainty and limitations | Research 5, P2/P3 | 20 |
| 5 | Ethics, authorization, and disclosure plan | Research 6 | 10 |
| 6 | Publication outline with claim–evidence map | Research 7, P3/P4 | 10 |
| 7 | Oral defense | All | 10 |

## Outcome coverage

The portfolio is the evidence set for the drafted research modules. A reviewer must be able to point to the named artifact and the rubric language that supports each outcome.

| Module outcome | Required portfolio evidence | Rubric evidence |
|---|---|---|
| `RES-01.O1` | Bounded question, hypotheses, and security threat model | Question and contribution; design |
| `RES-01.O2` | Study design with controls, data-collection procedure, and validity analysis | Design; analysis and uncertainty |
| `RES-01.O3` | Search protocol and literature matrix | Literature and evidence |
| `RES-02.O1` | Sampling, power/precision justification, and test selection | Design; analysis and uncertainty |
| `RES-02.O2` | Analysis of a dataset or measurement report with effect sizes and intervals | Analysis and uncertainty |
| `RES-02.O3` | Confounding, selection, leakage, and p-hacking review | Evidence and method; analysis |
| `RES-06.O1` | Ethics analysis of a concrete research scenario | Ethics and disclosure |
| `RES-06.O2` | Disclosure plan, ethics application/record, and data-management plan | Ethics and disclosure |
| `RES-06.O3` | Reproducibility, sharing, and dual-use assessment | Ethics and disclosure; artifact statement |
| `RES-07.O1` | Thesis or paper proposal with question, related work, method, ethics, and timeline | Question and contribution; writing |
| `RES-07.O2` | Defense record and revision after feedback | Oral defense |
| `RES-07.O3` | Pre-registered analysis with success, failure, and stopping criteria | Evidence and method |

Outcomes for `RES-03`, `RES-04`, and `RES-05` are not assessed here while those modules remain `planned`; tutorial 8 is a cross-module design tutorial, not their assessment.

## What each artifact must demonstrate

### 1. Literature and evidence

- Reproducible queries and screening.
- Claims separated from evidence.
- Primary sources distinguished from secondary summaries.
- Preprints and generated examples labeled.

### 2. Question and threat models

- Population, intervention or exposure, outcome, and scope.
- Null and alternative hypotheses where appropriate.
- Security threat model and validity threat model.

### 3. Design

- Unit of analysis.
- Treatment and baseline.
- Control variables and confounders.
- Sampling frame and exclusions.
- Power or precision justification.

### 4. Analysis

- Metrics with denominators.
- Effect sizes and uncertainty.
- Multiplicity and exploratory labels.
- Alternative explanations.

### 5. Ethics

- Authorization or consent.
- Data minimization and privacy.
- Dual-use assessment.
- Disclosure plan with roles and decision points.

### 6. Writing

- Claim–evidence map.
- Limitations that are specific.
- Artifact availability statement.
- No claim beyond the evidence.

### 7. Defense

You must be able to:

- state the contribution in one sentence;
- explain one result without notes;
- identify the strongest alternative explanation;
- state what would falsify the claim;
- explain what you withheld and why.

## Scoring

| Criterion | Weight | Passing | Proficient | Exemplary |
|---|---:|---|---|---|
| Question and contribution | 15 | Stated | Bounded and significant | Scope and falsification are precise |
| Evidence and method | 25 | Described | Reproducible | Independent rerun or justified restriction |
| Analysis and uncertainty | 20 | Reported | Intervals and alternatives | Sensitivity and limits are rigorous |
| Ethics and disclosure | 15 | Documented | Reviewed | Trade-offs are reasoned |
| Writing and claim discipline | 15 | Clear | Claims map to evidence | No claim exceeds the evidence |
| Oral defense | 10 | Answers basic questions | Explains decisions | Handles counterarguments |

**Pass:** 80/100, no criterion below 60%, and no critical failure.

## Critical failures

- Fabricated data, citations, or command output.
- Unauthorized testing.
- Missing ethics or disclosure for work that requires it.
- A central claim that cannot be explained or traced to evidence.
- Presenting a generated example as a measurement.

## Submission format

Submit a repository or archive containing:

```text
portfolio/
├── README.md
├── literature/
├── question/
├── design/
├── analysis/
├── ethics/
├── writing/
├── artifact/            # or a restriction statement
└── defense.md
```

Include a manifest with file names, purposes, and the tutorial or project that produced each artifact.

## Integrity

- Declare AI assistance for drafting, analysis, or code.
- Every citation must resolve to a source you opened.
- Every result must trace to raw evidence.
- The oral defense is the check that the work is yours to explain.

## Rubrics

Project-specific rubrics: [`research/projects/rubrics.md`](../../research/projects/rubrics.md).

## Answer key

`answer-key.md` is instructor-only and excluded from the published site.
