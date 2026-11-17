#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess, re, html, os

URLS = {
 "gz_shuang11":"https://www.gzns.gov.cn/gznsscjg/gkmlpt/content/11/11081/post_11081332.html",
 "beijing_shuang11":"https://scjgj.beijing.gov.cn/zwxx/scjgdt/202611/t20261106_4934851.html",
 "samr_shuang11":"https://www.samr.gov.cn/xw/mtjj/art/2026/art_83424c33ba3c45848a3ce2458f7f6668.html",
 "samr_shipin":"https://www.samr.gov.cn/xw/sj/art/2026/art_b7ab9755b9804087acc79fd6d7344d00.html",
 "samr_wulumuqi":"https://www.samr.gov.cn/fldys/sjdt/gzdt/art/2026/art_96052e1af180455595d473b6dea1687b.html",
 "21jingji_bake":"https://m.21jingji.com/article/20260630/herald/77f07c8db84307ebcb8c61f3686ad6fb.html",
 "eastmoney_chaye":"https://finance.eastmoney.com/a/202609053866004758.html",
 "xicha_songxue":"https://news.qq.com/rain/a/20261014A05S7200",
 "canxiaohe":"https://canxiaohe.com/11295.html",
 "chinahotel":"https://www.chinahotel.org.cn/articles/18042",
 "xynu_audit":"http://sjc.xynu.edu.cn/info/1016/5032.htm",
 "dzwww_chunxue":"https://www.dzwww.com/xinwen/jjxw/202611/t20261105_18275207.htm",
 "kafei_gafei":"https://www.gafei.com/kafeibiji-30273",
 "huxiu_waiMai":"https://m.huxiu.com/article/4833891.html",
}

def fetch(u):
    r = subprocess.run(["curl","-sL","--max-time","50","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36","--compressed",u],
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

os.makedirs("/tmp/p1111c",exist_ok=True)
for k,u in URLS.items():
    out=f"/tmp/p1111c/{k}.txt"
    if os.path.exists(out) and os.path.getsize(out)>800:
        print("skip",k); continue
    t = clean(fetch(u))
    open(out,"w",encoding="utf-8").write(t)
    print(k, len(t))
