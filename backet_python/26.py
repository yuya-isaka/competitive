import sys 
sys.setrecursionlimit(10**6)

def dfs(v, pv):
    global P

    for nv in G[v]:
        if nv != pv:
            P[nv] += P[v]
            dfs(nv, v)

n,q = map(int, input().split())
G = [[] for _ in range(n)]              # adjacent list
for i in range(n-1):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

P = [0]*n                               # add list
for i in range(q):
    p,x = map(int, input().split())
    P[p-1] += x


dfs(0, 0)
print(*P)

