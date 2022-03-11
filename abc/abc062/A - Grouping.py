x, y = map(int, input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]

for i in [a, b, c]:
    if x in i and y in i:
        print('Yes')
        exit()

print('No')
