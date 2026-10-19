# SYS-02 Assessment: Operating Systems Internals

> **Module:** SYS-02 · **Level:** L1 · **Type:** written quiz plus practical trace analysis · **Time:** 60 min written + 2 h practical · **Open book:** no for the written section; notes allowed for the practical · **Status:** drafted · **Validation:** structural

## Blueprint

| Outcome | Cognitive level | Item types | Weight |
|---|---|---|---:|
| SYS-02.O1 | Understand, apply | Short answer, comparison, diagram | 40% |
| SYS-02.O2 | Apply, analyze | Practical trace and `/proc` inspection | 35% |
| SYS-02.O3 | Analyze, evaluate | Boundary-failure scenario | 25% |

**Pass:** 80/100 overall, no outcome below 60%, and the practical report meets every evidence criterion.

## Instructions

- Use a disposable Linux VM or container for the practical. If one is unavailable, state that and answer the practical questions from the macOS alternatives in the lab; do not invent Linux output.
- Every practical claim must cite the command and a real output excerpt.
- Do not attach a tracer to a process you do not own.
- Do not include secrets from environment variables or trace buffers.

## Section 1: Foundations (20 points)

1. **(4 pts)** Explain the user/kernel transition during a system call. What does the CPU switch, and why must the kernel treat user pointers as untrusted?
2. **(4 pts)** Compare x86-64 rings and Arm exception levels. Why does a hypervisor need a level above the kernel?
3. **(4 pts)** What does a process have that a thread does not? What do threads share that makes them a weaker isolation boundary?
4. **(4 pts)** Explain the difference between an inode, a file descriptor, and an open file description.
5. **(4 pts)** What does the `s` bit in `-rwsr-xr-x` mean, and why is a setuid binary a security risk?

## Section 2: Mechanisms (30 points)

6. **(6 pts)** Explain `fork`, `exec`, and `wait`. What is inherited across `fork` and across `exec`? Why is `FD_CLOEXEC` a security control?
7. **(6 pts)** Explain the difference between a namespace and a cgroup. Give one security question each answers.
8. **(6 pts)** A process opens a file with `O_RDONLY`, then an attacker replaces the path with a symlink before the process reopens it. Name the vulnerability class, the kernel mechanism involved, and two defenses.
9. **(6 pts)** Explain what `seccomp` filters and what it does not filter. Why is a syscall allowlist not a complete sandbox?
10. **(6 pts)** Explain why a container is not a virtual machine. Which kernel component is shared, and what does that imply for a kernel vulnerability?

## Section 3: Practical analysis (35 points)

On a disposable Linux system:

1. Compile the `fileio.c` program from the SYS-02 lab.
2. Trace a successful read of a small file. Record the real trace.
3. Create a mode-`000` file and trace the failure as an unprivileged user. Record the exact `errno`.
4. Inspect `/proc/self/status` and explain `Uid`, `CapEff`, `NoNewPrivs`, and `Seccomp`.
5. Create a user and network namespace with `unshare` if permitted. Record the namespace links and explain what changed. If it fails, record the exact error.
6. Write a 300-word analysis that maps each observed syscall or field to a kernel abstraction and states two limitations of the evidence.

Submit the command log, real outputs, and the analysis.

## Section 4: Boundary-failure scenario (15 points)

A containerized web application runs as root inside the container, mounts `/var/run/docker.sock`, and has `CAP_SYS_ADMIN`. The host is shared with other tenants. An attacker compromises the application through a file-upload parser.

Identify:

1. the boundaries that were supposed to contain the attacker;
2. the control that failed at each boundary;
3. the evidence you would collect to determine the scope of compromise;
4. three changes that would materially reduce the blast radius.

## Practical rubric

| Criterion | Weight | Pass | Proficient | Exemplary |
|---|---:|---|---|---|
| Environment and reproducibility | 10 | OS and kernel | Versions and architecture | Another analyst can reproduce the trace |
| Trace interpretation | 25 | Identifies open/read | Maps descriptors and return values | Explains errors and short reads |
| Credentials and sandbox state | 20 | Lists fields | Explains each field | Relates capabilities to least privilege |
| Namespace evidence | 20 | Shows namespace links | Compares host and namespace | Explains the limits of user namespaces |
| Boundary analysis | 15 | Names a boundary | Names the failed control | Connects evidence, prevention, and residual risk |
| Evidence discipline | 10 | Includes outputs | Cites commands | Separates observation from inference |

## Academic integrity

The written section is individual. The practical may use documentation and your own notes. AI assistance must be disclosed. You must be able to explain every claim orally on request.

## Answer key

`answer-key.md` — instructor-only; excluded from the published site.
