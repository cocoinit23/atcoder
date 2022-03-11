n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10 ** 10
for i in range(n - k + 1):
    left = x[i]
    right = x[i + k - 1]
    ans = min(ans, abs(left) + abs(right - left), abs(right) + abs(right - left))

print(ans)
