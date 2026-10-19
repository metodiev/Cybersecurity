# Quality Audit Report

> **Audit date:** 2026-10-19 · **Repository state:** uncommitted working tree · **Scope:** the complete repository content and documentation toolchain.
> **Method:** automated checks were run first; expert judgments are labeled separately. This report distinguishes what was executed from what still requires human, Linux, browser, or external review.

## Table of contents

- [1. Executive assessment](#1-executive-assessment)
- [2. Automated checks performed](#2-automated-checks-performed)
- [3. Expert findings](#3-expert-findings)
- [4. Critical publication blockers](#4-critical-publication-blockers)
- [5. Fix batches and validation plan](#5-fix-batches-and-validation-plan)
- [6. Verification not performed](#6-verification-not-performed)
- [7. Audit limitations](#7-audit-limitations)

## 1. Executive assessment

The repository is structurally coherent and the documentation build is healthy. The manifest validates, local links resolve, Markdown lint is clean, the strict MkDocs build succeeds, and the SYS-01 macOS lab path was reproduced during this audit. The research track is unusually explicit about evidence, uncertainty, and unexecuted work.

The repository is **not ready for an unrestricted public release** as a complete academy. At the start of the audit, the highest-risk defects were governance and safety artifacts that the design declares mandatory but that did not exist, a broken documented container workflow, a stale source URL, a few contradictory technical statements, and research metadata that did not match the manifest. The resolution table records which defects were fixed.

No fabricated experimental results were found in the authored tutorials or lab solutions. Generated examples are generally labeled. The main integrity risk is the opposite: several documents are more stale or more confident than the current repository state.

## 2. Automated checks performed

These results were produced by commands run during this audit. They do not establish the truth of the underlying technical claims.

| Check | Command or method | Exact outcome | Interpretation |
|---|---|---|---|
| Full local gate | `make check` | Exit 0; 67 modules, 201 outcomes, 1,950 h, 5 paths, 149/149 sources; 59 Markdown files, 490 local links, 148 external links skipped, 0 missing nav targets; Markdown lint 0 findings; strict build completed in 0.62 s | Baseline documentation checks pass |
| Manifest structure | `.venv/bin/python scripts/validate_manifest.py` | Exit 0; schema, IDs, DAG, level monotonicity, path closure, and source ledger passed | Structural checks only; it does not validate semantic prerequisite adequacy |
| Local links and anchors | `.venv/bin/python scripts/check_links.py` | Exit 0; 490 links checked; 148 external skipped | Local links only; external checking is opt-in |
| Markdown lint | `make lint` through `make check` | Exit 0; 0 findings | Style/structure lint; it is not a technical review |
| Strict site build | `mkdocs build --strict` through `make check` | Exit 0; site built | Build success is not a claim that pages are accurate |
| Mermaid structure | `.venv/bin/python scripts/check_mermaid.py` | Exit 0; 75 blocks found and passed structural start-token checks | Structural checks are necessary but not sufficient; see the render row |
| Mermaid render | Initial `scripts/check_mermaid.py --render --require-render`: exit 1 because `mmdc` was unavailable and Homebrew Node failed to load `simdjson`. Follow-up with portable Node 22.23.3 and Mermaid CLI 12.0.0 | Follow-up exit 0; 75/75 blocks rendered | The current 75 blocks render; visual semantic review remains separate |
| Lab checksums | `shasum -a 256 -c SHA256SUMS` in both labs | All 9 listed files passed | Current listed source/script files match their recorded hashes |
| Lab script syntax | `python3 -m py_compile` and `bash -n` | Passed | Syntax only; not execution |
| SYS-01 macOS path | Fresh build, 30-run measurement, and evidence verifier in `/tmp/audit-sys01` | Four binaries built; measurement exit 0; 30-row CSV; verifier exit 0 | The macOS path is reproducible on this host; Linux path remains unexecuted |
| SYS-02 container build | `docker build -f labs/sys-02-syscalls-and-isolation/environment/Containerfile ...` | Image built successfully | Build success did not imply the lab workflow was complete |
| SYS-02 container workflow | `scripts/collect_evidence.sh`, then `scripts/verify_evidence.py` inside the image | Collector exit 0; `unshare` failed with `Operation not permitted`; verifier exit 127 because `python3` is absent | The documented container path cannot run the verifier; the default root user invalidates the unprivileged hypothesis |
| External source crawl | One-off HTTP GET against 148 URLs in `REFERENCES.md`; plus `scripts/check_links.py --external` | 122 HTTP 200, 6 HTTP 202, 14 HTTP 403/blocked, 6 connection failures; external checker reported one actual 404 (`N28`) plus 403/429/network failures | Most links resolve; the ledger has one confirmed broken URL and several known bot/rate-limit cases |
| Heading and fence scan | One-off parser over repository Markdown | No heading jumps, missing H1, or unbalanced fences found in the scanned set | A useful assistant check, not a substitute for rendered-page review |
| Git state | `git status --short` | All new content remains uncommitted | Release provenance is not yet established |

### Automated checks that are not exhaustive

- `validate_manifest.py` does not test whether a prerequisite is pedagogically sufficient.
- `check_links.py` does not test external links by default and its anchor slugger is an approximation of MkDocs.
- `check_mermaid.py` without `--render` only checks the first diagram token.
- The MkDocs build does not validate technical claims, alt text, accessibility, or whether a diagram communicates the intended mechanism.
- The lab scripts are syntax-checked; only SYS-01 was executed end to end on macOS in this audit.

## 3. Expert findings

Severity: **Critical** blocks publication; **High** materially misleads or breaks a learner path; **Medium** reduces quality or reproducibility; **Low** editorial or narrow-scope correction.

| ID | Severity | Affected file | Evidence | Recommended fix | Validation method |
|---|---|---|---|---|---|
| A01 | Critical | `README.md`, `LEARNING_PATHS.md`, `ARCHITECTURE_REVIEW.md`, `mkdocs.yml` | Required `LAB_SAFETY.md` is absent (`test -e LAB_SAFETY.md` fails); `LEARNING_PATHS.md` says the lab-safety checklist is mandatory; `ARCHITECTURE_REVIEW.md` says it was a gate before lessons | Add a reviewed lab-safety policy, link it from navigation and learner routes, and require its checklist in the lab review workflow | File exists; all three links resolve; `make check`; independent safety review still required |
| A02 | Critical | `CONTRIBUTING.md` | Required artifact is absent; repository claims maintainability and a CI workflow but documents no authoring, review, source, or AI policy | Add a concise authoring and review contract; link it from the home page and template guidance | File exists; links resolve; review roles and checks are explicit |
| A03 | Critical | `GLOSSARY.md` | Required artifact is absent; every tutorial is required to define terminology, but only module-local tables exist | Add a shared glossary with terms introduced by tutorials and links to the introducing lesson | File exists; terms match tutorial usage; links resolve |
| A04 | High | `PROGRESS_TRACKER.md` | Required artifact is absent; no learner-facing progress or evidence log exists despite the mastery model | Add a tracker template and status/gate definitions, seeded with authored modules | File exists; links resolve; no invented learner progress |
| A05 | High | `projects/` | Required capstone directory is absent; `CAP-01`–`CAP-05` exist only as manifest/catalog entries | Add a capstone index and briefs or explicitly scope the current release to a draft without claiming capstones are usable | Directory and briefs exist, or release statement is narrowed |
| A06 | High | `labs/sys-02-syscalls-and-isolation/environment/Containerfile`, `lab.md`, `reproducibility.md` | Built image has no `python3`; documented verifier exits 127. The image defaults to root, so the mode-`000` test succeeds (`exit_status=0`) instead of producing the expected unprivileged `EACCES` | Install Python, run the lab as an unprivileged UID, and document the root/non-root distinction | Rebuild; run collector and verifier as the default user; record real trace; update checksums |
| A07 | High | `REFERENCES.md` | `N28` URL `https://csrc.nist.gov/pubs/sp/800/101/r1/final` returns HTTP 404; the source is marked `V1` | Replace with the resolving NIST DOI/PDF URL, record the check date and verification code, and re-run the source crawl | HTTP check returns 200; source ID still declared/used |
| A08 | High | `research/01-literature-search-and-source-evaluation.md` | Line 207 says the answer key is “planned; not yet authored,” but `assessments/research/answer-key.md` exists | Correct the statement and avoid linking an instructor-only page from the published site | Text check; `make check`; site build |
| A09 | High | `CURRICULUM_MANIFEST.md` | Validation procedure invokes nonexistent `scripts/check_markdown.py`, `markdownlint-cli2`, and `scripts/render_mermaid.sh`; it calls the implemented scripts “planned” | Replace with the actual `make check`, `scripts/check_links.py`, `scripts/check_mermaid.py`, and lint commands; mark Mermaid render as optional/manual | Commands exist and run; documentation no longer names absent tools |
| A10 | High | `ARCHITECTURE_REVIEW.md` | The “Not performed” table says “No labs are authored yet,” “No rendered site,” and “No lab code exists yet” while two labs, a site, and lab code exist | Update the status table to current facts; distinguish historical M1 checks from current state | Text review; table links/files exist |
| A11 | High | `tutorials/sys-02-operating-systems/01-privilege-levels-and-kernel-boundary.md`, `02-processes-threads-and-scheduling.md`, `03-files-permissions-and-access-control.md` | Captured output contains a personal account name and environment-specific group/process data | Redact the account name in the published examples, label the redaction, and retain the real evidence privately if needed | Search for personal identifiers; inspect rendered output |
| A12 | High | `research/01`–`08`, `manifest/course-manifest.yaml` | Research tutorial headers state only preceding research tutorials, while manifest modules require `RSK-01`, `DAT-01`, `PRG-01`, or `RES-03`–`RES-05`; tutorial 8 says RES-03/04/05 are primary modules while those modules are `planned` | Add module-gate prerequisites to tutorial headers and label tutorial 8 as a cross-module design tutorial, not completion of the planned modules | Compare headers to manifest; validate links and status text |
| A13 | High | `assessments/research/assessment.md` | Portfolio assessment lists artifacts but does not map them to `RES-01`, `RES-02`, `RES-06`, and `RES-07` outcome IDs | Add an outcome-to-artifact matrix; require evidence for each mapped outcome | Reviewer can trace each outcome to an artifact and rubric |
| A14 | Medium | `tutorials/sys-01-computer-architecture/01-machine-model-and-execution.md` | Says x86-64 has 16 GPRs “`rax`–`r15`, plus `rsp` and `rbp`”; `rsp` and `rbp` are among the 16 GPRs | Correct the register inventory and distinguish general-purpose registers from special roles and `rip`/`rflags` | Technical reviewer check against Intel SDM/ABI |
| A15 | Medium | `tutorials/sys-02-operating-systems/02-processes-threads-and-scheduling.md` | Process row says signal handlers have “private dispositions”; thread row says “shared dispositions,” which contradicts the process-wide POSIX model | State process-wide dispositions and per-thread masks/pending signals in both rows | Technical reviewer check against POSIX |
| A16 | Medium | `tutorials/sys-02-operating-systems/README.md` | Says the macOS fallback “uses `dtruss`,” but the lab documents a Python descriptor/error fallback and does not execute `dtruss` | Align the overview with the actual fallback; describe `dtruss` as an optional platform tool with its constraints | Text cross-check against lab section |
| A17 | Medium | `tutorials/sys-02-operating-systems/01-privilege-levels-and-kernel-boundary.md`, `03-files-permissions-and-access-control.md` | “Secure boot” is listed among controls that deny root file access; Secure Boot validates boot components, not arbitrary runtime file reads | Replace with controls that actually constrain runtime access (LSMs, encryption, immutable attributes, kernel lockdown where applicable) | Technical reviewer check |
| A18 | Medium | `tutorials/sys-02-operating-systems/05-isolation-and-sandboxing.md` | A hypervisor claim is cited to `[N12]`, NIST SP 800-190 container guidance; the same paragraph says a VM escape attack surface is “usually smaller,” which is not established | Remove the mismatched citation and state only that the attack surface is different, not necessarily smaller | Citation-to-claim audit |
| A19 | Medium | `tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md` | Says a terminator canary contains bytes “that string functions stop at”; newline does not terminate `strcpy`, and behavior is function-specific | Qualify the claim and name the relevant string behavior | Technical reviewer check |
| A20 | Medium | `tutorials/sys-02-operating-systems/README.md`, `COURSE_MAP.md`, `manifest/course-manifest.yaml` | `SYS-02.O1` claims virtual memory, but SYS-02 tutorials defer virtual memory to SYS-01; assessment blueprint does not test it separately | Reword the outcome to apply the SYS-01 model, or add an explicit review section and assessment item | Outcome-to-tutorial-to-assessment trace |
| A21 | Medium | `labs/sys-02-syscalls-and-isolation/lab.md`, `scripts/collect_evidence.sh` | Trace filters use `openat` only while prose says accept `open`; on a libc that emits `open`, the denied trace has no matching open line | Include both `open` and `openat` in filters; keep the prose acceptance rule | Run on two libc/toolchain variants or statically verify filters |
| A22 | Medium | `labs/sys-02-syscalls-and-isolation/environment/Containerfile`, `reproducibility.md` | Base tag is not digest-pinned and apt packages are unversioned; the file acknowledges the first issue but not the package drift | Pin a digest or explicitly classify the image as a convenience environment and require image-ID capture; document the limitation | Rebuild twice and compare package/image metadata |
| A23 | Medium | `research/02-research-questions-hypotheses-and-threat-models.md` | Generated example asks whether a read-only root filesystem reduces host-file reads after a file-read vulnerability; read-only root does not generally reduce read access, and “no host mounts” makes the outcome near-trivial | Replace the example with a treatment that actually changes the measured access decision, such as non-root versus root for path-traversal writes | Method review; example remains labeled generated |
| A24 | Medium | `research/README.md` | Says there are “three kinds of statement,” then adds a fourth category, “assumption” | Call it four categories or “three evidence types plus assumptions” | Editorial check |
| A25 | Medium | `research/05-reproducibility-and-replication.md` | Presents R0–R4 as “reproducibility levels” without stating that they are course-defined, not ACM badges or a community standard | Label the scale as course-defined and distinguish it from ACM artifact badging | Compare with `[R13]`; reviewer check |
| A26 | Low | `LEARNING_PATHS.md` | Status says paths are sequences through “the 67 planned modules” although six modules are drafted | Say “67-module design; six drafted” and link the manifest | Text and manifest comparison |
| A27 | Low | `research/projects/02-replication-study.md`, `research/projects/README.md` | P2 prerequisites list tutorials but omit the technical module gates that `RES-02` requires | Add a module-gate note or justify the project-level exception | Reviewer trace to manifest |
| A28 | Low | `diagrams/dependency-graph.md` | “Result: 10 of 10 diagrams rendered successfully” is a historical metadata claim; this audit could not re-render because `mmdc` is unavailable | Keep as dated historical evidence or re-render; do not present it as a current gate result | Re-render or relabel as prior milestone evidence |
| A29 | Low | `scripts/check_links.py` | External checking used HEAD and classified HEAD 404 responses as dead even when GET returned 200, producing false 404s for `N28` and `N17` | Retry with GET on HEAD 404 as well as 403/405 | Re-run external checker; confirm no unclassified 404 remains |
| A30 | Medium | `COURSE_MAP.md`, `diagrams/dependency-graph.md`, `manifest/course-manifest.yaml` | Derived catalog and dependency views are hand-maintained; no automated synchronization check exists. A manual audit found no mismatch in module IDs, statuses, outcomes, or prerequisites at this revision | Add a manifest-to-catalog check and a diagram edge audit, or explicitly keep manual review as the release gate | Run the check on a deliberately drifted fixture; verify it fails |

### 3.1 Resolution status after the audit fixes

The findings table records the **pre-fix** evidence. This table records what was changed and what was actually checked afterward.

| ID | Status | Post-fix evidence |
|---|---|---|
| A01 | Fixed | `LAB_SAFETY.md` added, linked from the home page, learning paths, navigation, and progress gates |
| A02 | Fixed | `CONTRIBUTING.md` added with source, safety, review, and AI rules |
| A03 | Fixed | `GLOSSARY.md` added; its links and anchors pass `make check` |
| A04 | Fixed | `PROGRESS_TRACKER.md` added with status vocabulary, gates, and evidence template |
| A05 | Partial | `projects/README.md` adds a transparent capstone index and status; five briefs remain deferred |
| A06 | Fixed | Container image installs Python and runs as UID 1000; collector and verifier exit 0; denied open returns `EACCES`; `unshare` blocked by runtime |
| A07 | Fixed | `N28` now uses a DOI that resolves to the NIST PDF; targeted GET returned HTTP 200 |
| A08 | Fixed | Stale “not yet authored” statement replaced; site build passes |
| A09 | Fixed | Validation procedure now names `make check`, `check_links.py`, `check_mermaid.py`, and the optional render command |
| A10 | Fixed | Architecture review no longer claims labs/site/code do not exist; current limitations are explicit |
| A11 | Fixed | Personal account names replaced with `learner` and redaction notes added; the published tutorial search no longer finds the identifier |
| A12 | Fixed | Research tutorial headers now show module gates; tutorial 8 is labeled a cross-module design tutorial |
| A13 | Fixed | Research portfolio assessment has an outcome-to-artifact matrix |
| A14 | Fixed | x86-64 register inventory corrected |
| A15 | Fixed | Process/thread signal table corrected to process-wide dispositions |
| A16 | Fixed | SYS-02 overview now distinguishes the Python fallback from optional `dtruss` |
| A17 | Fixed | Secure Boot removed from runtime root-access claims |
| A18 | Fixed | Hypervisor citation removed; VM attack surface is described as different, not smaller |
| A19 | Fixed | Terminator-canary wording qualified |
| A20 | Fixed | SYS-02 outcome no longer claims virtual-memory instruction |
| A21 | Fixed | Collector filters include both `open` and `openat`; root execution is refused |
| A22 | Partial | Image identity and package drift remain a documented limitation; base digest is still not pinned |
| A23 | Fixed | Research question example now tests non-root versus root path-traversal writes |
| A24 | Fixed | Claim taxonomy now has four categories, including assumptions |
| A25 | Fixed | R0–R4 labeled course-defined, not a community standard |
| A26 | Fixed | Learning-path status distinguishes drafted and planned modules |
| A27 | Fixed | P2 prerequisites include RES-02 module gates |
| A28 | Fixed | Follow-up render with temporary Node 22.23.3 and Mermaid CLI 12.0.0 rendered 75/75 blocks |
| A29 | Fixed | External checker now retries GET after HEAD 404/405/403, avoiding false 404 classification |
| A30 | Open / manual | Manual comparison of all 67 module IDs, catalog statuses, outcome IDs, and prerequisites found no mismatch; automated synchronization remains deferred |
| Final local gate | Pass | `make check` exit 0; 67 modules, 201 outcomes, 1,950 h, 149/149 sources; 65 Markdown files, 572 local links, 0 missing nav targets; 0 lint findings; strict build 0.65 s |

## 4. Critical publication blockers

The pre-fix audit found four publication blockers. Their current disposition is:

1. **A01–A03 — fixed.** Safety, contribution, and glossary artifacts now exist and are linked.
2. **A06 — fixed for the container path.** The image includes Python and runs as UID 1000; the collector and verifier pass and the denied open returns `EACCES`. A clean Linux VM run is still required for `lab_validated`.
3. **A07 — fixed.** The broken `N28` URL was replaced with a DOI resolving to the NIST PDF.
4. **A09/A10 — fixed.** Validation commands and architecture-status claims now match the implemented scripts and repository state.

The remaining **scope and assurance limits** are:

- A05: the capstone index is present, but the five capstone briefs are not authored.
- A22: the SYS-02 base image tag is not digest-pinned; package drift is documented.
- No independent technical/safety review, clean Linux VM lab run, accessibility audit, or GitHub Actions run has been completed.

The repository can therefore be published as a **draft foundations and research-preview site**. It must not be described as a complete or independently validated academy.

## 5. Fix batches and validation plan

### Batch 1 — critical governance and safety

- Add `LAB_SAFETY.md`, `CONTRIBUTING.md`, `GLOSSARY.md`, and `PROGRESS_TRACKER.md`.
- Add navigation and home-page links.
- Update the architecture review so it does not claim the safety gate was satisfied before the policy existed.

### Batch 2 — reproducible lab and source corrections

- Fix the SYS-02 Containerfile (non-root user, Python verifier), collector root guard, and `open`/`openat` filters.
- Rebuild the container and run the collector and verifier as the default user; record actual output.
- Fix the `N28` source URL.
- Redact personal identifiers from captured examples.

### Batch 3 — content and metadata consistency

- Fix the research prerequisite/status/outcome mapping and stale answer-key statement.
- Correct the technical contradictions A14–A20.
- Replace the flawed research example A23.
- Update `CURRICULUM_MANIFEST.md`, `LEARNING_PATHS.md`, `COURSE_MAP.md`, and the manifest when outcomes or statuses change.
- Re-run `make check`, Mermaid structural checks, lab checksums, and the targeted container workflow.

## 6. Verification not performed

- Independent technical review by a second subject-matter expert.
- Full-text reading of all 149 sources; landing-page and metadata verification only.
- The initial Mermaid render attempt failed because the installed Homebrew Node runtime is broken; a follow-up with portable Node 22.23.3 and Mermaid CLI 12.0.0 rendered 75/75 blocks. Visual semantic review of every diagram is still outstanding.
- A clean Linux VM run for SYS-02; the container is not a substitute for namespace and kernel-policy testing.
- Windows lab paths and PE analysis.
- Accessibility audit with a screen reader and keyboard-only navigation.
- GitHub Actions execution.
- Legal review of authorization templates.
- Assessment calibration with real learners.
- External link revalidation over time; 403/202/429 responses are not the same as link death.

## 7. Audit limitations

- Expert judgments in section 3 are based on repository evidence and standard systems/research knowledge; they are not independent peer review.
- The external crawl used a single user agent and single time window; bot protection and rate limits can produce false failures.
- The SYS-02 container result is evidence about that image and runtime, not proof that the Linux VM path fails.
- The repository is uncommitted, so the audit cannot identify a stable release commit or compare against a reviewed baseline.
- A clean-clone test was not performed; the `docs/` symlink view and generated-site behavior may vary on filesystems that do not support symlinks.
