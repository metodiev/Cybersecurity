# Instructor Solution: Lab SYS-01

> **Access:** instructor-only. Excluded from the published MkDocs site. Exclusion is not access control for the repository; restrict repository or LMS permissions separately.

## 1. Validation record

| Item | Result |
|---|---|
| Host | macOS 27.0.1 (build 26A434), arm64 |
| Compiler | Apple clang 21.0.0 (clang-2100.3.34.2) |
| Python | 3.9.6 |
| Page size | 16384 bytes |
| Build matrix | Executed with `make all` |
| ASLR measurement | Executed, 30 runs, CSV and summary generated |
| Evidence verifier | Exit 0 on the generated CSV |
| Rebuild comparison | Executed; bytes differed, metadata stable |
| Linux path | **Not executed** |

The Linux commands and fields below are expected from the documented toolchain, not captured output. Do not present them as observations.

## 2. Build output

```text
$ make all
cc -O0 -g -Wall -Wextra -o layout layout.c
cc -O0 -g -Wall -Wextra -fno-stack-protector -o layout-nossp layout.c
cc -O0 -g -Wall -Wextra -fstack-protector-all -o canary canary.c
cc -O0 -g -Wall -Wextra -fno-stack-protector -o canary-nossp canary.c
```

Expected learner observation: four binaries. If the compiler rejects a flag, the learner must record the error and substitute the closest supported option.

## 3. Metadata results

Captured Mach-O headers:

```text
$ for f in layout layout-nossp canary canary-nossp; do otool -hv "$f" | tail -1; done
MH_MAGIC_64    ARM64        ALL  0x00     EXECUTE    18       1288   NOUNDEFS DYLDLINK TWOLEVEL PIE
MH_MAGIC_64    ARM64        ALL  0x00     EXECUTE    18       1288   NOUNDEFS DYLDLINK TWOLEVEL PIE
MH_MAGIC_64    ARM64        ALL  0x00     EXECUTE    17       1056   NOUNDEFS DYLDLINK TWOLEVEL PIE
MH_MAGIC_64    ARM64        ALL  0x00     EXECUTE    17       1056   NOUNDEFS DYLDLINK TWOLEVEL PIE
```

Expected interpretation:

- All four binaries are `MH_EXECUTE` and `PIE`.
- Enabling the stack protector did not change the executable format or PIE state.
- The `canary`/`canary-nossp` pair has different load-command counts and sizes from the `layout` pair because the source differs.

On Linux, expect `readelf -h` to report `Type: DYN` for PIE, and `readelf -l` to show `GNU_STACK` and `GNU_RELRO`. Exact output depends on the distribution toolchain.

## 4. Guard-symbol and disassembly results

Captured imports:

```text
$ for f in canary canary-nossp; do echo "$f:"; otool -Iv "$f" | grep -c 'stack_chk' || true; done
canary:
3
canary-nossp:
0
```

The count of three in `canary` reflects the guard symbol and failure handler entries in the import and symbol tables. The exact count is tool-specific; the critical observation is presence versus absence.

Captured `copy_name` prologue and check (trimmed):

```text
_copy_name:
0000000100000460	sub	sp, sp, #0x40
0000000100000464	stp	x29, x30, [sp, #0x30]
0000000100000468	add	x29, sp, #0x30
000000010000046c	adrp	x8, 4 ; 0x100004000
0000000100000470	ldr	x8, [x8] ; literal pool symbol address: ___stack_chk_guard
0000000100000474	ldr	x8, [x8]
0000000100000478	stur	x8, [x29, #-0x8]
...
00000001000004ac	ldur	x9, [x29, #-0x8]
00000001000004b0	adrp	x8, 4 ; 0x100004000
00000001000004b4	ldr	x8, [x8] ; literal pool symbol address: ___stack_chk_guard
00000001000004b8	ldr	x8, [x8]
00000001000004bc	subs	x8, x8, x9
00000001000004c0	b.eq	0x1000004cc
00000001000004c4	b	0x1000004c8
00000001000004c8	bl	0x10000059c ; symbol stub for: ___stack_chk_fail
```

Expected annotation:

1. Reserve the frame.
2. Save `x29` and `x30`.
3. Load the guard and store it at `[x29, #-0x8]`, between local data and saved control data.
4. Before return, reload the guard, compare, and call the failure handler on mismatch.
5. Restore `x29`/`x30` and return.

`canary-nossp` has no guard load, store, compare, or failure call.

## 5. ASLR measurement result

Captured summary from one 30-run sample on the validation host:

```json
{
  "runs": 30,
  "page_size": 16384,
  "regions": {
    "code":      {"distinct_pages": 30, "min_page": 262256, "max_page": 266945},
    "static":    {"distinct_pages": 30, "min_page": 262258, "max_page": 266947},
    "data":      {"distinct_pages": 30, "min_page": 262258, "max_page": 266947},
    "bss":       {"distinct_pages": 30, "min_page": 262258, "max_page": 266947},
    "heap":      {"distinct_pages": 30, "min_page": 262578, "max_page": 267349},
    "stack":     {"distinct_pages": 30, "min_page": 371902, "max_page": 376591}
  }
}
```

Evidence verifier:

```text
$ python3 scripts/verify_evidence.py --csv /tmp/sys01-aslr2.csv --min-runs 30
OK: 30 runs, page_size=16384, columns valid
```

**Interpretation:** on this host and sample, every region moved to a different page on each run. That supports H2 for this sample. It does **not** establish entropy, a distribution, or a guarantee about any other host. A learner who reports "30 distinct pages means 30 random bases are equally likely" has overclaimed.

## 6. Rebuild result

Two clean rebuilds produced different SHA-256 hashes for all four binaries. The metadata (format, PIE, load-command shape, and guard-symbol presence) was stable. This supports H3 as written: metadata is stable even when bytes differ. A learner who interprets H3 as "byte-identical rebuilds" should be corrected; the hypothesis deliberately concerns observable metadata.

## 7. Hypothesis decisions for the sample

| Hypothesis | Decision | Reason |
|---|---|---|
| H1 | Supported | `canary` has guard symbols and guard code; `canary-nossp` has none; both retain the same format and PIE state |
| H2 | Supported for this sample | Every measured region had 30 distinct pages across 30 runs on the capture host |
| H3 | Supported | Metadata matched across clean rebuilds; bytes did not |

These decisions are about the sample and environment, not universal claims.

## 8. Linux grading guidance

Accept `readelf` output that shows:

- `Type: DYN` for PIE and an interpreter;
- `.text`, `.data`, `.bss`, `.rodata`;
- `GNU_STACK` without `E`;
- `GNU_RELRO` for RELRO;
- stack-guard symbols in the protected build only.

The learner must quote the field or symbol. Do not require a specific address, section order, or instruction encoding.

## 9. Common learner errors

| Error | Why it is wrong | Feedback |
|---|---|---|
| Claiming ASLR entropy from 30 runs | The sample cannot support a distribution or entropy estimate | Require a limitation and a different design |
| Treating "no explicit flag" as "no protection" | The capture host's default already enabled protection | Require the guard-symbol evidence |
| Reporting a different learner's addresses as universal | Addresses are per-run and per-host | Accept any internally consistent values |
| Saying the canary protects the heap | Canaries are frame-scoped | Point to the frame diagram |
| Calling PIE equivalent to ASLR | PIE enables randomization; the loader must randomize | Explain the dependency |
| Omitting the rebuild comparison | H3 is untested | Require hashes and metadata |

## 10. Cleanup verification

Confirm the learner removed compiled binaries and kept the evidence package. Confirm no compiled binaries or personal paths are in the submission.
