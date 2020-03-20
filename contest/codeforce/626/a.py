n = int(input())

ans = []
for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))

    check = False
    for i in range(1, 1 << t):
        tmp = 0
        anslist = []
        for j in range(t):
            if i >> j & 1:
                tmp += a[j]
                anslist.append(j)

        if tmp % 2 == 0:
            ans.append(anslist)
            check = True
            break

    if check == False:
        ans.append([-1])

for i in ans:
    L = [str(a+1) for a in i]

    L = ' '.join(L)
    if L == '0':
        L = '-1'
    else:
        print(len(i))
    print(L)