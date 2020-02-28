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


n, k = map(int, input().split())
h = np.array(list(map(int, input().split())))

dp = np.array([0] * n)

for i in range(1, n):
    j = max(0, i-k)
    dp[i] = np.min(np.abs(h[i] - h[j:i]) + dp[j:i])

print(dp[-1])

