N = input()
N_int = int(N)

ans = 0
for i in range(3, 18, 3):
    if N_int >= 10 ** i:
        ans += N - (10 ** i - 1)
print(ans)