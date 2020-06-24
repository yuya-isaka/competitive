import sys
import itertools
import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    x, y, a, b, c = map(int, readline().split())
    p = sorted(map(int, readline().split()), reverse=True)
    q = sorted(map(int, readline().split()), reverse=True)
    r = sorted(map(int, readline().split()), reverse=True)

    z = sorted(p[:x] + q[:y] + r, reverse=True)
    ans = sum(z[:x+y])
    print(ans)

if __name__ == "__main__":
    main()
    pass