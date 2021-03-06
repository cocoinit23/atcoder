from typing import List
from functools import reduce
import math


def gcd(int_list: List[int]) -> int:
    return reduce(math.gcd, int_list)


def lcm(int_list: List[int]) -> int:
    return reduce(lambda x, y: (x * y) // math.gcd(x, y), int_list)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def warshall_floyd(graph):
    # graph: compressed sparse graph, N x N array of distances
    # Pypy is faster due to nested loop
    n = len(graph)

    for i in range(n):
        graph[i][i] = 0

    for i in range(n):  # via point
        for j in range(n):  # start
            for k in range(n):  # goal
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    return graph


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


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.parent[self.find(x)]
