A, B, M = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
mina = min(a)
minb = min(b)

ans = mina + minb

for i in range(M):
    x,y,c = map(int, input().split())
    x -= 1
    y -= 1
    ans = min(ans, a[x] + b[y] - c)

print(ans)




