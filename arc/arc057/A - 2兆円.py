a, k = map(int, input().split())
goal = 2 * 10 ** 12

ans = 0
if k == 0:
    ans = goal - a
else:
    while a < goal:
        a += 1 + k * a
        ans += 1
print(ans)
