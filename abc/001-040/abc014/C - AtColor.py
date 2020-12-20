n = int(input())
imos = [0] * (1000002)

for _ in range(n):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1

for i in range(1, 1000002):
    imos[i] += imos[i - 1]

ans = max(imos)
print(ans)
