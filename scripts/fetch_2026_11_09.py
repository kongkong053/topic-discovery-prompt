#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, concurrent.futures
QUERIES = [
 ("d1_pay","预付卡 退款 判决 法院 2026年11月 消费者 胜诉","法院判决预付卡退款案例，含金额、法院、日期"),
 ("d1_fmt","格式条款 无效 判决 2026年10月 法院 消费者 违约金","格式条款无效判决，含金额与法院"),
 ("d2_pun","市场监管总局 行政处罚 2026年11月 平台 罚款 公布","平台类行政处罚，罚款金额、主体、日期"),
 ("d3_36kr","site:36kr.com 2026年11月 消费 套路 消费者 钱","36氪消费套路报道，含具体数字"),
 ("d3_dep","36氪 押金 预付 充值 套路 消费者 2026","押金/预付套路深度报道"),
 ("d4_close","2026年 关店 数据 报告 门店 净减少 行业 报告","行业开关店数据报告，含具体数字"),
 ("d5_hei","黑猫投诉 2026年10月 数据 投诉量 行业 排行","黑猫投诉月报，含投诉量数字"),
 ("d7_edu","高校 食堂 审计 违规 收费 2026 公告","高校食堂审计违规公告，含金额"),
]
def run(it):
    k,q,o=it
    out=f"/tmp/exa1109_{k}.json"
    subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
    return k
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(run,QUERIES): print(r)
