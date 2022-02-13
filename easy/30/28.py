n = int(input())
A_list = list(map(int, input().split()))

ans: int = 0
flag: bool = False
while True:
    for i in range(len(A_list)):
        if A_list[i] % 2 == 1 or A_list[i] == 0:
            flag = True
            break
        A_list[i] //= 2
    if flag:
        break
    ans += 1
print(ans)