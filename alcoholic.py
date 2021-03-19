N, X = map(int, input().split())

total = 0

for i in range(1,1+N):
    ml, percent = map(int, input().split())
    total += ml * (percent)
    if total > 100*X:
        print(i)
        exit()
print("-1")