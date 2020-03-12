ans = []
n = int(input())

for _ in range(n):
    flag = False
    x = int(input())
    a = list(map(int, input().split()))

    tmp = [a[0]]
    for i in range(1, x):
        if a[i] in tmp and a[i-1] != a[i]:
            ans.append("YES")
            flag = True
            break

        tmp.append(a[i])

    if flag == False:
        ans.append("NO")

for i in ans:
    print(i)

