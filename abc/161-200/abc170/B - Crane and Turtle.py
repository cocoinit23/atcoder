x, y = map(int, input().split())

for i in range(101):
    for j in range(101):
        if i + j == x and 2 * i + 4 * j == y:
            print('Yes')
            exit()

print('No')
