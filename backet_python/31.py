from collections import deque

w, h = map(int, input().split())
a = [[0] * (w+2)] 
b = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]
c = [[0] * (w+2)]
a = a + b + c                   # input data

dxdy1 = [(1, -1), (1, 0), (1, 1), (0, 1), (0, -1), (-1, 0)]
dxdy2 = [(1, 0), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

s = deque()
s.append((0, 0))

done = [[0] * (w + 2) for _ in range(h + 2)]            # same a list 

ans = 0
while s:
    d = s.popleft()
    for dx, dy in (dxdy1 if d[1] % 2 else dxdy2):
        x = d[0] + dx
        y = d[1] + dy
        if 0 <= x < w + 2 and 0 <= y < h + 2:
            if not(a[y][x] or done[y][x]):
                s.append((x, y))
                done[y][x] = 1
            if a[y][x]:
                ans += 1

print(ans)