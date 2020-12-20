k, n = map(int, input().split())
a = [int(x) for x in input().split()]

diff = [a[i + 1] - a[i] for i in range(n - 1)] + [k - a[-1] + a[0]]
ans = sum(diff) - max(diff)
print(ans)
