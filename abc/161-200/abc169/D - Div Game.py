from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
p = prime_factorize(n)
c = Counter(p)

ans = 0
for key, value in c.most_common():
    x = 1
    while x <= c[key]:
        ans += 1
        c[key] -= x
        x += 1

print(ans)
