s = list(input())

ans = ''
for i in s:
    if i == 'B':
        if len(ans) > 0:
            ans = ans[:-1]
        else:
            continue
    else:
        ans += i

print(ans)
