import numpy as np  

n, w = map(int, input().split())
dp = np.full(n*1000+1, float('inf'))
dp[0] = 0

for _ in range(n):
    weight, value = map(int, input().split())
    dp[value:] = np.minimum(dp[value:], dp[:-value] + weight) 

print(np.max(np.where(dp <= w)))