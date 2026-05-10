"""verify.py — 验证本地 Agent 是否按白名单完成了最小任务。

判定标准：
1. 仓库根目录存在 agent_note.txt
2. 它的内容（去掉首尾空白）严格等于 'created by local agent'
"""

from __future__ import annotations

import sys
from pathlib import Path

EXPECTED = "created by local agent"
NOTE = Path(__file__).parent / "agent_note.txt"


def main() -> int:
    print(f"[验证] 检查 {NOTE.name} 是否存在...")
    if not NOTE.exists():
        print(f"[失败] 找不到 {NOTE}。Agent 还没运行 scripts/safe_create_note.sh，或者越界写到了别处。")
        return 1
    if not NOTE.is_file():
        print(f"[失败] {NOTE} 存在但不是普通文件。")
        return 1

    try:
        text = NOTE.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"[失败] 读取 {NOTE} 失败: {exc}")
        return 1

    actual = text.strip()
    if actual != EXPECTED:
        print("[失败] 内容不符合预期。")
        print(f"        期望: {EXPECTED!r}")
        print(f"        实际: {actual!r}")
        return 1

    print(f"[成功] agent_note.txt 内容符合预期: {EXPECTED!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
