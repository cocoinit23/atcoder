n = int(input())
ans = 1000 - n % 1000
ans %= 1000
print(ans)
