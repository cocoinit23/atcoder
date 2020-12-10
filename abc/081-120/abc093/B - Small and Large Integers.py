a, b, k = map(int, input().split())

if b - a < k * 2:
    for i in range(a, b + 1):
        print(i)
else:
    for i in list(range(a, a + k)) + list(range(b - k + 1, b + 1)):
        print(i)
