#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

URLS = {
 "sz_typical":"https://sf.sz.gov.cn/ztzl/hg/yjxx/zdly/ggyx/content/post_13048817.html",
 "bj_food_ad":"https://scjgj.beijing.gov.cn/zwxx/scjgdt/202611/t20261111_4941343.html",
 "coffee_map":"https://www.36kr.com/p/4056129698993285",
 "luxury_gold":"https://www.21jingji.com/article/20261116/herald/7468021f8fc69b7b83918a68d10928a5.html",
 "yoga_hn":"http://hn315.net.cn/web_newones.asp?id=21772",
 "tea_chat":"https://www.drinknewspaper.com/news/10546.html",
 "heimao_ecom":"https://tousu.xincai.com/articles/view/443108/",
 "samr_shuang11":"https://www.samr.gov.cn/xw/zj/art/2026/art_c79205935e4b4ef889a85c60a32cd304.html",
 "samr_wulumuqi":"https://www.samr.gov.cn/fldys/sjdt/gzdt/art/2026/art_96052e1af180455595d473b6dea1687b.html",
 "yuzhixiang":"https://ag.yueniuzq.com/insight/yuzhicai-jiage-chuandao-yijia-nengli/",
 "pingdingshan":"https://www.guangzhou315.com/html/web/anlifenxi/2117167210512236545.html",
 "luckin_lucky":"https://www.36kr.com/p/4056473489560457",
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

os.makedirs("/tmp/pages1117",exist_ok=True)
for k,u in URLS.items():
    out=f"/tmp/pages1117/{k}.txt"
    if os.path.exists(out) and os.path.getsize(out)>500:
        print("skip",k); continue
    t = clean(fetch(u))
    open(out,"w",encoding="utf-8").write(t)
    print(k, len(t))
