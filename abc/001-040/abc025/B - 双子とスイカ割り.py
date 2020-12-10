n, a, b = map(int, input().split())

ans = 0
for _ in range(n):
    s, d = input().split()
    d = int(d)

    if s == 'East':
        sign = 1
    else:
        sign = -1

    if d < a:
        d = a
    elif d > b:
        d = b

    ans += sign * d

if ans < 0:
    print('West', abs(ans))
elif ans > 0:
    print('East', ans)
else:
    print(0)
