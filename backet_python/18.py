n = int(input())
s = set(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))

ans = 0
for i in range(q):
    if t[i] in s:
        ans += 1

print(ans)
