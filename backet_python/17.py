import itertools

def check(queen):
    for r1, c1 in queen:
        if not all((r1 == r2 and c1 == c2) or (r1 + c1 != r2 + c2 and r1 - c1 != r2 - c2) for r2, c2 in queen):
            return False
    return True

k = int(input())
R, C = [[i for i in range(8)] for _ in range(2)]
q = []
for _ in range(k):
    r, c = map(int, input().split())
    q.append((r, c))
    R.remove(r)
    C.remove(c)

for l in itertools.permutations(C):
    q_tmp = q[:] + list(zip(R, l))
    if check(q_tmp):
        for i, j in sorted(q_tmp):
            print("." * j + "Q" + "." * (8 - j - 1))
        break