n, w = map(int, input().split())

import numpy as np 

dp = np.full(1000*n+1, w+1, dtype=int)

dp[0] = 0

for i in range(n):
    weight, value = map(int, input().split())
    dp[value:] = np.minimum(dp[value:], dp[:-value] + weight)

print(np.max(np.where(dp <= w)))