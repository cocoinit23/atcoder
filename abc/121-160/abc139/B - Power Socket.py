a, b = map(int, input().split())

total = 1
tap = 0

while total < b:
    total = total + a - 1
    tap += 1

print(tap)
