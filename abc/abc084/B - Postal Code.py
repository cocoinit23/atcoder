a, b = map(int, input().split())
s = input()

if s[a] == '-' and s[:a].isdigit() and s[a + 1:].isdigit():
    print('Yes')
else:
    print('No')
