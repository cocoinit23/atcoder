n, x, t = map(int, input().split())

if n % x == 0:
    ans = n // x
else:
    ans = n // x + 1

ans *= t
print(ans)