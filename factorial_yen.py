p = int(input())
import math
number = 1
# print(p)
count = 0
while True:
    if math.factorial(number) <= p:
        number += 1
    else:
        number -= 1
        # print(f"number is {number}")
        p = p - math.factorial(number)
        number = 1
        count += 1
        # print(p)
    if p<=0:
        break
print(count)