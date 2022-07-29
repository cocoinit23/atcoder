n = int(input())

table = {}
for _ in range(n):
    s = input()

    if s in table:
        print(f'{s}({table[s]})')
        table[s] += 1
    else:
        print(s)
        table[s] = 1
