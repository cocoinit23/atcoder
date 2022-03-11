from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

cs = Counter(s)
ct = Counter(t)

ans = 0
for key in cs.keys():
    ans = max(ans, cs[key] - ct[key])

print(ans)
