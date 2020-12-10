n, k = map(int, input().split())
d = input().split()

while set(list(str(n))) & set(d) != set():
    n += 1

print(n)
