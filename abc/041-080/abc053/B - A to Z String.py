s = input()
n = len(s)

l = 0
r = 0

for i in range(n):
    if s[i] == 'A':
        l = i
        break

for i in reversed(range(n)):
    if s[i] == 'Z':
        r = i
        break

ans = len(s[l:r + 1])
print(ans)
