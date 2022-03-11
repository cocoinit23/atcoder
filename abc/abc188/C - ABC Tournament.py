n = int(input())
a = list(map(int, input().split()))

next = a.copy()
while len(next) > 2:
    temp = []
    for i in range(len(next) // 2):
        temp.append(max(next[2 * i], next[2 * i + 1]))
    next = temp

ans = a.index(min(next)) + 1
print(ans)
