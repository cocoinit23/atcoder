n, m = map(int, input().split())
ab = sorted(list(map(int, input().split())) for _ in range(m))


def dfs(now, count):
    if count <= 2 and visit[n] == 0:
        visit[now] = 1
        if count <= 1:
            for x in graph[now]:
                dfs(x, count + 1)


flag = False
if ab[0][0] == 1:
    graph = [[] for _ in range(n + 1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (n + 1)
    dfs(1, 0)

    if visit[n] == 1:
        flag = True

print('POSSIBLE') if flag else print('IMPOSSIBLE')
