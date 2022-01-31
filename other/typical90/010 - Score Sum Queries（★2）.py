n = int(input())
c1 = [0] * (n + 1)
c2 = [0] * (n + 1)
for i in range(1, n + 1):
    c, p = map(int, input().split())
    if c == 1:
        c1[i] = p
    elif c == 2:
        c2[i] = p

cumsum1 = [0] * (n + 1)
cumsum1[1] = c1[1]
cumsum2 = [0] * (n + 1)
cumsum2[1] = c2[1]
for i in range(2, n + 1):
    cumsum1[i] = cumsum1[i - 1] + c1[i]
    cumsum2[i] = cumsum2[i - 1] + c2[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    ans1 = cumsum1[r] - cumsum1[l - 1]
    ans2 = cumsum2[r] - cumsum2[l - 1]
    print(ans1, ans2)
