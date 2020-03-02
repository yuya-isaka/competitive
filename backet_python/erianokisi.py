import numpy as np  

n , w = map(int, input().split())

dp = np.zeros(w+1)

for _ in range(n):
    weight, value = map(int, input().split())

    dp[weight:] = np.maximum(dp[weight:], dp[:-weight] + value)

print(int(dp[-1]))


