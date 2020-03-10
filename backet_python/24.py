import sys
sys.setrecursionlimit(2000000)

def depth_search(i, t):
    if d[i]:                           # memo
        return t
    d[i] = t                           # record
    t += 1                             # update
    for v in adj[i]:
        t = depth_search(v-1, t)
    f[i] = t                           # record
    t += 1                             # update
    return t

n = int(input())                                                        # input
adj = [list(map(int, input().split()))[2:] for _ in range(n)]

d = [0] * n                                                             # initialize
f = [0] * n

t = 1                                                                   # calculate
for i in range(n):
    if d[i] == 0:
        t = depth_search(i, t)

for i, df in enumerate(zip(d, f)):                                      # output
    print(i + 1, *df)

