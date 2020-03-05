n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
m = [int(i) for i in input().split()]

ans = []
for i in range(1 << n):
    tmp = 0
    for j in range(n):
        if i >> j & 1:
            tmp += A[j]
    ans.append(tmp)

ans = set(ans)

for i in range(q):
    print("yes" if m[i] in ans else "no")
