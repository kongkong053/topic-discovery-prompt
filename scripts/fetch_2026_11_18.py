#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2026-11-18 -> 日期尾号8 -> 实际表: 2/10/18/26 -> 维度1+维度3+维度5+维度6
import subprocess, time, json, os

QUERIES = [
    ("d1_a", "裁判文书 2026 退费 判决 消费者 法院 退还 案例 金额",
     "2026年退费维权类法院判决：金额、法院、判决要点"),
    ("d1_b", "2026 格式条款 无效 法院 判决 霸王条款 消费者 判决 金额",
     "2026年格式条款无效判决案例与金额"),
    ("d1_c", "2026年 虚假宣传 判决 法院 处罚 退一赔三 案例 金额",
     "2026年虚假宣传判决/退一赔三案例金额"),
    ("d3_a", "site:36kr.com 2026年11月 涨价 成本 毛利 消费者 多付",
     "36氪2026年11月关于涨价、成本结构、消费者多付的钱的深度报道"),
    ("d3_b", "site:36kr.com 2026年11月 闭店 亏损 品牌 加盟 预付",
     "36氪2026年11月闭店/亏损/加盟预付深度报道"),
    ("d3_c", "36氪 2026年11月 押金 套路 消费者 行业内幕 佣金 分成 谁赚钱",
     "36氪2026年11月押金套路与产业链分成内幕"),
    ("d5_a", "黑猫投诉 2026年11月 投诉 数据 报告 退款难 占比 增长 行业",
     "黑猫投诉2026年10-11月数据报告：投诉量、增长、集中品类、退款难占比"),
    ("d5_b", "2026年11月 消协 12315 投诉 通报 预付式消费 退费 典型案例 数据",
     "2026年11月消协/12315投诉通报与典型案例数据"),
    ("d5_c", "2026年11月 消费者协会 通报 预付卡 健身房 教培 洗浴 退款 案例 金额",
     "2026年11月消协通报的预付卡行业退费案例与金额"),
    ("d6_a", "2026 海关 走私 查处 案值 万元 起 进口 违规 通报",
     "2026年海关查处走私/违规案例的案值与数量"),
    ("d6_b", "2026 进口 成本 零售价 差价 关税 跨境电商 税率 成本 变化",
     "2026年进口成本与零售价差价、关税税率变化"),
    ("d6_c", "2026年 海关 总署 通报 进口 违规 处罚 金额 奶粉 奢侈品 化妆品",
     "2026年海关查处进口违规商品的金额与品类"),
]


def ok(f):
    try:
        json.load(open(f))
        return True
    except Exception:
        return False


for k, q, o in QUERIES:
    out = f"/tmp/exa1118_{k}.json"
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
