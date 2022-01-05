N, W = map(int, input().split())
AB =[[0]*2 for _ in range(N)]

for i in range(N):
    A, B = map(int, input().split())
    AB[i][0], AB[i][1] = A, B
AB = sorted(AB, reverse=True, key=lambda x: x[0])

weight = 0
deli = 0

for a, b in AB:
    deli += a * min(b, W - weight)
    weight += min(b, W - weight)
print(deli)