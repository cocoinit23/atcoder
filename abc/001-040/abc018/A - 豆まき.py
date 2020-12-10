s = [int(input()) for _ in range(3)]
ans = [sorted(s, reverse=True).index(i) for i in s]
[print(i + 1) for i in ans]
