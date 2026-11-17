#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json

# 2026-11-11 -> 日期尾号1 -> 维度1+2+3+4? 检查规则: 11 -> 3、11、19、27 -> 维度2+维度4+维度7+维度8
QUERIES = [
 ("d2_a","市场监管总局 垄断协议 行政处罚决定书 2026年11月 罚款 滥用市场支配地位","反垄断处罚决定书，含罚没金额与案由"),
 ("d2_b","平台 二选一 处罚 2026年 双十一 合规提示 先涨价后降价","平台监管处罚与双十一合规"),
 ("d2_c","不正当竞争 处罚 罚款 2026年10月 假冒 虚假宣传 市场监管","不正当竞争处罚案例"),
 ("d4_a","窄门餐眼 闭店率 2026 净关店 万家 餐饮 数据","闭店率与净关店数据"),
 ("d4_b","零售 闭店 数据 2026 联商网 便利店 净增","零售门店开关店数据"),
 ("d7_a","高校 食堂 审计 违规 收费 2026 公告","高校食堂审计公告"),
 ("d7_b","大学 食堂 食材成本 毛利率 审计 2026 外包 违规","高校食堂成本审计"),
 ("d8_a","茶饮 咖啡 闭店 加盟商 2026年10月 亏损","茶饮咖啡加盟商亏损数据"),
 ("d8_b","餐饮 外卖 补贴 退潮 亏损 2026年11月 闭店","餐饮外卖亏损"),
 ("d8_c","预制菜 成本 售价 差价 2026年11月 暴利","预制菜与行业暴利"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k,q,o in QUERIES:
    out=f"/tmp/exa1111_{k}.json"
    if ok(out):
        print("skip",k); continue
    for attempt in range(3):
        try:
            subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
        except Exception as e:
            print("err",k,e)
        if ok(out):
            print("OK",k); break
        print("retry",k,attempt); time.sleep(15)
    else:
        print("GIVEUP",k)
    time.sleep(5)
