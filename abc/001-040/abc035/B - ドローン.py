s = input()
t = int(input())

x = abs(s.count('R') - s.count('L'))
y = abs(s.count('U') - s.count('D'))
dist = x + y
unk = s.count('?')

if t == 1:
    print(dist + unk)
else:
    if dist - unk > 0:
        print(dist - unk)
    else:
        unk -= dist
        if unk % 2 == 0:
            print(0)
        else:
            print(1)
