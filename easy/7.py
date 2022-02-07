a = []

for _ in range(3):
    a.append(list(map(int, input().split())))
ans = [[-1] * 3 for _ in range(3)]
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == a[i][j]:
                ans[i][j] = 0

for i in range(3):
    if ans[i][0] == ans[i][1] == ans[i][2] == 0:
        print("Yes")
        exit()

for j in range(3):
    if ans[0][j] == ans[1][j] == ans[2][j] == 0:
        print("Yes")
        exit()

if ans[0][0] == ans[1][1] == ans[2][2] == 0:
    print("Yes")
    exit()

if ans[0][2] == ans[1][1] == ans[2][0] == 0:
    print("Yes")
    exit()
print("No")
