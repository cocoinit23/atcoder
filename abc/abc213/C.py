h, w, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

a = sorted(set([i[0] for i in ab]))
a_map = {j: i + 1 for i, j in enumerate(a)}
ab = [[a_map[i], j] for i, j in ab]

b = sorted(set([i[1] for i in ab]))
b_map = {j: i + 1 for i, j in enumerate(b)}
ab = [[i, b_map[j]] for i, j in ab]

for i in ab:
    print(*i)
