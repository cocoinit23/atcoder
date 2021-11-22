n, m = map(int, input().split())
a = [list(input()) for _ in range(2 * n)]
rank = [[0, i] for i in range(2 * n)]


def battle(x, y):
    if x == y:
        return -1
    elif (x == 'G' and y == 'C') or (x == 'C' and y == 'P') or (x == 'P' and y == 'G'):
        return 0
    else:
        return 1


for i in range(m):
    for j in range(n):
        p1 = rank[2 * j][1]
        p2 = rank[2 * j + 1][1]

        result = battle(a[p1][i], a[p2][i])

        if result == 0:
            rank[2 * j][0] -= 1
        elif result == 1:
            rank[2 * j + 1][0] -= 1

    rank.sort()

for _, i in rank:
    print(i + 1)
