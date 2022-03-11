n = int(input())

money = 0
ans = 1
while money < n:
    money += ans
    ans += 1

print(ans - 1)
