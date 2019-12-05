N = float(input())

if N % 2 == 0:
    result = 0.5
else:
    result = 1 - N // 2 / N

print(result)
