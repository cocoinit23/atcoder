n = input()

flag = False
for s in n:
    if s == '7':
        flag = True
        break

print('Yes') if flag else print('No')
