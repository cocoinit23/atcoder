x, y = map(int, input().split())

if x != y:
    ans = 3 - x - y
else:
    ans = x

print(ans)
