s = input()
n = len(s)
s = [s[i] for i in range(n)]

l = (n - 1) // 2
r = (n + 3) // 2

left = s[:l]
right = s[r - 1:]

if s == list(reversed(s)) and left == list(reversed(left)) and right == list(reversed(right)):
    print('Yes')
else:
    print('No')
