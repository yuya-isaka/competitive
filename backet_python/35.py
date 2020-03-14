N, W = map(int, input().split())

value, weight = [], []

for _ in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j - weight[i] >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j - weight[i]] + value[i])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[N][W])