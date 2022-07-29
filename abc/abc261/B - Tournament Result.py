n = int(input())

a = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        x = a[i][j]
        y = a[j][i]
        if (x == 'W' and y != 'L') or (x == 'L' and y != 'W') or (x == 'D' and y != 'D'):
            print('incorrect')
            exit()

print('correct')
