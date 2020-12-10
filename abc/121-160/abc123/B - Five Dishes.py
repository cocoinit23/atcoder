dish = [int(input()) for x in range(5)]
hitoketa = list(map(int, [str(x)[-1] for x in dish]))

last = 999
for i in hitoketa:
    if not i % 10 == 0:
        last = min(last, i)

if last != 999:
    last = dish[hitoketa.index(last)]
else:
    last = dish[0]

ans = last
skip = False

for i in dish:
    if i == last and not skip:
        skip = True
    elif i % 10 == 0:
        ans += i
    else:
        ans += (i // 10 + 1) * 10

print(ans)
