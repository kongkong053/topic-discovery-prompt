#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json

QUERIES = [
 ("u1","乌鲁木齐市房地产业协会 垄断协议 处罚 新市监反垄断〔2026〕27号 罚款 金额","乌鲁木齐房协垄断案罚没金额与内容"),
 ("u2","2026中国餐饮业年度报告 连锁化率 闭店 客单价 数据","2026餐饮年报核心数据"),
 ("u3","咖啡陪你 加盟商 2亿 退款 拖欠 2026 陆常青","咖啡陪你欠款详情"),
 ("u4","餐饮 收尸人 二手设备 回收 涨价 2026 设备残值","餐饮二手设备回收市场数据"),
 ("u5","外卖 平台 抽佣 2026 新规 佣金 上限 商家 比例","外卖佣金新规与实际比例"),
 ("u6","高校 食堂 食材成本 占比 60% 四川 新规 解读 承包 净利润率5%","高校食堂新规解读"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k,q,o in QUERIES:
    out=f"/tmp/exa1111b_{k}.json"
    if ok(out):
        print("skip",k); continue
    for attempt in range(3):
        try:
            subprocess.run(["bash","/root/topic-discovery-prompt/scripts/exa_fetch.sh",out,q,o],capture_output=True,timeout=300)
        except Exception as e:
            print("err",k,e)
        if ok(out):
            print("OK",k); break
        print("retry",k,attempt); time.sleep(12)
    else:
        print("GIVEUP",k)
    time.sleep(4)
