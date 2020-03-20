import decimal
import math
a, b, c = map(int, input().split())

d = c - a - b

if d > 0 and d * d > 4 * a * b:
    print("Yes")
else:
    print("No")