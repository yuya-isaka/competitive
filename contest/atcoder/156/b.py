n, k = map(int, input().split())
ans = 0
tmp = 1
while tmp <= n:
    tmp *= k
    ans += 1
print(ans)