import itertools

num = list(map(int, input().split()))

ans = []
combi = itertools.combinations(num, 3)
for c in combi:
    ans.append(sum(c))

ans = sorted(ans, reverse=True)[2]
print(ans)
