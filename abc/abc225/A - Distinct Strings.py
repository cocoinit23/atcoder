import itertools

s = input()

ans = itertools.permutations(s, len(s))
ans = [''.join(i) for i in ans]
ans = len(set(ans))
print(ans)