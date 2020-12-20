from collections import Counter

n = int(input())
l = [Counter(input()) for _ in range(n)]

ans = ''
c = sorted(l[0])

for key in c:
    m = l[0][key]
    for i in range(1, n):
        m = min(m, l[i][key])
    ans += key * m

print(ans)
