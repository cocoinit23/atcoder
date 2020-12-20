n = int(input())

ans = 1
cnt = 0
for i in range(1, n + 1):
    count = 0
    temp = i
    while temp % 2 == 0:
        count += 1
        temp //= 2

    if cnt < count:
        cnt = count
        ans = i

print(ans)
