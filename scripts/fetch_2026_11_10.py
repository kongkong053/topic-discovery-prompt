#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2026-11-10 (尾号10 → 维度1+维度3+维度5+维度6)
import subprocess, concurrent.futures

QUERIES = [
 ("d1_a","预付卡 退款 判决 法院 2026年11月 消费者 胜诉 霸王条款","法院判决预付卡退费/格式条款无效案例，含金额、法院、日期"),
 ("d1_b","格式条款 无效 判决 2026年10月 法院 消费者 违约金 培训","格式条款无效判决，含金额与法院"),
 ("d1_c","解除 合同 退款 判决 2026 法院 消费者 预付费","合同解除退款判决，含具体数字"),
 ("d3_a","site:36kr.com 2026年11月 涨价 成本 餐饮 毛利","36氪餐饮成本结构报道"),
 ("d3_b","site:36kr.com 押金 预付 充值 跑路 2026","36氪预付/押金套路深度报道"),
 ("d3_c","site:36kr.com 加盟 坑 纠纷 2026 亏损","36氪加盟商纠纷报道"),
 ("d5_a","黑猫投诉 2026年10月 投诉量 排行 行业 数据","黑猫投诉月报数据"),
 ("d5_b","12315 投诉 虚假宣传 2026 典型案例 罚款","消协/12315典型案例"),
 ("d5_c","预付卡 健身房 关门 投诉 退款 2026年10月","健身房/预付卡投诉"),
 ("d6_a","海关 2026年10月 查处 案值 走私 进口","海关查处通报，含案值"),
 ("d6_b","进口 成本 零售价 差价 关税 2026年11月","进口商品成本与零售价差，含数字"),
 ("d6_c","跨境电商 税率 成本 2026年10月 海关","跨境电商税率与成本变化"),
]

def run(it):
    k,q,o=it
    out=f"/tmp/exa1110_{k}.json"
    try:
        subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
    except Exception as e:
        print(k,"ERR",e)
    return k

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        for r in ex.map(run,QUERIES): print(r)
