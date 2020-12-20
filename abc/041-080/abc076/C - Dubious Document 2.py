s = input()
t = input()

n = len(s)
m = len(t)

if t in s:
    print(s.replace('?', 'a'))
else:
    ans = []
    for i in range(n - m + 1):
        bubun = s[i:i + m]
        flag = True
        for j in range(m):
            x = bubun[j]
            y = t[j]
            if x == y:
                continue
            elif x == '?':
                continue
            else:
                flag = False
                break

        if flag:
            ans.append((s[:i] + t + s[i + m:]).replace('?', 'a'))

    print(sorted(ans)[0]) if ans else print('UNRESTORABLE')
