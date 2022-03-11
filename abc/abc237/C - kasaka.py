s = input()
n = len(s)

l = 0
r = n - 1

while s[l] == s[r] == 'a' and l < r:
    l += 1
    r -= 1

while s[r] == 'a' and l < r:
    r -= 1

while l < r:
    if s[l] != s[r]:
        break

    l += 1
    r -= 1

print('Yes' if l >= r else 'No')
