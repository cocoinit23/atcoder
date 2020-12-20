n = int(input())
a = list(map(int, input().split()))

check = 1
ans = 0

for i in range(n):
    if a[i] == check:
        check += 1
        ans += 1

if ans == 0:
    print(-1)
else:
    print(n - ans)
