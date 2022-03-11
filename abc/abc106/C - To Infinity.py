s = input()
k = int(input())

limit = min(100, k)

ans = 1
for i in range(limit):
    if s[i] != '1':
        ans = s[i]
        break

print(ans)