n, k = map(int, input().split())
ab = sorted(list(map(int, input().split())) for _ in range(n))

count = 0
for a, b in ab:
    count += b
    if count >= k:
        print(a)
        break
