n = int(input())
c = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    divisor = []
    for j in range(n):
        if i != j and c[i] % c[j] == 0:
            divisor.append(c[j])
    s = len(divisor)
    ans += (s + 2) / (2 * s + 2) if s % 2 == 0 else 0.5

print(ans)
