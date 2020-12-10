n, k = map(int, input().split())
s = input()

s_sorted = sorted(s)
ans = ''
count = 0

for i in range(n):
    for c in s_sorted:
        temp = 0 if c == s[i] else 1
        t = s_sorted.copy()
        t.remove(c)
        for j in range(i + 1, n):
            if s[j] in t:
                t.remove(s[j])
            else:
                temp += 1

        if count + temp <= k:
            ans += c
            s_sorted.remove(c)
            if c != s[i]:
                count += 1
            break
print(ans)
