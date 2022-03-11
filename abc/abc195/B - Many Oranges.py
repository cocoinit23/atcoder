a, b, w = map(int, input().split())
w *= 1000

minimum = float('inf')
maximum = 0

for i in range(1, w + 1):
    if a * i <= w <= b * i:
        minimum = min(minimum, i)
        maximum = max(maximum, i)

print(minimum, maximum) if maximum != 0 else print('UNSATISFIABLE')
