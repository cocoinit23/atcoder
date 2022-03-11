n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

num_leaf = 0
l = [1e9] * (n + 1)
r = [0] * (n + 1)

stack = [(~1, 0), (1, 0)]
while stack:
    curr, prev = stack.pop()
    if curr > 0:
        if graph[curr] == [prev]:
            num_leaf += 1
            l[curr] = num_leaf
            r[curr] = num_leaf
        else:
            stack.append([~curr, None])
            for next_v in graph[curr]:
                if next_v == prev:
                    continue
                stack.append([next_v, curr])

    else:
        curr = ~curr
        for child_v in graph[curr]:
            l[curr] = min(l[curr], l[child_v])
            r[curr] = max(r[curr], r[child_v])

for i in range(1, n + 1):
    print(l[i], r[i])

"""
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

num_leaf = 0
l = [1e9] * (n + 1)
r = [0] * (n + 1)

def dfs(vertex, parent):
    global num_leaf, l, r
    if graph[vertex] == [parent]:
        num_leaf += 1
        l[vertex] = num_leaf
        r[vertex] = num_leaf
    else:
        min_l = num_leaf + 1
        max_r = num_leaf + 1
        for next_v in graph[vertex]:
            if next_v == parent:
                continue
            dfs(next_v, vertex)
            min_l = min(min_l, l[next_v])
            max_r = max(max_r, r[next_v])
        l[vertex] = min_l
        r[vertex] = max_r


dfs(1, 0)

for i in range(1, n + 1):
    print(l[i], r[i])
"""
