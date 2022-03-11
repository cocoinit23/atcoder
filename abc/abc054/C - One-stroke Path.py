n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n + 1)


def dfs(now, depth):
    if visit[now]:
        return 0
    if depth == n:
        return 1

    count = 0
    visit[now] = 1
    if graph[now]:
        for i in graph[now]:
            count += dfs(i, depth + 1)
    visit[now] = 0

    return count


ans = dfs(1, 1)
print(ans)
