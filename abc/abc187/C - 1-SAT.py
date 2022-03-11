n = int(input())

a = set()
b = set()
for _ in range(n):
    s = input()
    if s[0] == '!':
        a.add(s[1:])
    else:
        b.add(s)

ans = a & b
print('satisfiable') if ans == set() else print(list(ans)[0])
