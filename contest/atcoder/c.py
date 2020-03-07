import math

a, b = map(int, input().split())

ans = float('inf')
check = False
for i in range(1251):
    i = float(i)
    A = i * 0.08
    B = i * 0.1

    if math.floor(A) == a and math.floor(B) == b:
        ans = min(ans, i)
        check = True

if check:
    print(int(ans))
else:
    print(-1)



