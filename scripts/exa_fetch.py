#!/usr/bin/env python3
"""exa 抓取封装：usage exa_fetch.py <outfile> <query> <objective>"""
import json
import subprocess
import sys

out, query, objective = sys.argv[1], sys.argv[2], sys.argv[3]
payload = json.dumps({"query": query, "numResults": 10, "objective": objective}, ensure_ascii=False)
proc = subprocess.run(
    ["mcporter", "call", "exa.web_search_exa", "--args", payload, "--output", "json"],
    capture_output=True, text=True, cwd="/root",
)
with open(out, "w", encoding="utf-8") as fh:
    fh.write(proc.stdout)
    fh.write("\n---STDERR---\n")
    fh.write(proc.stderr)
print(f"WROTE {out} {len(proc.stdout)} bytes")
