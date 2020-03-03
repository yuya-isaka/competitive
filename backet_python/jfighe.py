
import numpy as np  

n, w = map(int, input().split()) 

dp = np.array([0] * (w+1)) 

for i in range(n):
    weight, value = map(int, input().split())

    dp[weight:] = np.maximum(dp[weight:], dp[:-weight] + value) 

print(int(dp[-1]))