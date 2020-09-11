n = int(input())

h = n // 3600
n %= 3600

m = n // 60
n %= 60

print('%02d:%02d:%02d' % (h, m, n))
