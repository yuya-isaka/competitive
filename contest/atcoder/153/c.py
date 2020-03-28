n, k = map(int,input().split())

h = list(map(int, input().split()))

if n <= k:
    print(0)

else:
    h.sort()
    ans = sum(h[0:n-k])
    print(ans)