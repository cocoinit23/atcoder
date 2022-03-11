from heapq import heapify, heappop, heappush

n, k = map(int, input().split())
p = list(map(int, input().split()))

topk = p[:k]
heapify(topk)

ans = topk[0]
print(ans)
for i in range(k, n):
    val = p[i]
    if val <= ans:
        print(ans)
    else:
        heappush(topk, val)
        heappop(topk)
        ans = topk[0]
        print(ans)
