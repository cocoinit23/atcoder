n = int(input())
x = []

aoki = 0
takahashi = 0

for _ in range(n):
    a, b = map(int, input().split())
    x.append([a, b, a + a + b])
    aoki += a

x.sort(key=lambda x: (x[2]), reverse=True)

ans = 0
for a, b, _ in x:
    if aoki < takahashi:
        break

    aoki -= a
    takahashi += a + b
    ans += 1

print(ans)
