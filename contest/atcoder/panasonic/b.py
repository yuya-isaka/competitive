h, w = map(int, input().split())

a = h * w

if h == 1 or w == 1:
    print(1)
    exit()

print((a + 1) //2)