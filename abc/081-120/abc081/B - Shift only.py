n = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        flag = True
        if a[i] % 2 != 0:
            flag = False
            break
        else:
            a[i] /= 2

    if flag:
        ans += 1
    else:
        break

print(ans)
