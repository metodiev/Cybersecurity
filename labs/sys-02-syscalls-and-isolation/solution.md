# Instructor Solution: Lab SYS-02

> **Access:** instructor-only. Excluded from the published MkDocs site. Exclusion is not access control for the repository; restrict repository or LMS permissions separately.

## 1. Validation record

| Item | Result |
|---|---|
| Host | macOS 27.0.1 (build 26A434), arm64 |
| Linux VM | Not available in the validation session |
| `strace` | Not available on the capture host |
| `collect_evidence.sh` | `bash -n` passed; not executed |
| `verify_evidence.py` | Passed against a temporary synthetic fixture; not a real experiment |
| macOS descriptor/error fallback | Executed; real output below |

**Do not treat the expected syscall categories in this solution as captured output.** They describe what a successful Linux trace should contain.

## 2. Hypothesis evidence standards

| Hypothesis | Evidence that would support it | Evidence that would weaken it |
|---|---|---|
| H1 | Unprivileged trace shows `openat(...) = -1 EACCES`; exit status nonzero; a separate root run may show a successful open | Unprivileged open succeeds without a capability/ACL explanation; errno is not `EACCES` |
| H2 | `id` inside namespace shows UID 0; host `id` shows original UID; new `user`, `net`, `pid`, and `mnt` inode numbers; `ip link` shows loopback only | UID mapping is not as predicted; host interfaces are visible; namespace inodes are unchanged |
| H3 | Container `Seccomp` differs from host and `CapEff` is a strict subset | Container is unconfined, `Seccomp: 0`, or capability set is not reduced |

If a hypothesis is not tested, the learner must say so. "Not tested" is a valid result; a fabricated comparison is not.

## 3. Expected successful trace categories

A learner's Linux trace should contain lines in these categories:

| Step | Expected syscall | Expected result |
|---|---|---|
| Open | `openat(AT_FDCWD, "<path>", O_RDONLY)` | Non-negative descriptor, often 3 |
| Read | `read(<fd>, "<bytes>", 16)` | 0..16, depending on file size and short reads |
| Write | `write(1, "<bytes>", <n>)` | `<n>` on success |
| Close | `close(<fd>)` | 0 |
| Exit | `exit_group(0)` | Does not return |

Accept `open` instead of `openat` on some libc/kernel/toolchain combinations. The descriptor in `read` and `close` must match the one returned by `openat`. Do not require a specific number; require consistency and evidence.

## 4. Expected permission-failure categories

A learner's unprivileged trace should contain a failed open:

- return value `-1`;
- symbolic error `EACCES`;
- exit status nonzero;
- stderr message from `fileio`.

The exact trace formatting is tool-specific. The learner must quote the real line and include `id`, `ls -l`, and the command.

If the learner runs as root, the open may succeed because of `CAP_DAC_OVERRIDE`. That is a different experiment. Require the learner to record it separately and explain the capability.

## 5. macOS fallback output (executed)

The following was captured on the validation host. It demonstrates descriptors and `EACCES` but **not** a syscall trace:

```text
$ python3 - <<'PY'
import os, errno
fd = os.open('/etc/hosts', os.O_RDONLY)
print('open returned fd:', fd)
data = os.read(fd, 16)
print('read returned bytes:', data)
os.close(fd)
print('close returned: None')
try:
    os.open('/etc/master.passwd', os.O_RDONLY)
except OSError as e:
    print('denied errno:', e.errno, errno.errorcode[e.errno])
PY
open returned fd: 3
read returned bytes: b'##\n# Host Databa'
close returned: None
denied errno: 13 EACCES
```

Teaching points:

- descriptor 3 is the first free descriptor in this process;
- the read returned exactly the requested 16 bytes in this run; short reads are allowed;
- `EACCES` is error 13 on this platform;
- the fallback does not show syscall names or kernel argument decoding.

## 6. Namespace expectations

If `unshare -Urn --fork --pid --mount-proc` succeeds:

- `id` often shows `uid=0(root) gid=0(root)` inside the user namespace;
- the host `id` still shows the original UID;
- `/proc/self/ns/user`, `net`, `pid`, and `mnt` have different inode numbers from the host;
- `ip link` usually shows only `lo`;
- `/proc/self/cgroup` may be unchanged unless a cgroup namespace was created.

If it fails with `Operation not permitted`, the learner must record the error and explain that unprivileged user namespaces are restricted by policy. Full credit is available for a correct failure analysis.

## 7. Container expectations

For a default Docker container:

- it has its own mount, PID, network, IPC, UTS, and cgroup namespaces;
- it shares the host kernel;
- `HostConfig.Privileged` should be `false`;
- `CapAdd` should be empty, though the runtime still grants a default capability set;
- `Seccomp` may be `2` if a default profile is applied;
- the cgroup path identifies the container's cgroup.

These are expectations, not captured results. The learner must record the actual runtime output and image ID.

## 8. Boundary-failure analysis

### Scenario A: root service writes into a world-writable directory

- **Failed control:** least privilege and path-based trust.
- **Evidence:** effective UID, `openat` resolution, symlink target, directory mode, mount options.
- **Prevention:** drop privileges, use `openat` with `O_NOFOLLOW`/`O_CREAT|O_EXCL`, write to a service-owned directory, set `nosuid,nodev,noexec`.

### Scenario B: privileged container with the runtime socket

- **Failed control:** container isolation and control-plane separation.
- **Evidence:** `docker inspect` (`Privileged`, `CapAdd`, mounts), capability mask, namespace links, socket path.
- **Prevention:** never use `--privileged` for untrusted workloads; drop capabilities; do not mount the runtime socket; use a rootless or VM-isolated runtime; enforce admission policy.

### Scenario C: user namespace assumed to be a boundary

- **Failed control:** the assumption that a user namespace contains all kernel effects.
- **Evidence:** new `user` and `mnt` namespace inodes, mount table, capability set inside the namespace, kernel version.
- **Prevention:** restrict unprivileged user namespaces where not needed; patch the kernel; combine with seccomp and LSMs; use a VM or microVM for untrusted workloads.

## 9. Grading guidance

Award full credit when:

- the learner quotes a real trace line and explains each field;
- the descriptor chain is consistent;
- the exact errno is present;
- credentials and capabilities are interpreted, not just listed;
- a failed namespace task is documented with the exact error;
- "not tested" is used honestly;
- the boundary analysis names a control, evidence, prevention, and residual risk.

Deduct for:

- hard-coded syscall numbers or descriptors without evidence;
- claiming host root from a user namespace;
- treating `strace` as complete;
- running the permission test as root without a separate unprivileged run;
- calling a container "secure" because it is not privileged;
- fabricating Linux output.

## 10. Common learner errors

| Error | Why it is wrong | Feedback |
|---|---|---|
| Hard-coding descriptor 3 | Descriptors depend on prior opens | Require the actual trace |
| Reporting `EACCES` without the syscall line | The error code alone does not identify the operation | Require trace plus stderr plus `id` |
| Claiming UID 0 inside a namespace is host root | User namespaces map identities | Revisit SYS-02.5 |
| Ignoring `Seccomp: 0` | An unconfined process has a larger attack surface | Require interpretation |
| Treating a failed `unshare` as failure of the lab | Policy restrictions are a valid finding | Require exact error and explanation |

## 11. Cleanup verification

Confirm the learner removed `evidence/fileio`, synthetic files, and any container. Confirm the evidence package contains no real credentials, secrets, or unrelated personal data.
