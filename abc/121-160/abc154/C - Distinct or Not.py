n = int(input())
a = list(map(int, input().split()))

a.sort()
isDistinct = True
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        isDistinct = False
        break

print('YES') if isDistinct else print('NO')
