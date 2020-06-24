import sys
import itertools
import numpy as np
import time
import math
import re

sys.setrecursionlimit(10**7)

from collections import defaultdict
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    S = input()[::-1]
    MOD = 2019
    
    X = [0]
    for i, s in enumerate(S):
        X.append((X[-1] + int(s) * pow(10, i, MOD)) % MOD)
    
    C = Counter(X)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)




if __name__ == "__main__":
    main()
    pass