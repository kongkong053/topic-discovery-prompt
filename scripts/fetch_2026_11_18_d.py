#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("d5_g", "深圳 市场监管 网络交易 执法 典型案例 2026年9月21日 GEO 虚假宣传 刷单 价格欺诈 罚款 金额",
     "深圳市监局2026-09-21网络交易典型案例各案罚款金额"),
    ("d1_f", "2026年 法院 判例 预付卡 押金 退还 金额 消费者 维权 典型案例 发布 2026年11月",
     "2026年法院发布的预付卡/押金退还典型案例与金额"),
    ("d6_g", "2026年11月 进口 税 调整 新政 生效 中国 消费者 终端价格 影响 数据",
     "2026年11月生效的进口税调整对终端价格影响"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118d_{k}.json"
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
