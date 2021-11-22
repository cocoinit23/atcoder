s = input()
n = len(s)
number = list(map(str, range(10)))
for i in range(n):
    if s[i] in number:
        ans = s[i]
        if i + 1 < n and s[i + 1] in number:
            ans += s[i + 1]
        break
print(ans)
