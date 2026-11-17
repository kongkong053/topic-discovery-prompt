#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2026-11-12 -> 日期尾号2 -> 维度1+维度3+维度5+维度6
import subprocess, time, json

QUERIES = [
 ("d1_a","法院 判决 退费 预付卡 消费者 2026年11月 格式条款 无效","维度1 退费维权类判决"),
 ("d1_b","法院 判决 虚假宣传 退一赔三 2026年11月 消费者","维度1 欺诈处罚类判决"),
 ("d1_c","霸王条款 隐藏费用 合同 纠纷 判决 2026年10月 11月","维度1 合同猫腻类判决"),
 ("d3_a","site:36kr.com 加盟商 亏损 2026 品牌 闭店","维度3 36氪加盟纠纷"),
 ("d3_b","site:36kr.com 暴利 毛利率 行业 2026 消费","维度3 36氪暴利行业"),
 ("d3_c","site:36kr.com 涨价 成本 2026 会员 订阅 会员费","维度3 36氪涨价成本"),
 ("d3_d","36氪 2026年11月 预付 跑路 充值 押金 套路","维度3 36氪预付跑路"),
 ("d5_a","黑猫投诉 2026年11月 预付卡 退款 投诉量 增长","维度5 消费者投诉数据"),
 ("d5_b","12315 虚假宣传 处罚 2026年 消费者 投诉 热点","维度5 12315数据"),
 ("d5_c","黑猫投诉 2026 双十一 投诉 报告 数据","维度5 双十一投诉"),
 ("d6_a","海关 查处 案值 走私 2026年11月 消费品","维度6 海关走私"),
 ("d6_b","跨境电商 税率 成本 2026年11月 新规 进口","维度6 跨境电商税率"),
 ("d6_c","进口 商品 零售价 差价 关税 2026 消费者","维度6 进口差价"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k,q,o in QUERIES:
    out=f"/tmp/exa1112_{k}.json"
    if ok(out):
        print("skip",k); continue
    for attempt in range(3):
        try:
            subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
        except Exception as e:
            print("err",k,e)
        if ok(out):
            print("OK",k); break
        print("retry",k,attempt); time.sleep(10)
    else:
        print("GIVEUP",k)
    time.sleep(3)
