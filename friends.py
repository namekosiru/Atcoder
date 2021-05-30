import numpy as np
n, k = map(int, input().split())

money_dict = {}

for _ in range(n):
    a, b = map(int, input().split())
    if a not in money_dict.keys():
        money_dict[a] =  b
    else:
        money_dict[a] = money_dict[a] + b

village_number = 0
money_array = sorted(list(money_dict.items()))

while k>0:
    village_number += k
    k = 0
    if len(money_array) <= 1:
        if money_array[0][0] <= village_number:
            village_number += money_array[0][1]
            break
    for i in range(len(money_array)):
        if money_array[i][0] > village_number:
            del money_array[:i]
            break
        k += money_array[i][1]


print(village_number)