n = int(input())
a = sorted([tuple(map(int, input().split())) for _ in range(n)])
m = int(input())
b = sorted([tuple(map(int ,input().split())) for _ in range(m)])
U = set(b)

for i in range(m):
    flag = True
    tmp = (b[i][0] - a[0][0], b[i][1] - a[0][1])
    for j in range(1, n):
        if (a[j][0] + tmp[0], a[j][1] + tmp[1]) not in U:
            flag = False
            break
    if flag:
        print(*tmp)