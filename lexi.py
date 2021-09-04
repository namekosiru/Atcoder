s,t = input().split()

lis = sorted([s, t])

if lis.index(s) == 0:
    print("Yes")
else:
    print("No")