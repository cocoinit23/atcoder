n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
now = 1
flag = False
for _ in range(n):
    ans += 1
    now = a[now - 1]
    if now == 2:
        flag = True
        break

print(ans) if flag else print(-1)
