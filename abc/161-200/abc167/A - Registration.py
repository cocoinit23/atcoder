s = input()
t = input()

if len(s) + 1 == len(t) and s == t[:-1]:
    print('Yes')
else:
    print('No')