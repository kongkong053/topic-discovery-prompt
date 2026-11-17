#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, glob, sys, textwrap

for f in sorted(glob.glob("/tmp/exa1117_*.json")):
    print("="*100)
    print(f)
    try:
        d = json.load(open(f))
    except Exception as e:
        print("ERR", e); continue
    txt = json.dumps(d, ensure_ascii=False)
    # try find text field
    cands = d.get("content") or d.get("results") or d.get("text") or []
    if isinstance(cands, dict):
        cands = [cands]
    def walk(o, depth=0):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("title","url","publishedDate","author","text","summary","highlights") and isinstance(v,(str,list)):
                    s = v if isinstance(v,str) else " | ".join(map(str,v))
                    print(f"  [{k}] {s[:1200]}")
                else:
                    walk(v, depth+1)
        elif isinstance(o, list):
            for v in o[:12]:
                walk(v, depth+1)
    walk(cands)
