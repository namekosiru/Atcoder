N = int(input())
T_K = []
for _ in range(N):
    T_K.append(list(map(int, input().split())))

for i in T_K[-1][2:]:
    print(i)