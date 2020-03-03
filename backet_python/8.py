import numpy as np

n = int(input())
a, b = [], []
for i in range(n):
    A, B = map(int ,input().split())
    a.append(A)
    b.append(B)

a = np.array(a)
b = np.array(b)

mida = np.median(a)
midb = np.median(b)

print(int(np.sum(np.abs(a - mida)) + np.sum(np.abs(b - midb)) + np.sum(np.abs(a - b))))