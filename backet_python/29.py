r, c = map(int, input().split())

sy, sx = map(int, input().split())

gy, gx = map(int, input().split())

v = [input() for _ in range(r)]
d = [[0]*c for _ in range(r)]

from collections import deque
que = deque()
que.append((sy-1, sx-1))

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

while que:
    y, x = que.popleft()
    if y == gy-1 and x == gx-1:
        break

    for i, j in direct:
        dy, dx = y + i, x + j

        if 0 <= dx < c and 0 <= dy < r and v[dy][dx] != '#' and d[dy][dx] == 0:
            d[dy][dx] = d[y][x] + 1
            que.append((dy, dx))

print(d[gy-1][gx-1])
