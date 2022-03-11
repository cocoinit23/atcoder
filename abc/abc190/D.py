n = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


div = make_divisors(2 * n)
ans = 0
for i in range(len(div) // 2):
    if div[i] % 2 != div[-i-1] % 2:
        ans += 1
ans *= 2
print(ans)
