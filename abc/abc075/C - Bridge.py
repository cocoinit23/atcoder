n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]


def dfs(curr):
    visit[curr] = 1
    for x in graph[curr]:
        if visit[x] == 0:
            dfs(x)


ans = 0
for i in range(m):
    temp = ab[:i] + ab[i + 1:]
    graph = [[] for _ in range(n + 1)]
    for a, b in temp:
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (n + 1)
    dfs(1)

    if sum(visit[1:]) != n:
        ans += 1

print(ans)
