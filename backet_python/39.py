n = int(input())
e = list(map(int, input().split()))
result = e[-1]
dp = [[0]*21 for _ in range(n-1)]
dp[0][e[0]] = 1

for i in range(1, n-1):
  for j in range(21):
    if j+e[i] <= 20:
      dp[i][j+e[i]] += dp[i-1][j]
    if j-e[i] >= 0:
      dp[i][j-e[i]] += dp[i-1][j]
print(dp[n-2][result])
