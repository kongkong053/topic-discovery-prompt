#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, concurrent.futures
QUERIES = [
 ("d3_dep","36氪 押金 预付 充值 套路 消费者 2026 报道","押金/预付套路深度报道，含具体金额和数字"),
 ("d5_hei","黑猫投诉 2026年10月 投诉 数据 报告 行业 投诉量","黑猫投诉月报/榜单，含投诉量数字"),
 ("d7_edu","高校 食堂 审计 公告 违规 收费 2026","高校食堂审计违规公告，含具体金额"),
 ("d8_food","餐饮 闭店 加盟 2026年11月 报道 36氪 亏","餐饮加盟闭店深度报道，含数字"),
]
def run(it):
    k,q,o=it
    out=f"/tmp/exa1109b_{k}.json"
    subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
    return k
for it in QUERIES:
    print(run(it)); time.sleep(12)
