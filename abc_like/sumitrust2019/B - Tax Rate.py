n = int(input())

ans = 0

for i in range(100):
    ans = 100 * n + i
    if ans % 108 == 0:
        ans = ans // 108
        break
    else:
        pass

print(':(') if ans == 0 else print(ans)
