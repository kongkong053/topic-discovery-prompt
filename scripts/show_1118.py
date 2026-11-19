#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, glob, sys, re


def walk(obj):
    out = []
    if isinstance(obj, dict):
        if "text" in obj and isinstance(obj["text"], str):
            out.append(obj["text"])
        if "title" in obj and isinstance(obj["title"], str):
            out.append("TITLE: " + obj["title"])
        if "url" in obj and isinstance(obj["url"], str):
            out.append("URL: " + obj["url"])
        if "publishedDate" in obj and obj["publishedDate"]:
            out.append("DATE: " + str(obj["publishedDate"]))
        for v in obj.values():
            out.extend(walk(v))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(walk(v))
    return out


files = sorted(sys.argv[1:]) if len(sys.argv) > 1 else sorted(glob.glob("/tmp/exa1118_*.json"))
for f in files:
    print("=" * 100)
    print("FILE:", f)
    print("=" * 100)
    try:
        d = json.load(open(f))
    except Exception as e:
        print("ERR", e)
        continue
    lines = walk(d)
    seen = set()
    for ln in lines:
        ln = ln.strip()
        if not ln or ln in seen:
            continue
        seen.add(ln)
        print(ln[:1400])
