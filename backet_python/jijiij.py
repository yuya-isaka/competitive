while True:
    ans = 0
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):

            c = x - (i+j)

            if j < c and c <= n:
                ans += 1

    print("%d"%(ans))