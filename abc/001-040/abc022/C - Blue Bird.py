n, m = map(int, input().split())
dist = [[1e9] * n for i in range(n)]
x = []

def warshall_floyd(dist):
    n = len(dist)

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

    return dist

for i in range(m):
    u, v, l = map(int, input().split())
    if u == 1:
        x.append([v - 1, l])
    else:
        dist[u - 1][v - 1] = l
        dist[v - 1][u - 1] = l


dist=warshall_floyd(dist)

ans = 1e9
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        ans = min(ans, x[i][1] + x[j][1] + dist[x[i][0]][x[j][0]])

print(-1) if ans == 1e9 else print(int(ans))
