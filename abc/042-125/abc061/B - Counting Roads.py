n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ans = [[] for _ in range(n + 1)]
for a, b in ab:
    ans[a].append(b)
    ans[b].append(a)

for i in range(1, n + 1):
    print(len(ans[i]))
