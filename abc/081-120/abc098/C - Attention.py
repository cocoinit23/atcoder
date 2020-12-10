n = int(input())
s = input()

w = [0] * n
e = [0] * n

for i in range(n):
    if i == 0:
        if s[i] == 'W':
            w[i] = 1
            e[i] = 0
        else:
            w[i] = 0
            e[i] = 1
    else:
        if s[i] == 'W':
            w[i] = w[i - 1] + 1
            e[i] = e[i - 1]
        else:
            w[i] = w[i - 1]
            e[i] = e[i - 1] + 1

ans = 10 ** 10
for i in range(n):
    if i == 0:
        ans = min(ans, e[-1] - e[0])
    elif i == n:
        ans = min(ans, w[-1])
    else:
        right = e[-1] - e[i]
        left = w[i - 1]
        ans = min(ans, left + right)

print(ans)
