n, k = map(int, input().split())

a = [int(i) for i in input().split()]

ans = float('inf')
for i in range(1 << n):
    res = 0
    cnt = 0
    m = 0
    for j in range(n):
        if i >> j & 1:
            cnt += 1
            res += max(m-a[j] + 1, 0)
            m = max(m+1, a[j])
        else:
            m = max(m, a[j])

    if cnt == k:
        ans = min(ans, res)

print(ans)
