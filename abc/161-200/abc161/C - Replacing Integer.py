n, k = map(int, input().split())

n %= k
n = min(n, abs(n - k))
print(n)
