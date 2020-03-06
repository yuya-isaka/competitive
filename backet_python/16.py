import itertools
n = int(input())
a = tuple([int(i) for i in input().split()])
b = tuple([int(i) for i in input().split()])

l = list(itertools.permutations(range(1,n+1)))

print(abs(l.index(a) - l.index(b)))



