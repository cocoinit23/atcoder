s = input()
k = int(input())
n = len(s)
ans = []
for i in range(n - k + 1):
    sub = s[i:i + k]
    ans.append(sub)

ans = len(set(ans))
print(ans)
