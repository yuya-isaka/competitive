s = input()


length = len(s)//2
if len(s) % 2 != 0:
    print("No")
    exit(0)

tmp = 0
for i in range(0, len(s), 2):
    if s[i] == 'h' and s[i+1] == 'i':
        tmp += 1

if length == tmp:
    print("Yes")
else:
    print("No")
