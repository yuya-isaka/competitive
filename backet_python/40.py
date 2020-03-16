"""
2個入力ループこんな書き方もあるんだな．

dp[この日+1日まで決まっている][iにこのパスタを選んだ時][i+1にこのパスタを選んだ時]
0は何も選んでない状態と考える

今日あるパスタを選んだ時の場合の数は，2日前に選んだパスタと昨日に選んだパスタの組み合わせの数．
あとは3日連続同じパスタの場合と，すでにパスタが予定されていた場合で条件分けしたらいいのか．
"""
N, K = map(int, input().split())
source = [0] * (N+1)
for x, y in (map(int, input().split()) for _ in range(K)):
    source[x] = y

mod = 10000

dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]
dp[0][0][0] = 1
ans = 0
for i in range(1, N+1):
    for j in range(0, 4):
        for k in range(0, 4):
            for l in range(1, 4):
                if (source[i] > 0 and source[i] != l) or (j == k and k == l):
                        continue
                dp[i][k][l] += dp[i-1][j][k]
                dp[i][k][l] %= mod
                if i == N:
                    ans += dp[i-1][j][k]
                    ans %= mod

print(ans)
