n = int(input())
h = [int(x) for x in input().split()]
h.reverse()

flag = True

for i in range(1, n):
    if h[i - 1] >= h[i]:
        continue
    elif h[i] == h[i - 1] + 1:
        h[i] -= 1
    else:
        flag = False
        break

print('Yes') if flag else print('No')
