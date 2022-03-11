x, y, a, b = map(int, input().split())

ans = 0
while x < y:
    if x * a > y and x + b > y:
        break

    if x * a < y and x * a <= x + b:
        x *= a
        ans += 1
    else:
        if (y - x) % b == 0:
            ans += (y - x) // b - 1
        else:
            ans += (y - x) // b
        break

print(ans)
