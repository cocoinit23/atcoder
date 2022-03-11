# s = input()
# n = len(s)

import random, string


def randomname(n):
    # randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    randlst = [random.choice(string.ascii_letters) for i in range(n)]
    return ''.join(randlst)


while True:
    n = random.randint(1, 1000)
    s = randomname(n).lower()

    ansans = False
    temp = s
    for _ in range(n):
        if temp == temp[::-1]:
            ansans = True
            break
        temp = 'a' + s

    if set(s) == set('a') or s == s[::-1]:
        ans = True
    elif s[-1] != 'a':
        ans = s == s[::-1]
    else:
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if s[i] != 'a':
                idx = i
                break

        temp = s[:idx + 1]
        ans = temp == temp[::-1]

    if ans != ansans:
        print(s, ans, ansans)
    # print('Yes' if ans else 'No')
