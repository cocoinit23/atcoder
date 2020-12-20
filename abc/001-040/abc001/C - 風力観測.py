from decimal import *

deg, dis = map(int, input().split())

deg *= 10
deg += 1125
deg %= 36000
dir = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
dir = dir[deg // 2250]

dis = Decimal(Decimal(dis) / Decimal(60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
dis = int(dis * 10)

if dis <= 2:
    w = 0
elif dis <= 15:
    w = 1
elif dis <= 33:
    w = 2
elif dis <= 54:
    w = 3
elif dis <= 79:
    w = 4
elif dis <= 107:
    w = 5
elif dis <= 138:
    w = 6
elif dis <= 171:
    w = 7
elif dis <= 207:
    w = 8
elif dis <= 244:
    w = 9
elif dis <= 284:
    w = 10
elif dis <= 326:
    w = 11
else:
    w = 12

dir = (dir if w != 0 else 'C')
print(dir, w)
