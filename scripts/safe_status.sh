#!/usr/bin/env bash
# 只允许：打印当前目录路径 + 当前目录文件列表。
# 不读子目录、不读父目录、不读用户主目录、不动任何文件。
set -euo pipefail

echo "[safe_status] cwd: $(pwd)"
echo "[safe_status] files in cwd:"
ls -1
