n = int(input())
a = list(map(int, input().split()))

increase = [1 if a[i + 1] - a[i] > 0 else 0 for i in range(n - 1)]

if sum(increase) == n - 1:
    ans = (n + 1) * n // 2
else:
    ans = n
    count = 0
    for i in range(len(increase)):
        if increase[i] == 1:
            if i == len(increase) - 1:
                count += 1
                ans += (1 + count) * count // 2
            else:
                count += 1
        else:
            ans += (1 + count) * count // 2
            count = 0

print(ans)
