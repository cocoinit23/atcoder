n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

used = [0] * n
ans = 0
for i in range(n):
    now = t[i]
    if i < k:
        if now == 'r':
            used[i] = 'p'
            ans += p
        elif now == 's':
            used[i] = 'r'
            ans += r
        else:
            used[i] = 's'
            ans += s
    elif k <= i < n - k:
        prev = used[i - k]
        next = t[i + k]
        if now == 'r':
            if prev != 'p':
                used[i] = 'p'
                ans += p
            else:
                if next == 's':
                    used[i] = 's'
                elif next == 'p':
                    used[i] = 'p'
        elif now == 's':
            if prev != 'r':
                used[i] = 'r'
                ans += r
            else:
                if next == 'p':
                    used[i] = 'p'
                elif next == 'r':
                    used[i] = 'r'
        else:
            if prev != 's':
                used[i] = 's'
                ans += s
            else:
                if next == 'r':
                    used[i] = 'r'
                elif next == 's':
                    used[i] = 's'
    else:
        prev = used[i - k]
        if now == 'r' and prev != 'p':
            used[i] = 'p'
            ans += p
        elif now == 's' and prev != 'r':
            used[i] = 'r'
            ans += r
        elif now == 'p' and prev != 's':
            used[i] = 's'
            ans += s
print(ans)
