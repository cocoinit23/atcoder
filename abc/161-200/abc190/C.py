n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

pattern = []
for i in range(2 ** k):
    temp = [0] * k
    for j in range(k):
        if i >> j & 1:
            temp[j] = 1
    pattern.append(temp)

ans = 0
for p in pattern:
    dish = [0] * (n + 1)
    for i, j in zip(cd, p):
        dish[i[j]] = 1
    val = 0
    for a, b in ab:
        if dish[a] == dish[b] == 1:
            val += 1
    ans = max(ans, val)

print(ans)
