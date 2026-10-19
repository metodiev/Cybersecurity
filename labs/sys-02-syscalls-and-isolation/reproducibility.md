# Reproducibility Notes: Lab SYS-02

> **Lab:** [`lab.md`](lab.md) · **Rubric:** [`rubric.md`](rubric.md) · **Instructor solution:** `solution.md` (excluded from the published site)
> **Last validated:** 2026-10-19 on macOS 27.0.1, arm64 (partial path only)

## 1. What was validated

| Item | Status | Evidence |
|---|---|---|
| `collect_evidence.sh` shell syntax | Validated | `bash -n` exit 0 |
| `verify_evidence.py` logic | Validated against a temporary fixture | Exit 0 on a synthetic fixture; fixture deleted |
| macOS descriptor and `EACCES` fallback | Validated | Real output recorded in `solution.md` |
| Linux VM trace, credentials, namespaces | Not executed | Requires a Linux runtime |
| Container comparison | Not executed | Docker daemon was not running |
| `Containerfile` build | Not executed | Requires a container build |

The fixture used to test the verifier was a temporary test input, not experimental evidence. Do not cite it as a result.

## 2. Primary environment: disposable Linux VM

Recommended because namespace and container-inspection tasks may be restricted inside a container.

Record:

```bash
uname -a
cat /etc/os-release
cat /proc/version
cc --version
strace -V
id
```

Minimum packages: `build-essential`, `strace`, `util-linux`, `iproute2`, optional `libcap2-bin`.

Do not use a production host. Take a snapshot before the lab and revert after cleanup.

## 3. Secondary environment: container

The `environment/Containerfile` builds a Debian-based tracing environment. It is optional and **not** suitable for all namespace tests.

Build and record the image identity:

```bash
docker build -f environment/Containerfile -t sys02-lab:local .
docker image inspect --format '{{.Id}}' sys02-lab:local | tee evidence/image-id.txt
```

Caveats:

- The base tag is not digest-pinned. Record the resolved image ID and build date.
- Default container seccomp, capability, and namespace settings differ by runtime.
- Do not use `--privileged` or `CAP_SYS_ADMIN`.
- `unshare` may fail inside the container even when it works in a VM.

## 4. Exact commands

From `labs/sys-02-syscalls-and-isolation`:

```bash
shasum -a 256 -c SHA256SUMS   # macOS
sha256sum -c SHA256SUMS       # Linux
scripts/collect_evidence.sh evidence
scripts/verify_evidence.py --dir evidence
```

The collector creates `evidence/` and does not modify files outside it. Review it before execution.

## 5. What may vary

| Observation | Expected variation | How to record it |
|---|---|---|
| Syscall names | `open` versus `openat` by libc/kernel | Quote the actual trace line |
| Descriptor number | Usually 3, but not guaranteed | Record the value, do not hard-code it |
| Short reads | File size and kernel behavior | Record requested and returned counts |
| Extra syscalls | libc startup, locale, dynamic loading | Keep the filter and explain unrelated lines |
| UID inside a user namespace | Mapping-dependent | Record host and namespace values |
| Interface list | Namespace and runtime-dependent | Record names and count |
| `Seccomp` value | Runtime and policy-dependent | Record the number and explain its meaning |
| Capability mask | User and runtime-dependent | Record the mask and decode it |
| Cgroup path | systemd, container runtime, or VM-dependent | Quote the actual path |

## 6. Known nondeterminism

- **PID and descriptor reuse:** do not compare exact PIDs or descriptors across runs.
- **Trace interleaving:** `-f` can interleave threads; identify the process/thread IDs.
- **Startup noise:** dynamic loading may add file-related syscalls before `main`.
- **Namespace policy:** unprivileged user namespaces may be disabled or restricted.
- **Container profiles:** the runtime's default seccomp and capability sets are not universal.
- **Kernel version:** field names and semantics can change.

## 7. Evidence retention and privacy

- Traces can contain paths, command-line arguments, environment values, and buffer previews.
- Use only synthetic files and test data.
- Do not trace a process that handles real credentials.
- Redact home directories and hostnames before sharing a report.
- Keep raw evidence locally; submit only what the rubric requires.

## 8. Manual testing still required

1. Run the full Linux VM path on a clean snapshot and record real traces.
2. Test `unshare -Urn` on at least two distributions or kernel configurations and record policy differences.
3. Build the Containerfile and record the resolved image ID and default `Seccomp`/`CapEff`.
4. Confirm the verifier against the real evidence directory, not only the fixture.
5. Test whether the distribution's `strace` uses `open` or `openat` and adjust the filter guidance if needed.
6. Confirm cleanup removes the container and temporary files.

## 9. Review checklist

- [ ] Environment record includes kernel, distribution, compiler, and `strace`.
- [ ] Source integrity check passed.
- [ ] The unprivileged and root runs are recorded separately.
- [ ] The exact errno is present.
- [ ] Namespace evidence includes host and namespace values.
- [ ] A failed `unshare` is recorded with the exact error.
- [ ] Container results include image ID and runtime configuration.
- [ ] Limitations and manual-testing gaps are stated.
