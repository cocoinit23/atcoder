n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(q)]

A = []


def dfs(num):
    if len(num) == n:
        A.append(num)
    else:
        now = num[-1]
        for i in range(now, m + 1):
            dfs(num + [i])


for i in range(1, 10):
    dfs([i])

ans = 0
for now in A:
    point = 0
    for a, b, c, d in abcd:
        if now[b-1] - now[a-1] == c:
            point += d

    ans = max(ans, point)

print(ans)
