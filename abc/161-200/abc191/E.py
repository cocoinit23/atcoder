def dijkstra(graph):
    # graph: compressed sparse graph, N x N array of distances
    import heapq

    n = len(graph)
    result = []

    for start in range(n):
        dist = [1e20] * n
        dist[start] = 0
        q = []
        heapq.heapify(q)
        heapq.heappush(q, start)

        while q:
            cur = heapq.heappop(q)
            for goal in range(n):
                if start == goal:
                    continue
                if graph[cur][goal] != 0 and dist[goal] > dist[cur] + graph[cur][goal]:
                    dist[goal] = dist[cur] + graph[cur][goal]
                    heapq.heappush(q, goal)

        result.append(dist)

    return result


n, m = map(int, input().split())

graph = [[1e8] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

res = dijkstra(graph)
for i in range(n + 1):
    for j in range(n + 1):
        if res[i][j] == 1e8 or i == j:
            res[i][j] = None

for i in range(1, n + 1):
    ans = -1
    cost = None
    for j in range(1, n + 1):
        if res[i][j] is None or res[j][i] is None:
            continue
        cost = min(res[i][j] + res[j][i], graph[i][i])
    print(ans) if cost is None else print(cost)
