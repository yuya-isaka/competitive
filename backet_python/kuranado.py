import sys
import numpy as np
import itertools
import heapq
import bisect
import math
import queue
from operator import itemgetter #sortedの対象を決めたい
from fractions import gcd #最大公約数
from copy import deepcopy #参照で影響されないコピー
from collections import Counter, deque, defaultdict #要素ごとの出現回数、双方向アクセス可能データ型
from functools import reduce
mod = 1000000007
inf = 10**10
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def sieve_of_eratosthenes(n):
    if not isinstance(n,int):
        raise TypeError("n is not int")
    if n<2:
        raise ValueError("n is not effective")
    prime = [1]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        if prime[i] == 1:
            for j in range(2*i,n+1):
                if j%i == 0:
                    prime[j] = 0
    res = []
    for i in range(2,n+1):
        if prime[i] == 1:
            res.append(i)
    return res
 
def factorial(i):
    if i == 1:
        return 1
    else:
        return i*factorial(i-1)
 
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    def findroot(self,x):
        if x == self.parent[x]:
            return x
        else:
            y = self.parent[x]
            y = self.findroot(self.parent[x])
            return y
    
    def union(self,x,y):
        px = self.findroot(x)
        py = self.findroot(y)
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py
 
    def same_group_or_no(self,x,y):
        return self.findroot(x) == self.findroot(y)
# template


def main():
    n, w = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]

    dp = np.zeros([n+1, w+1])
    
    for i, itm in enumerate(wv):
        dp[i+1, :itm[0]] = dp[i, :itm[0]]
        dp[i+1, itm[0]:] = np.max([dp[i, itm[0]:], dp[i, :w-itm[0]+1] + itm[1]], axis=0)

    print(int(dp[n, w]))


if __name__ == "__main__":
    main()

