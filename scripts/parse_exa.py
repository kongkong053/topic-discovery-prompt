import json, sys, re
for path in sys.argv[1:]:
    print("="*80)
    print("FILE:", path)
    raw = open(path, encoding="utf-8").read()
    raw = raw.split("---STDERR---")[0]
    try:
        data = json.loads(raw)
        text = data["content"][0]["text"]
    except Exception as e:
        print("PARSE FAIL", e)
        print(raw[:2000])
        continue
    # split into blocks by Title:
    blocks = re.split(r"\n(?=Title: )", text)
    for b in blocks:
        m = re.match(r"Title: (.*?)\nURL: (.*?)\nPublished: (.*?)\n", b, re.S)
        if not m:
            continue
        title, url, pub = m.groups()
        print("-"*70)
        print("TITLE:", title)
        print("URL:", url)
        print("PUB:", pub)
        body = b[m.end():]
        print(body[:2600])
