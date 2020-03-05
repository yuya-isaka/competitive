n, m = map(int, input().split())
xy = set([tuple(map(int, input().split())) for _ in range(m)]) #走査する時はsetにするのが定石　でも二次元配列には使えないから注意

ans = 0
for i in range(1 << n):
    tmp = []
    for j in range(n):
        if i >> j & 1:
            tmp.append(j)

    tmp = sorted(tmp)
    length = len(tmp)
    flag = True
    for j in range(length):
        for k in range(j+1, length):
            if (tmp[j]+1, tmp[k]+1) not in xy: #順番に入ってるからこれができる
                flag = False
                break

        if not flag:
            break

    if flag:
        ans = max(ans, length)

print(ans)
