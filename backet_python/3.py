s = input()

ans = 0
cnt = 0
for i in s:
    if i in 'ACGT':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)

print(ans)