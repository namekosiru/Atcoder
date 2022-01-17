import itertools

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
count = 0
for index in itertools.combinations(range(len(XY)), 3):
    i1, i2, i3 = index
    x0, y0 = XY[i1]
    x1, y1 = XY[i2]
    x2, y2 = XY[i3]
    a, b = [x1-x0, y1-y0], [x2-x0, y2-y0]
    S = abs(a[0]*b[1]-a[1]*b[0])
    if S > 0:
        count += 1
print(count)