#!/usr/bin/env python3
import json, subprocess, sys, concurrent.futures

QUERIES = [
 # 维度1 裁判文书网
 ("d1a", "法院 判决 格式条款 无效 消费者 退费 2026年", "找2026年最新法院判决：格式条款无效、预付卡退款、培训退费的判例，带案号金额"),
 ("d1b", "虚假宣传 判决 退一赔三 2026 法院 典型案例", "找2026年法院判决的虚假宣传/欺诈案件，带具体金额和日期"),
 ("d1c", "假冒伪劣 查处 判决 2026 消费", "找2026年假冒伪劣查处案例，带金额"),
 # 维度3 36氪
 ("d3a", "site:36kr.com 预付 跑路 充值 2026", "36氪 2026年预付卡/充值跑路报道，带具体数字"),
 ("d3b", "site:36kr.com 押金 套路 消费者 2026", "36氪 2026年押金套路/消费者坑人报道"),
 ("d3c", "site:36kr.com 暴利 行业 毛利率 2026 消费者", "36氪 2026年暴利行业毛利率拆解"),
 ("d3d", "site:36kr.com 涨价 成本 餐饮 2026 消费者", "36氪 2026年涨价成本报道"),
 # 维度6 海关/贸易
 ("d6a", "海关 查处 案值 走私 2026年 消费品", "2026年海关查处走私/违规案值与税率，带日期"),
 ("d6b", "进口 成本 零售价 差价 2026 关税 消费品", "2026年进口成本与零售价差价、关税成本"),
 ("d6c", "跨境电商 税率 成本 2026年新政", "2026年跨境电商税率与成本变化"),
 # 维度8 行业内幕
 ("d8a", "眼镜 茶叶 婚纱 珠宝 暴利 成本 2026", "2026年行业内幕：暴利结构与成本占比"),
 ("d8b", "茶饮 咖啡 加盟商 亏损 2026 供应链", "2026年茶饮咖啡加盟商与供应链机制"),
 ("d8c", "预制菜 成本 售价 差价 2026 餐饮", "2026年预制菜成本售价差价机制"),
 ("d8d", "美容 牙科 宠物 培训 收费 乱象 2026 投诉", "2026年消费乱象：收费套路与投诉数据"),
]

def run(item):
    key, q, obj = item
    payload = json.dumps({"query": q, "numResults": 8, "objective": obj}, ensure_ascii=False)
    p = subprocess.run(["mcporter","call","exa.web_search_exa","--args",payload,"--output","json"],
                       capture_output=True, text=True, cwd="/root", timeout=240)
    return key, q, p.stdout, p.stderr

out = open("/root/topic-discovery-prompt/_raw_2026-11-04.txt","w",encoding="utf-8")
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for key,q,so,se in ex.map(run, QUERIES):
        out.write("="*80+"\nQUERY[%s]: %s\n"%(key,q)+"-"*80+"\n")
        raw = so.split("---STDERR---")[0]
        try:
            data = json.loads(raw)
            text = data["content"][0]["text"]
            blocks = text.split("\n---\n")
            for b in blocks:
                out.write(b[:3000]+"\n\n")
        except Exception as e:
            out.write("PARSE FAIL %s\n"%e)
            out.write(raw[:2000]+"\n")
        out.write(se[:500]+"\n")
out.close()
print("done")
