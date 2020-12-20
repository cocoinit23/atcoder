n, m = map(int, input().split())

ab = []
for i in range(n):
    ab.append([int(x) for x in input().split()])

ab.sort(key=lambda x: x[0])

ans = 0
while m > 0:
    a, b = ab.pop(0)
    ans += min(m, b) * a
    m -= min(m, b)

print(ans)
