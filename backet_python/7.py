n = int(input())
h = [tuple(map(int, input().split())) for _ in range(n)]

s = set(h)

ans = 0
for i in range(n):
    x1, y1 = h[i]
    for j in range(i+1, n):
        x2, y2 = h[j]
        dx, dy = x2 - x1, y2-y1
        if (x1-dy, y1+dx) in s and (x2-dy, y2+dx) in s:
            ans = max(ans, dx**2 + dy**2)

print(ans)

