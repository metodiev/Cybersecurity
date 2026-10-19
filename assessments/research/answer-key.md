# Answer Key: Research Track Knowledge Checks

> **Access:** instructor-only. Excluded from the published site. Do not distribute before the assessment.

## Research 1: Literature search

1. **Protocol as method.** It defines the sampling frame, queries, dates, and screening, so another reviewer can reproduce the review and assess coverage bias.
2. **Criterion versus reason.** A criterion is the rule fixed before screening; a reason explains why a specific record failed a criterion.
3. **Preprint labeling.** A preprint has not completed peer review; labeling prevents readers from treating it as established evidence and prompts a check for a published version.
4. **PRISMA-style flow.** It reports identification, deduplication, screening, exclusions with reasons, and inclusion, making the selection auditable.
5. **Extraction.** "The paper says X" omits the method, population, evidence, and uncertainty needed to judge whether X is supported and applicable.

## Research 2: Questions and threat models

1. **Answerable.** An observation or argument could answer it, and the population, system, and outcome are specified.
2. **Operationalization.** It turns an abstract construct into variables, metrics, and evidence so the claim can be tested.
3. **Null versus alternative.** The null states no difference or no relationship; the alternative states the expected difference or relationship.
4. **Validity threat model.** It covers selection, confounding, measurement, leakage, overfitting, and scope, which are not properties of the adversary.
5. **Pre-registration.** It separates confirmatory tests from exploratory analysis and reduces the chance of post-hoc rationalization, while still allowing exploratory results to be reported as such.

## Research 3: Design

1. **Baseline versus control.** A baseline is the comparison condition; a control variable is a factor held constant.
2. **Unit of analysis.** It determines what counts as an independent observation and therefore the sample size and valid analysis.
3. **Power.** The probability of detecting an effect of a given size if it exists; it needs effect size, variance, sample size, alpha, and test.
4. **Randomization limits.** It does not remove measurement error, selection into the study, or external-validity limits.
5. **Benchmark overstatement.** Benchmarks may be unrepresentative and may be optimized against, so performance can exceed real-world performance.

## Research 4: Measurement and statistics

1. **p-value.** The probability of data at least as extreme as observed, assuming the null hypothesis and model; it is not the probability the null is true.
2. **Interval.** It communicates a range of plausible values and the precision of an estimate, unlike a single point.
3. **Statistical versus practical.** A statistically detectable effect may be operationally trivial; practical significance depends on costs and context.
4. **Multiplicity.** Many tests increase false positives; correction or exploratory labeling controls the error rate or the interpretation.
5. **Confusion matrix.** A single metric can hide the trade-off between false positives and false negatives, especially under class imbalance.

## Research 5: Reproducibility

1. **Reproducibility versus replicability.** Reproducibility reruns the same data and method; replicability tests the claim with new data or a new study.
2. **Seeds and versions.** They make stochastic procedures and environment-dependent behavior repeatable and allow drift to be detected.
3. **Replication report.** It includes the original claim, protocol, deviations, environment, results, comparison criterion, uncertainty, and limitations.
4. **Failed replication.** It can reveal scope, implementation, environment, or analysis differences and can refine the original claim.
5. **Badge limits.** An artifact badge indicates that an artifact was reviewed against a policy; it does not prove the scientific claim is true or that every environment can rerun it.

## Research 6: Ethics

1. **Authorization versus consent.** Authorization permits system access; consent permits human participation after understanding risks. Neither implies the other.
2. **Menlo.** It adapts respect for persons, beneficence, and justice to ICT research and adds respect for law and public interest.
3. **CVD phases.** Private report, acknowledgment, validation, fix coordination, verification, and coordinated publication, with escalation if needed.
4. **Controlled access.** It allows qualified researchers to reproduce while reducing privacy, dual-use, or confidentiality risk.
5. **Ethics section.** It states authorization or consent, review, data handling, dual-use assessment, disclosure, and conflicts.

## Research 7: Writing

1. **Claim–evidence map.** A table linking each claim to its scope, evidence, uncertainty, alternative, and limitation.
2. **Abstract scope.** The abstract is the most-read summary; overclaiming there misleads readers who never reach the limitations.
3. **Threat model section.** Adversary capabilities, assets, trust boundaries, assumptions, and attack surface.
4. **Artifact restrictions.** State what is withheld, why, who can access it, and under what conditions.
5. **Limitation versus excuse.** A limitation bounds the claim; an excuse avoids responsibility for a fixable design defect.

## Research 8: Domain designs

1. **Unit in fuzzing.** A program or campaign, depending on the question; unique triaged bugs are the outcome, not the unit, unless the design says otherwise.
2. **Intention versus behavior.** Self-reported intention does not demonstrate what people do under real constraints.
3. **Model checking.** It verifies a property in a model under assumptions and bounds; it does not prove the deployed system secure.
4. **Deception study.** Justification, review, and debriefing, plus consent or a justified waiver.
5. **Domain threat models.** Bugs, human behavior, and formal models have different sources of error, so their validity threats differ.

## Scoring notes

Award full credit for a correct answer with a reason. Deduct for:

- treating a p-value as a posterior probability;
- claiming model checking proves the deployed system;
- conflating reproducibility and replication;
- claiming a container is a VM;
- presenting a generated example as a measurement.
