# LEARNING — agent-lab-openclaw-minimal

> 这份文件回答：「我跑完这个仓库，应该真的学到什么？」

## 你跑完应该能回答的问题

1. 「白名单脚本」相比"让 Agent 直接跑任意 shell"，安全等级差多少？
2. 一个本地 Agent 想要安全，至少需要哪几道闸门？
3. `verify.py` 这种"客观验收脚本"在 Agent 工程中起的作用是什么？
4. 当 Agent 想做一件超出 `AGENT_TASK.md` 列表的事（比如"我顺便升级一下 Python 包"），你怎么阻止？

## 实操验证清单（务必动手）

### 路线 A — 你装了 `openclaw`
- [ ] `which openclaw && openclaw --help`
- [ ] `cd agent-lab-openclaw-minimal`
- [ ] 用它打开本目录，把 `AGENT_TASK.md` 全文交给它（具体命令看你装的版本）
- [ ] 等 Agent 完成（应该按顺序跑 `safe_status.sh` → `safe_create_note.sh` → `verify.py`）
- [ ] 期间观察：
  - 它有没有想 `cd ..` 或 `cd ~`？应该被拒绝
  - 它有没有想读 `~/.ssh` / `~/.cursor`？应该被拒绝
  - 它有没有想"顺便"`npm install`？应该被拒绝
- [ ] 最终 `python3 verify.py` 输出 `[成功]`

### 路线 B — 你没装 openclaw（人当一回 Agent）
- [ ] `cd agent-lab-openclaw-minimal`
- [ ] 严格按 `AGENT_TASK.md` 的顺序：
  ```bash
  bash scripts/safe_status.sh
  bash scripts/safe_create_note.sh
  python3 verify.py
  ```
- [ ] 每一步看它打印的内容
- [ ] 注意：**这条路线就是这个仓库已经自测过的，确保你的环境也能跑通**

### 阶段 C — 越界拒绝实验（关键）
**这是教育性最强的环节。**

读一遍 `scripts/safe_create_note.sh`，**它写死了**：
- 创建文件的位置（仓库根）
- 文件名（`agent_note.txt`）
- 文件内容（`created by local agent`）

试着想象一下：

- [ ] 如果 Agent 跟你说"能不能允许我把文件路径作为参数传进去？我想存到 `~/Documents/`"
- [ ] **拒绝它**——这是边界
- [ ] 如果允许了参数，Agent 就可以写**任意路径**——白名单瞬间失效
- [ ] 这是为什么 `safe_create_note.sh` **不接受任何参数**

### 阶段 D — verify.py 攻防演练
- [ ] 让 Agent（或人）"作弊"：直接 `echo "created by local agent" > agent_note.txt` 而**不**走脚本
- [ ] 跑 `python3 verify.py` → **会通过**！
- [ ] 思考：现在的 verify 只检查"结果"，不检查"过程"。这有没有问题？
- [ ] **这是一个真问题**：Agent 工程里，"事后验证 vs 事中拦截"是两种不同的安全策略

### 阶段 E — 把这套思路迁移到你自己的项目
- [ ] 想象你以后想让 Agent 做"备份某个目录"——你会写一个 `safe_backup.sh`，里面写死源路径和目标路径吗？
- [ ] 还是允许 Agent 自由传参？
- [ ] 如果允许传参，你会用什么手段限制（路径正则白名单？是否在仓库内？）？

## 自检题

1. `safe_create_note.sh` 用了 `set -euo pipefail`，这三个开关分别防什么？
2. `safe_create_note.sh` 怎么定位"仓库根"？如果有人把脚本符号链接到别处，会不会出问题？
3. `verify.py` 现在只看结果，怎么改造成"也看过程"？（提示：可以记录脚本调用日志）
4. 同一个项目，能不能让 Claude Code、OpenCLaw、Cursor agent 模式**轮流**来跑这套白名单？换句话说，**白名单是不是 Agent 中立的**？

## 与其它仓库的连接

| 关系 | 仓库 | 为什么去看 |
| --- | --- | --- |
| **同类对照** | `agent-lab-claude-code-minimal` | 它让 Agent 自由写代码，本仓库只让它跑白名单脚本——两种紧度的边界 |
| **能力骨架** | `api-lab-tool-calling-minimal` | "模型出意图 + 白名单执行"是 Agent 内核；本仓库是把这件事 **搬进真正的 shell 脚本** |
| **离线 / 隐私** | `api-lab-ollama-local-minimal` | 本地 Agent + 本地模型 = 完全离线工作流，是个有趣的方向 |

## 你应该感受到的"啊哈"瞬间

- 当你意识到 `safe_create_note.sh` 故意**不接受参数**——你理解"参数化的便利性"和"安全紧度"是天然互斥的。
- 当你跑 `bash scripts/safe_status.sh` 看到只是 `pwd + ls`——你会想"这就够了？"，对，**就够了**。Agent 不需要每个工具都强大，需要每个工具都**可被理解**。
- 当你做完阶段 D 的"作弊"实验，发现 `verify.py` 居然通过——你理解了"事后验证"的局限性，也理解了真正的安全 Agent 框架（如沙盒、cgroup、虚拟机）为什么必要。
