n, m = map(int, input().split())
graph = [[1e9] * n for i in range(n)]
x = []

for i in range(m):
    u, v, l = map(int, input().split())
    if u == 0:
        x.append([v - 1, l])
    else:
        graph[u - 1][v - 1] = l
        graph[v - 1][u - 1] = l

for i in range(n):
    graph[i][i] = 0

print(graph)

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

ans = 1e9
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        ans = min(ans, x[i][1] + x[j][1] + graph[x[i][0]][x[j][0]])

print(-1) if ans == 1e9 else print(int(ans))
