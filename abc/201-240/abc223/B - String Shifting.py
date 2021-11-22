s = input()
n = len(s)

s *= 2

ans = []
for i in range(n):
    ans.append(s[i:i + n])

ans.sort()

print(ans[0])
print(ans[-1])
