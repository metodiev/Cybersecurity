# Evaluation Rubric: Lab SYS-02

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
| 2 | Environment and reproducibility | 10 | Records OS, kernel, and tools | Records versions, architecture, and exact commands | Another analyst can reproduce the trace and namespace checks |
| 3 | Syscall trace and file-descriptor analysis | 20 | Identifies the open and read calls | Maps descriptors and return values | Explains short reads, error paths, and trace limitations |
| 4 | Credential and sandbox analysis | 15 | Lists UID, capabilities, and `Seccomp` | Explains each field | Relates the fields to least privilege and a concrete risk |
| 5 | Namespace and resource evidence | 15 | Shows namespace links | Compares host and namespace inodes and interfaces | Explains why a user namespace is not a complete boundary |
| 6 | Boundary-failure analysis | 15 | Names a boundary | Names the failed control and evidence | Connects prevention, detection, and residual risk |
| 7 | Analysis and uncertainty | 10 | States decisions for testable hypotheses | Distinguishes observation from inference | Handles "not tested" and inconclusive results honestly |
| 8 | Safety and evidence discipline | 5 | No unauthorized target or fabricated output | Commands and outputs are traceable | Evidence index is complete and consistent |

## Critical failures

Any of the following results in a failing grade for the lab:

- Attaching a tracer to a process the learner does not own.
- Using `--privileged` or adding `CAP_SYS_ADMIN` without explicit written authorization.
- Testing a remote or production system.
- Fabricating, editing, or borrowing another machine's trace or `/proc` output.
- Claiming a container escape or exploitation result that was not demonstrated.
- Disabling SIP, seccomp, ASLR, or kernel hardening.

## Evidence checklist

- [ ] Environment record with OS, kernel, architecture, compiler, `strace`, and runtime.
- [ ] Successful trace with descriptor consistency.
- [ ] Denied trace with the exact errno and exit status.
- [ ] Credential snapshot with UID/GID, capabilities, `Seccomp`, and `NoNewPrivs`.
- [ ] Host and namespace inode comparison.
- [ ] Namespace experiment output, including a recorded failure if applicable.
- [ ] Container comparison or an explicit "not tested" statement.
- [ ] Boundary analysis for scenarios A–C.
- [ ] At least four limitations and one confounder.

## Reviewer notes

- Accept `open` or `openat` depending on libc and toolchain.
- Do not require a specific capability mask; require correct interpretation.
- A root run that succeeds where the unprivileged run failed is a valid observation if it is recorded separately and explained.
- If `unshare` is blocked by policy, full credit is available for a correct error capture and explanation.
- H3 is optional; no penalty when the learner states that no container runtime was available.

## Feedback format

Provide:

1. **What worked:** two specific strengths with evidence.
2. **What is missing:** the criterion and the evidence required.
3. **Next action:** one concrete revision that would raise the grade.
4. **Score:** per criterion and total.
