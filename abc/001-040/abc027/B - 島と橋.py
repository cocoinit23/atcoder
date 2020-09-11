n = int(input())
a = list(map(int, input().split()))

if sum(a) % n != 0:
    print(-1)
else:
    ans = 0
    for i in range(1, n):
        left = a[:i]
        right = a[i:]
        if sum(left) / len(left) != sum(right) / len(right):
            ans += 1

    print(ans)
