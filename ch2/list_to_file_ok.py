#リスト型のデータをファイルに保存（成功例）
import json

a_list=['バナナ','リンゴ','パイナップル']
with open('a_list.json','w',encoding='utf-8') as fp:
    json_str = json.dumps(a_list, ensure_ascii=False)
    fp.write(json_str)