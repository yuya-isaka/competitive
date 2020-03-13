import sys
sys.setrecursionlimit(2000000)

n = int(input())
m = [list(map(int, input().split()))[2:] for _ in range(n)]

def dfs(x, time):
    first[x] = time
    time += 1
    for v in m[x]:
        if first[v-1] == 0:
            time = dfs(v-1, time)
    finish[x] = time
    time += 1
    return time

first = [0] * n
finish = [0] * n

time = 1
for i in range(n):
    if first[i] == 0:
        time = dfs(i, time)

for i, xy in enumerate(zip(first, finish)):
    print(i+1, *xy)