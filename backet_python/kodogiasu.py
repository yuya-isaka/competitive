import sys
import itertools
from operator import itemgetter #sortedの対象を決めたい
from fractions import gcd #最大公約数
from math import ceil, floor, sqrt, isinf #小数点切り上げ、切り捨て、平方根
from copy import deepcopy #参照で影響されないコピー
from collections import Counter, deque #要素ごとの出現回数、双方向アクセス可能データ型
import heapq
import numpy as np
from functools import reduce
sys.setrecursionlimit(200000)

input = sys.stdin.readline
# template


n = int(input())
h = list(map(int, input().split()))

dp = [1e9] * n

dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
    if(i > 1):
         dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

print(dp[-1])
