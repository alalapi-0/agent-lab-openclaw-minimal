# 给 OpenCLaw（小龙虾 / Open Cursor Local Agent / 任意类似的本地 Agent 工具）的任务

> 你（OpenCLaw 或类似工具）已被启动在 `agent-lab-openclaw-minimal/` 这个目录。
> 请只在本目录内操作，按顺序完成下面的最小任务。

## 任务（按顺序）

1. 运行 `bash scripts/safe_status.sh`
   - 这只会打印当前路径与目录文件列表。
   - 你应该把它的输出原样展示给用户。

2. 运行 `bash scripts/safe_create_note.sh`
   - 这只会在仓库根目录创建 `agent_note.txt`，写入固定内容 `created by local agent`。
   - 不要传任何参数，不要修改这个脚本。

3. 运行 `python3 verify.py`
   - 它会检查 `agent_note.txt` 是否存在、内容是否正确。
   - 输出包含 `[成功]` 即视为完成。

## 边界（必须遵守）

- 只许执行本仓库内 `scripts/` 下的两个白名单脚本，外加 `python3 verify.py`
- 不许执行仓库外的命令（不许 `cd ..`、不许 `cd ~`）
- 不许读取用户主目录下的敏感文件（`~/.ssh`、`~/.aws`、`~/.cursor`、密钥、配置）
- 不许联网下载任何东西
- 不许 `rm`、`sudo`、`git push --force`
- 不许修改 `verify.py` / `AGENT_TASK.md` / `README.md` / `scripts/*.sh`
- 不许写入 `agent_note.txt` 以外的任何文件

## 提示

- 这个任务非常小。不要"顺便重构"、"顺便加 README"、"顺便改一下脚本"。
- 如果你（Agent）发现你想做的事不在白名单里，**停下来问用户**，不要自己批准。
