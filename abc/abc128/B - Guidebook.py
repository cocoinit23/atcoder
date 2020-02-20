n = int(input())
sp = []
for i in range(n):
    s, p = input().split()
    sp.append([s, int(p)])

sorted_sp = sorted(sp, key=lambda x: x[1], reverse=True)
sorted_sp = sorted(sorted_sp, key=lambda x: x[0])

for i in range(n):
    print(sp.index(sorted_sp[i]) + 1)
