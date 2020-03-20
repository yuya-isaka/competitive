n = int(input())
ans = ['' for _ in range(n)]


def dfs(i, mx):
    if i == n:
        print(''.join(ans))
        return
    for j in range(mx+1):
        ans[i] = chr(ord('a') + j)
        dfs(i+1, max(j+1, mx))


dfs(0, 0)