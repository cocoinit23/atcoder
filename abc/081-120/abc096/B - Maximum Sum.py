abc = sorted(list(map(int, input().split())))
k = int(input())

ans = abc[0] + abc[1] + abc[2] * (2 ** k)
print(ans)
