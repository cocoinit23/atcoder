from collections import deque

n, m, s = map(int, input().split())

tree = [[] for _ in range(n+1)]
for i in range(m):
    u, v, a, b = map(int, input().split())
    tree[u].append([v, a, b])

cd = [[]]
for i in range(n):
    cd.append(list(map(int, input().split())))

print(tree)
print(cd)
