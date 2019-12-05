n = int(input())

ans = 0

for i in range(100):
    val = 100 * n + i
    if val % 108 == 0:
        ans = val // 108
        break
    else:
        pass

print(':(') if ans == 0 else print(ans)
