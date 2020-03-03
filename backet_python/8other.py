import numpy as np

n = int(input())
a, b = np.array([], dtype=np.int64), np.array([], dtype=np.int64)

for i in range(n):
    A, B = map(int, input().split())
    a = np.append(a, A)
    b = np.append(b, B)

ans = float('inf')
for i in a:
    for j in b:
        ans = min(ans, int(np.sum(np.abs(a - i)) + np.sum(np.abs(b - j)) + np.sum(np.abs(a - b))))

print(ans)

