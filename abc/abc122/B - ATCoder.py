s = [x for x in list(map(str, input()))]

ans = 0
acgt = 0

for x in s:
    if x == 'A' or x == 'T' or x == 'G' or x == 'C':
        acgt += 1
        ans = max(acgt, ans)
    else:
        acgt = 0

print(ans)
