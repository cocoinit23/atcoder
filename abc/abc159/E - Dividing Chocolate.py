h, w, k = map(int, input().split())
area = h * w

if area <= 2 * k:
    print(0)
elif k == 1:
    print(area)
else:
    ans = 0

    while area >= k:
        ans += 1
        area //= k

    print(ans) if area % k == 0 else print(ans + 1)
