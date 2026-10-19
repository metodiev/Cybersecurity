# SYS-01 Assessment: Computer Architecture and Memory

> **Module:** SYS-01 · **Level:** L1 · **Type:** written quiz plus practical analysis · **Time:** 60 min written + 2 h practical · **Open book:** no for the written section; notes allowed for the practical · **Status:** drafted · **Validation:** structural

## Blueprint

| Outcome | Cognitive level | Item types | Weight |
|---|---|---|---:|
| SYS-01.O1 | Understand, apply | Short answer, diagram, trace | 40% |
| SYS-01.O2 | Apply, analyze | Practical binary inspection | 35% |
| SYS-01.O3 | Analyze, evaluate | Scenario and mitigation analysis | 25% |

**Pass:** 80/100 overall, no outcome below 60%, and the practical report meets every evidence criterion.

## Instructions

- Answer the written section without notes, then complete the practical section with your tools.
- Every practical claim must cite a command and an output excerpt.
- Do not include a working exploit. This assessment is about analysis and defense.
- If a result differs from what you expected, report the difference; do not edit it.

## Section 1: Foundations (20 points)

1. **(4 pts)** Explain the fetch-decode-execute cycle in five steps. Name the register that holds the address of the next instruction on x86-64 and on AArch64.
2. **(4 pts)** What is the difference between an ISA and an ABI? Give one concrete consequence of a calling-convention mismatch.
3. **(4 pts)** Why must a lab report record the compiler, flags, and platform when presenting disassembly?
4. **(4 pts)** Explain the difference between a virtual address and a physical address, and the role of the TLB.
5. **(4 pts)** Why is `malloc` memory not guaranteed to be zeroed, and what security problem can that cause?

## Section 2: Architecture and memory (30 points)

6. **(6 pts)** Draw the user address space of a typical 64-bit process. Label `.text`, `.rodata`, `.data`, `.bss`, heap, memory-mapped libraries, and stack. State the permissions of each region on a modern system with NX and W^X.
7. **(8 pts)** For the following AArch64 leaf function, explain each instruction and identify the return register:

   ```text
   sub sp, sp, #0x10
   str w0, [sp, #0xc]
   str w1, [sp, #0x8]
   ldr w8, [sp, #0xc]
   ldr w9, [sp, #0x8]
   add w8, w8, w9
   str w8, [sp, #0x4]
   ldr w0, [sp, #0x4]
   add sp, sp, #0x10
   ret
   ```

8. **(8 pts)** Explain how a linear overflow of a stack buffer can reach a saved return address. Include the roles of the frame pointer, the link register or return slot, and the stack canary.
9. **(8 pts)** A 32-bit service forks a worker after loading configuration. Explain two reasons its ASLR is weaker than a 64-bit service that execs a new process per request.

## Section 3: Binary analysis practical (35 points)

Compile a small C program with a non-leaf function, then:

1. Record the OS, architecture, compiler, version, and flags.
2. Identify the executable format and whether it is position-independent. Cite the header field.
3. List the sections or segments that contain code, read-only data, writable data, and zero-initialized data.
4. Disassemble the non-leaf function. Annotate the prologue, the call, and the epilogue.
5. Compile the same source with stack protection enabled. Identify the canary load, store, and check, or explain why the compiler did not emit one.
6. State whether the stack is executable and whether RELRO is present. Cite the evidence.
7. Write a 300-word analysis of which exploit steps the observed mitigations affect and which they do not.

Submit the report and an evidence index. Addresses and instruction encodings will differ from any example; that is expected.

## Section 4: Scenario analysis (15 points)

A document-conversion service runs as a dedicated user, accepts untrusted files, and writes output to a shared directory. The service is compiled with NX, PIE, and stack canaries, but the shared directory is world-writable and the service follows user-supplied output paths.

Identify:

1. the most likely memory-safety and non-memory risks;
2. the control that addresses each risk;
3. the evidence you would collect to determine whether the control is working;
4. one residual risk that remains after the controls.

## Practical rubric

| Criterion | Weight | Pass | Proficient | Exemplary |
|---|---:|---|---|---|
| Environment record | 10 | OS and compiler | Versions and flags | Another learner can rebuild |
| Format and mitigation evidence | 25 | Names format | Cites header/segment fields | Explains PIE/NX/RELRO precisely |
| Disassembly annotation | 30 | Finds prologue | Explains each security-relevant instruction | Explains leaf/non-leaf and canary placement |
| Analysis and limits | 25 | Lists mitigations | Maps to exploit steps | States residual risk and unproven claims |
| Evidence discipline | 10 | Includes outputs | Cites commands | Distinguishes observation from inference |

## Academic integrity

The written section is individual. The practical may use documentation and your own notes. AI assistance must be disclosed. You must be able to explain every claim orally on request.

## Answer key

`answer-key.md` — instructor-only; excluded from the published site.
