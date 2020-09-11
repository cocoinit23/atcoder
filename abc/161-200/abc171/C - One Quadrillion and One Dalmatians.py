n = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

n -= 1
ans = ''
while n >= 0:
    ans = alphabet[n % 26] + ans
    n //= 26
    n -= 1

print(ans)
