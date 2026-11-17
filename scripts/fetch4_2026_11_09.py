#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, pathlib
QUERIES = [
 ("d2_a", "2026年 市场监管 处罚 平台 佣金 抽成 罚款 互联网平台 滥用市场支配地位", "找2026年针对互联网平台/大型企业滥用支配地位、捆绑收费、限制竞争的行政处罚，要具体金额、当事人、日期"),
 ("d2_b", "2026年 反垄断 行政处罚 联合定价 转售价格维持 固定价格 处罚决定 2026年10月 11月", "找2026年10-11月公布的反垄断行政处罚案件，尤其是价格类、限制交易类，要企业数量、罚款金额、日期、文号"),
 ("d4_a", "窄门餐眼 2026年 10月 餐饮 闭店率 净关店 万家 数据", "找2026年最新餐饮/零售门店闭店数据，要具体门店数、闭店率、时间区间"),
 ("d3_a", "site:36kr.com 2026年11月 成本 售价 暴利 套路 消费者 维权", "找2026年11月36氪关于消费陷阱、成本结构、维权套路的深度报道，要具体金额、案例、发布日期"),
 ("d5_a", "2026年 消协 通报 投诉 热点 预付式消费 直播带货 老年人 典型案例", "找2026年10-11月中消协/黑猫/消保委发布的消费维权典型案例，要具体金额、套路、日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109d_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout))
