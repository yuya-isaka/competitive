n = int(input())
s = input()

ans = 0
for i in range(0, 1000):
    i = str(i).zfill(3)

    try:
        id1 = s.index(i[0])
        id2 = s.index(i[1], id1+1)
        id3 = s.index(i[2], id2+1)
        ans += 1
    except ValueError:
        continue

print(ans)