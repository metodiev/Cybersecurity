# Reproducibility Notes: Lab SYS-01

> **Lab:** [`lab.md`](lab.md) · **Rubric:** [`rubric.md`](rubric.md) · **Instructor solution:** `solution.md` (excluded from the published site)
> **Last validated:** 2026-10-19 on macOS 27.0.1, arm64

## 1. What was validated

| Item | Status | Evidence |
|---|---|---|
| Starter sources compile with `make all` | Validated | `make` output captured during repository validation |
| `measure_aslr.py` runs 30 iterations and writes CSV | Validated | CSV and summary generated on the capture host |
| `verify_evidence.py` accepts a 30-row CSV | Validated | Exit 0 on the generated CSV |
| macOS metadata and guard analysis | Validated | Recorded in `solution.md` |
| Linux ELF metadata and guard analysis | Not executed | Commands are documented; a Linux VM or container is required |
| Windows/PE path | Not covered | Out of scope |

## 2. Validated environment

| Component | Value |
|---|---|
| OS | macOS 27.0.1 (build 26A434) |
| Architecture | arm64 |
| Compiler | Apple clang 21.0.0 (clang-2100.3.34.2) |
| Python | 3.9.6 |
| Page size | 16384 bytes |
| Mermaid | Not used for lab execution; diagrams are documentation |

The lab's scripts use only the Python standard library. No package installation is required.

## 3. Exact build commands

From `labs/sys-01-memory-and-binaries/starter`:

```bash
make clean
make all
```

The Makefile expands to:

```bash
cc -O0 -g -Wall -Wextra -o layout layout.c
cc -O0 -g -Wall -Wextra -fno-stack-protector -o layout-nossp layout.c
cc -O0 -g -Wall -Wextra -fstack-protector-all -o canary canary.c
cc -O0 -g -Wall -Wextra -fno-stack-protector -o canary-nossp canary.c
```

Record the actual compiler output. If the compiler does not support a flag, record the error and substitute the closest supported option; do not silently omit it.

## 4. Exact measurement commands

From `labs/sys-01-memory-and-binaries`:

```bash
mkdir -p evidence
python3 scripts/measure_aslr.py \
  --binary starter/layout \
  --runs 30 \
  --csv evidence/aslr-observations.csv \
  | tee evidence/aslr-summary.json
python3 scripts/verify_evidence.py \
  --csv evidence/aslr-observations.csv \
  --min-runs 30
```

## 5. Source integrity

`SHA256SUMS` records the lab's starter sources and scripts. Verify it before running:

```bash
shasum -a 256 -c SHA256SUMS   # macOS
sha256sum -c SHA256SUMS       # Linux
```

If a hash mismatches, stop and report it. Do not run modified scripts as if they were the reviewed versions.

## 6. What may vary

| Observation | Expected variation | How to record it |
|---|---|---|
| Addresses and page numbers | Per-run, per-process | CSV |
| Distinct page counts | Host- and sample-dependent | Summary JSON |
| Page size | 4096 on many x86-64 systems; 16384 on the capture host | Environment table |
| Section and symbol names | Platform- and toolchain-dependent | Metadata capture |
| Compiler defaults | May enable stack protection without an explicit flag | Build log and guard analysis |
| Binary bytes | May differ across rebuilds because of linker metadata | Hash comparison |
| Tool output formatting | Differs across binutils, LLVM, and macOS versions | Keep the raw output |

## 7. Known nondeterminism

- **ASLR:** addresses are expected to vary when randomization is active. A single run is not evidence of a distribution.
- **Linker metadata:** build UUIDs, timestamps, or paths may change the bytes while leaving format and symbols unchanged.
- **Filesystem paths:** debug information may embed build paths. Do not include personal paths in a public report.
- **CPU and OS:** cache and scheduling behavior can influence timing experiments; this lab does not measure timing.

## 8. Evidence retention

Keep the text evidence, CSV, and summary JSON. Do not commit compiled binaries. If addresses could identify a sensitive environment, replace the high-order bytes with a redaction note and keep the original locally; state the redaction in the report.

## 9. Manual testing still required

1. Run the full Linux path on a clean x86-64 VM or container with binutils installed.
2. Confirm the `GNU_STACK` and `GNU_RELRO` fields on a PIE build.
3. Repeat on a 4 KiB-page host and compare page counts.
4. Test a non-PIE build (`-no-pie`) and document the flag support.
5. If Windows is in scope for a future revision, add a PE path with `dumpbin` or an equivalent tool.

## 10. Review checklist

- [ ] Environment record is complete.
- [ ] The build used the reviewed sources (hash check).
- [ ] The CSV has at least 30 rows and passes the verifier.
- [ ] Metadata and guard evidence are present for all four builds.
- [ ] The report separates observation from inference.
- [ ] Limitations and manual-testing gaps are stated.
