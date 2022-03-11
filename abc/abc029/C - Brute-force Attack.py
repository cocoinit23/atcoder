import itertools

n = int(input())

ans = itertools.product('abc', repeat=n)
for l in ans:
    print(''.join(l))
