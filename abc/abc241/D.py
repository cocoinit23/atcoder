from heapq import heapify, heappush, heappop

q = int(input())

a = []
b = []
heapify(a)
heapify(b)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        heappush(a, x)
        heappush(b, -x)
    else:
        c, x, k = map(int, query)
        temp = []
        if c == 2:
            while a and a[0] <= x:
                temp.append(a[0])
                heappop(a)

            if temp and len(temp) >= k:
                ans = temp[-k]
            else:
                ans = -1
            print(ans)

            for i in temp:
                heappush(a, i)
        else:
            while b and -b[0] >= x:
                temp.append(b[0])
                heappop(b)

            if temp and len(temp) >= k:
                ans = -temp[-k]
            else:
                ans = -1

            print(ans)

            for i in temp:
                heappush(b, i)
