#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

URLS = {
 "chip_price":"https://www.36kr.com/p/4054718912107398",
 "ipad_price":"https://eu.36kr.com/zh/p/4066462361621639",
 "phone_shrink":"https://eu.36kr.com/zh/p/4054861669275529",
 "gym_card":"https://news.bjd.com.cn/2026/11/16/12033088.shtml",
 "cqrb_15":"https://www.cqrb.cn/jingji/zixun/2026-11-16/2822477_pc.html",
 "gmw_ai":"https://m.gmw.cn/2026-11/17/content_1304586902.htm",
 "meitong_ai":"https://news.10jqka.com.cn/20261116/c681849704.shtml",
 "pet_ins":"https://zxb.ccn.com.cn/html/zxb/20261102/142971.html",
 "life_battery":"https://news.qq.com/rain/a/20261106A039BP00",
 "shuibei":"https://m.jiemian.com/article/6994792.html",
 "czs_diamond":"http://field.10jqka.com.cn/20261114/c681821073.shtml",
 "jj_zhibao":"https://www.36kr.com/p/3528510058437511",
 "tea_material":"https://jmcy.cn/zhiku/mixue-guming-chabaidao-shangshi-cai-bao-duijue-8f2c",
 "canjie_99":"https://www.canjie.cn/article/663",
 "yuzhi_91":"https://ag.yueniuzq.com/insight/yuzhicai-pricing-bargaining-power/",
 "maoyuanchang":"https://www.36kr.com/p/3758008949342723",
 "shouxihuo":"https://www.36kr.com/p/4062475799499654",
 "caipian":"https://www.thenewslens.com/article/270861",
 "meituan_comm":"https://www.36kr.com/p/1239051011106436",
}

def fetch(u):
    r = subprocess.run(["curl","-sL","--max-time","60","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36","--compressed",u],
                       capture_output=True)
    return r.stdout.decode("utf-8","ignore")

def clean(h):
    h = re.sub(r'<script.*?</script>','',h,flags=re.S|re.I)
    h = re.sub(r'<style.*?</style>','',h,flags=re.S|re.I)
    h = re.sub(r'<[^>]+>',' ',h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+',' ',h)
    h = re.sub(r'\n\s*\n+','\n',h)
    return h

os.makedirs("/tmp/pages1117b",exist_ok=True)
for k,u in URLS.items():
    out=f"/tmp/pages1117b/{k}.txt"
    if os.path.exists(out) and os.path.getsize(out)>500:
        print("skip",k); continue
    t = clean(fetch(u))
    open(out,"w",encoding="utf-8").write(t)
    print(k, len(t))
