x = int(input())

ans = 1
for b in range(1, 100):
    for p in range(2, 100):
        if b ** p <= x:
            ans = max(ans, b ** p)

print(ans)
