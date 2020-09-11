s = input()

doremi = 'WBWBWWBWBWBWWBWBWWBWBWBW'

now = s[:12]
if now == doremi[0:12]:
    print('Do')
elif now == doremi[2:14]:
    print('Re')
elif now == doremi[4:16]:
    print('Mi')
elif now == doremi[5:17]:
    print('Fa')
elif now == doremi[7:19]:
    print('So')
elif now == doremi[9:21]:
    print('La')
else:
    print('Si')
