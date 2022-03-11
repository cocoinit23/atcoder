n = int(input())
p = [x for x in map(int, input().split())]

memo = []

for i in range(1, n):
    if p[i - 1] > p[i]:
        memo.append(i)

flag = True

if len(memo) >= 3:
    flag = False
elif len(memo) == 0:
    flag = True
elif len(memo) == 1:
    pp = p
    pp[memo[0] - 1], pp[memo[0]] = pp[memo[0]], pp[memo[0] - 1]
    for i in range(1, n):
        if pp[i - 1] > pp[i]:
            flag = False
            break
elif len(memo) == 2:
    pp = p
    pp[memo[0] - 1], pp[memo[1]] = pp[memo[1]], pp[memo[0] - 1]
    for i in range(1, n):
        if pp[i - 1] > pp[i]:
            flag = False
            break

print('YES') if flag else print('NO')
