import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)

dp = [-1] * n

def dfs(i):
    if dp[i] != -1:
        return dp[i]

    tmp = 0
    for j in g[i]:
        tmp = max(tmp, dfs(j) + 1)

    dp[i] = tmp
    return tmp

for i in range(n):
    dfs(i)

print(max(dp))

