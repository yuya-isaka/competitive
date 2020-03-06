s = input()
t = input()

ans = 0
j = 0
i = 0
while i != len(s):
    if j == len(t):
        ans += 1
        i -= 1
        j = 0
        continue

    if s[i] == t[j]:
        j += 1
    else:
        j = 0

    i += 1

if j == len(t):
    ans += 1

print(ans)


#繰り返し長さ分を測って、一緒だったらcheckを増やして規定に達したら答えにプラスしていく方式を試した　ダメだった

#sの中にtが何個あるか調べれば行けるかなーと思ったけど
#なかなかうまくいかない
#一個の時は間の数だけで良いからその分を引けば良いと思ったけど、うまくいかないk