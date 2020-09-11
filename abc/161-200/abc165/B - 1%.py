x = int(input())

now = 100
ans = 0
while now < x:
    ans += 1
    now = int(now * 1.01)

print(ans)
