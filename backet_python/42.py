"""
N個の都市を全て調べる
    限界の日にちまでを全て調べる
        その日に次の都市に行く場合か，そのまま待機する場合で，最小値をとる
"""
N, M = map(int, input().split())
d = [int(input()) for i in range(N)]
c = [int(input()) for i in range(M)]

dp = [[10**10 for j in range(M+1)] for i in range(N+1)]
dp[0][0] = 0

for j in range(1, M+1):
    dp[0][j] = 0

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j]+d[i]*c[j])

print(dp[N][M])
