d, g = map(int, input().split())
pc = []
for i in range(d):
    pc.append(list(map(int, input().split())))

complete = []
for i in range(2 ** d):
    temp = [0] * d
    for j in range(d):
        if (i >> j) & 1:
            temp[j] = 1
    complete.append(temp)

ans = 10 ** 9
for i in range(len(complete)):
    score = g
    solved = 0
    for j in range(d):
        zenkan = complete[i][j]
        num = pc[j][0]
        bonus = pc[j][1]
        point = (j + 1) * 100
        if zenkan == 1:
            solved += num
            score -= num * point + bonus

    if score <= 0:
        ans = min(ans, solved)
    else:
        for j in reversed(range(d)):
            zenkan = complete[i][j]
            num = pc[j][0]
            bonus = pc[j][1]
            point = (j + 1) * 100
            if zenkan == 0:
                if score - (num - 1) * point > 0:
                    solved += num - 1
                    score -= (num - 1) * point
                else:
                    if score % point == 0:
                        solved += score // point
                    else:
                        solved += score // point + 1
                    ans = min(ans, solved)
                    break

print(ans)
