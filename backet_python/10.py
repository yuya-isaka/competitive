n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

ans = []
for i in range(1 << n):
    tmp = 0
    for j in range(n):
        if i >> j & 1:
            tmp += a[j]
    ans.append(tmp)

u = set(ans)
for i in range(q):
    print("yes" if m[i] in u else "no")
