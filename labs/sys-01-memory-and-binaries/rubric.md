# Evaluation Rubric: Lab SYS-01

> **Audience:** learner and reviewer. **Total:** 100 points. **Mastery:** 80 points, no criterion below 60%, no critical failure.
> **Lab:** [`lab.md`](lab.md) · **Instructor solution:** `solution.md` (excluded from the published site)

## Scoring levels

| Level | Points | Descriptor |
|---|---:|---|
| Exemplary | 90–100% of criterion | Complete, precise, reproducible, and critically examined |
| Proficient | 80–89% | Correct and evidence-based with minor gaps |
| Passing | 70–79% | Mostly correct; some claims lack evidence or nuance |
| Not yet | below 70% | Missing evidence, incorrect reasoning, or unsupported claims |

## Criteria

| # | Criterion | Weight | Passing | Proficient | Exemplary |
|---|---|---:|---|---|---|
| 1 | Research question and hypotheses | 10 | Restates the question and hypotheses | Explains what would refute each hypothesis | Connects the design to the question and anticipates alternative explanations |
| 2 | Environment and reproducibility | 15 | Records OS, compiler, and flags | Records versions, page size, and exact commands | Another learner can rebuild and rerun from the report alone |
| 3 | Build matrix and metadata | 15 | Builds all four binaries | Compares format, PIE, sections, and guard symbols | Explains each observed difference and its cause |
| 4 | Disassembly and control-flow analysis | 15 | Identifies the prologue and epilogue | Annotates guard load, store, compare, and failure path | Explains leaf versus non-leaf frames and why the guard is placed where it is |
| 5 | Measurement design and execution | 15 | Produces a CSV with 30 runs | Defines the metric and validates the CSV | Discusses sample size, page alignment, and what the design cannot estimate |
| 6 | Analysis and uncertainty | 15 | States a decision for each hypothesis | Distinguishes observation from inference | Handles inconclusive results and alternative explanations honestly |
| 7 | Limitations and threats to validity | 5 | Lists limitations | Names a confounder and its effect | Explains how the design controls or acknowledges each threat |
| 8 | Safety and evidence discipline | 5 | No unauthorized target or fabricated output | Commands and outputs are traceable | Evidence index is complete and consistent |
| 9 | Communication | 5 | Report is understandable | Tables and structure aid the argument | Executive summary and technical detail are both accurate |

## Critical failures

Any of the following results in a failing grade for the lab:

- Fabricating, editing, or padding command output or CSV rows.
- Running the lab against a system the learner does not own or have written authorization to test.
- Disabling host protections (ASLR, SIP, firewall) or using privileged containers without explicit authorization.
- Submitting a working exploit instead of an analysis.
- Claiming an entropy estimate from the 30-run sample.

## Evidence checklist

- [ ] Environment record with OS, architecture, compiler, flags, tool versions, page size.
- [ ] Four builds identified by name.
- [ ] Header and section/segment evidence for each build.
- [ ] Guard-symbol and disassembly comparison with annotations.
- [ ] `aslr-observations.csv` with at least 30 runs and six parsed addresses per row.
- [ ] `aslr-summary.json` with per-region distinct page counts.
- [ ] Rebuild hashes and metadata comparison.
- [ ] Hypothesis decisions with reasons.
- [ ] At least four limitations and one confounder.

## Reviewer notes

Use the learner's own evidence, not the instructor solution, to award points. If a result differs from the instructor's sample but is internally consistent and correctly interpreted, award full credit. The goal is defensible measurement, not matching a specific address or count.

## Feedback format

Provide:

1. **What worked:** two specific strengths with evidence.
2. **What is missing:** the criterion and the evidence required.
3. **Next action:** one concrete revision that would raise the grade.
4. **Score:** per criterion and total.
