n = input()
a = len(n) // 2
x = n[:a]
y = n[a:]

if len(x) != len(y):
    ans = 10 ** (len(y) - 1) - 1
else:
    ans = int(x)
    if int(x) > int(y):
        ans -= 1

print(ans)
