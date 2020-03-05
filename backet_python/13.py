import numpy as np 
n, m = map(int, input().split()) #行と列の数
a = [list(map(int, input().split())) for _ in range(n)] #お煎餅二次元配列
a = np.array(a)

ans = 0
for i in range(1 << n):
    tmp = np.array([[i >> j & 1 for j in range(n)]]).T #二次元配列じゃないと転置できないと言うか意味ないみたい
    x = np.sum(a ^ tmp, axis=0) #排他的論理和で逆になるの使う

    ans = max(ans, np.sum(np.maximum(x, n-x))) #maximumが改めて便利　ここでもブロードキャストしてる

print(ans)
