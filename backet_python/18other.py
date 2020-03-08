n = int(input())
s = [int(i) for i in input().split()]

q = int(input())
t = [int(i) for i in input().split()]

ans = 0
for i in range(q):

    left = 0
    right = n-1

    while left <= right:
        mid = (right+left) // 2

        if t[i] < s[mid]:
            right = mid -1
        elif t[i] > s[mid]:
            left = mid + 1
        else:
            ans += 1
            break

print(ans)