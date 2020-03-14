h, w = map(int, input().split())
maze = [input() for _ in range(h)]

from collections import deque

que = deque()
que.append((0,0))

d = [[0]*w for _ in range(h)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d[0][0] = 1

flag = False
while que:
    x, y = que.popleft()

    if x == h-1 and y == w-1:
        flag = True
        break

    for i, j in direction:
        dx, dy = x + i, y + j
        if 0<=dx<h and 0<=dy<w and d[dx][dy] == 0 and maze[dx][dy] != '#':
            d[dx][dy] = d[x][y] + 1
            que.append((dx, dy))

if flag == False:
    print(-1)
    exit()

res = 0
for i in range(h):
    res += maze[i].count('#')

res += d[-1][-1]


print(h*w - res)

