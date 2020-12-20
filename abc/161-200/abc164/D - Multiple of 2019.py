s = input()
n = len(s)

mod = 2019
cnt = [0] * mod
cnt[0] = 1
digit = 1
now = 0

for i in range(1, n + 1):
    now += int(s[-i]) * digit
    digit *= 10
    digit %= mod
    now %= mod
    cnt[now] += 1

ans = 0
for i in cnt:
    ans += i * (i - 1) // 2

print(ans)
