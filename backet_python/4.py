import numpy as np 

n, m = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(n)])

ans = 0
for i in range(m):
    for j in range(m):
        if i >= j:
            continue

        tmp = np.sum(np.maximum(a[:, i], a[:, j]))
        ans = max(ans, tmp)

print(ans)