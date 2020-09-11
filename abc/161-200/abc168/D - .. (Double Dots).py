from collections import deque

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a = ab[i][0]
    b = ab[i][1]
    graph[a].append(b)
    graph[b].append(a)

inf = 100100100
ans = [[inf, inf] for _ in range(n + 1)]
ans[0] = [0, 0]
ans[1] = [0, 0]

q = deque([1])
while q:
    now = q.popleft()
    depth = ans[now][1]
    for x in graph[now]:
        if ans[x][0] == inf:
            q.append(x)
            if ans[x][1] > depth + 1:
                ans[x][0] = now
                ans[x][1] = depth + 1

print('Yes')
for i in range(2, n + 1):
    print(ans[i][0])
