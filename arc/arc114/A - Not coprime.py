import math


def sieve_of_eratosthenes(n):
    if n <= 1:
        return []
    prime = [2]
    limit = n ** 0.5
    data = [i for i in range(3, n + 1, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [i for i in data if i % data[0] != 0]

    return prime + data


n = int(input())
x = list(map(int, input().split()))

primes = sieve_of_eratosthenes(50)
m = len(primes)

ans = 1e99
for i in range(2 ** m):
    temp = 1
    for j in range(m):
        if (i >> j) & 1:
            temp *= primes[j]

    update = True
    for j in x:
        if math.gcd(temp, j) == 1:
            update = False
            break

    if update:
        ans = min(ans, temp)

print(ans)
