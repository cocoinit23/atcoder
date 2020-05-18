n = int(input())

ans = 999
for i in range(1, 9):
    ans = i * 111
    if ans >= n:
        ans = min(ans, ans)

print(ans)
