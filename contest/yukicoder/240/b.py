# 解説を見たらわかるけど
# つまり、交互に偶数と奇数が出ることになることに気付けるかがポイント　これは制約をしっかり見ないと気付けない。　
a, b, x, n = map(int, input().split())

if x % 2 == 0:
    print(0, n//2)
else:
    print(n//2, 0)

# mod = 2**32

# a, b, x, n = map(int, input().split())

# listlist = [0] * (n*2)

# for i in range(0, len(listlist)):
#     tmp = a * x % mod
#     tmp = (tmp + b) % mod
#     x = tmp
#     listlist[i] = tmp

# taka = []
# aoki = []
# for i in range(len(listlist)):
#     flag = True
#     if listlist[i] % 2 == 0:
#         flag = True
#     else: 
#         flag = False

#     if i % 2 == 0:
#         if flag:
#             taka.append(1)
#         else:
#             taka.append(0)

#     else:
#         if flag:
#             aoki.append(1)
#         else:
#             aoki.append(0)

# takacount = str(min(taka.count(1), taka.count(0)))
# aoki = str(min(aoki.count(1), aoki.count(0)))

# print(takacount + ' ' + aoki)

#純粋に、その入力分を調べていく
#まずはどんな数列が出るか調べて、それを試して行った
#ダメだった。
