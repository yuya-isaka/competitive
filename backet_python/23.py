n, m = map(int, input().split())
p = [int(input()) for _ in range(n)]
p.append(0)
p.sort()

a = []
for i in range(n+1):
    for j in range(i, n+1):
        k = p[i] + p[j]
        if k <= m:
            a.append(k)
a.sort()

import bisect
ans = 0
for i in a:
    j = bisect.bisect_right(a, m-i)
    tmp = i + a[j-1]
    ans = max(ans, tmp)

print(ans)
