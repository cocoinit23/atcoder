n, x = map(int, input().split())

val = 0
ans = -1
for i in range(n):
    v, p = map(int, input().split())
    val += v * p
    if val > x * 100:
        ans = i + 1
        break
print(ans)
