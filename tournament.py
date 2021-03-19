N = int(input())
A = list(map(int, input().split()))
A_copy = A.copy()

len_number = len(A) // 2

while len_number != 1:
    wins = []
    for i in range(len_number):
        if A[2*i] >= A[2*i+1]:
            wins.append(A[2*i])
        else:
            wins.append(A[2*i+1])
    len_number = len(wins) // 2
    A = wins.copy()
print(A_copy.index(min(A))+1)