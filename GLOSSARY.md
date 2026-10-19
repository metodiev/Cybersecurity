# Glossary

> **Status:** shared terminology. **Last updated:** 2026-10-19.
> Tutorials define terms in context; this page is the common reference for learners and authors. If a tutorial uses a term before defining it, that is an authoring defect.

## How to use this glossary

- Read the definition before relying on a term in a lab or assessment.
- Follow the **Introduced in** link for the fuller mechanism, examples, and limitations.
- Do not treat a one-line definition as sufficient for an advanced claim. The linked lesson is the authoritative explanation.

## Systems and security

| Term | Definition | Introduced in |
|---|---|---|
| **ABI** | Application Binary Interface: the calling convention, register roles, stack alignment, data layout, and symbol conventions that let compiled code interoperate. | [SYS-01.1](tutorials/sys-01-computer-architecture/01-machine-model-and-execution.md#isa-versus-abi) |
| **Address space layout randomization (ASLR)** | Randomization of the base addresses of mappings such as the stack, heap, libraries, and sometimes the executable. It raises the cost of address prediction; it is not immunity. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#aslr-and-pie) |
| **Application binary interface** | See **ABI**. | [SYS-01.1](tutorials/sys-01-computer-architecture/01-machine-model-and-execution.md#isa-versus-abi) |
| **BSS** | The executable section holding zero-initialized writable data. It normally occupies no file bytes and is allocated at load time. | [SYS-01.2](tutorials/sys-01-computer-architecture/02-memory-layout-and-stack-frames.md#the-user-address-space) |
| **Canary** | A guard value placed in a stack frame between local buffers and saved control data; it is checked before return. It protects the frame where it is placed, not the heap. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#stack-canaries) |
| **Cgroup** | A Linux control-group mechanism that organizes processes and applies resource limits such as CPU, memory, and PID counts. | [SYS-02.5](tutorials/sys-02-operating-systems/05-isolation-and-sandboxing.md#cgroups) |
| **Control-flow integrity (CFI)** | A family of checks that restricts indirect calls and jumps to targets allowed by a policy. Coarse and fine-grained policies provide different guarantees. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#cfi-and-shadow-stacks) |
| **Copy-on-write (COW)** | A sharing optimization in which parent and child initially share pages read-only; a write creates a private copy. | [SYS-01.2](tutorials/sys-01-computer-architecture/02-memory-layout-and-stack-frames.md#virtual-memory) |
| **CVD** | Coordinated vulnerability disclosure: a private report, validation, fix coordination, verification, and coordinated publication process. It is not a universal deadline or a substitute for authorization. | [Research 6](research/06-ethics-disclosure-and-open-science.md#coordinated-vulnerability-disclosure) |
| **ELF** | Executable and Linkable Format, used by Linux and many Unix-like systems for object files, executables, shared libraries, and core files. | [SYS-01.3](tutorials/sys-01-computer-architecture/03-binary-anatomy-and-calling-conventions.md#elf) |
| **Exception level** | An Arm privilege level: EL0 user, EL1 kernel, EL2 hypervisor, and EL3 secure monitor on Armv8-A. | [SYS-02.1](tutorials/sys-02-operating-systems/01-privilege-levels-and-kernel-boundary.md#two-modes-many-names) |
| **File descriptor (FD)** | A per-process integer that indexes an open file description. It can be inherited across `fork` and, unless close-on-exec is set, across `exec`. | [SYS-02.3](tutorials/sys-02-operating-systems/03-files-permissions-and-access-control.md#the-layers) |
| **Inode** | Filesystem metadata for an object, including type, mode, owner, size, timestamps, and data pointers. A name is a directory entry that refers to an inode. | [SYS-02.3](tutorials/sys-02-operating-systems/03-files-permissions-and-access-control.md#the-layers) |
| **Instruction set architecture (ISA)** | The instruction set, registers, addressing modes, and privilege model visible to software. | [SYS-01.1](tutorials/sys-01-computer-architecture/01-machine-model-and-execution.md#isa-versus-abi) |
| **Namespace** | A Linux kernel mechanism that gives processes a private view of a global resource such as mounts, PIDs, networking, IPC, users, or time. | [SYS-02.5](tutorials/sys-02-operating-systems/05-isolation-and-sandboxing.md#linux-namespaces) |
| **NX / DEP** | No-execute or data-execution prevention: a policy that marks writable data pages non-executable. It blocks direct injected-code execution but not code reuse. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#nx-wx-and-code-reuse) |
| **Open file description** | The kernel object holding an open file's offset, flags, and status. Multiple file descriptors can refer to the same description. | [SYS-02.3](tutorials/sys-02-operating-systems/03-files-permissions-and-access-control.md#the-layers) |
| **PIE** | Position-independent executable: an executable that can be loaded at a randomized base, enabling ASLR for the main image. | [SYS-01.3](tutorials/sys-01-computer-architecture/03-binary-anatomy-and-calling-conventions.md#elf) |
| **Privilege ring** | An x86 privilege level. Mainstream systems use ring 0 for the kernel and ring 3 for user code; rings 1–2 are rarely used. | [SYS-02.1](tutorials/sys-02-operating-systems/01-privilege-levels-and-kernel-boundary.md#two-modes-many-names) |
| **Process** | An executing program instance with an address space, one or more threads, credentials, descriptors, signal state, limits, and kernel bookkeeping. | [SYS-02.2](tutorials/sys-02-operating-systems/02-processes-threads-and-scheduling.md#what-a-process-is) |
| **RELRO** | Relocation read-only: a linker/loader hardening feature that makes part or all of the GOT read-only after relocation. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#relro-and-the-got) |
| **seccomp** | A Linux syscall filter that evaluates a BPF policy and can allow, kill, trap, or return an error for a syscall. It does not validate pointed-to memory or file paths. | [SYS-02.4](tutorials/sys-02-operating-systems/04-system-calls-and-tracing.md#seccomp) |
| **setuid** | A Unix mode bit that causes an executable to run with the file owner's effective UID. It is a privilege grant and a high-value attack target. | [SYS-02.3](tutorials/sys-02-operating-systems/03-files-permissions-and-access-control.md#unix-mode-bits) |
| **SIP** | macOS System Integrity Protection, which restricts modification of selected system paths and resources even for privileged users. | [SYS-02.1](tutorials/sys-02-operating-systems/01-privilege-levels-and-kernel-boundary.md#credentials) |
| **Stack frame** | The per-call stack region containing saved control data, locals, arguments, alignment, and optional protection such as a canary. | [SYS-01.2](tutorials/sys-01-computer-architecture/02-memory-layout-and-stack-frames.md#stack-frames) |
| **System call (syscall)** | A controlled transition from user mode to kernel mode to request an operation the kernel mediates, such as opening a file or creating a process. | [SYS-02.4](tutorials/sys-02-operating-systems/04-system-calls-and-tracing.md#the-system-call-abi) |
| **TOCTOU** | Time-of-check-to-time-of-use: a race in which the object or path checked differs from the object later used. | [SYS-02.3](tutorials/sys-02-operating-systems/03-files-permissions-and-access-control.md#path-resolution-and-races) |
| **Virtual address** | The address a process uses; the MMU translates it through page tables to a physical frame. | [SYS-01.2](tutorials/sys-01-computer-architecture/02-memory-layout-and-stack-frames.md#virtual-memory) |
| **W^X** | A policy that no page is simultaneously writable and executable. JITs and some runtimes need carefully controlled exceptions. | [SYS-01.4](tutorials/sys-01-computer-architecture/04-memory-safety-and-mitigations.md#nx-wx-and-code-reuse) |

## Research methods

| Term | Definition | Introduced in |
|---|---|---|
| **Alternative explanation** | A competing account for an observed result that the design must address or rule out before making a causal or comparative claim. | [Research 2](research/02-research-questions-hypotheses-and-threat-models.md#research-threat-models) |
| **Baseline** | The comparison condition measured under comparable settings. It is not simply "the old system." | [Research 3](research/03-experimental-design-baselines-and-sampling.md#treatment-baseline-and-control) |
| **Confounder** | A factor that varies with the treatment and the outcome and can create a spurious association. | [Research 3](research/03-experimental-design-baselines-and-sampling.md#treatment-baseline-and-control) |
| **Effect size** | The magnitude of a difference or association, reported with its direction, scale, and uncertainty rather than only as a significance decision. | [Research 4](research/04-measurement-statistics-and-uncertainty.md#effect-size-and-practical-significance) |
| **Operationalization** | Turning an abstract construct into observable variables, metrics, and evidence. | [Research 2](research/02-research-questions-hypotheses-and-threat-models.md#operationalization) |
| **p-value** | The probability of data at least as extreme as the observation, assuming the null hypothesis and statistical model. It is not the probability that the null is true. | [Research 4](research/04-measurement-statistics-and-uncertainty.md#p-values) |
| **Pre-registration** | Recording the primary question, outcomes, and analysis plan before data collection to separate confirmatory from exploratory work. | [Research 2](research/02-research-questions-hypotheses-and-threat-models.md#hypotheses) |
| **Replicability** | The extent to which a new study with new data reaches a consistent conclusion. | [Research 5](research/05-reproducibility-and-replication.md#definitions) |
| **Reproducibility** | The extent to which the same data, code, and method produce the same result. | [Research 5](research/05-reproducibility-and-replication.md#definitions) |
| **Threat model (security)** | A structured description of assets, adversaries, capabilities, trust boundaries, attack surface, and assumptions for the system under study. | [Research 2](research/02-research-questions-hypotheses-and-threat-models.md#security-threat-model) |
| **Validity threat model** | A structured account of selection, confounding, measurement, leakage, overfitting, and scope problems that could make an inference wrong. | [Research 2](research/02-research-questions-hypotheses-and-threat-models.md#validity-threat-model) |

## Contributing a definition

Add a term only when it is used by more than one lesson or is easy to confuse with a nearby concept. Include a link to the lesson that explains the mechanism, not only a dictionary definition. For a disputed or version-dependent term, state the scope and date in the linked lesson.
