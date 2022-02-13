N: int = int(input())
P: list = list(map(int, input().split()))

ans: int = 1
min_num: int = P[0]
for i in range(1, len(P)):
    if P[i] <= min_num:
        ans += 1
        min_num = P[i]
    
print(ans)