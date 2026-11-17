#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json

QUERIES = [
    ("f1", "虎嗅 4.12万课包一节没上 200万预付款 合法消失 培训 大课包",
     "虎嗅报道中200万预付款如何合法消失的具体机制与数字"),
    ("f2", "绿捷 校园餐 串通投标 陪标 86个项目 3.23亿元 吊销营业执照 上海",
     "绿捷校园餐串标案的具体金额与机制细节"),
    ("f3", "巨量引擎 取消返点 广告代理商 服务商 2026 11月",
     "巨量引擎取消返点对商家广告成本的影响机制与数字"),
    ("f4", "36氪 具身数据采集 40元接单 20元雇人 合格率50% 利润为负",
     "具身数据采集产业链的计价结构与数字"),
    ("f5", "36氪 冷冻贝果 2.9元 开业首日4万 投流 加盟 招商 门店",
     "冷冻贝果加盟商投流依赖与闭店机制数字"),
    ("f6", "2026 会议营销 会销 保健品 老年 免费赠品 健康讲座 处罚 罚没 金额",
     "会议营销/会销模式的具体套路与罚没金额"),
    ("f7", "2026年11月 长三角 违法广告 典型案例 罚款 金额 医疗 保健",
     "长三角违法广告典型案例的具体罚单金额"),
    ("f8", "2026 双十一 电脑 价格 比618还贵 内存 涨价 等到 消费者",
     "双十一电脑涨价与内存涨价的传导数字"),
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
        print("retry", k, attempt); time.sleep(8)
    else:
        print("GIVEUP", k)
    time.sleep(2)
