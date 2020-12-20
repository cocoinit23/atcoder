time = list(map(int, input().split()))
time.sort()
print(sum(time[:2]))
