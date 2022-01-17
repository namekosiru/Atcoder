n, m = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        B[i][j] -= 1

si, sj = B[0][0]//7, B[0][0]%7

if(sj+m-1>=7):
    print("No")
    exit()

for i in range(n):
    for j in range(m):
        nb = (si + i)*7 + sj + j
        if(B[i][j] != nb):
            print("No")
            exit()

print("Yes")