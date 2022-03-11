n, q = map(int, input().split())
x = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


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
                    stack.append(~next_node)
                    stack.append(next_node)
        elif curr_node < 0:  # postorder
            out_time[~curr_node] = curr_time
            if parent[~curr_node] != -1:
                tour.append(parent[~curr_node])

    return tour, in_time, out_time



tour, in_time, out_time = EulerTour(n, graph, 0)


class SegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele for i in range(2 * self.num)]
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(
                self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(
                self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def segfunc(x, y):
    if x[0] > y[0]:
        return x
    else:
        return y


ide_ele = (-1, -1)  # value, in_time

init_list = [ide_ele] * len(tour)
st = SegmentTree(init_list, segfunc, ide_ele)
for i in range(n):
    st.update(in_time[i], (x[i], in_time[i]))

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    start = in_time[v]
    end = out_time[v]
    buffer = []
    for i in range(k):
        value_time_tuple = st.query(start, end)
        buffer.append(value_time_tuple)
        st.update(value_time_tuple[1], ide_ele)

    value_time_tuple = st.query(start, end)
    ans = value_time_tuple[0]
    print(ans)

    for value_time_tuple in buffer:
        st.update(value_time_tuple[1], value_time_tuple)

"""
import sys

sys.setrecursionlimit(300000)

n, q = map(int, input().split())
x = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
subtree_value = [[] for _ in range(n)]


def dfs(curr):
    visited[curr] = True
    val = [x[curr]]
    for node in graph[curr]:
        if not visited[node]:
            val += dfs(node)
            if len(val) > 20:
                val.sort(reverse=True)
                val = val[:20]

    subtree_value[curr] = sorted(val, reverse=True)

    return val


dfs(0)

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    ans = subtree_value[v][k]
    print(ans)
"""
