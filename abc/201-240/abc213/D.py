import sys
from collections import deque

sys.setrecursionlimit(1000000)
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)

prev = deque([])
ans = [1]
visited[1] = True


def dfs(cur):
    global prev, ans

    for i in sorted(graph[cur]):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            prev.append(cur)
            dfs(i)
            p = prev.pop()
            ans.append(p)


dfs(1)
print(*ans)
