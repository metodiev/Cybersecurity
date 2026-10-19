#!/usr/bin/env bash
# Collect syscall, credential, and namespace evidence on a disposable Linux host.
set -euo pipefail

if [ "$(uname -s)" != "Linux" ]; then
  echo "ERROR: this script requires Linux. Use the macOS fallback in lab.md." >&2
  exit 2
fi

OUT="${1:-evidence}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(dirname "$SCRIPT_DIR")"
mkdir -p "$OUT"

{
  echo "\$ uname -a"; uname -a
  echo; echo "\$ cat /etc/os-release"; cat /etc/os-release
  echo; echo "\$ cc --version"; cc --version
  echo; echo "\$ strace -V"; strace -V
  echo; echo "\$ id"; id
} >"$OUT/environment.txt" 2>&1

cc -O0 -g -Wall -Wextra -o "$OUT/fileio" "$LAB_DIR/starter/fileio.c"
printf 'synthetic lab data\n' >"$OUT/sample.txt"
printf 'synthetic restricted data\n' >"$OUT/restricted.txt"
chmod 000 "$OUT/restricted.txt"

strace -f -e trace=openat,read,write,close,exit_group \
  -o "$OUT/trace-success.txt" "$OUT/fileio" "$OUT/sample.txt" \
  >"$OUT/stdout-success.txt" 2>"$OUT/stderr-success.txt"

set +e
strace -f -e trace=openat,exit_group \
  -o "$OUT/trace-denied.txt" "$OUT/fileio" "$OUT/restricted.txt" \
  >"$OUT/stdout-denied.txt" 2>"$OUT/stderr-denied.txt"
DENIED_STATUS=$?
set -e
printf 'exit_status=%s\n' "$DENIED_STATUS" >"$OUT/denied-status.txt"

grep -E '^(Uid|Gid|CapEff|CapPrm|NoNewPrivs|Seccomp):' /proc/self/status \
  >"$OUT/status-fields.txt" 2>&1 || true
ls -l /proc/self/ns >"$OUT/namespaces.txt" 2>&1 || true
cat /proc/self/cgroup >"$OUT/cgroup.txt" 2>&1 || true

set +e
unshare -Urn --fork --pid --mount-proc sh -c '
  echo "--- id"; id
  echo "--- links"; ip link 2>&1 || true
  echo "--- namespaces"; ls -l /proc/self/ns
  echo "--- cgroup"; cat /proc/self/cgroup
' >"$OUT/namespace-experiment.txt" 2>&1
UNSHARE_STATUS=$?
set -e
printf 'exit_status=%s\n' "$UNSHARE_STATUS" >"$OUT/namespace-status.txt"

if command -v sha256sum >/dev/null 2>&1; then
  (cd "$OUT" && find . -maxdepth 1 -type f ! -name SHA256SUMS -print0 \
    | sort -z \
    | xargs -0 sha256sum >SHA256SUMS)
fi

echo "Evidence written to $OUT"
echo "Review: environment.txt, trace-success.txt, trace-denied.txt, status-fields.txt, namespaces.txt, namespace-experiment.txt"
