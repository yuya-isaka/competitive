import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global w, h, c

    if c[x][y] == 0:
        return

    c[x][y] = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            dx = x + i
            dy = y + j
            if 0<=dx<h and 0<=dy<w:
                dfs(dx, dy)

    return

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    c = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for x in range(h):
        for y in range(w):
            if c[x][y] == 1:
                ans += 1
                dfs(x, y)

    print(ans)
