#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, json, pathlib
QUERIES = [
 ("d3_c", "医美耗材价格暴跌 华熙生物 巨子生物 爱美客 玻尿酸 出厂价 2026年11月 36氪", "找2026年11月医美耗材（玻尿酸/胶原蛋白）价格暴跌的具体数据：出厂价、终端售价、机构成本占比、降价幅度、企业营收、发布日期"),
 ("d4_c", "2026年 便利店 母婴 美妆 门店 关闭 净减少 数据 窄门餐眼 2026年10月", "找2026年10-11月便利店、母婴、美妆、宠物等非餐饮零售门店关闭的最新数据，要具体门店数、净减数、时间区间、监测机构"),
 ("d1_e", "2026年11月 法院 判决 消费者 预付 退款 格式条款 典型案例 中国消费者报", "找2026年10-11月法院判决的消费者维权新案例（预付、加盟、培训、直播、老年消费），要具体金额、法院、判决要点、发布日期"),
 ("d2_e", "紫竹医药 转售价格 1264.36万元 罚款 2023年 北京市场监管局 避孕药 价格 限制 转售", "找紫竹医药案（北京市场监管局2023年处罚，2022修正反垄断法）的完整细节：产品名、经销商数量、价格限制方式、罚款金额、判决/处罚日期"),
]
for tag, q, obj in QUERIES:
    out = f"/tmp/exa1109f_{tag}.json"
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    r = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root")
    pathlib.Path(out).write_text(r.stdout + r.stderr, encoding="utf-8")
    print(tag, len(r.stdout))
