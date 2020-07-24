n = int(input())

ans = [0] * (10 ** 4 + 1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            s = x * x + y * y + z * z + x * y + y * z + z * x
            if s <= 10 ** 4:
                ans[s] += 1

for i in range(1, n + 1):
    print(ans[i])
