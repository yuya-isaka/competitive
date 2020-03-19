# maspyさん参考
# https://atcoder.jp/contests/joi2015ho/submissions/8528395
# こんな風にnumpy使いこなしたい

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
A = np.array(read().split(),np.int64)

# 2周もつ
# 円環を解く時こうするとわかりやすいとスライドで言ってた
# concatenateは連結という意味で，numpy配列をがったああああああいできる．
A = np.concatenate([A,A])

# 残サイズごとに
dp = np.zeros(N,np.int64) 
for n in range(1,N+1):
    dp = np.append(dp,dp[0]) # 毎回後ろに最初の配列を追加する（これで円環を表現している？）
    player = (N - n) & 1 # 偶奇（こういう風にもかけるんだね〜）　例えば全体の数が８でnが２だったら6になるので，ビットは立ってない．だから0になる．
    # 以下はスライドの紹介の通り（numpy使いこなしてる）
    if player == 0:
        # JOI君
        left = dp[1:N+1] + A[:N]
        right = dp[:N] + A[n-1:N+n-1]
        dp = np.maximum(left,right)
    else:
        # IOIちゃん
        dp = np.where(A[:N] > A[n-1:N+n-1], dp[1:N+1], dp[:N])

answer = dp.max()
print(answer)
