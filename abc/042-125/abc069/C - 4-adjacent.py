n = int(input())
a = list(map(int, input().split()))

even = sum([1 for i in a if i % 2 == 0])
odd = sum([1 for i in a if i % 2 != 0])
multiple4 = sum([1 for i in a if i % 4 == 0])

flag = False
if even - multiple4 == 0:
    if multiple4 >= odd - 1:
        flag = True
else:
    if multiple4 >= odd:
        flag = True

print('Yes') if flag else print('No')
