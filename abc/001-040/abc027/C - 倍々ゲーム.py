import math

n = int(input())

depth = int(math.log2(n)) + 1

x = 1
turn = 0
depth %= 2

while x <= n:
    if turn + depth == 1:
        x = 2 * x + 1
    else:
        x = 2 * x

    turn = (turn + 1) % 2
    ans = ['Takahashi', 'Aoki'][turn]

print(ans)
