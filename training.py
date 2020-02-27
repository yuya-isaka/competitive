import sys
import itertools
from operator import itemgetter #sortedの対象を決めたい
from fractions import gcd #最大公約数求めたい
from math import ceil, floor, sqrt #小数点切り上げ、切り捨て、平方根求めたい
from copy import deepcopy #参照で影響されないコピーが作られる
from collections import Counter, deque #要素ごとの出現回数を数える。双方向アクセス可能データ型
import heapq
from functools import reduce
sys.setrecursionlimit(200000)

input = sys.stdin.readline
# template


p = int(input())
a = list(map(int,input().split()))

b = list(set(a))
n = len(b) #種類の数

s = 0
t = 0
num = 0
ass = p
count = [0 for i in range(max(a)+2)] #count[i]:iの出現数

while True:
    while t < p and num < n:
        if count[a[t]] == 0:
            num += 1
        count[a[t]] += 1
        t += 1
    if num < n:
        break
    ass = min(ass,t-s)
    if count[a[s]]-1 == 0:
        num -=1
    count[a[s]] -=1
    s += 1
print(ass)

