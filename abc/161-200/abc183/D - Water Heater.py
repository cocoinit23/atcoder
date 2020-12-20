n, w = map(int, input().split())
stp = [list(map(int, input().split())) for _ in range(n)]

imos = [0] * (20 ** 5 + 10)

l = 0
r = 0
for s, t, p in stp:
    imos[s] += p
    imos[t] -= p
    l = min(l, s)
    r = max(r, t)

imos = imos[l:r + 10]

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

print('Yes') if max(imos) <= w else print('No')
