N = int(input())

xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])

length = 0

for i in range(N):
    for j in range(i, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5) > length:
            length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)
print(length)