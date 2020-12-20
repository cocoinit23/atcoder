n = int(input())
x = list(map(int, input().split()))

manhattan = sum(map(abs, x))
print(manhattan)

euclid = sum(map(lambda i: i ** 2, x)) ** 0.5
print(euclid)

chebyshev = max(map(abs, x))
print(chebyshev)
