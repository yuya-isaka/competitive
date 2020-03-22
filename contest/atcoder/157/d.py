#!/usr/bin/env python3
import numpy as np
stdin = open(0)

N, K = map(int, stdin.readline().split())
A = np.array(stdin.read().split(), np.int64)

"""
このnumpyの使い方凄すぎるねん
"""
A = np.sort(A)
zero = A[A == 0]
pos = A[A > 0]
neg = A[A < 0]


def f(x):
    """count the number of products , <= x"""
    cnt_tpl = 0
    # zero and ...
    if x >= 0:
        cnt_tpl += len(zero) * N
    # positive and ...
    cnt_tpl += np.searchsorted(A, x // pos, side='right').sum()
    # negative and ...
    cnt_tpl += (N - np.searchsorted(A, (-x - 1) // (-neg), side='right')).sum()
    # a^2
    cnt_tpl -= np.count_nonzero(A * A <= x)
    assert cnt_tpl % 2 == 0
    return cnt_tpl // 2


left = -10 ** 18
right = 10 ** 18
while left + 1 < right:
    x = (left + right) // 2
    if f(x) >= K:
        right = x
    else:
        left = x


print(right)
