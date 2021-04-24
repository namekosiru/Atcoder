from itertools import product

N = int(input())
A = list(map(int, input().split()))

INF = 1e9
ans = INF

if len(A) == 1:
    print(A[0])

else:
    for bit in range(2**(N-1)):
        log_sum = A[0]
        xor = 0
        for i in range(1, N):
            if (bit>>(i-1)) & 1:
                xor = xor ^ log_sum
                log_sum = 0
                log_sum = log_sum | A[i]
            else:
                log_sum = log_sum | A[i]

        xor = xor ^ log_sum
        ans = min(ans, xor)
    print(ans)