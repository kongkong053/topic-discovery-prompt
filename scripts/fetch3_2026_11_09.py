#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, sys, pathlib
QUERIES = [
 ("d2_pun2", "市场监管总局 2026年 反垄断 行政处罚 预拌混凝土 协会 价格调整 罚款", "找2026年市场监管总局或省市监局对行业协会统一涨价作出行政处罚的案件，要具体企业数量、涨价幅度、罚款金额、决定书文号和发布日期"),
 ("d1_jc", "机动车检测机构 联营 整合 垄断 判决 最高法 2026 反垄断典型案例", "找最高法2026年反垄断典型案例中涉及机动车检测机构联合定价、整合为两家、某公司要求分配16万元被驳回的案例，要案号、法院、金额、发布日期"),
 ("d1_zuotiao", "免费体验 足疗 充值45万 退款 法院 判决 2026 健康管理公司", "找2026年法院判决免费体验引流、老年人大额充值足疗/养生项目后退款纠纷的案例，要充值金额、判决退费金额、公司股东连带责任、法院和发布日期"),
 ("d1_meirong", "女王形象大使 全年打造计划 诚意金 10960 美容 过敏 判决 2026", "找2026年美容预付合同中约定双方不得终止、诚意金不折现的判决案例，要合同名称、金额、判决结果、法院、发布日期"),
 ("d4_yaodian", "2026年 零售药店 门店 减少 1.55万家 上市连锁 三季报 净增", "找2026年11月报道的全国零售药店门店数量变化和三季报连锁药店开店关店数据，要具体数字、来源媒体和发布日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109c_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout), r.stderr[:200])
