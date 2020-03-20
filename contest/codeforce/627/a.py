n = int(input())

ans = []
for _ in range(n):
    x = int(input())
    a = list(map(int, input().split()))

    flag = True
    for i in range(x-1):
        if abs(a[i] - a[i+1]) % 2 != 0:
            ans.append("NO")
            flag = False
            break

    if flag:
        ans.append("YES")

for i in ans:
    print(i)