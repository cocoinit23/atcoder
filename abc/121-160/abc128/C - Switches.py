n, m = map(int, input().split())
s = []
for i in range(m):
    s.append(list(map(int, input().split()[1:])))
p = [int(x) for x in input().split()]

ans = 0

for i in range(2 ** n):
    isLightOn = [False] * m
    for k in range(m):
        count = 0
        for j in range(len(s[k])):
            if (i >> s[k][j] - 1) & 1:
                count += 1
        if count % 2 == p[k]:
            isLightOn[k] = True
    if sum(isLightOn) == m:
        ans += 1

print(ans)
