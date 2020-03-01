import numpy as np  

n, k = map(int, input().split())
h = np.array([int(i) for i in input().split()])

dp = np.array([0] * n)

for i in range(1, n):
    j = max(i-k, 0)
    dp[i] = np.min(np.abs(h[i] - h[j:i]) + dp[j:i])

print(dp[-1])