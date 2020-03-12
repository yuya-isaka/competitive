n = int(input())
g = [input().split()[2:] for _ in range(n)]

from collections import deque
que = deque()
que.append(0)
d = [0] + [-1] * n

while que:
    u = que.popleft()

    for v in g[u]:
        v = int(v) - 1

        if d[v] < 0:
            d[v] = d[u] + 1
            que.append(v)

for i in range(n):
    print(i+1, d[i])

"""
・グラフの数を受け取る
・グラフを作る．今回は隣接リストで必要な部分だけを残してリスト化する
・キュー用の配列を作る（これはなんでもいい．普通のリストでも可）．そのキューには1番初めのスタート位置を入れておく
・最短距離を置いておくリストを用意
・queの中身がなくなるまで続ける
・queの中身を取り出して，それにくっついてるノードを全て舐めていく．int方で入力を受け取っていないから注意．1-indexを0-indexに変える．
・もしそこにまだBFSが訪れていなかったら，そこに前回の場所から1足した物を代入
・探索用のqueに追加しておく．追加しておくことでまたそのノードとつながってるところを調べることができる
・最後は出力．全てのノードの最短距離を出力
"""
