n = int(input())
a = list(map(int, input().split()))

stack = [[a[0]]]
print(1)

prev = None
ans = 1
for i in a[1:]:
    if stack:
        prev = stack[-1][0]
        if i == prev:
            stack[-1].append(i)
            ans += 1
            if len(stack[-1]) == i:
                stack.pop()
                ans -= i
        else:
            stack.append([i])
            prev = i
            ans += 1
    else:
        stack.append([i])
        prev = i
        ans += 1

    print(ans)
