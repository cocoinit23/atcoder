a, b = map(int, input().split())

ans = [0] * 1000
for i in range(1, 1000):
    ans[i] = ans[i - 1] + i

n = b - a - 1
ans = ans[n] - a
print(ans)
