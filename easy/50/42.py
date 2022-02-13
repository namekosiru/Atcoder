n, m = map(int, input().split())
ans: set = set(range(1, m+1))
for _ in range(n):
    k, *A = map(int, input().split())
    A_set = set(A)
    ans = ans & A_set
print(len(ans))
