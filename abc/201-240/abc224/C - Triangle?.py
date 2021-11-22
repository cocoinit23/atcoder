from itertools import combinations

n = int(input())

coord = [list(map(int, input().split())) for _ in range(n)]

combi = combinations(range(n), 3)

ans = 0
for i, j, k in combi:
    x1, y1 = coord[i]
    x2, y2 = coord[j]
    x3, y3 = coord[k]

    if x1 == x2 == x3 or y1 == y2 == y3:
        continue
    elif (x3 - x2) * (y2 - y1) == (x2 - x1) * (y3 - y2):
        continue
    else:
        ans += 1

print(ans)
