#!/usr/bin/env python3
import json, subprocess, concurrent.futures

QUERIES = [
 # 维度2 监管/反垄断处罚
 ("d2a", "市场监管总局 行政处罚 2026年10月 罚没 万元 平台", "2026年10-11月市场监管处罚公告，带罚没金额、日期、当事人"),
 ("d2b", "反垄断 处罚 2026 滥用市场支配地位 罚款 金额", "2026年反垄断滥用支配地位/垄断协议处罚案，带金额与日期"),
 ("d2c", "平台 佣金 收费 处罚 2026 外卖 电商 二选一", "2026年平台佣金/二选一处罚，带金额"),
 # 维度5 消费者投诉
 ("d5a", "黑猫投诉 2026年10月 预付卡 退款 投诉量", "2026年10月黑猫投诉预付卡退款类投诉数据"),
 ("d5b", "12315 2026 消费维权 典型案例 虚假宣传 处罚", "2026年12315/消协典型案例，带金额"),
 ("d5c", "培训机构 健身房 关门 退费 2026年10月 报道", "2026年10月预付卡跑路退费报道，带具体金额"),
 # 维度7 高校后勤/食堂审计
 ("d7a", "高校 食堂 审计公告 2026 违规 收费 金额", "2026年高校食堂/后勤审计公告，带违规金额与文号"),
 ("d7b", "大学食堂 承包 毛利率 违规 2026 通报", "2026年高校食堂承包违规通报，带金额"),
 ("d7c", "高校 采购 食堂 违规 审计署 2026", "2026年高校采购/食堂违规审计，带金额"),
 # 维度3 36氪
 ("d3a", "site:36kr.com 2026 闭店 亏损 品牌 加盟", "36氪 2026年品牌闭店亏损报道，带数字"),
 ("d3b", "site:36kr.com 2026 预付 跑路 充值 套路", "36氪 2026年预付卡跑路报道"),
 ("d3c", "site:36kr.com 2026 涨价 成本 毛利 消费者", "36氪 2026年成本毛利拆解"),
]

def run(item):
    key, q, obj = item
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    p = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root", timeout=300)
    return key, q, p.stdout, p.stderr

out = open("/root/topic-discovery-prompt/_raw_2026-11-05.txt","w",encoding="utf-8")
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for key,q,so,se in ex.map(run, QUERIES):
        out.write("="*80+"\nQUERY[%s]: %s\n"%(key,q)+"-"*80+"\n")
        raw = so.split("---STDERR---")[0]
        try:
            data = json.loads(raw)
            text = data["content"][0]["text"]
            for b in text.split("\n---\n"):
                out.write(b[:3000]+"\n\n")
        except Exception as e:
            out.write("PARSE FAIL %s\n"%e)
            out.write(raw[:1500]+"\n")
        out.write(se[:300]+"\n")
out.close()
print("done")
