s = input()
t = input()

s += s

flag = False
for i in range(len(s)):
    if s[i:i + len(t)] == t:
        flag = True
        break

print('Yes') if flag else print('No')
