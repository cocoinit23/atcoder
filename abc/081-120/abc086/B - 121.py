a, b = input().split()

flag = False
for i in range(1000):
    if i * i == int(a + b):
        flag = True
        break

print('Yes') if flag else print('No')
