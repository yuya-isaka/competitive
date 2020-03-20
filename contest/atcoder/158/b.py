n, a, b = map(int, input().split())

tmp = n // (a+b)
tmpamari = n % (a+b)

ans = tmp * a
ans += min(tmpamari, a)

print(ans)