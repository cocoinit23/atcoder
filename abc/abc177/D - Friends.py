n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]


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


uf = UnionFind(n)

for a, b in ab:
    uf.union(a, b)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, uf.count(i))

print(ans)
