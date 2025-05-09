import json, graphviz, sys

#JSONファイルを指定
json_file = 'family-tokugawa.json'

#ただし引数があればそのファルを読み込む
if len(sys.argv) >= 2:
    json_file = sys.argv[1]
with open(json_file, encoding='utf-8') as fp:
    family_data = json.load(fp)

#Graphvizの利用開始
g =graphviz.Graph('family', format='svg', filename=json_file+'_s')
g.attr(rankdir='LR') #横向きの図にする

#一世代ずつノードをつなげていく
for f in family_data:
    father = f['parents'][0] #父
    mother = f['parents'][1] if len(f['parents']) >=2 else '' #母
    children = f['children'] #子
    #「父 → ポイント → 母」のノードを作る
    g.node(father, style='filled', fillcolor='#f0f0ff', shape="box")
    fa_mo = father + '_' + mother # 父と母をつなげるポイントを用意
    g.node(fa_mo, shape='point')
    g.edge(father,fa_mo,'父', dir = 'none')
    if mother != '': # 母が明らかであれば父とつなげる
        g.node(mother, style='filled', fillcolor='#fff0e0')
        g.edge(fa_mo, mother, '母', dir='none')
    #子どもたちの処理
    for child in children:
        g.node(child,style='filled', fillcolor='#f0f0ff', shape="box")
        g.edge(fa_mo,child,'子',dir='forward')
#出力と表示
g.view()