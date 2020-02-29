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
    n = int(input())
    abc = [list(map(int, input().split())) for _ in range(n)]

    a, b, c = 0, 0, 0
    for x, y, z in abc:
        a, b, c = max(b, c) + x, max(a, c) + y, max(a, b) + z

    print(max(a, b, c))



if __name__ == "__main__":
    main()

