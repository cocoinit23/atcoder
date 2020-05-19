a, b, c, d = map(int, input().split())

ans = [0] * 110

for i in range(a, b):
    ans[i] += 1
for j in range(c, d):
    ans[j] += 1

print(ans.count(2))
