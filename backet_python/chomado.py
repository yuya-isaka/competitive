moji = ['a', 'b', 'c']

def f(rest, s):
    if rest == 0:
        print(s)

    else:
        for i in range(3):
            f(rest-1, s + moji[i])

n = int(input())

f(n, "")