N = int(input())

H = list(map(int, input().split()))
tmp = H[0]
for i in range(1, len(H)):
    if tmp < H[i]:
        tmp = H[i]
    else:
        break

print(tmp)
