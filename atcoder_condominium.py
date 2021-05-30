N, K = map(int, input().split())
count = 0
for n in range(1, N+1):
    for k in range(1, K+1):
        count += int(f"{n}0{k}")
print(count)