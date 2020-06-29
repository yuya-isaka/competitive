INF = 10 ** 10
v, e = map(int, input().split())
adj = [[INF] * v for _ in range(v)]
for _ in range(e):
    s, t, d = map(int, input().split())
    adj[s][t] = d

mem = {}
end = 2 ** v - 1
def minCost(state, pos):
    if (state, pos) in mem:
        return mem[(state, pos)]

    if state == end:
        return adj[pos][0]

    mask = 1
    ret = INF
    for to in range(v):
        if mask & state:
            mask <<= 1
            continue

        ret = min(ret, adj[pos][to] + minCost(state | mask, to))
        mask <<= 1

    mem[(state, pos)] = ret
    return ret

result = minCost(1, 0)
if result >= INF:
    print(-1)
else:
    print(result)