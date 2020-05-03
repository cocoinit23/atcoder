a, b, c = sorted(list(map(int, input().split())))

ans = 0
if a % 2 == b % 2 == c % 2:
    ans += (c - b) // 2 + (c - a) // 2
elif a % 2 == b % 2:
    ans += 1
    a += 1
    b += 1
    ans += (c - b) // 2 + (c - a) // 2
elif a % 2 == c % 2:
    ans += 1
    a += 1
    c += 1
    ans += (c - b) // 2 + (c - a) // 2
elif c % 2 == b % 2:
    ans += 1
    c += 1
    b += 1
    ans += (c - b) // 2 + (c - a) // 2

print(ans)
