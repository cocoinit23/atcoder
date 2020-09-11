s = input()
k = int(input())
n = len(s)

s = list(s)
ans = []
for i in range(n + 1):
    for j in range(i + 1, min(i + 1 + k, n + 1)):
        ans.append(str(''.join(s[i:j])))

ans = sorted(list(set(ans)))
print(ans[k - 1])
