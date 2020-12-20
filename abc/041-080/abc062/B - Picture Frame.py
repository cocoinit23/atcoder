h, w = map(int, input().split())
a = ['#' + input() + '#' for _ in range(h)]

print('#' * (w + 2))
for x in a:
    print(x)
print('#' * (w + 2))
