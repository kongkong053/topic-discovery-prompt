#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, time, json, os

QUERIES = [
    ("b1", "2026年11月 深圳市市场监督管理局 网络交易监管执法 典型案例 GEO 虚假宣传 处罚 金额",
     "深圳网络交易执法典型案例中GEO虚假宣传、刷单炒信、有奖销售违规的具体案情与罚款金额"),
    ("b2", "2026年11月 12315平台 曝光 案例 处罚 金额 明码标价 虚假宣传 食品 电商",
     "12315平台曝光的典型处罚案例与金额"),
    ("b3", "2026年11月 消协 通报 案例 预付 退款 拖延 金额 培训机构 健身 美容 消费",
     "2026年11月消协通报的预付式消费拖延退款案例与金额"),
    ("b4", "site:36kr.com 2026年11月 预制菜 供应链 出厂价 终端 售价 差价 消费者",
     "36氪2026年11月预制菜供应链成本与终端售价差报道"),
    ("b5", "site:36kr.com 2026年11月 眼镜 眼镜片 成本 售价 验光 暴利 毛利",
     "36氪2026年11月眼镜成本售价与暴利深度报道"),
    ("b6", "2026年11月 宠物 医疗 保险 消费 投诉 套路 保费 赔付 数据",
     "2026年11月宠物医疗/宠物险的套路与数据"),
    ("b7", "2026年 双十一 之后 电商 商家 先涨价 后降价 处罚 罚款 金额 市场监管 2026年11月 典型案例",
     "双十一后先涨价后降价的处罚案例与金额"),
    ("b8", "2026年11月 化妆品 医美 直播 虚假 宣传 处罚 案例 罚款 金额 市场监管",
     "2026年11月化妆品医美直播虚假宣传处罚案例与金额"),
    ("b9", "2026年11月 餐饮 加盟 供应商 设备 绑定 总部 强制 采购 加盟商 成本 调查",
     "餐饮加盟中总部强制设备采购/供应商绑定的机制与成本数据"),
    ("b10", "2026年 婚纱摄影 珠宝 钻戒 定制 差价 成本 供应链 溢价 报道",
     "婚纱摄影与定制珠宝的差价与机制"),
    ("b11", "2026年11月 汽车 4S店 维修 保养 配件 加价 消费者 投诉 数据",
     "2026年11月汽车售后维修配件加价的投诉数据"),
    ("b12", "2026年11月 奶茶 咖啡 加盟 供应商 原料 采购价 总部 抽成 物料 成本 占比",
     "奶茶咖啡加盟中原料采购价与总部抽成的具体数据"),
]

def ok(f):
    try:
        json.load(open(f)); return True
    except Exception:
        return False

for k, q, o in QUERIES:
    out = f"/tmp/exa1117b_{k}.json"
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
