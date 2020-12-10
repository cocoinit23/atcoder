n, m = map(int, input().split())

if n == 1 and m == 1:
    ans = 1
elif n == 1 or m == 1:
    ans = max(n, m) - 2
else:
    ans = (n - 2) * (m - 2)

print(ans)
