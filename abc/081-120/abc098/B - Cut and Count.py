n = int(input())
s = input()

ans = 0
for i in range(n):
    left = s[:i]
    right = s[i:]
    match = set(left) & set(right)
    ans = max(ans, len(match))

print(ans)
