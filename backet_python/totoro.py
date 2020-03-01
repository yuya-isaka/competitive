import numpy as np

n, k = map(int, input().split())
h = [int(i) for i in input().split()]

dp = [0] * n

for i, val in enumerate(h):
    if i > 0:
        p = max(i-k, 0)
        dp[i] = min(j + abs(l - val) for j, l in zip(dp[p:i], h[p:i]))

print(dp[-1])