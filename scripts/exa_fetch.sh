#!/bin/bash
# exa 抓取封装：用法 exa_fetch.sh <outfile> <query> <objective>
set -e
OUT="$1"; Q="$2"; OBJ="$3"
cd /root
mcporter call exa.web_search_exa --args "$(python3 - "$Q" "$OBJ" <<'PY'
import json,sys
print(json.dumps({"query":sys.argv[1],"numResults":10,"objective":sys.argv[2]},ensure_ascii=False))
PY
)" --output json > "$OUT" 2>&1
echo "WROTE $OUT $(wc -c < "$OUT")"
