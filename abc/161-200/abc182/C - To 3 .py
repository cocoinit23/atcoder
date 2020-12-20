n = input()
k = len(n)

ans = 10 ** 10
for i in range(1, 2 ** k):
    pattern = [0] * k
    for j in range(k):
        if (i >> j) & 1:
            pattern[j] = 1

    temp = 0
    for p, q in zip(pattern, n):
        temp += p * int(q)
    if temp % 3 == 0:
        ans = min(ans, k - sum(pattern))

print(ans if ans != 10 ** 10 else -1)
