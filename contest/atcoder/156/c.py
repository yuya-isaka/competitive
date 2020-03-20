n = int(input())
x = list(map(int, input().split()))
ans = float('inf')
for i in range(1, 101):
    tmp = 0
    for j in range(n):
        tmp += (i - x[j])**2
    ans = min(ans, tmp)
print(ans)