n, m, x = map(int, input().split())
a = list(map(int, input().split()))

lis = [0 for _ in range(n+1)]

for ai in a:
    lis[ai] = 1
print(min(sum(lis[x:]), sum(lis[:x])))