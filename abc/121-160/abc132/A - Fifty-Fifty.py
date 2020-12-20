s = input()
s = sorted(s)

if s[0] != s[1] or s[2] != s[3] or s[0] == s[3]:
    print('No')
else:
    print('Yes')
