#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, pathlib
QUERIES = [
 ("d2_c", "2026年10月 11月 市场监管 行政处罚 公示 滥用市场支配地位 限定交易 转售价格 罚没", "找2026年10-11月新公布的市场监管行政处罚案件，尤其是价格限制、二选一、限定交易类，要企业数量、金额、日期、文号"),
 ("d3_b", "site:36kr.com 2026年11月 消费者 套路 维权 成本 陷阱 调查 记者", "找2026年11月36氪关于消费者被套路的具体调查报道，要具体人物、金额、平台、日期"),
 ("d4_b", "2026年11月 便利店 烘焙 咖啡 门店 关闭 数据 报告 净减少", "找2026年10-11月零售/餐饮门店关闭的最新数据，尤其非餐饮品类（便利店、烘焙、美妆、母婴），要具体数字、监测机构、日期"),
 ("d2_d", "2026年 反垄断 处罚 水泥 混凝土 联合销售 配额 最高法 典型案例 六 孔某", "找最高法2026年反垄断典型案例六涉及水泥混凝土企业联合销售、配额制定向销售、高交低补的案件，要企业数、罚款金额、刑事罚金、日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109e_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout))
