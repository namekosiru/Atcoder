import numpy as np
matrix = []
h, w = map(int, input().split())

for _ in range(h):
    matrix.append(list(map(int, input().split())))

for i in np.array(matrix).T:
    print(*i)