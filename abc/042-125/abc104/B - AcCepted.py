s = input()

flag = True

if s[0] != 'A' or s.count('C') != 1 or s[2:-1].count('C') != 1:
    flag = False
else:
    for i in range(1, len(s)):
        if s[i] != 'C' and s[i].isupper():
            flag = False

print('AC') if flag else print('WA')
