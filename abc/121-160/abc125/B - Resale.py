n = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

diff = [x - y for (x, y) in zip(v, c)]
ans = sum([x for x in diff if x > 0])
print(ans)
