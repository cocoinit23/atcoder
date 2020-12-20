n, x = map(int, input().split())
m = sorted(int(input()) for _ in range(n))

ans = n
x -= sum(m)

while m:
    cost = m.pop(0)
    ans += x // cost
    x %= cost

print(ans)
