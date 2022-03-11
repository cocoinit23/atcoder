s = input()
n = int(input()) - 1

ans = s[n // 5] + s[n % 5]
print(ans)
