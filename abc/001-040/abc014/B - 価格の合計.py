n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
bit = bin(x)[2:]
if len(bit) != n:
    bit = '0' * (n - len(bit)) + bit

for i, j in zip(bit, reversed(a)):
    ans += int(i) * j

print(ans)
