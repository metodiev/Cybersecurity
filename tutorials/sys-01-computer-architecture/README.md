# SYS-01: Computer Architecture and Memory

> **Level:** L1 · **Prerequisites:** ORI-01 · **Effort:** 28 h (10 reading, 14 practice, 4 assessment) · **Status:** drafted · **Validation:** structural

This module builds the machine model you need before touching exploitation, detection, or forensics. It is written for an experienced software developer who has not necessarily studied computer architecture. Every unfamiliar systems term is defined before it is used.

## Why this module exists

Most security failures at the systems level are failures to understand what the machine actually does:

- A bounds check is removed, and a write lands on a saved return address.
- A pointer is used after `free`, and the allocator hands the same memory to an attacker-controlled object.
- A mitigation such as ASLR is assumed to stop exploitation, but an information leak defeats it.
- A "safe" language calls into C, and the safety guarantee stops at the boundary.

You cannot reason about those failures from source code alone. You need a model of registers, instruction execution, virtual memory, stack frames, executable formats, and compiler-inserted defenses.

## Module outcomes

By the end of SYS-01 you can:

1. **SYS-01.O1** — Explain fetch-decode-execute, register use, caches, virtual memory, and stack/heap layout, and trace a C function call at the instruction level.
2. **SYS-01.O2** — Given a compiled x86-64 or ARM64 binary, annotate its sections, calling convention, and memory layout using `readelf`/`objdump` or equivalent tools.
3. **SYS-01.O3** — Evaluate how NX, ASLR, canaries, and speculative execution affect both security and performance in a written analysis.

The module assessment is in [`assessments/sys-01/assessment.md`](../../assessments/sys-01/assessment.md). The lab is in [`labs/sys-01-memory-and-binaries/lab.md`](../../labs/sys-01-memory-and-binaries/lab.md).

## Prerequisite order

Read the tutorials in this order. Each one assumes the previous one.

| # | Tutorial | Focus | Est. |
|---|---|---|---|
| 1 | [Machine model and instruction execution](01-machine-model-and-execution.md) | CPU, registers, fetch-decode-execute, caches, endianness | 6 h |
| 2 | [Memory layout and stack frames](02-memory-layout-and-stack-frames.md) | Virtual memory, pages, text/data/heap/stack, calling into a function | 7 h |
| 3 | [Binary anatomy and calling conventions](03-binary-anatomy-and-calling-conventions.md) | ELF, Mach-O, PE, sections, symbols, linkage, ABIs | 7 h |
| 4 | [Memory safety and mitigations](04-memory-safety-and-mitigations.md) | Overflow, UAF, canaries, NX, ASLR, PIE, RELRO, CFI, speculation | 8 h |

The lab and assessment assume all four tutorials.

## A note on platforms and versions

Examples were captured on **macOS 27.0.1 on arm64** with **Apple clang 21.0.0**, and are labelled as such. Linux and Windows differ in executable format, tools, page size, and syscall numbers. Where a command is Linux-only, the tutorial gives the command and describes what to inspect without pretending the output was captured on this machine.

> **Version note (2026-10-19).** Page size, compiler defaults, mitigation defaults, and kernel behavior change. Re-check them on your own system and record the versions in your lab report. Do not generalize a macOS observation to Linux or Windows without evidence.

## Safety

This module is **low risk** and requires no network isolation. You will compile and inspect your own programs. Do not run untrusted binaries or disable system protections on a machine you rely on. The lab uses only programs you compile from supplied source.

## Evidence standard

Every exercise asks for evidence: the command, the output, the environment, and your interpretation. "It worked" is not evidence. A screenshot without the command is not reproducible. If your output differs from the examples, record the difference and explain the platform or version.

## Cross-links

- Prerequisite: [ORI-01: Security Mindset, Ethics, Law, and Labcraft](../../COURSE_MAP.md#ori-01-security-mindset-ethics-law-and-labcraft)
- Next module: [SYS-02: Operating Systems Internals](../sys-02-operating-systems/README.md)
- Follow-up: [SYS-03: Linux Administration and Hardening](../../COURSE_MAP.md#sys-03-linux-administration-and-hardening)
- Source ledger: [REFERENCES.md](../../REFERENCES.md)
