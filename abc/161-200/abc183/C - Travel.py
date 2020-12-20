import itertools

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

all = itertools.permutations(range(1, n))

ans = 0
for x in all:
    now = 0
    temp = 0
    for i in x:
        temp += t[now][i]
        now = i
        if temp > k:
            break
    temp += t[now][0]
    if temp == k:
        ans += 1

print(ans)
