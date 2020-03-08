D = int(input())
n = int(input())
m = int(input())

d = [0]
for _ in range(n-1):
    d.append(int(input()))
d.append(D)
d.sort()

k = []
for i in range(m):
    k.append(int(input()))

import bisect

ans = 0
for i in k:
    tmp = bisect.bisect_left(d, i)
    dist = d[tmp] - i
    if tmp != 0:
        dist = min(dist, i - d[tmp-1])
    ans += dist

print(ans)
