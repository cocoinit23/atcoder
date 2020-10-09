t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

if m > n:
    print('no')
else:
    for i in b:
        temp = True
        for j in a:
            if j <= i <= j + t:
                a.remove(j)
                temp = False
                break
        if temp:
            print('no')
            exit()

    print('yes')
