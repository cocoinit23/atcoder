s = input()[::-1]

now = 0
while now < len(s):
    if s[now:now + 7] == 'dreamer'[::-1]:
        now += 7
    elif s[now:now + 6] == 'eraser'[::-1]:
        now += 6
    elif s[now:now + 5] == 'dream'[::-1]:
        now += 5
    elif s[now:now + 5] == 'erase'[::-1]:
        now += 5
    else:
        print('NO')
        exit()

print('YES')
