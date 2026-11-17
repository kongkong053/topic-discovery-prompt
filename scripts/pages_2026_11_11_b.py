#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

URLS = {
 "shouyin":"https://www.21jingji.com/article/20260102/herald/acb7f6d611074e2a4ae7e56737decf88.html",
 "wulumuqi_news":"http://news.10jqka.com.cn/20261109/c681617987.shtml",
 "kafeibeini2":"https://www.gafei.com/kafeibiji-30273",
 "ccfa":"http://www.ccfa.org.cn/portal/cn/xiangxi.jsp?id=447139",
 "chinanews_canyin":"https://www.chinanews.com.cn/cj/2026/09-12/10695387.shtml",
 "haiyang_retry":"https://news.qq.com/rain/a/20260122A03RNL00",
 "huxiu_life":"https://m.huxiu.com/article/4889581.html",
}

def fetch(u):
    r = subprocess.run(["curl","-sL","--max-time","45","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64)","--compressed",u],
                       capture_output=True, text=True)
    return r.stdout

def clean(h):
    h = re.sub(r'<script.*?</script>','',h,flags=re.S|re.I)
    h = re.sub(r'<style.*?</style>','',h,flags=re.S|re.I)
    h = re.sub(r'<[^>]+>',' ',h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+',' ',h)
    h = re.sub(r'\n\s*\n+','\n',h)
    return h

os.makedirs("/tmp/pages1111b",exist_ok=True)
for k,u in URLS.items():
    out=f"/tmp/pages1111b/{k}.txt"
    if os.path.exists(out) and os.path.getsize(out)>500:
        print("skip",k); continue
    t = clean(fetch(u))
    open(out,"w",encoding="utf-8").write(t)
    print(k, len(t))
