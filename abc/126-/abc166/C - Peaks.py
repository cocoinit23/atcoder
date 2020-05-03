n, m = map(int, input().split())
h = [-1] + list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]

link = [[] for _ in range(n + 1)]
for x in ab:
    a, b = x[0], x[1]
    link[a].append(b)
    link[b].append(a)

ans = [0] + [1] * n
for i in range(len(link)):
    for j in link[i]:
        if h[i] <= h[j]:
            ans[i] = 0

print(sum(ans))
