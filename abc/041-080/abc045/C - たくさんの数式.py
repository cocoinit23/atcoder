s = list(input())
n = len(s)

pattern = []
for i in range(2 ** (n - 1)):
    temp = [0] * (n - 1)
    for j in range(n - 1):
        if (i >> j) & 1:
            temp[j] = 1
    pattern.append(temp)

ans = 0
for p in pattern:
    sum = s[0]
    for i in range(n - 1):
        if p[i]:
            sum += '+'
        sum += s[i + 1]
    ans += eval(sum)

print(ans)
