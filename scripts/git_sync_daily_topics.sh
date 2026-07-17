#!/bin/bash
# 每日同步选题产出到 GitHub（2026-07-17 起：只同步本仓库，不再碰 life-business-video-workflow）
set -e
cd /root/topic-discovery-prompt

# 暂存主库 + 当天的新每日文件
TODAY=$(date +%Y-%m-%d)
git add topics.csv
git add "topics_daily_${TODAY}.csv" 2>/dev/null || true

# 无改动就退出
if git diff --cached --quiet; then
  exit 0
fi

# 提交
git commit -m "daily: topic discovery ${TODAY}"

# 推送；冲突时 rebase 重试
git push origin main 2>&1 || {
  git pull --rebase origin main
  git push origin main
}
