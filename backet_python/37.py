n, m = map(int, input().split())

c = list(map(int, input().split()))

dp = [[float('inf')]*(n+1) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
    for j in range(n+1):
        if j - c[i] >= 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-c[i]] + 1)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

print(dp[m][n])