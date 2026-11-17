#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, glob, re, sys

def show(k):
    p=f"/tmp/exa1110_{k}.json"
    try:
        d=json.load(open(p))
    except Exception as e:
        print("###",k,"PARSE ERR",e); return
    txt=d.get("content",[{}])[0].get("text","") if isinstance(d.get("content"),list) else str(d)
    print("="*70)
    print("###",k,"len",len(txt))
    print(txt[:9000])

for k in sys.argv[1:]:
    show(k)
