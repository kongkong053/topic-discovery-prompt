# 钱花哪儿了 · 每日选题发现

抖音号「钱花哪儿了」的选题发现系统。**本仓库是选题产出的独立家**（2026-07-17 起与视频工作流仓库解耦）——每日 agent 的 prompt、选题主库、每日新增都在这里，不再写入 `life-business-video-workflow` 仓库。

## 快速导航

| 文件 | 用途 |
|------|------|
| `TOPIC_DISCOVERY_PROMPT.md` | 每日选题 cron job 的完整 prompt（Claude 优化对象） |
| `topics.csv` | 选题主库（所有已收录选题；2026-07-14 前的历史行含旧 T 编号，新行一律日期开头） |
| `topics_daily_*.csv` | 每日新增选题 |
| `scripts/git_sync_daily_topics.sh` | 自动同步脚本（推送到本仓库） |
| `covered_concepts.md` | 去重池：已覆盖概念 + 可反复挖的搜索方向（2026-07-17 自视频仓库迁入） |

## 选题标准

- 每条必须有至少 2 个可验证的具体数字
- 标题里必须有具体价格/比例数字
- 核心标准：「卧槽感」——读者看完想的是「我靠，原来是这样」

## 同步节奏

- 10:00 选题发现 cron → 写入本仓库 `topics.csv` + `topics_daily_{日期}.csv`
- 10:30 GitHub 同步 cron → 推送本仓库（`scripts/git_sync_daily_topics.sh`）

## 与视频仓库（life-business-video-workflow）的边界

- **本仓库产出候选**，下游（视频仓库的每周军火库任务 / 人工选题）从这里读 `topics_daily_*.csv`，过选题宪法后才在视频仓库 `knowledge/topic-bank.yaml` 立正式 T 编号。
- **不要写视频仓库的 `data/topics.csv`**——那份文件由 `sync_topics_from_kb.py` 从 topic-bank 自动重建，追加会分叉冲突（2026-07 已发生过一次，本仓库主库里 T037/T038 与视频仓库正式选题撞号即此遗留）。
- 本仓库不编 T 号，T 编号是视频仓库 topic-bank 的 ID 空间。
