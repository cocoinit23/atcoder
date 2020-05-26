n = int(input())
a = list(map(int, input().split()))

ans1 = 0
total1 = 0
sign1 = True
for i in a:
    total1 += i
    if sign1 and total1 < 0:
        ans1 += abs(total1) + 1
        total1 = 1
    elif not sign1 and total1 > 0:
        ans1 += abs(total1) + 1
        total1 = -1
    elif sign1 and total1 == 0:
        ans1 += 1
        total1 = 1
    elif not sign1 and total1 == 0:
        ans1 += 1
        total1 = -1
    else:
        pass

    sign1 = not sign1

ans2 = 0
total2 = 0
sign2 = False
for j in a:
    total2 += j
    if sign2 and total2 < 0:
        ans2 += abs(total2) + 1
        total2 = 1
    elif not sign2 and total2 > 0:
        ans2 += abs(total2) + 1
        total2 = -1
    elif sign2 and total2 == 0:
        ans2 += 1
        total2 = 1
    elif not sign2 and total2 == 0:
        ans2 += 1
        total2 = -1
    else:
        pass

    sign2 = not sign2

print(min(ans1, ans2))
