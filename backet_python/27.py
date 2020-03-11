m = int(input())
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
 
def dfs(i, j):
    flag[i][j] = 1
    ret = 0
    for dy, dx in directions:
        ny = i + dy
        nx = j + dx
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1 and flag[ny][nx] == 0:
                ret = max(ret, dfs(ny, nx))
    flag[i][j] = 0
    return ret + 1
 
 
flag = [[0] * m for _ in range(n)]                 # flag list
ans = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            ans = max(ans, dfs(i, j))
print(ans)