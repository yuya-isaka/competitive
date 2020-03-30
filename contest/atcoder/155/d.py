# import numpy as np
# stdin = open(0)

n, k = map(int, input().split())
a = list(map(int, input().split()))
# N, K = map(int, stdin.readline().split())
# A = np.array(stdin.read().split(), np.int64)
minus = [-x for x in a if x < 0]
plus = [x for x in a if x >= 0]
minus.sort()
plus.sort()
# A = np.sort(A)
# zero = A[A == 0]
# pos = A[A > 0]
# neg = A[A < 0]

def cnt(x):
    ans = 0
    if x < 0:
        x = -x
        r = 0
        for num in minus[::-1]:
            while r < len(plus) and plus[r] * num < x:
                r += 1
            ans += len(plus) -  r
        return ans

    r = 0
    for num in minus[::-1]:
        if num * num <= x: ans -= 1
        while r < len(minus) and minus[r] * num <= x:
            r += 1
        ans += r
    r = 0
    for num in plus[::-1]:
        if num * num <= x: ans -= 1
        while r < len(plus) and plus[r] * num <= x:
            r += 1
        ans += r
    ans //= 2
    ans += len(minus) * len(plus)    
    return ans
# def f(x):
#     """count the number of products , <= x"""
#     cnt_tpl = 0
#     # zero and ...
#     if x >= 0:
#         cnt_tpl += len(zero) * N
#     # positive and ...
#     cnt_tpl += np.searchsorted(A, x // pos, side='right').sum()
#     # negative and ...
#     cnt_tpl += (N - np.searchsorted(A, (-x - 1) // (-neg), side='right')).sum()
#     # a^2
#     cnt_tpl -= np.count_nonzero(A * A <= x)
#     assert cnt_tpl % 2 == 0
#     return cnt_tpl // 2

bottom = 0
top = 2*(10**18) + 2
# left = -10 ** 18
# right = 10 ** 18

while top - bottom > 1:
    mid = (top + bottom) // 2
    if cnt(mid - 10**18-1) < k:
        bottom = mid
    else:
        top = mid
# while left + 1 < right:
#     x = (left + right) // 2
#     if f(x) >= K:
#         right = x
#     else:
#         left = x

print(int(top - 10**18-1))
# print(right)