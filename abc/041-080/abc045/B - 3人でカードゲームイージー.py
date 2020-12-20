a = list(input())
b = list(input())
c = list(input())

now = a.pop(0)
while True:
    if eval('%s' % now):
        now = eval(str(now)).pop(0)
    else:
        print(now.upper())
        exit()
