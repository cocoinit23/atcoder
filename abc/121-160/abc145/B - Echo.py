n = int(input())
s = input()

a = int(n / 2)

if n % 2 != 0:
    print('No')
else:
    if s[:a] == s[a:]:
        print('Yes')
    else:
        print('No')
