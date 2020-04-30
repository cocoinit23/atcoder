antenna = []
for i in range(5):
    antenna.append(int(input()))
k = int(input())

can = True

for i in antenna:
    for j in antenna:
        if i == j or i < j:
            continue
        else:
            if abs(i - j) > k:
                can = False
                break
            else:
                continue

print('Yay!') if can else print(':(')
