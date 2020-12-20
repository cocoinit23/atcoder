s = input()
s = list(s)

flag = 0

for i in range(len(s)):
    if i % 2 == 0 and s[i] == 'L':
        flag += 1
    elif i % 2 == 1 and s[i] == 'R':
        flag += 1

if flag > 0:
    print('No')
else:
    print('Yes')
