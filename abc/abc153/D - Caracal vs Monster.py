import math

h = int(input())
memo = [0]
cnt = 0

while h > 1:
    cnt += 1
    memo.append(cnt)
    h = math.floor(h / 2)

ans = 0
for i in range(len(memo)):
    ans += 2 ** memo[i]

print(ans)
