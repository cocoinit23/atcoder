import math

x = int(input())

while True:
    flag = True
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            flag = False

    if flag:
        print(x)
        exit()
    else:
        x += 1
