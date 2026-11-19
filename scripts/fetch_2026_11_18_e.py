#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("d2_g", "2026年11月 市场监管 处罚 平台 大数据 杀熟 二选一 罚款 万元 公告",
     "2026年11月平台经济领域监管处罚金额与案件类型"),
    ("d2_h", "2026年11月 反垄断 处罚 罚款 金额 经营者集中 罚没",
     "2026年11月反垄断处罚案件与罚款金额"),
    ("d8_g", "2026年 餐饮 加盟商 亏损 闭店 品牌 供应链 赚钱 36氪 2026年11月",
     "2026年11月餐饮加盟商成本结构与品牌抽成机制"),
    ("d8_h", "2026年 预制菜 成本 售价 差价 餐饮 供应商 毛利率",
     "2026年预制菜成本售价差价与供应商毛利率"),
    ("d5_f", "2026年11月 黑猫投诉 预付卡 退款 餐饮 酒店 旅游 投诉量 数据",
     "2026年11月消费者投诉热点与预付卡投诉量数据"),
    ("d1_g", "2026年11月 法院 判决 格式条款 霸王条款 消费者 赔偿 金额 典型",
     "2026年11月法院判格式条款无效的典型案例与金额"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118e_{k}.json"
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
