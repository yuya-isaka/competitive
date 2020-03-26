from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s)
m = 0
for v in c.values():
	m = max(m, v)
ans = []
for k, v in c.items():
	if v == m:
		ans.append(k)
ans.sort()
print(*ans, sep="\n")