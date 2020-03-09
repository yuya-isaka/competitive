# これで大事なところは、どの高さにしたらいいのかってとこに注目して、その高さを全探索していく。でもその高さの上限がint(1e14)だからこれは実行制限エラーになるということで、
# 二部探索していくことを考える。二部探索の仕方も工夫がいる。その高さにした時全ての秒数が可能かどうか調べないといけない。それはO(n)なので十分計算できる。 

def ok(tmpheight):
    checksecond = sorted([(tmpheight - height[i]) // seconds[i] for i in range(n)])  #順番に秒数をオーバーしてないか見るからsortしないと意味ない
    for i in range(n):
        if checksecond[i] < 0 or checksecond[i] < i: # まずそもそも0以下だったら作れないということ
            return False
    return True

n = int(input())
height = [0]*n
seconds = [0]*n
for i in range(n):
    height[i], seconds[i] = map(int, input().split())

left = 0
right = int(1e14)
while left < right: # 二部探索は
    mid = (left + right) // 2

    if ok(mid):
        right = mid
    else:
        left = mid + 1

print(right)