def EulerTour(n, graph, root):
    """
    (n: int, graph: List[List[int]], root: int) -> Tuple[List[int], List[int], List[int]]:

    :param n: the number of vertex points
    :param graph: 2D matrix of N vertices given by the edges
    :param root: start node index

    :return tour: order of visited vertex
    :return in_time: first time of each vertex
    :return out_time: last time of each vertex

    example:
    graph = [[] for _ in range(n)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tour, in_time, out_time = EulerTour(n, graph, 0)
    """

    parent = [-1] * n
    stack = [~root, root]  # postorder, preorder
    curr_time = -1
    tour = []
    in_time = [-1] * n
    out_time = [-1] * n
    while stack:
        curr_node = stack.pop()
        curr_time += 1
        if curr_node >= 0:  # preorder
            tour.append(curr_node)
            if in_time[curr_node] == -1:
                in_time[curr_node] = curr_time

            for next_node in graph[curr_node]:
                if next_node != parent[curr_node]:
                    parent[next_node] = curr_node
                    # for i in range(len(graph[next_node])):
                    #    next_next_node = graph[next_node][i]
                    #    if next_next_node == curr_node:
                    #        del graph[next_node][i]
                    #        break
                    stack.append(~next_node)
                    stack.append(next_node)
        elif curr_node < 0:  # postorder
            out_time[~curr_node] = curr_time
            if parent[~curr_node] != -1:
                tour.append(parent[~curr_node])

    return tour, in_time, out_time


n = int(input())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i] = sorted(graph[i])

tour, in_time, out_time = EulerTour(n, graph, 0)

tour = [i + 1 for i in tour]
print(*tour)

"""
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
"""
