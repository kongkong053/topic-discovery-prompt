#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("d3_g", "36氪 2026年11月 消费者 投诉 套路 曝光 调查 记者 暗访",
     "36氪2026年11月消费者套路暗访调查报道"),
    ("d3_h", "site:36kr.com 2026年11月 会员费 涨价 续费 自动续费 订阅 消费者 权益",
     "36氪2026年11月自动续费/会员涨价消费者权益"),
    ("d5_f", "2026年11月 消协 预付 资金监管 平台 上线 信托 账户 7日无理由 试点 城市",
     "2026年11月各地预付资金监管平台上线与数据"),
    ("d6_f", "2026 海关 判决 走私 案值 亿 消费品 品牌 授权 假货 刑期",
     "2026年海关走私案件量刑与案值"),
    ("d1_e", "2026年11月 法院 判决 押金 退还 平台 条款 无效 消费者 案例",
     "2026年11月法院判决押金退还与格式条款案例"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118c_{k}.json"
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
