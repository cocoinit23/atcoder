s = input()
k = int(input())
n = len(s)

pl = 0
pr = 0
ans = 0
temp = 0
replace = k

while pr < n:
    l = s[pl]
    r = s[pr]

    if r == 'X':
        temp += 1
        pr += 1
    elif r == '.' and replace > 0:
        temp += 1
        pr += 1
        replace = max(replace - 1, 0)
    else:
        if pr == pl:
            pr += 1
        else:
            pl += 1
            temp = max(temp - 1, 0)
            if l == '.':
                replace = min(replace + 1, k)

    ans = max(ans, temp)

print(ans)
