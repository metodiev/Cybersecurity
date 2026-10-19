# SYS-02: Operating Systems Internals

> **Level:** L1 · **Prerequisites:** SYS-01 · **Effort:** 32 h (12 reading, 16 practice, 4 assessment) · **Status:** drafted · **Validation:** structural

This module explains the operating-system mechanisms that security depends on: privilege levels, processes, files and permissions, system calls, and isolation. It continues directly from [SYS-01](../sys-01-computer-architecture/README.md), which established the machine and memory model.

## Why this module exists

A process is not just "a running program." It is an address space, one or more threads, a credential set, open file descriptors, signal handlers, resource limits, and a set of kernel-visible attributes. Most privilege-escalation and container-escape findings are failures in how those pieces are separated.

The module teaches you to answer questions such as:

- Which mode was the CPU in when this happened, and what was the transition?
- Which credential did the kernel check, and against which object?
- Which file descriptor pointed at which open file description, and who else shared it?
- Which namespace or cgroup boundary was supposed to contain the process?
- What evidence would prove the boundary failed rather than assuming it did?

## Module outcomes

By the end of SYS-02 you can:

1. **SYS-02.O1** — Explain process and thread lifecycle, scheduling, virtual memory, syscalls, file descriptors, and user/kernel transitions.
2. **SYS-02.O2** — Trace a program's syscalls and map observed behavior to kernel abstractions using `strace`, `dtrace`, or equivalent tooling.
3. **SYS-02.O3** — Analyze a privilege-boundary violation scenario and identify the kernel control that failed and the evidence that would confirm it.

The lab is in [`labs/sys-02-syscalls-and-isolation/lab.md`](../../labs/sys-02-syscalls-and-isolation/lab.md). The assessment is in [`assessments/sys-02/assessment.md`](../../assessments/sys-02/assessment.md).

## Prerequisite order

| # | Tutorial | Focus | Est. |
|---|---|---|---|
| 1 | [Privilege levels and the kernel boundary](01-privilege-levels-and-kernel-boundary.md) | Rings, exception levels, syscall transition, credentials | 6 h |
| 2 | [Processes, threads, and scheduling](02-processes-threads-and-scheduling.md) | Lifecycle, `fork`/`exec`, signals, scheduling, injection | 7 h |
| 3 | [Files, permissions, and access control](03-files-permissions-and-access-control.md) | Inodes, descriptors, mode bits, ACLs, TOCTOU | 7 h |
| 4 | [System calls and tracing](04-system-calls-and-tracing.md) | ABI, `errno`, `strace`/`dtrace`, seccomp, evidence | 6 h |
| 5 | [Isolation and sandboxing](05-isolation-and-sandboxing.md) | Namespaces, cgroups, containers, VMs, sandboxes | 6 h |

## Platform notes

Examples were captured on **macOS 27.0.1 on arm64**, with **Apple clang 21.0.0** and the system Python 3.9. The syscall-tracing lab is designed for Linux because `strace` is the most reproducible teaching tool; the macOS fallback uses `dtruss` and is documented with its root and SIP constraints. Windows equivalents are named for comparison, not claimed as tested here.

> **Version note (2026-10-19).** Syscall numbers, scheduler behavior, namespace features, and default security modules differ by kernel version and distribution. Record `uname -a` and the distribution release in every lab report.

## Safety

The tutorials are **low risk**. The lab creates namespaces and traces local processes; it does not attack a remote system. Use a disposable Linux VM or container. Do not run `strace` against processes you do not own, and do not disable SIP or other host protections on a machine you rely on.

## Evidence standard

A syscall trace is evidence only when it includes the command, the process tree, the architecture, the kernel version, and the relevant trace lines. "The program opened a file" is not evidence; the `openat` line and its return value are.

## Cross-links

- Prerequisite: [SYS-01: Computer Architecture and Memory](../sys-01-computer-architecture/README.md)
- Next: [SYS-03: Linux Administration and Hardening](../../COURSE_MAP.md#sys-03-linux-administration-and-hardening)
- Related: [SYS-04: Windows Architecture, Registry, NTFS, and AD Preview](../../COURSE_MAP.md#sys-04-windows-architecture-registry-ntfs-and-ad-preview)
- Source ledger: [REFERENCES.md](../../REFERENCES.md)
