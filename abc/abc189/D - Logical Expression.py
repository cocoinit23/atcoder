n = int(input())
s = [input() for _ in range(n)]

ans = [0] * (n + 1)
for i in range(1, n + 1):
    if s[i - 1] == "AND":
        ans[i] = max(ans[i - 1], 1)
    else:
        ans[i] = max(ans[i - 1], 1) + 2 ** i

print(ans[n])
