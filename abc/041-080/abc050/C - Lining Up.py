from collections import Counter

n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

combi = []
for i in range(n):
    l = i
    r = n - i - 1
    combi.append(abs(l - r))

if sorted(combi) == sorted(a):
    c = Counter(combi)
    ans = 1
    for i in c.values():
        ans *= i
        ans %= mod
else:
    ans = 0

print(ans)
