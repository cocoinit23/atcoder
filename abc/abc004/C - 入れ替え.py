n = int(input())
s = list(range(1, 7))

quotient = n // 5
reminder = n % 5

quotient %= 6
s = s[quotient:] + s[:quotient]

for i in range(reminder):
    s[i], s[i + 1] = s[i + 1], s[i]

print(''.join(map(str, s)))
