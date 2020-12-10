from collections import Counter
from itertools import combinations

n = int(input())
s = []
for i in range(n):
    temp = input()[0]
    if temp in ['M', 'A', 'R', 'C', 'H']:
        s.append(temp)

c = Counter(s)
combi = combinations(c.values(), 3)

ans = 0
for a, b, c in combi:
    ans += a * b * c

print(ans)
