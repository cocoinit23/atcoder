from itertools import combinations

n, k = map(int, input().split())
a = [int(x) for x in input().split()]

combi = list(combinations(a, 2))

ans = []
for x, y in combi:
    ans.append(x * y)

ans = sorted(ans)
print(ans[k - 1])
