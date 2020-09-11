s = input()

left = int(s[:2])
right = int(s[2:])

if 0 < left <= 12 and 0 < right <= 12:
    print('AMBIGUOUS')
elif 0 < left <= 12 < right or right == 0 < left <= 12:
    print('MMYY')
elif 0 < right <= 12 < left or left == 0 < right <= 12:
    print('YYMM')
else:
    print('NA')
