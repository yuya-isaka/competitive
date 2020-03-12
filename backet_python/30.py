import sys
from collections import deque

H, W, N = map(int, input().split())
c = [input() for a in range(H)]


def place(symbol):
  for y in range(H):
    x = c[y].find(symbol)
    if -1 != x:
      return list([y, x])


s_y, s_x = place('S')
g_y, g_x = place(str(1))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

count = 0

for h in range(N):
  if 1 <= h:
    s_y, s_x = place(str(h))
    g_y, g_x = place(str(h+1))
  d = [[sys.maxsize for b in range(W)] for a in range(H)]
  q = deque([[s_y, s_x]])
  d[s_y][s_x] = 0
  while len(q) > 0:
    y, x = q.popleft()
    if y == g_y and x == g_x:
      count += d[y][x]
      break
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= nx and nx <= W-1 and 0 <= ny and ny <= H-1 and c[ny][nx] != 'X' and d[ny][nx] == sys.maxsize:
        q.append([ny, nx])
        d[ny][nx] = d[y][x]+1


print(count)
