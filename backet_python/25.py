import sys
sys.setrecursionlimit(10000)

def dfs(x, y, c):
    if c[y][x] == 0:
        return

    c[y][x] = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            dy = y + i
            dx = x + j
            if 0<=dx<len(c[0]) and 0<=dy<len(c):
                dfs(dx, dy, c)

    return

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    c = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if c[y][x] == 1:
                ans += 1
                dfs(x, y, c)

    print(ans)


    


