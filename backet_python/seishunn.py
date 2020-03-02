import numpy as np  

n, k = map(int, input().split())
h = np.array([int(i) for i in input().split()])

dp = np.array([0] * n)

for i in range(1, n):
    j = max(0, i-k)
    dp[i] = np.min(dp[j:i] + abs(h[i] - h[j:i]))

print(dp[-1])

