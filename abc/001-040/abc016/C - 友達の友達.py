from collections import deque

n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n):
    dist = [1e10] * n
    dist[i] = 0
    q = deque()
    q.append(i)
    while q:
        cur = q.popleft()
        for j in range(n):
            if i == j:
                continue
            if graph[cur][j] != 0 and dist[j] > dist[cur] + 1:
                dist[j] = dist[cur] + 1
                q.append(j)

    ans = sum([1 for i in dist if i == 2])
    print(ans)
