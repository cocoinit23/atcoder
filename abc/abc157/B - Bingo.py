a = []
for i in range(3):
    a += map(int, input().split())

n = int(input())

for i in range(n):
    b = int(input())
    for j in range(9):
        if b == a[j]:
            a[j] = 'o'

isBingo = False
bingo = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
for elem in bingo:
    if a[elem[0]] == 'o' and a[elem[1]] == 'o' and a[elem[2]] == 'o':
        isBingo = True
        break

print('Yes') if isBingo else print('No')
