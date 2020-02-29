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


def main():
    n, k = map(int, input().split())
    h = [int(i) for i in input().split()]

    dp = [0] * n

    for i in range(1, n):
        L = [dp[j] + abs(h[i] - h[j]) for j in range(max(0, i-k), i)]
        dp[i] = min(L)

    print(dp[-1])

if __name__ == "__main__":
    main()

