
n = int(input())

abc = [list(map(int, input().split())) for _ in range(n)]

a, b, c = 0, 0, 0
for x, y, z in abc:
    a, b, c = max(b, c) + x, max(a, c) + y, max(b, c) + z 

print(max(a, b, c))
