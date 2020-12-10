s = input()

n = len(s)

sum = 0

l = s[:n // 2]
l = [x for x in l]
r = s[n // 2:]
r = [x for x in reversed(r)]

for (x, y) in zip(l, r):
    if x != y:
        sum += 1

print(sum)
