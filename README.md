# 钱花哪儿了 · 每日选题发现

抖音号「钱花哪儿了」的选题发现系统。

## 快速导航

| 文件 | 用途 |
|------|------|
| `TOPIC_DISCOVERY_PROMPT.md` | 每日选题 cron job 的完整 prompt（Claude 优化对象） |
| `topics.csv` | 选题主库（所有已收录选题） |
| `data/topics_daily_*.csv` | 每日新增选题 |
| `scripts/git_sync_daily_topics.sh` | 自动同步脚本 |

## 选题标准

- 每条必须有至少 2 个可验证的具体数字
- 标题里必须有具体价格/比例数字
- 核心标准：「卧槽感」——读者看完想的是「我靠，原来是这样」

## 同步节奏

- 10:00 选题发现 cron → 写入 `topics.csv` + `topics_daily_{日期}.csv`
- 10:30 GitHub 同步 cron → 推送上述文件
