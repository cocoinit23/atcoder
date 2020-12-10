n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    while i % 2 == 0 or i % 3 == 2:
        if i % 2 == 0:
            i -= 1
            ans += 1
        if i % 3 == 2:
            i -= 1
            ans += 1

print(ans)
