#!/usr/bin/env bash
# 只允许：在仓库根目录创建 agent_note.txt，内容固定。
# 不接受任何参数，不接受任何外部输入路径。
set -euo pipefail

# 取脚本所在目录的上一级，作为仓库根
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
TARGET="$REPO_ROOT/agent_note.txt"

echo "created by local agent" > "$TARGET"
echo "[safe_create_note] wrote $TARGET"
