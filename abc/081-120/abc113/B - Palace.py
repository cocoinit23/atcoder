n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

temp = [t - i * 0.006 for i in h]
diff = [abs(i - a) for i in temp]

print(diff.index(min(diff)) + 1)
