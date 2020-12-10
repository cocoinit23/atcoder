n, k = map(int, input().split())

ans = 0

for i in range(1, n + 1):
    count = 0
    point = i
    while point < k:
        point *= 2
        count += 1

    ans += 1 / n * (0.5 ** count)

print(ans)
