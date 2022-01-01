x, n = map(int, input().split())
p = list(map(int, input().split()))

if n == 0:
    print(x)
else:
    num = list(set(range(-200, 200)) ^ set(p))
    num = sorted([[abs(i - x), i] for i in num])
    if len(num) >= 2 and num[0][0] == num[1][0]:
        print(min(num[0][1], num[1][1]))
    else:
        print(num[0][1])
