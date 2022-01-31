h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

rowsum = [sum(i) for i in a]
colsum = []
for i in range(w):
    val = 0
    for j in range(h):
        val += a[j][i]
    colsum.append(val)

ans = []
for i in range(h):
    temp = []
    for j in range(w):
        val = rowsum[i] + colsum[j] - a[i][j]
        temp.append(val)
    ans.append(temp)

for i in ans:
    print(*i)
