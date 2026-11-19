#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("d2_i", "深圳 市场监管 2026年9月21日 GEO服务 虚假宣传 案 罚款 金额 网络交易 典型案例",
     "深圳GEO服务虚假宣传案与网络刷单案的具体罚款金额"),
    ("d8_i", "2026年 预制菜 强制性国家标准 征求意见 防腐剂 保质期 12个月 商务部 2026",
     "预制菜新国标强制内容与实施时间"),
    ("d5_g", "2026年11月 AI数字人主播 直播带货 标识 处罚 罚款 金额 虚假宣传",
     "AI数字人直播带货未标识的处罚案例与金额"),
    ("d5_h", "2026年11月 预付卡 跑路 退费 法院 判例 金额 消费者 体育 健身 教培",
     "2026年11月预付卡跑路维权新案例与金额"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118f_{k}.json"
    if ok(out):
        print("skip", k)
        continue
    for attempt in range(3):
        try:
            subprocess.run(["bash", "/root/topic-discovery-prompt/scripts/exa_fetch.sh", out, q, o],
                           capture_output=True, timeout=300)
        except Exception as e:
            print("err", k, e)
        if ok(out):
            print("OK", k)
            break
        print("retry", k, attempt)
        time.sleep(8)
    else:
        print("GIVEUP", k)
    time.sleep(1)
