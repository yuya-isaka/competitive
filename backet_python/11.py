N, M = map(int ,input().split())
light = [list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(M)]
p = [int(i) for i in input().split()]

ans = 0

for i in range(1 << N):
    flag = True
    for m in range(M):
        onsum = 0
        for j in range(N):
            if i >> j & 1 and j in light[m]:
                onsum+=1
        if onsum%2!=p[m]:
            flag = False
            break
    if flag == True:
        ans+=1

print(ans)