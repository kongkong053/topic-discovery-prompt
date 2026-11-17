#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json

QUERIES = [
    ("e2_a", "2026年11月 市场监管 虚假宣传 处罚 典型案例 金额 万元 预付式消费 养老",
     "2026年11月新公布的处罚案例，案由、罚款金额、违法所得"),
    ("e2_b", "2026年 双十一 平台 先涨价后降价 处罚 罚款 案例 电商 价格欺诈 查处",
     "双十一价格欺诈实际处罚案例与罚单金额"),
    ("e2_c", "2026年 反垄断 罚没 总额 行业协会 组织 统一定价 猪肉 蔬菜 生鲜 配送 罚单",
     "2026年生鲜/配送/零售领域行业协会组织垄断处罚案例"),
    ("e5_a", "2026年11月 消协 通报 预付式消费 卷款跑路 烘焙 教培 餐饮 案例 数据",
     "2026年11月各地消协预付式消费通报中的具体案例与数字"),
    ("e5_b", "2026年 双十一 消费者 投诉 退货 预售 定金 不退 平台 规则 数据 退款难",
     "双十一预售定金不退/退款难的规则与数据"),
    ("e7_a", "2026年 高校 食堂 承包 招标 违规 审计 通报 金额 学校 学生 餐费 返还",
     "2026年高校食堂违规收费/返点具体金额通报"),
    ("e7_b", "2026年 大学 采购 食堂 设备 中标 金额 异常 低价 审计 质疑 公告",
     "高校食堂设备采购中标金额异常的具体案例数字"),
    ("e3_a", "site:36kr.com 2026年11月 会员 涨价 订阅 涨价 通知 用户 权益",
     "36氪2026年11月关于会员涨价/订阅涨价的报道"),
    ("e3_b", "site:36kr.com 2026年11月 佣金 分成 抽成 商家 平台 比例 新规",
     "36氪2026年11月关于平台抽佣/佣金/分成的报道"),
    ("e3_c", "36氪 2026年11月 预付 跑路 押金 投诉 商家 卷款 消费者",
     "36氪2026年11月预付/押金/跑路的深度报道"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k, q, o in QUERIES:
    out = f"/tmp/exa1113_{k}.json"
    if ok(out):
        print("skip", k); continue
    for attempt in range(3):
        try:
            subprocess.run(["bash", "/root/topic-discovery-prompt/scripts/exa_fetch.sh", out, q, o],
                           capture_output=True, timeout=300)
        except Exception as e:
            print("err", k, e)
        if ok(out):
            print("OK", k); break
        print("retry", k, attempt); time.sleep(10)
    else:
        print("GIVEUP", k)
    time.sleep(2)
