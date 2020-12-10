s = ''.join(sorted(list(input())))
t = ''.join(sorted(list(input()), reverse=True))

print('Yes') if s < t else print('No')
