#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-08 选题发现并行抓取（维度1+2+5+8）"""
import json, subprocess, concurrent.futures, pathlib

QUERIES = [
    ("d1_ka", "预付卡 概不退费 判决 法院 退还 训练卡 2026年10月", "裁判文书/法院判决原文，含金额、案号、法院、日期"),
    ("d1_xie", "格式条款 无效 判决 违约金 消费者 2026年11月", "法院认定格式条款无效的判决，含金额与法院"),
    ("d2_punish", "市场监管 处罚 2026年10月 预付式消费 违法 案例 公布", "预付式消费违法处罚案例，含罚款金额、主体、日期"),
    ("d2_mid", "平台 佣金 过高 垄断 处罚 2026年10月 罚款", "平台抽佣/垄断处罚，含金额与日期"),
    ("d5_hei", "黑猫投诉 2026年10月 投诉 最多 品牌 退款 拒绝", "黑猫投诉月榜/行业投诉数据，含投诉量数字"),
    ("d5_gym", "健身房 关门 跑路 投诉 退费 2026年10月", "健身房/预付卡跑路投诉案例，含金额"),
    ("d8_yu", "餐饮 外卖 补贴 退潮 亏损 2026年10月 36氪", "餐饮外卖行业亏损/补贴退潮数据"),
    ("d8_cha", "茶饮 咖啡 加盟商 亏损 闭店 2026年10月", "茶饮咖啡加盟商亏损数据"),
]

def run(item):
    key, q, obj = item
    out = pathlib.Path(f"/tmp/exa_{key}.json")
    cmd = ["bash", "/root/topic-discovery-prompt/scripts/exa_fetch.sh", str(out), q, obj]
    subprocess.run(cmd, capture_output=True, timeout=300)
    return key, out.exists(), out.stat().st_size if out.exists() else 0

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(run, QUERIES):
        print(r)
