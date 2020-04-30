n = int(input())

ans = 999
for i in range(1, 9):
    val = i * 111
    if val >= n:
        ans = min(ans, val)

print(ans)
