N = int(input())

a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])
c = sorted([int(i) for i in input().split()])

import bisect

ans = 0
for i in range(N):
    lefta = bisect.bisect_left(a, b[i])
    leftc = N - bisect.bisect_right(c, b[i])

    ans += lefta * leftc

print(ans)