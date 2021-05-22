import collections

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

a_dict = collections.Counter(A_list)
c_dict = collections.Counter(C_list)
# print(a_dict)
# print(c_dict)
total = 0
for i in range(N):
    total += c_dict[i+1] * a_dict[B_list[i]]
print(total)