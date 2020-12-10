import sys

s = int(input())

sequence = [s] * 1000000

i = 1
while True:
    n = sequence[i - 1]
    if n % 2 == 0:
        sequence[i] = sequence[i - 1] // 2
    else:
        sequence[i] = 3 * sequence[i - 1] + 1

    for j in range(i):
        if sequence[i] == sequence[j]:
            print(i + 1)
            sys.exit()
    i += 1
