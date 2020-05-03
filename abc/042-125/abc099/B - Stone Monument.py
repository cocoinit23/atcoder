a, b = map(int, input().split())

val = [0] * 1000
for i in range(1, 1000):
    val[i] = val[i - 1] + i

n = b - a - 1
ans = val[n] - a
print(ans)
