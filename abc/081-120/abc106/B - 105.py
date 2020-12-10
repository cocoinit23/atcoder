n = int(input())

ans = 0

for i in range(105, n + 1, 2):
    divisor = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            divisor.append(j)
            divisor.append(i // j)

    if len(divisor) == 8:
        ans += 1

print(ans)
