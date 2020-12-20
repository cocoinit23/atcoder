n = int(input())

total = [i for i in range(1, n + 1)]
fizz = [i for i in range(1, n + 1) if i % 3 == 0]
buzz = [i for i in range(1, n + 1) if i % 5 == 0]
fizzbuzz = [i for i in range(1, n + 1) if i % 15 == 0]

ans = sum(total) - sum(fizz) - sum(buzz) + sum(fizzbuzz)
print(ans)
