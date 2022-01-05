A, B = input().split()
A, B = A[::-1], B[::-1]


for i in range(min(len(A), len(B))):
    tmp = int(A[i]) + int(B[i])
    if tmp >= 10:
        print("Hard")
        exit()
print("Easy")
