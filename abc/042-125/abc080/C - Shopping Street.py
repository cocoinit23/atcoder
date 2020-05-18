n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

pattern = []
for i in range(2 ** 10):
    temp = [0] * 10
    for j in range(10):
        if (i >> j) & 1:
            temp[j] = 1
    pattern.append(temp)
pattern.remove([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

ans = -10 ** 10
for i in range(len(pattern)):
    my_store = pattern[i]
    profit = 0
    for j in range(n):
        same_open = [x & y for (x, y) in zip(pattern[i], f[j])]
        profit += p[j][sum(same_open)]
    ans = max(ans, profit)

print(ans)
