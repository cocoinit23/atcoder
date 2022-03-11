def sieve_of_eratosthenes(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(n ** 0.5)
    data = [i for i in range(3, n + 1, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [i for i in data if i % data[0] != 0]

    return prime + data


a, b, c, d = map(int, input().split())

prime = sieve_of_eratosthenes(200)

for i in range(a, b + 1):
    aoki = False
    for j in range(c, d + 1):
        val = i + j
        if val in prime:
            aoki = True
            break
    if not aoki:
        break

print('Aoki' if aoki else 'Takahashi')
