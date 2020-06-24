n, x, y = map(int, input().split())

d = [0]*(n-1)

for i in range(n-1):
    for j in range(i+1,n):
        d[min(j-i-1, abs(x-1-i) + abs(y-1-j))] += 1

for i in range(n-1):
    print(d[i])