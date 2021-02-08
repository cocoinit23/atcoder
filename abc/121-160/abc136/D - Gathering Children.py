s = list(input())
n = len(s)

ans = [0] * n

cnt = 0
for i in range(n):
    if s[i] == "R":
        cnt += 1
    else:
        even = cnt // 2
        odd = cnt - even
        ans[i] += even
        ans[i - 1] += odd
        cnt = 0

for i in range(n - 1, -1, -1):
    if s[i] == "L":
        cnt += 1
    else:
        even = cnt // 2
        odd = cnt - even
        ans[i] += even
        ans[i + 1] += odd
        cnt = 0

print(*ans)
