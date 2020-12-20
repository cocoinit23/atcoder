n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = x
for i in a:
    if d % i == 0:
        ans += d // i
    else:
        ans += d // i + 1

print(ans)
