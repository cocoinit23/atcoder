n = int(input())

a = 2025 - n
ans = []
for i in range(9):
    for j in range(9):
        if a == (i + 1) * (j + 1):
            ans.append([i + 1, j + 1])

for i in range(len(ans)):
    print(str(ans[i][0]) + ' x ' + str(ans[i][1]))
