n = input()
s = str(input())

result = []

for i in range(int(n)):
    if s[i:i + 1] != s[i + 1:i + 2]:
        result.append(s[i:i + 1])

print(len(result))
