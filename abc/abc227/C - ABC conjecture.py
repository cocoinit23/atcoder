n = int(input())

ans = 0

for a in range(1, n + 1):
    if a ** 3 > n:
        break

    for b in range(a, n + 1):
        if a * b * b > n:
            break

        ans += n // a // b - b + 1

print(ans)
