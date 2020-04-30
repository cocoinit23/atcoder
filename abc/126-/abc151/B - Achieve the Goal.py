n, k, m = map(int, input().split())
a = [int(x) for x in input().split()]

ans = m * n - sum(a)

if ans > k:
    print(-1)
else:
    print(max(ans, 0))
