n = int(input())
w = [input() for _ in range(n)]

if len(set(w)) != len(w):
    print('No')
else:
    ans = True
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            ans = False
            break

    print('Yes') if ans else print('No')
