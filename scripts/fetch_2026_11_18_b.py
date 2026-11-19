#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("d3_d", "site:36kr.com 2026年11月 会员 订阅 续费 涨价 消费者 多付 隐形 收费",
     "36氪2026年11月会员订阅/续费/隐形收费"),
    ("d3_e", "site:36kr.com 2026年11月 茶饮 咖啡 餐饮 供应链 差价 分成 加盟商 亏",
     "36氪2026年11月餐饮供应链差价与加盟商亏损"),
    ("d3_f", "36氪 2026年11月 二手 回收 翻新 以旧换新 套路 价差 报告",
     "36氪2026年11月以旧换新/回收翻新套路"),
    ("d5_d", "2026年11月 消协 通报 直播 带货 虚假宣传 处罚 典型案例 罚款 金额",
     "2026年11月消协通报直播带货典型案例与罚款"),
    ("d5_e", "2026年11月 12315 曝光 押金 退还 平台 扣费 案例 金额 媒体调查",
     "2026年11月押金退还难媒体调查案例与金额"),
    ("d6_d", "2026 海关 处罚 决定书 跨境电商 伪报 逃税 税款 金额 玩具 化妆品",
     "2026年海关跨境电商伪报逃税处罚决定书金额"),
    ("d6_e", "2026年11月 进口 关税 调整 国家 税率 上调 消费 影响 数据",
     "2026年11月各国进口关税调整与对消费端影响"),
    ("d1_d", "2026年11月 法院 判决 消费者 欺诈 三倍赔偿 直播 预付 新案例 金额",
     "2026年11月法院判决消费欺诈三倍赔偿新案例"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118b_{k}.json"
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
