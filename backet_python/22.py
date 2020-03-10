p = float(input())
eps = 1e-8

def f(x):
    return x + p * pow(2, -x / 1.5)

left = 0
right = p

while (right - left) > eps:
    mid = (right - left) / 3

    if f(left+mid) < f(right-mid):
        right -= mid
    else:
        left += mid

print(round(f(left), 10))

