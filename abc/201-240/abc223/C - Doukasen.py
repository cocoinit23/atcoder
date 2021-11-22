n = int(input())

ab = [list(map(int, input().split())) for _ in range(n)]

total_time = 0
for a, b in ab:
    total_time += a / b

goal = total_time / 2

ans = 0
for a, b in ab:
    if a / b < goal:
        goal -= a / b
        ans += a
    else:
        ans += b * goal
        break

print(ans)
