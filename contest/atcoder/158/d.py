from collections import deque

s = deque(input())

q = int(input())

check = 1
for _ in range(q):
    t = list(input().split())
    if t[0] == '1':
        check = 1 - check
    else:
        if t[1] == '1':
            if check == 1:
                s.appendleft(t[2])
            else:
                s.append(t[2])
        else:
            if check == 1:
                s.append(t[2])
            else:
                s.appendleft(t[2])



if check == 1:
    print(''.join(s))
else:
    s = list(reversed(s))
    print(''.join(s))
