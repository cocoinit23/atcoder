n, m, x = map(int, input().split())
a = list(map(int, input().split()))

cost = [0] * (n + 1)
for i in a:
    cost[i] = 1

left = cost[:x + 1]
right = cost[x:]

ans = min(sum(left), sum(right))
print(ans)
