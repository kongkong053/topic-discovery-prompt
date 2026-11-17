#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
 ("d1_a","预付卡 退款 判决 法院 2026年11月 消费者 胜诉 霸王条款","法院判决预付卡退费/格式条款无效案例，含金额、法院、日期"),
 ("d1_b","格式条款 无效 判决 2026年10月 法院 消费者 违约金 培训","格式条款无效判决，含金额与法院"),
 ("d1_c","解除合同 退款 判决 法院 消费者 2026年 新规 预付费","合同解除退款判决，含具体数字"),
 ("d3_b","site:36kr.com 押金 预付 充值 跑路 2026","36氪预付/押金套路深度报道"),
 ("d3_c","site:36kr.com 加盟 坑 纠纷 2026 亏损 闭店","36氪加盟商纠纷报道"),
 ("d5_a","黑猫投诉 2026年10月 投诉量 排行 行业 数据","黑猫投诉月报数据"),
 ("d5_b","12315 消协 虚假宣传 典型案例 2026年10月 罚款","消协/12315典型案例"),
 ("d6_a","海关 查处 2026年10月 案值 走私 进口 通报","海关查处通报，含案值"),
 ("d6_c","跨境电商 税率 成本 2026年10月 海关 新规","跨境电商税率与成本变化"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k,q,o in QUERIES:
    out=f"/tmp/exa1110_{k}.json"
    if ok(out):
        print("skip",k); continue
    for attempt in range(4):
        subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
        if ok(out):
            print("OK",k); break
        print("retry",k,attempt); time.sleep(20)
    else:
        print("GIVEUP",k)
    time.sleep(8)
