import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    g[i][j] = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            dx = x + i
            dy = y + j

            if 0<=dx<h and 0<=dy<w and g[dx][dy] == 1:
                dfs(dx, dy)
    return

while True:
    w, h = map(int, input().split())
    if not (w or h):
        break

    g = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)