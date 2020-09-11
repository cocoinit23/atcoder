n = int(input())
limit = int(n ** 0.5 + 1)

ans = 10 ** 10
for i in range(1, limit):
    if n % i == 0:
        f = max(len(str(i)), len(str(n // i)))
        ans = min(ans, f)

print(ans)
