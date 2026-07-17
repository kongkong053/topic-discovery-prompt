#!/bin/bash
# 每日同步 topics.csv 和每日选题文件到 GitHub
set -e
cd /root/life-business-video-workflow

# 暂存主文件 + 当天的新每日文件
TODAY=$(date +%Y-%m-%d)
git add data/topics.csv
git add "data/topics_daily_${TODAY}.csv"

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
