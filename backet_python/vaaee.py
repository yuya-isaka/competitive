from collections import deque
import sys
sys.setrecursionlimit(10**5)


def bfs():
    # global w, h, data, que

    while len(que):
        x, y = que.popleft()
        if data[x][y] == 0:
            continue

        data[x][y] = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                dx, dy = x + i, y + j
                if 0 <= dx < h and 0 <= dy < w:
                    que.append((dx, dy))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    data = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for x in range(h):
        for y in range(w):
            if data[x][y] == 1:
                que = deque()
                que.append((x, y))
                ans += 1
                bfs()

    print(ans)
