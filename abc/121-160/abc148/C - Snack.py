import fractions

a, b = map(int, input().split())

ans = a * b // fractions.gcd(a, b)
print(ans)
