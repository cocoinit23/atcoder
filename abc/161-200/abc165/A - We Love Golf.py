k = int(input())
a, b = map(int, input().split())

flag = False
for i in range(a, b + 1):
    if i % k == 0:
        flag = True
        break

print('OK') if flag else print('NG')
