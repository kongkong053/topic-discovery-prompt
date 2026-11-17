#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, pathlib
QUERIES = [
 ("d2_f", "宿迁市商品混凝土行业协会 17家 企业 垄断协议 处罚 涨价 幅度 混凝土价格 上涨", "找宿迁市商品混凝土行业协会组织17家混凝土企业垄断协议的处罚细节：涨价幅度、涨价次数、处罚金额、违法所得、市场份额、2026年2月处罚细节"),
 ("d1_g", "机动车检测 联营垄断 四家检测机构 合并 收费标准 上涨 车检费用 消费者 多付 多少钱", "找机动车检测机构整合联营垄断案对车主检测费用的实际影响：检测费上涨幅度、当地检测费水平、消费者多付金额、案件具体数据"),
 ("d3_e", "2026年11月 36氪 医美 机构 获客 成本 低价引流 升单率 12% 童颜针 成本 千元", "找2026年医美行业具体案例：某机构的具体收费与成本、消费者实际花费、获客成本、升单率、具体产品名称与价格"),
 ("d4_e", "康巴赫 关店14家 珠宝 门店 关闭 潮玩星球 148家 缩减 99家 2026 谷子店", "找2026年珠宝/潮玩/二次元门店关闭的具体数据：品牌、门店数变化、时间、监测机构、发布日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109h_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout))
