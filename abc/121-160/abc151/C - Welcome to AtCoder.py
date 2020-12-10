n, m = map(int, input().split())

submit = []
for i in range(m):
    temp = [x for x in input().split()]
    submit.append(temp)

ac = [0] * (n + 1)
wa = [0] * (n + 1)

for i in range(m):
    result = submit[i][1]
    question = int(submit[i][0])

    if result == 'AC' and ac[question] == 0:
        ac[question] = 1
    elif result == 'WA' and ac[question] == 0:
        wa[question] += 1

for i in range(n + 1):
    if ac[i] != 1:
        wa[i] = 0

print(sum(ac), sum(wa))
