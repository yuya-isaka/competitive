def longest_common(m, n):
	N = len(n)
	dp = [0]*(N+1)
	for x in m:
		dp_kari = dp[:]
		for j, y in enumerate(n):
			if x == y:
				dp[j+1] = dp_kari[j]+1
			elif dp[j+1] < dp[j]:
				dp[j+1] = dp[j]
	return dp[N]


for _ in range(int(input())):
    x = input()
    y = input()
    print(longest_common(x, y))
