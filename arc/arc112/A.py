t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if 2 * l > r:
        print(0)
    else:
        ans = (r - 2 * l + 1) * (r - l) // 2
        print(ans)
