n, w = map(int, input().split())

value, weight = [], []
for i in range(n):
    a, b = map(int,input().split())
    value.append(a)
    weight.append(b)

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(n):
    for j in range(w+1):
        if j - weight[i] >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i+1][j-weight[i]] + value[i])

        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[n][w])
