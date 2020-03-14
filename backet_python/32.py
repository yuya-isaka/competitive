from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    w, h = map(int, input().split())

    if w == 0:
        exit()

    wall = [list(map(int, input().split())) for _ in range(2 * h - 1)]

    d = [[0]*w for _ in range(h)]
    d[0][0] = 1

    q = deque()
    q.append((0, 0))

    while q:
        sy, sx = q.popleft()
        for i in range(4):
            ty = sy + dy[i]
            tx = sx + dx[i]
            if 0<=tx<w and 0<=ty<h and d[ty][tx] == 0 and wall[sy + ty][(sx + tx) // 2] != 1:
                d[ty][tx] = d[sy][sx] + 1
                q.append((ty, tx))

    print(d[-1][-1])