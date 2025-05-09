import json
#表示したいデータ
data = {"名前": "スズキ", "趣味": ["釣り","宝探し","プログラミング"]}
#わかりやすく表示
print(json.dumps(
    data,
    indent=4,
    ensure_ascii=False
))

