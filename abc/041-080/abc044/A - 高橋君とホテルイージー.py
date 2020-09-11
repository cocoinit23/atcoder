n, k, x, y = list(map(int, [input() for _ in range(4)]))

ans = min(n, k) * x + max(0, n - k) * y
print(ans)
