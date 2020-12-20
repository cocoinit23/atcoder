s = [int(x) for x in list(map(str, input()))]

ans = 0

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ans += 1
        s[i] = 1 - s[i - 1]

print(ans)
