def fib(i):
    if i <= 1:
        return 1

    if d[i] != 0:
        return d[i]

    d[i] = fib(i-1) + fib(i-2)
    return d[i]

n = int(input())

d = [0] * (n+1)


print(fib(n))