n = int(input())
s = input()

if s == 'b':
    ans = 0
else:
    accessory = 'b'
    ans = -1

    for i in range(1, n + 1):
        if i % 3 == 0:
            accessory = 'b' + accessory + 'b'
        elif i % 3 == 1:
            accessory = 'a' + accessory + 'c'
        else:
            accessory = 'c' + accessory + 'a'

        if s == accessory:
            ans = i
            break

print(ans)
