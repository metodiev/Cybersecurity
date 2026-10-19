# Answer Key: SYS-01 Assessment

> **Access:** instructor-only. Excluded from the published site. Do not distribute to learners before the assessment.

## Section 1

1. **Fetch-decode-execute (4 pts).** Fetch the instruction at the PC; decode the opcode and operands; fetch operands from registers or memory; execute in the ALU or load/store unit; write the result and update flags; advance the PC or take a branch. The PC is `rip` on x86-64 and `pc` on AArch64. Award full credit for five correct stages plus both register names.

2. **ISA vs ABI (4 pts).** The ISA defines instructions, registers, and privilege levels; the ABI defines calling convention, register preservation, stack alignment, and data layout. A mismatch means a callee reads arguments from the wrong registers or fails to preserve a register the caller expects, causing incorrect results or memory corruption. Citation: [L10], [L11].

3. **Version record (4 pts).** Compiler optimization and defaults change stack frames, inlining, and inserted checks. The same source can produce different binaries. Without versions, the disassembly cannot be reproduced or compared. Accept answers that mention optimization level, ABI, and mitigation defaults.

4. **Virtual vs physical (4 pts).** A virtual address is used by the program; the MMU translates it through page tables to a physical frame. The TLB caches recent translations. Award full credit for mentioning page tables and the TLB.

5. **malloc (4 pts).** `malloc` returns uninitialized storage for performance; it does not zero. Reading it can disclose data from earlier allocations (keys, pointers, personal data). `calloc` zeroes. Citation: [L13] for C/POSIX allocation semantics; [A08] for memory disclosure classes.

## Section 2

6. **Address space (6 pts).** Award 1 point per correctly labeled region (up to 6) and require permissions:
   - `.text`: read + execute.
   - `.rodata`: read, no execute.
   - `.data`: read + write, no execute.
   - `.bss`: read + write, no execute, zero-filled.
   - Heap: read + write, no execute.
   - Libraries: read + execute for code, read + write for data.
   - Stack: read + write, no execute.
   Deduct if the learner draws the stack growing upward without noting the convention.

7. **Leaf function (8 pts).** 1 point per instruction group:
   - reserve 16 bytes;
   - spill `a` and `b`;
   - load both;
   - add;
   - store local;
   - load return register `w0`;
   - release frame;
   - return via `x30` (link register).
   The return register is `w0` (the 32-bit view of `x0`).

8. **Overflow to return address (8 pts).** The buffer is adjacent to higher-address frame state. A linear write past the buffer overwrites the canary (if present), then saved `x29`/`rbp`, then saved `x30`/return address. On function return, the corrupted address is loaded into the PC. The canary is checked before the epilogue and aborts on mismatch. Award credit for the order and the check.

9. **ASLR weakness (8 pts).** Two of:
   - 32-bit address space has far fewer possible bases;
   - `fork` without `exec` shares the parent's randomized layout, so brute force can succeed across children;
   - a single leak reveals the base for that process and its children;
   - low-entropy mappings or disabled randomization on some systems.
   Award full credit for two correct, distinct reasons. Citation: [A08].

## Section 3

Use the lab rubric. Key checks:

- **Format/PIE:** ELF `Type: DYN` with an interpreter, or Mach-O `PIE` flag.
- **Sections/segments:** code in `.text`/`__TEXT`; read-only data in `.rodata`/`__TEXT`; writable data in `.data`/`__DATA`; zero-filled in `.bss`/`__common`.
- **Prologue/epilogue:** `push rbp`/`mov rbp,rsp`/`sub rsp` or `stp x29,x30`/`sub sp`; epilogue reverses it.
- **Canary:** `___stack_chk_guard` or `__stack_chk_guard` load/store/check; failure handler call.
- **NX:** `GNU_STACK` without `E`, or non-executable stack segment.
- **RELRO:** `GNU_RELRO`, or `__DATA_CONST` on macOS.

Deduct for unsupported claims ("ASLR prevents exploitation") and for missing environment data.

## Section 4

Expected risks and controls:

| Risk | Control | Evidence | Residual |
|---|---|---|---|
| Memory corruption in the converter | Memory-safe language, sandbox, NX/ASLR/canaries | Build flags, crash telemetry, sanitizer runs | Zero-days and logic bugs |
| Path traversal or symlink write | Object-based file API, `O_NOFOLLOW`, per-job directory, drop privileges | `strace`, code review, permissions | Kernel or filesystem bugs |
| World-writable output directory | Sticky bit or per-user directory; `nosuid,nodev,noexec` | `ls -ld`, mount options | Other tenants with same UID |
| Resource exhaustion | cgroups, `RLIMIT_*`, timeouts | cgroup stats, OOM logs | Legitimate load spikes |
| Malicious file parser bug | Sandbox, seccomp, least privilege | Sandbox profile, syscall trace | Shared-kernel risk |

Award full credit for at least three risks with matched controls and evidence, plus one honest residual risk.

## Misconception flags

Deduct up to 5 points for any of these presented as fact:

- "ASLR makes exploitation impossible."
- "A canary protects the heap."
- "NX prevents all code execution."
- "The compiler output is the source."
- "Virtual addresses are physical addresses."

## Oral follow-up

Ask the learner to explain one instruction in their own disassembly without notes and to state one thing the lab did not prove.
