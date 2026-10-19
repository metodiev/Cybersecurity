# Answer Key: SYS-02 Assessment

> **Access:** instructor-only. Excluded from the published site. Do not distribute to learners before the assessment.

## Section 1

1. **Syscall transition (4 pts).** The process places the syscall number and arguments in ABI-defined registers and executes the trap instruction. The CPU switches to a privileged level, saves the user context, switches to a kernel stack, dispatches the syscall, validates arguments, performs the operation, and returns. User pointers must be copied or validated because user memory can change concurrently and may be malformed; dereferencing directly can fault or create a TOCTOU issue. Citation: [L01], [L12].

2. **Rings and exception levels (4 pts).** x86-64 has rings 0–3; mainstream OSes use ring 0 for the kernel and ring 3 for user code. Armv8-A has EL0 (user), EL1 (kernel), EL2 (hypervisor), EL3 (secure monitor). A hypervisor needs a level above the guest kernel so the guest cannot disable or bypass virtualization controls. Citation: [L11], [L12].

3. **Process vs thread (4 pts).** A process has its own address space, file descriptor table, credentials, signal dispositions, resource limits, and namespace membership. Threads share the address space, descriptors, credentials, and signal dispositions; each has its own stack, registers, and TLS. Shared authority makes a thread compromise more contained than a process compromise only if the process itself is contained. Citation: [L28], [L13].

4. **Inode/FD/open file description (4 pts).** An inode is file metadata and data pointers, independent of names. A file descriptor is a per-process integer indexing an open file description. An open file description holds the offset, flags, and status and can be shared by multiple descriptors (for example, after `dup` or `fork`). Citation: [L06], [L13].

5. **Setuid (4 pts).** The `s` bit in the owner execute position makes the executable run with the file owner's effective UID. It is risky because any vulnerability in the program can be used to execute code with the owner's authority; setuid binaries are high-value privilege-escalation targets. Setuid on scripts is commonly ignored. Citation: [L07], [L13].

## Section 2

6. **fork/exec/wait (6 pts).** `fork` creates a child with a copy of the address space (copy-on-write), credentials, descriptor table, signal dispositions, and environment. `exec` replaces the image but preserves the PID, credentials (subject to setuid), and descriptors unless `FD_CLOEXEC`. `wait` reaps the child. `FD_CLOEXEC` prevents accidental descriptor inheritance, which can leak sockets, files, or secrets to an untrusted program. Award full credit for inheritance details and the security rationale.

7. **Namespace vs cgroup (6 pts).** A namespace isolates *what a process can see* (mounts, PIDs, network, users). A cgroup limits *what a process can consume* (CPU, memory, PIDs). Security questions: namespaces — can this process see or signal another process? cgroups — can this process exhaust host resources? Neither is sufficient alone. Citation: [L04], [L05].

8. **TOCTOU (6 pts).** The vulnerability is a time-of-check-to-time-of-use race. The kernel resolves path components and checks traverse permissions; the attacker changes a component between the check and the use. Defenses: `openat` with directory descriptors, `O_NOFOLLOW`, `O_CREAT|O_EXCL`, per-job directories, dropping privileges before path resolution. Award credit for the race and two defenses. Citation: [L13], [L06].

9. **seccomp (6 pts).** seccomp filters syscall numbers and argument register values with a BPF program. It does not inspect pointed-to memory, file paths, network destinations, or the correctness of allowed operations. A syscall allowlist is therefore one layer, combined with namespaces, cgroups, LSMs, and least privilege. Citation: [L02], [L18].

10. **Container vs VM (6 pts).** A container is a process (or group) on the host kernel, confined by namespaces, cgroups, capabilities, seccomp, and LSMs. A VM runs a guest kernel under a hypervisor. Containers share the host kernel, so a kernel vulnerability can cross the boundary; a VM escape must compromise the hypervisor or a device model. Neither is absolute. Citation: [N12], [L04].

## Section 3

Use the lab rubric. Key checks:

- **Trace:** `openat` returns a non-negative fd; `read` uses that fd; `write` uses 1; `close` returns 0; `exit_group` ends the process. Accept `open` on older toolchains.
- **EACCES:** exact `-1 EACCES (Permission denied)` or the language-level equivalent; learner must connect it to credentials and mode bits.
- **`/proc/self/status`:** four UID values, capability mask, `NoNewPrivs`, `Seccomp` mode. Require correct interpretation, not a specific mask.
- **Namespaces:** new `user`, `net`, `pid`, `mnt` inode numbers; UID 0 inside a user namespace is not host root.
- **Limitations:** a trace shows only traced syscalls; it may omit kernel-internal work, library logic, and buffer contents. Namespace inspection is a point-in-time snapshot.

Deduct for fabricated Linux output, hard-coded syscall numbers, or claiming host root from a user namespace.

## Section 4

Expected boundaries and failed controls:

| Boundary | Failed control | Evidence | Reduction |
|---|---|---|---|
| Container to host | Root in container plus `CAP_SYS_ADMIN`; privileged capabilities | `docker inspect`, `/proc/<pid>/status`, capability mask | Run as non-root, drop all capabilities, `no_new_privs`, read-only rootfs |
| Container to control plane | Runtime socket mounted | Mount table, socket path, Docker API access | Do not mount the socket; use a restricted proxy or VM-isolated runtime |
| Tenant to tenant | Shared host kernel and weak isolation | Namespace/cgroup membership, kernel version, host logs | VM or microVM isolation; patched kernel; admission policy |
| Application to data | Upload parser compromise | Parser logs, file paths, outbound connections | Sandbox the parser, seccomp, least privilege, egress policy |

Evidence to collect: container configuration, capability set, mount table, namespace links, cgroup path, process tree, network connections, file integrity, host audit logs, and the kernel version. Award full credit for at least three boundaries, matched controls, and concrete evidence.

## Misconception flags

Deduct up to 5 points for any of these presented as fact:

- "A container is a lightweight VM."
- "Root inside a user namespace is host root."
- "seccomp blocks all attacks."
- "`strace` shows everything."
- "A setuid binary is safe if it is compiled with stack protection."

## Oral follow-up

Ask the learner to explain one real trace line without notes and to name one boundary their evidence did **not** prove.
