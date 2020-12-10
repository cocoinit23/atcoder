k = int(input())

if k % 2 == 0 or k % 5 == 0:
    print(-1)
else:
    ans = 1
    num = 7
    while True:
        if num % k == 0:
            print(ans)
            break
        else:
            ans += 1
            num += 7 * pow(10, ans - 1, k)
            num %= k
