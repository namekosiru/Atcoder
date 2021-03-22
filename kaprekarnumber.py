N, K = input().split()
int_N, int_K = int(N), int(K)

for _ in range(int_K):
    N_list = list(N)
    min_num = sorted(N_list)
    max_num = sorted(N_list, reverse=True)
    N = str(int("".join(max_num)) - int("".join(min_num)))
print(int(N))