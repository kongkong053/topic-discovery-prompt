#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, glob, re

def show(pattern, limit=1400):
    for f in sorted(glob.glob(pattern)):
        print("="*100); print(f)
        try: d = json.load(open(f))
        except Exception as e:
            print("ERR", e); continue
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k in ("title","url","publishedDate","text","highlights") and isinstance(v,(str,list)):
                        s = v if isinstance(v,str) else "\n".join(map(str,v))
                        s = re.sub(r'\n-{3,}.*','',s)
                        print(f"  [{k}] {s[:limit]}")
                    else:
                        walk(v)
            elif isinstance(o, list):
                for v in o[:10]: walk(v)
        walk(d)

show("/tmp/exa1117b_*.json")
