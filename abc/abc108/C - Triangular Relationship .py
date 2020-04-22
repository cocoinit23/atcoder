n, k = map(int, input().split())

ans = (n // k) ** 3

if k % 2 == 0:
    temp = 0
    for i in range(1, n + 1):
        if i % k == k // 2:
            temp += 1

    ans += temp ** 3

print(ans)
