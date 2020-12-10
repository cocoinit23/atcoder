abc = list(map(int, input().split()))
abc.sort()
print(abc[2] * 10 + abc[0] + abc[1])
