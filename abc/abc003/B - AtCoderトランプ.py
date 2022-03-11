s = input()
t = input()
n = len(s)

for i in range(n):
    if s[i] != t[i]:
        if s[i] != '@' and t[i] != '@':
            print('You will lose')
            exit()
        elif s[i] == '@' and t[i] not in 'atcoder':
            print('You will lose')
            exit()
        elif t[i] == '@' and s[i] not in 'atcoder':
            print('You will lose')
            exit()

print('You can win')

