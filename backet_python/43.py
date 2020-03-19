"""
・・・・・・・・
・・・・・・・・
・・・・・・・・
・・・・・・・・
・・・・・・・・
上記のような，文字列の繰り返し入力の場合
先に配列を作っておき s = [[]for _ in range(n)]
その後，行数分入力を受け取り，先に作った配列に列数分一個ずつappendしていく s[j].append(ss[j])

まあこれは思いつけた！！！
"""

n = int(input())
s = [[]for _ in range(n)]
for i in range(5):
  ss = input()
  for j in range(n):
    s[j].append(ss[j])
inf = float('inf')

dp = [[[inf]for _ in range(3)]for _ in range(n)]
dp[0][0] = 5-s[0].count("W")
dp[0][1] = 5-s[0].count("R")
dp[0][2] = 5-s[0].count("B")

for i in range(1, n):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2])+5-s[i].count("W")
  dp[i][1] = min(dp[i-1][0], dp[i-1][2])+5-s[i].count("R")
  dp[i][2] = min(dp[i-1][1], dp[i-1][0])+5-s[i].count("B")

print(min(dp[-1]))
