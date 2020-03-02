a, b, c, x, y = map(int, input().split())

ans = float('inf')
for i in range(max(x, y) + 1):
    tmp = c*2*i + max(0, x-i) * a + max(0, y-i) * b
    ans = min(ans, tmp)

print(ans)