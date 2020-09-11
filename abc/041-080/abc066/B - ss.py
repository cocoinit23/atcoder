s = input()

ans = 0
for i in range(1, len(s)):
    temp = s[:-i]
    n = len(temp) // 2
    if temp[:n] == temp[n:]:
        ans = max(ans, len(temp))

print(ans)
