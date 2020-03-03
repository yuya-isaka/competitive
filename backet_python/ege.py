s = input()

ans = 0
tmp = 0
for i in s:
    if i in 'ACGT':
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0

ans = max(ans, tmp)
print(ans)