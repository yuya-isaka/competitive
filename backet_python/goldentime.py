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

def retmax(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    dp = np.zeros([3, n+1])

    for i, a_l in enumerate(a):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[k, i+1] = retmax(dp[k, i+1], dp[j, i] + a_l[k])

    print(int(np.max(dp[:, n], axis=0)))


if __name__ == "__main__":
    main()
