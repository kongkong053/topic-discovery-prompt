#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, pathlib
QUERIES = [
 ("d1_f", "最高法 2026年 反垄断典型案例 六 机动车检测 农产品批发 具体案情 判决 金额", "找最高法2026年9月10日发布的6件反垄断典型案例中涉及机动车检测、农产品批发、水泥混凝土的具体案情：违法主体数量、行为方式、罚金/罚款金额、消费者承担的价格后果、案件来源"),
 ("d3_d", "site:36kr.com 2026年11月 记者 调查 消费者 套路 保证金 隐性收费 中介 维权", "找2026年11月36氪关于消费者隐性成本/套路的具体调查报道，需要具体人物、金额、环节、日期"),
 ("d4_d", "2026年10月 11月 服装 珠宝 宠物 门店 关闭 数据 报告 净减少 万家", "找2026年10-11月非餐饮零售（服装/珠宝/宠物/美妆/3C）门店关闭数据：净减少门店数、闭店率、监测机构、发布日期"),
 ("d5_b", "2026年11月 黑猫投诉 预付 押金 退款 投诉量 增长 数据 平台 报告", "找2026年10-11月黑猫投诉或其他平台最新投诉数据：涉及预付卡/押金/教育培训的投诉量、增长率、典型金额、发布日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109g_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout))
