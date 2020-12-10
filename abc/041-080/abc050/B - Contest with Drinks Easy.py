n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

for p, x in px:
    ans = 0
    for i in range(n):
        if i == p - 1:
            ans += x
        else:
            ans += t[i]
    print(ans)
