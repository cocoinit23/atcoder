n, k = map(int, input().split())

if k < 0:
    k = -k

combi = [0] * (2 * n + 1)
for i in range(2, 2 * n + 1):
    combi[i] = min(i - 1, 2 * n - i + 1)

ans = 0
for i in range(k, 2 * n + 1):
    ans += combi[i] * combi[i - k]

print(ans)
