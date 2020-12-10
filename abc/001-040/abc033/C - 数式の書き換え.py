ans = 0
for s in input().split('+'):
    if '*' in s:
        if not '0' in s:
            ans += 1
    else:
        if s != '0':
            ans += 1

print(ans)
