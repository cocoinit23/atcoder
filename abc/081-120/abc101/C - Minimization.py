n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
n -= k
k -= 1

if n % k == 0:
    ans += n // k
else:
    ans += n // k + 1

print(ans)
