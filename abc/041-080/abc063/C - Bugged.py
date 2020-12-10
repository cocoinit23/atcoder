n = int(input())
s = sorted([int(input()) for _ in range(n)])

ans = sum(s)
if ans % 10 != 0:
    print(ans)
else:
    cnt = 0
    for i in s:
        if i % 10 == 0:
            cnt += 1
        else:
            ans -= i
            print(ans)
            break

    if cnt == n:
        print(0)
