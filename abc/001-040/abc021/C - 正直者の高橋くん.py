from collections import deque

n = int(input())
a, b = map(lambda x: int(x) - 1, input().split())
m = int(input())
xy = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
mod = 10 ** 9 + 7

graph = [[] for _ in range(n)]
for x, y in xy:
    graph[x].append(y)
    graph[y].append(x)

dist = [1e9] * n
dist[a] = 0
dp = [0] * n
dp[a] = 1

q = deque()
q.append(a)

while q:
    now = q.popleft()
    for next in graph[now]:
        if dist[next] == 1e9:
            dist[next] = dist[now] + 1
            dp[next] += dp[now]
            dp[next] %= mod
            q.append(next)
        elif dist[next] == dist[now] + 1:
            dp[next] += dp[now]
            dp[next] %= mod

print(dp[b])
