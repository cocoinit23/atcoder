n = int(input())

flag = 0
for i in range(9):
    for j in range(9):
        if n == (i + 1) * (j + 1):
            flag += 1

if flag != 0:
    print('Yes')
else:
    print('No')
