n = int(input())

table = [[0] * 10 for _ in range(10)]

for i in range(1, n + 1):
    sentou = int(str(i)[0])
    matsubi = int(str(i)[-1])
    table[sentou][matsubi] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += table[i][j] * table[j][i]

print(ans)
