N = int(input())
a_b = []
for _ in range(2):
    a_b.append(list(map(int, input().split())))
total = 0
for i in range(N):
    total += a_b[0][i] * a_b[1][i]

if total == 0:
    print("Yes")
else:
    print("No")