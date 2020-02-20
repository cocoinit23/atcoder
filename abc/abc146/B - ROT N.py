n = int(input())
s = input()

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
aa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''

for i in range(len(s)):
    b = a.find(s[i])
    res += aa[b + n]

print(res)
