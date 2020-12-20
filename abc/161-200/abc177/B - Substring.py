s = input()
t = input()

ans = 100000

n = len(s)
m = len(t)

for i in range(n - m + 1):
    temp = s[i:i + m]
    count = 0
    for a, b in zip(temp, t):
        if a != b:
            count += 1
    ans = min(count, ans)

print(ans)
