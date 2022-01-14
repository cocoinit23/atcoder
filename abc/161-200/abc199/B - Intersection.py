n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = max(a)
y = min(b)

if x > y:
    ans = 0
else:
    ans = y - x + 1

print(ans)
