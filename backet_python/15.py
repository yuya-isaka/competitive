import math
import itertools

n = int(input())
x, y = [0]*n, [0]*n
for i in range(n):
    a, b = map(int, input().split())
    x[i], y[i] = a, b
l = list(itertools.permutations(range(n)))

tmp = 0
for p in l:
    for j in range(n-1):
        a = p[j]
        b = p[j+1]
        tmp += math.sqrt((x[a]-x[b])**2 + (y[a]-y[b])**2)

print(round(tmp/len(l), 10))

