a, b, c, k = map(int, input().split())

if a == b == c:
    print(0)
    exit()

if k % 2 == 0: print((a-b))
else: print(-1*(a-b))
