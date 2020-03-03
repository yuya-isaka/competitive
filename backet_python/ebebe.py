import numpy as np  

n, m = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(n)])

ans = 0
for i in range(m):
    for j in range(i, m):
        tmp = np.sum(np.maximum(a[:, i], a[:, j]))
        ans = max(tmp, ans)

print(ans)