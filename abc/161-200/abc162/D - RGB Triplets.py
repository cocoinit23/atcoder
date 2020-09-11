n = int(input())
s = list(input())

r = sum([1 for x in s if x == 'R'])
g = sum([1 for x in s if x == 'G'])
b = sum([1 for x in s if x == 'B'])
ans = r * g * b

for i in range(n):
    for j in range(i + 1, n):
        k = 2 * j - i
        if j < k <= n - 1:
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1

print(ans)
