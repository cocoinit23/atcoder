n = int(input())
x = list(map(int, input().split()))

y = sorted(x)
mid1 = y[(n + 1) // 2]
mid2 = y[(n - 1) // 2]

for i in range(n):
    if mid1 == mid2:
        ans = mid1
    elif x[i] >= mid1:
        ans = mid2
    elif x[i] <= mid2:
        ans = mid1

    print(ans)
