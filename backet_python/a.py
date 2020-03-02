while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break

    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j <= i:
                continue

            c = x - (i + j)

            if c > j and c <= n:
                ans += 1

    print("%d"%(ans))