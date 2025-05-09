#リスト型のデータをファイルに保存しようとして失敗している例
a_list=['バナナ','リンゴ','パイナップル']
with open('error.json','w', encoding='utf-8') as fp:
    fp.write(a_list)
    
