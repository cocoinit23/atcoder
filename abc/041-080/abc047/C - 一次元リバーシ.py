s = input()

ans = ''
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        ans += s[i - 1]

print(len(ans))
