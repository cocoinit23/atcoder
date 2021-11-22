import sys

sys.setrecursionlimit(100000)

n = int(input())
c = list(map(int, input().split()))

graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
color_list = set()
good = []


def dfs(cur):
    visited[cur] = True
    color = c[cur - 1]
    is_color_used = False
    if not (color in color_list):
        color_list.add(color)
        good.append(cur)
        is_color_used = True
    for next in graph[cur]:
        if not visited[next]:
            dfs(next)
    if is_color_used:
        color_list.remove(color)


dfs(1)
good.sort()
for i in good:
    print(i)
