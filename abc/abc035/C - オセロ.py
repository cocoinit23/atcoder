n, q = map(int, input().split())

count = [0] * (n + 1)
for _ in range(q):
    l, r = map(int, input().split())
    count[l - 1] += 1
    count[r] -= 1

ans = [0] * n
ans[0] = count[0] % 2
for i in range(n - 1):
    ans[i + 1] = (ans[i] + count[i + 1]) % 2

print(''.join(map(str, ans)))
