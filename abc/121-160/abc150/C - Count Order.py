import itertools

n = [int(x + 1) for x in range(int(input()))]
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

seq = list(itertools.permutations(n))

for i in range(len(seq)):
    if seq[i] == tuple(p):
        a = i
    if seq[i] == tuple(q):
        b = i

print(abs(a - b))
