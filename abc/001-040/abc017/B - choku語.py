x = input()

ans = True
if x == '':
    pass
else:
    i = 0
    while i < len(x):
        if x[i] == 'o' or x[i] == 'k' or x[i] == 'u':
            i += 1
        elif x[i:i + 2] == 'ch':
            i += 2
        else:
            ans = False
            break

print('YES') if ans else print('NO')
