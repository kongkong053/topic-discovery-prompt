#!/bin/bash
# 每日同步选题产出到 GitHub（2026-07-17 起：只同步本仓库，不再碰 life-business-video-workflow）
set -e
cd /root/topic-discovery-prompt

# 暂存主库 + 当天的新每日文件
TODAY=$(date +%Y-%m-%d)

# 主库和每日增量必须使用同一套 6 列契约；避免只把扩展格式写进 topics.csv，
# 导致下游只读 topics_daily_*.csv 时漏题。
python3 - "topics.csv" "topics_daily_${TODAY}.csv" <<'PY'
import csv
import pathlib
import sys

expected = ["date", "标题", "卧槽点", "来源类型", "核心数据", "适合结构环节"]
for raw_path in sys.argv[1:]:
    path = pathlib.Path(raw_path)
    if not path.exists():
        continue
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows or rows[0] != expected:
        raise SystemExit(f"{path}: CSV header must be {expected}")
    bad_rows = [index for index, row in enumerate(rows[1:], start=2) if len(row) != 6]
    if bad_rows:
        raise SystemExit(f"{path}: rows must have 6 columns; bad rows: {bad_rows}")
PY

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
