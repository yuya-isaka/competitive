while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    ans = 0
    for i in range(1, x+1):
        for j in range(i+1, x+1):

            c = y - (i+j)

            if c > j and c <= x:
                ans += 1

    print("%d"%(ans))