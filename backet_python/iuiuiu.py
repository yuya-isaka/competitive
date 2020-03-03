n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]

x, y, z = 0, 0, 0
for a, b, c in h:
    x, y, z = max(y,z) + a, max(x,z) + b, max(x,y) + c

print(max(x, y, z))