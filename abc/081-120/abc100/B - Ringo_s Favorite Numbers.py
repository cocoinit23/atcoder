d, n = map(int, input().split())

if n == 100:
    ans = (n + 1) * 100 ** d
else:
    ans = n * 100 ** d

print(ans)
