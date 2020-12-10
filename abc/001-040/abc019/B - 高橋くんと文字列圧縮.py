s = input()

ans = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cnt += 1
    else:
        ans += str(cnt)
        cnt = 1
        ans += s[i]

ans += str(cnt)
print(ans)
