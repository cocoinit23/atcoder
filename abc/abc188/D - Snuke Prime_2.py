n, x = map(int, input().split())

event = []
service = []
for _ in range(n):
    a, b, v = map(int, input().split())
    a -= 1
    event.append(a)
    event.append(b)
    service.append([a, b, v])

event.sort()
compress = {a: i for i, a in enumerate(event)}

imos = [0] * len(event)
for a, b, c in service:
    imos[compress[a]] += c
    imos[compress[b]] -= c

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

ans = 0
for i in range(len(imos) - 1):
    diff = event[i + 1] - event[i]
    ans += min(x, imos[i]) * diff

print(ans)
