# Lab Template

> Copy this file to `labs/[MODULE-ID]/lab.md`. Keep the instructor solution in a separate file that learners cannot see.

## Lab metadata

| Field | Value |
|---|---|
| Lab ID | `[LAB-ID]` |
| Module | `[MODULE-ID]` |
| Level | `[L0-L5]` |
| Estimated duration | `[HOURS] h` |
| Risk | `low / moderate / high` |
| Isolation | `none / recommended / required` |
| Network | `host-only / internal / emulated / none` |
| Status | `planned` |
| Validation | `unvalidated` |
| Rubric | `rubric.md` |
| Instructor solution | `solution.md` (excluded from publication) |
| Reproducibility notes | `reproducibility.md` |

## Research or learning question

`[THE QUESTION THE LEARNER IS INVESTIGATING, NOT JUST THE TASK TO PERFORM]`

### Hypotheses

| ID | Hypothesis | Prediction | What would refute it |
|---|---|---|---|
| H1 | `[HYPOTHESIS]` | `[OBSERVABLE PREDICTION]` | `[OBSERVATION]` |
| H2 | `[HYPOTHESIS]` | `[OBSERVABLE PREDICTION]` | `[OBSERVATION]` |

If the lab is purely procedural, state why a hypothesis is not appropriate and use a learning question instead.

### Measurement plan

| ID | Metric | Operational definition | Evidence required | Analysis |
|---|---|---|---|---|
| M1 | `[METRIC]` | `[HOW IT IS MEASURED]` | `[FILE, COMMAND, OUTPUT]` | `[WHAT IT SUPPORTS]` |
| M2 | `[METRIC]` | `[HOW IT IS MEASURED]` | `[FILE, COMMAND, OUTPUT]` | `[WHAT IT SUPPORTS]` |

Do not make a quantitative claim that the measurement plan cannot support.

## Objectives

1. `[OBSERVABLE TASK]`
2. `[OBSERVABLE TASK]`
3. `[OBSERVABLE TASK]`

## Safety and authorization

- [ ] I own the target or have written authorization.
- [ ] The environment is isolated from untrusted networks.
- [ ] Snapshots are enabled and tested.
- [ ] Only synthetic data and test credentials are used.
- [ ] Stop conditions are documented.
- [ ] Cleanup steps are documented.

**Stop conditions:** `[WHAT ENDS THE LAB, WHO DECIDES, AND HOW TO RECOVER]`

## Environment and versions

| Component | Version | Notes |
|---|---|---|
| Host OS | `[VERSION]` | `[ARCHITECTURE]` |
| Virtualization | `[TOOL/VERSION]` | `[SNAPSHOT NAME]` |
| Target | `[IMAGE/VERSION]` | `[SOURCE]` |
| Tooling | `[TOOL/VERSION]` | `[INSTALL METHOD]` |

## Network boundaries

| Interface | Network | Purpose | Allowed destinations |
|---|---|---|---|
| `[IFACE]` | `[CIDR]` | `[PURPOSE]` | `[DESTINATIONS]` |

`[EXPLAIN WHY THE ISOLATION IS SUFFICIENT FOR THIS LAB.]`

## Setup

```bash
# Replace with setup commands.
[SETUP COMMAND]
```

Verification before starting:

```bash
[VERIFY COMMAND]
```

Expected: `[EXPECTED OUTPUT]`

## Tasks

### Task 1: `[TITLE]`

**Question:** `[WHAT THE LEARNER MUST DETERMINE]`

```bash
[COMMAND]
```

**Expected observation:** `[WHAT SHOULD HAPPEN]`

**Evidence to capture:** `[OUTPUT, LOG, HASH, TIMESTAMP]`

### Task 2: `[TITLE]`

**Question:** `[WHAT THE LEARNER MUST DETERMINE]`

```bash
[COMMAND]
```

**Expected observation:** `[WHAT SHOULD HAPPEN]`

**Evidence to capture:** `[OUTPUT, LOG, HASH, TIMESTAMP]`

### Task 3: `[TITLE]`

**Question:** `[WHAT THE LEARNER MUST DETERMINE]`

```bash
[COMMAND]
```

**Expected observation:** `[WHAT SHOULD HAPPEN]`

**Evidence to capture:** `[OUTPUT, LOG, HASH, TIMESTAMP]`

## Verification

A lab is complete only when:

- [ ] The stated observation was reproduced.
- [ ] The evidence includes the command, output, environment, and timestamp.
- [ ] Any deviation from the expected result is explained.
- [ ] The learner can explain why the result occurred.

Verification command:

```bash
[VERIFY COMMAND]
```

Expected result: `[EXPECTED]`

## Troubleshooting

| Symptom | Likely cause | Check | Resolution |
|---|---|---|---|
| `[SYMPTOM]` | `[CAUSE]` | `[COMMAND]` | `[FIX]` |
| `[SYMPTOM]` | `[CAUSE]` | `[COMMAND]` | `[FIX]` |

## Cleanup

```bash
[CLEANUP COMMAND]
```

- [ ] Revert the snapshot or destroy the environment.
- [ ] Remove test credentials and artifacts.
- [ ] Confirm no lab interface is bridged.
- [ ] Record the final state.

## Extension challenges

1. `[ADD A BASELINE OR CONTROL]`
2. `[MEASURE A RATE OR COMPARE TWO CONFIGURATIONS]`
3. `[ADD DETECTION OR MITIGATION]`

## Limitations and manual testing status

| Limitation or path | Status | Notes |
|---|---|---|
| `[LIMITATION]` | `[executed / not executed / out of scope]` | `[IMPACT]` |
| `[PLATFORM PATH]` | `[executed / not executed]` | `[WHAT REMAINS]` |

## Reproducibility notes

`[ENVIRONMENT PINS, KNOWN NONDETERMINISM, EVIDENCE RETENTION, AND WHAT ANOTHER REVIEWER NEEDS]`

## Evaluation rubric

The rubric is a separate file: `labs/[MODULE-ID]/rubric.md`. It must state weights, pass thresholds, critical failures, and evidence requirements.

## Instructor solution

Store the solution in `labs/[MODULE-ID]/solution.md` and restrict access. The solution must include:

- exact commands and observed output;
- a validation record separating executed from unexecuted paths;
- expected learner mistakes;
- grading notes for each objective;
- safety incidents and how to handle them.

## Completion checklist

- [ ] Objectives are observable.
- [ ] Safety and authorization are explicit.
- [ ] Environment and versions are recorded.
- [ ] Setup and verification were tested on a clean environment.
- [ ] Every task has expected observations and evidence requirements.
- [ ] Cleanup is tested.
- [ ] Troubleshooting covers the failures actually encountered.
- [ ] Extension challenges turn the lab into a small study.
