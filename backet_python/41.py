"""
全ての日を調べる．
    それぞれの日である服を選ぶ．（これが今調べている日の条件にあっているか調べておく）
        前の日に選んだ服を選ぶ．（この中で，1番絶対値の差が大きくなっているものを選ぶ）
        選んだやつを配列にメモしておく

この作業の繰り返し

これは初期化がポイント（1番最初を選ぶ時，条件に当てはまっているか調べる処理は，繰り返しの処理とは別だから，ループの外で前処理しないといけない）
"""
d, n = map(int, input().split())
T = [int(input()) for _ in range(d)]
ABC = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(d)]

t0 = T[0]
for j in range(n):
  a, b, c = ABC[j]
  if t0 < a or t0 > b:
    dp[0][j] = -float("inf")

for i in range(1, d):
  for j in range(n):
    a, b, c = ABC[j]
    if a <= T[i] <= b:
      for k in range(n):
        dp[i][j] = max(dp[i][j], dp[i-1][k]+abs(c-ABC[k][2]))

print(max(dp[-1]))
