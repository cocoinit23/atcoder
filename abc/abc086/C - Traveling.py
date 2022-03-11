n = int(input())
txy = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]

flag = True
for i in range(1, n + 1):
    t = txy[i][0] - txy[i - 1][0]
    x = abs(txy[i][1] - txy[i - 1][1])
    y = abs(txy[i][2] - txy[i - 1][2])

    if not t >= x + y or not t % 2 == (x + y) % 2:
        flag = False
        break

print('Yes') if flag else print('No')
