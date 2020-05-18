x, y = map(int, input().split())

ans = 1
while 2 * x <= y:
    ans += 1
    x *= 2

print(ans)
