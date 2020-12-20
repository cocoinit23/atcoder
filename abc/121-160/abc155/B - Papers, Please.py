n = int(input())
a = [int(x) for x in input().split()]

flag = True
for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 != 0 and a[i] % 5 != 0:
            flag = False
            break

print('APPROVED') if flag else print('DENIED')
