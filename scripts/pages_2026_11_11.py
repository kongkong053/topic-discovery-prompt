#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os, json

URLS = {
 "wulumuqi":"https://www.samr.gov.cn/fldys/sjdt/gzdt/art/2026/art_96052e1af180455595d473b6dea1687b.html",
 "kafeibeini":"https://m.gafei.com/views-31469",
 "huiyang":"https://news.qq.com/rain/a/20260122A03RNL00",
 "sichuan_canteen":"https://cbgc.scol.com.cn/news/8038182",
 "chabaidao":"https://www.huxiu.com/article/4899137.html",
 "xicha":"https://news.qq.com/rain/a/20261014A05S7200",
 "nansha":"https://www.gzns.gov.cn/gznsscjg/gkmlpt/content/11/11081/post_11081332.html",
 "samr_1111":"https://www.samr.gov.cn/xw/mtjj/art/2026/art_83424c33ba3c45848a3ce2458f7f6668.html",
 "canyin2026":"https://www.chinahotel.org.cn/articles/18042",
 "fenzhong":"https://www.samr.gov.cn/fldys/tzgg/index.html",
 "tmtpost":"https://www.tmtpost.com/8199206.html",
 "gafei_coffee":"https://www.gafei.com/kafeibiji-149248",
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

os.makedirs("/tmp/pages1111",exist_ok=True)
for k,u in URLS.items():
    out=f"/tmp/pages1111/{k}.txt"
    if os.path.exists(out) and os.path.getsize(out)>500:
        print("skip",k); continue
    h = fetch(u)
    t = clean(h)
    open(out,"w",encoding="utf-8").write(t)
    print(k, len(h), len(t))
