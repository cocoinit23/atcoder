from typing import List, Tuple
from functools import reduce
import math

import bisect


def gcd(int_list):
    """
    :param int_list: List[int]
    :return: int, greatest common divisor
    """
    return reduce(math.gcd, int_list)


def lcm(int_list):
    """
    lcm = x * y / gcd(x,y)
    :param int_list: List[int]
    :return: int, least common multiple
    """
    return reduce(lambda x, y: (x * y) // math.gcd(x, y), int_list)


def sieve_of_eratosthenes(n):
    """
    :param n: counting limit
    :return: List[int], prime numbers
    """
    if n <= 1:
        raise ValueError
        # return []

    prime = [2]
    limit = int(n ** 0.5)
    data = [i for i in range(3, n + 1, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [i for i in data if i % data[0] != 0]

    return prime + data


def make_divisors(n):
    """
    :param n: int
    :return: List[int], divisors
    """
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

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.parent[self.find(x)]


def base_10_to_n(x: int, n: int) -> str:
    if int(x / n):
        return base_10_to_n(int(x / n), n) + str(x % n)
    return str(x % n)


def base_n_to_10(x: str, n: int) -> int:
    out = 0
    for i in range(1, len(str(x)) + 1):
        out += int(x[-i]) * (n ** (i - 1))
    return out


def EulerTour(n, graph, root):
    """
    (n: int, graph: List[List[int]], root: int) -> Tuple[List[int], List[int], List[int]]:

    :param n: the number of vertex points
    :param graph: 2D matrix of N vertices given by the edges
    :param root: start node index

    :return tour: order of visited vertex
    :return in_time: first visiting time of each vertex
    :return out_time: last visiting time of each vertex

    example:
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

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
                    stack.append(~next_node)
                    stack.append(next_node)
        elif curr_node < 0:  # postorder
            out_time[~curr_node] = curr_time
            if parent[~curr_node] != -1:
                tour.append(parent[~curr_node])

    return tour, in_time, out_time


class SegmentTree:
    """
    1-index is preferred because
        1. the number of digits is equal to the depth of tree.
        2. the parent can be obtained by right shift of child.
                0001
               /   \
            0010   0011
            / \     / \
        0100 0101 0110 0111

    examples of operator and identity:
        min, float('inf')
        max, -float('inf')
        lambda x,y:x+y, 0
        lambda x,y:x*y, 1
        math.gcd, 0
    """

    def __init__(self, array, operator, identity):
        n = len(array)
        self.offset = 2 ** (n - 1).bit_length()
        self.operator = operator
        self.identity = identity
        self.tree = [identity] * (2 * self.offset)

        # building segment tree
        for i, val in enumerate(array):
            self.set(i, val)

    def set(self, idx, value):
        idx += self.offset
        self.tree[idx] = value

        while idx > 1:
            # get parent
            idx >>= 1
            # update parent by its child
            left = 2 * idx
            right = 2 * idx + 1
            self.tree[idx] = self.operator(self.tree[left], self.tree[right])

    def get(self, left, right):
        left += self.offset
        right += self.offset
        result = self.identity

        while left <= right:
            if left & 1:
                result = self.operator(result, self.tree[left])
                left += 1
            if right & 0:
                result = self.operator(result, self.tree[right])
                right -= 1

            left >>= 1
            right >>= 1

        return result
